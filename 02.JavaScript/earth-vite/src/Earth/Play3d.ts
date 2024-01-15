import * as THREE from "three";
import { Cartesian3 } from "cesium";
import { FontLoader } from "three/examples/jsm/loaders/FontLoader";
import { TextGeometry } from "three/examples/jsm/geometries/TextGeometry";
import Control from "./Control";
// import MotionLine from "./Line";
import {
  DataMedia,
  DataMedia3dProp,
  DataMedia3dPropKml,
  DataMedia3dPropOverlay,
  DataMedia3dPropModel,
  DataMedia3dPropMotionLine,
  LineData,
} from "./Interface/DataMedia";

class Play3d {
  public clearAllThree: () => void;

  public showImage: (data?: string, media_prop?: string) => void;
  public showVideo: (data?: string, media_prop?: string) => void;
  public showText: (data?: string, media_prop?: string) => void;

  public showModel: (data?: string, media_prop?: string) => void;
  public showKml: (data?: string, media_prop?: string) => void;
  public showMotionLine: (data?: string, media_prop?: string) => void;
  public showOverlay: (data?: string, media_prop?: string) => void;

  public llaToVectorPoints: (lla_array: any) => any[];
  public createThreeObject: (
    material: any,
    geometry: any,
    dataMedia: DataMedia,
    dataMediaProp: DataMedia3dProp
  ) => void;
  public cartToVec: (cart: any) => THREE.Vector3;
  public llaToCartesian3: (longitude: any, latitude: any, altitude: any) => any;

  public scene: any;
  public _plane_objects: Array<any>;
  public _sprite_objects: Array<any>;
  public _3D_objects: Array<any>;
  public _motion_line: Array<any>;
  public setPlaneOrientedToCamera: (cameraState: any) => void;
  public initLight: () => void;

  constructor(scene: any, fontsServer: string) {
    this._plane_objects = [];
    this._sprite_objects = [];
    this._3D_objects = [];
    this._motion_line = [];
    this.scene = scene;

    this.cartToVec = function (cart) {
      return new THREE.Vector3(cart.x, cart.y, cart.z);
    };
    this.llaToCartesian3 = (longitude, latitude, altitude) => {
      return Cartesian3.fromDegrees(longitude, latitude, altitude);
    };

    this.setPlaneOrientedToCamera = (cameraState) => {
      if (cameraState.heading !== null) {
        let _plane_objects_count = this._plane_objects.length;
        if (this._plane_objects.length > 0) {
          for (let i = _plane_objects_count - 1; i >= 0; i--) {
            let item = this._plane_objects[i];
            if (item.showTime > 0) {
              let current_time = new Date().getTime();

              let myTime = current_time - item.addTime;
              let showTime = item.showTime * 1000;
              if (myTime >= showTime) {
                let parent = item.threeMesh.parent;
                if (parent !== null) {
                  parent.remove(item.threeMesh);
                }
                this._plane_objects.slice(i, 1);
              }
            }
            let heading = cameraState.heading;
            item.threeMesh.rotation.z = Math.PI * (-heading / 180);
            // let tilt = cameraState.tilt;
            // item.threeMesh.rotation.x = Math.PI * (tilt/90);
          }
        }
      }
    };
    this.clearAllThree = () => {
      let _plane_objects_count = this._plane_objects.length;
      if (this._plane_objects.length > 0) {
        for (let i = _plane_objects_count - 1; i >= 0; i--) {
          let item = this._plane_objects[i];
          let parent = item.threeMesh.parent;
          if (parent !== null) {
            parent.remove(item.threeMesh);
            this._plane_objects.slice(i, 1);
          }
        }
      }
    };
    this.createThreeObject = (material, geometry, dataMedia, dataMediaProp) => {
      let mesh = new THREE.Mesh(geometry, material);
      if (dataMedia.media_type === "text") {
        geometry.computeBoundingBox();
        mesh.position.x =
          0.5 * (geometry.boundingBox.max.x - geometry.boundingBox.min.x);
      }
      // let axes = new THREE.AxesHelper(2000)
      // mesh.add(axes);
      let MeshYup = new THREE.Group();
      MeshYup.add(mesh);
      // let axes_group = new THREE.AxesHelper(7000000);
      // MeshYup.add(axes_group);
      let center = Cartesian3.fromDegrees(
        dataMediaProp.longitude,
        dataMediaProp.latitude
      );
      let latDir = this.cartToVec(center).normalize();
      MeshYup.position.copy(this.cartToVec(center));
      MeshYup.translateOnAxis(latDir, dataMediaProp.altitude);
      this.scene.add(MeshYup);
      let centerHigh = Cartesian3.fromDegrees(
        dataMediaProp.longitude,
        dataMediaProp.latitude,
        6371000 + dataMediaProp.altitude
      );
      MeshYup.lookAt(centerHigh.x, centerHigh.y, centerHigh.z);
      mesh.rotation.z = (-Math.PI * 150) / 180;
      if (dataMediaProp.parallel === 0) {
        mesh.rotation.x = (-Math.PI * 90) / 180;
        mesh.rotation.z = -Math.PI;
      }

      let _3DOB = {
        id: dataMedia.name,
        threeMesh: MeshYup,
        subMesh: mesh,
        longitude: dataMediaProp.longitude,
        latitude: dataMediaProp.latitude,
        altitude: dataMediaProp.altitude,
        addTime: new Date().getTime(),
        showTime: dataMedia.media_time,
      };

      this._plane_objects.push(_3DOB);
    };

    this.initLight = () => {
      //添加环境光
      let ambientLight = new THREE.AmbientLight(0xffffff);
      scene.add(ambientLight);

      let spotLight = new THREE.SpotLight(0xffffff);
      spotLight.position.set(25, 30, 50);
      spotLight.castShadow = true;
      scene.add(spotLight);
    };
    this.llaToVectorPoints = (lla_array) => {
      const vectorArray = [];
      for (let i = 0, len = lla_array.length / 3; i <= len; i++) {
        vectorArray.push(
          this.cartToVec(
            this.llaToCartesian3(
              lla_array[i][0],
              lla_array[i][1],
              lla_array[i][2]
            )
          )
        );
      }
      return vectorArray;
    };

    this.showImage = (media = "", media_prop = "") => {
      if (media && media_prop) {
        let dataMedia: DataMedia = JSON.parse(media);
        let dataMediaProp: DataMedia3dProp = JSON.parse(media_prop);

        let media_delay = dataMedia.media_delay;
        if (!media_delay) {
          media_delay = 0;
        }
        setTimeout(() => {
          let textureLoader = new THREE.TextureLoader(); // 纹理加载器
          let texture = textureLoader.load(dataMediaProp.file);
          let material = new THREE.MeshBasicMaterial({
            map: texture,
            side: THREE.DoubleSide,
            transparent: true,
          });
          if (dataMediaProp.aspect) {
            dataMediaProp.height = dataMediaProp.width / dataMediaProp.aspect;
          }
          let geometry = new THREE.PlaneGeometry(
            dataMediaProp.width,
            dataMediaProp.height
          ); //平面
          this.createThreeObject(material, geometry, dataMedia, dataMediaProp);
        }, media_delay * 1000);
      }
    };
    this.showVideo = (media = "", media_prop = "") => {
      if (media && media_prop) {
        let dataMedia: DataMedia = JSON.parse(media);
        let dataMediaProp: DataMedia3dProp = JSON.parse(media_prop);
        let media_delay = dataMedia.media_delay;
        if (!media_delay) {
          media_delay = 0;
        }
        setTimeout(() => {
          new Promise<HTMLVideoElement>(function (resolve, reject) {
            const videoElem = document.createElement("video");
            videoElem.src = dataMediaProp.file;
            videoElem.loop = true;
            videoElem.muted = true;
            videoElem.autoplay = true;
            videoElem.width = dataMediaProp.width;
            videoElem.crossOrigin = "anonymous";
            // video.src = dataMedia.mediaFile;
            videoElem.style.position = "absolute";
            videoElem.style.zIndex = "-9999";
            document.body.appendChild(videoElem);
            // 当前帧的数据是可用的
            videoElem.onloadeddata = function () {
              resolve(videoElem);
            };
            videoElem.onerror = function () {
              reject("video 后台加载失败");
            };
          }).then((video) => {
            let texture = new THREE.VideoTexture(video);
            let material = new THREE.MeshBasicMaterial({
              map: texture, // 设置纹理贴图
              side: THREE.DoubleSide,
            });
            let geometry = new THREE.PlaneGeometry(
              dataMediaProp.width,
              (dataMediaProp.width / video.videoWidth) * video.videoHeight
            ); //平面
            this.createThreeObject(
              material,
              geometry,
              dataMedia,
              dataMediaProp
            );
          });
        }, media_delay * 1000);
      }
    };
    this.showText = (media = "", media_prop = "") => {
      if (media && media_prop) {
        let dataMedia: DataMedia = JSON.parse(media);
        let dataMediaProp: DataMedia3dProp = JSON.parse(media_prop);
        let media_delay = dataMedia.media_delay;
        if (!media_delay) {
          media_delay = 0;
        }
        setTimeout(() => {
          let font_height = dataMediaProp.depth;
          if (!font_height) {
            font_height = 1;
          }
          const loader = new FontLoader();
          loader.load(
            fontsServer.concat(dataMediaProp.font, ".json"),
            (font) => {
              let parameters = {
                font: font,
                size: parseInt(dataMediaProp.font_size) * 8,
                height: font_height,
                curveSegments: 24,
              };
              let textGeometry = new TextGeometry(
                dataMediaProp.file,
                parameters
              );
              // let material = new THREE.MeshBasicMaterial();

              let color = parseInt(dataMediaProp.font_color, 16);
              let material = new THREE.MeshPhongMaterial({ color: color });
              this.createThreeObject(
                material,
                textGeometry,
                dataMedia,
                dataMediaProp
              );
            }
          );
        }, media_delay * 1000);
      }
    };

    this.showMotionLine = (media = "", media_prop = "") => {
      if (media && media_prop) {
        let dataMedia: DataMedia = JSON.parse(media);
        let dataMediaProp: DataMedia3dPropMotionLine = JSON.parse(media_prop);
        let media_delay = dataMedia.media_delay;
        if (!media_delay) {
          media_delay = 0;
        }
        setTimeout(() => {
          let lineData: LineData = {
            coordinateList: dataMediaProp.coordinate_list,
            lineLength: dataMediaProp.line_divide,
            lineColor: dataMediaProp.color,
            moveSpeed: dataMediaProp.motion_speed,
            isCircleLine: dataMediaProp.is_circle,
            lineDivide: dataMediaProp.line_divide,
          };
          this._motion_line.push(lineData);
        }, media_delay * 1000);
      }
    };
    this.showModel = (media = "", media_prop = "") => {
      if (media && media_prop) {
        let dataMedia: DataMedia = JSON.parse(media);
        let dataMediaProp: DataMedia3dPropModel = JSON.parse(media_prop);
        let media_delay = dataMedia.media_delay;
        if (!media_delay) {
          media_delay = 0;
        }
        setTimeout(() => {
          let geometry;
          switch (dataMediaProp.geometry_type) {
            case "box":
              geometry = new THREE.BoxGeometry();
              break;
            case "dodecahedron":
              geometry = new THREE.DodecahedronGeometry();
              break;
            default:
              geometry = new THREE.BoxGeometry();
              break;
          }

          const material = new THREE.MeshPhongMaterial({
            color: 0x00ff00,
          });
          const mesh = new THREE.Mesh(geometry, material);
          mesh.scale.set(
            dataMediaProp.sizeX,
            dataMediaProp.sizeY,
            dataMediaProp.sizeZ
          ); //scale object to be visible at planet scale
          mesh.position.z += dataMediaProp.altitude; // translate "up" in Three.js space so the "bottom" of the mesh is the handle
          mesh.rotation.x = Math.PI / 2; // rotate mesh for Cesium's Y-up system
        }, media_delay * 1000);
      }
    };
    this.showKml = (media = "", media_prop = "") => {
      if (media && media_prop) {
        let dataMedia: DataMedia = JSON.parse(media);
        let dataMediaProp: DataMedia3dPropKml = JSON.parse(media_prop);
        let media_delay = dataMedia.media_delay;
        if (!media_delay) {
          media_delay = 0;
        }
        setTimeout(() => {
          let kml = dataMediaProp.file;
          Control.load_kml(kml);
        }, media_delay * 1000);
      }
    };
    this.showOverlay = (media = "", media_prop = "") => {
      if (media && media_prop) {
        let dataMedia: DataMedia = JSON.parse(media);
        let dataMediaProp: DataMedia3dPropOverlay = JSON.parse(media_prop);
        let media_delay = dataMedia.media_delay;
        if (!media_delay) {
          media_delay = 0;
        }
        setTimeout(() => {
          let kml = dataMediaProp.file;
          Control.load_kml(kml);
        }, media_delay * 1000);
      }
    };
  }
}

export default Play3d;
