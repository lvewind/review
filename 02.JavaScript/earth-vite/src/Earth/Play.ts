import * as THREE from "three";
import Play3d from "./Play3d";
import Play2d from "./Play2d";
import Utils from "../Utils/Utils";
import Control from "./Control";
import CameraState from "./Interface/CameraState";
import axios from "axios";
import CesiumCamera from "./CesiumCamera";

class Play {
  public init: () => void;
  public setEarth: () => void;
  public render: () => void;
  public GetCameraState: () => CameraState;
  public Play2d: Play2d;
  public Play3d: Play3d;
  // public cesiumWindow: Window | null;
  public scene: any;
  public camera: any;
  public renderer: any;
  public cameraMatrix = { cvm: [], ci_vm: [], fov_y: 0 };
  public setCameraMatrix: (camera_matrix: string) => void;
  public updateThreeCamera: () => void;
  public postCameraState: (cameraState: CameraState) => void;
  public updateCamera: () => void;
  public cesiumCamera: CesiumCamera;

  constructor(fontsServer = "") {
    this.setEarth = () => {
      // Control.SetLatLngFormatting("decimal");
      // Control.SetMemoryCacheSize("5120");
      // Control.EarthSettingSync();
      // Control.setEarthStyle(0);
      // window.Module.SystemPresenter_SetMemoryUsageTargetMb(65535);
    };
    this.init = () => {
      let fov = 45;
      let width = window.innerWidth;
      let height = window.innerHeight;
      let aspect = width / height;
      let near = 50;
      let far = 64000;
      this.scene = new THREE.Scene();
      this.camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
      this.camera.matrixAutoUpdate = false;
      // this.camera.up.x = 0;
      // this.camera.up.y = 0;
      // this.camera.up.z = 1;
      this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      this.renderer.setSize(window.innerWidth, window.innerHeight);

      let Am_light = new THREE.AmbientLight(0xffffff, 2);
      this.scene.add(Am_light);

      // let axes = new THREE.AxesHelper(7000000)
      // this.scene.add(axes);

      this.renderer.domElement.style.position = "absolute";
      this.renderer.domElement.style.pointerEvents = "None";

      document.body.appendChild(this.renderer.domElement);
      this.setEarth();
      Utils.initFonts(fontsServer);
      window.addEventListener(
        "message",
        (event) => {
          if (event !== null) {
            this.cameraMatrix = event.data;
            console.log("this.cameraMatrix: ", this.cameraMatrix);
          } else {
            console.log("Cesium Camera Position is Null.");
          }
        },
        false
      );
    };
    this.init();
    this.GetCameraState = () => {
      return Utils.parseCameraState(Control.getCurrentCameraStateUrl());
    };

    this.Play2d = new Play2d();
    this.Play3d = new Play3d(this.scene, fontsServer);
    this.cesiumCamera = new CesiumCamera();
    this.updateThreeCamera = () => {
      if (this.cameraMatrix.fov_y > 0) {
        this.camera.fov = this.cameraMatrix.fov_y;
        let cvm = this.cameraMatrix.cvm;
        let ci_vm = this.cameraMatrix.ci_vm;

        this.camera.lookAt(new THREE.Vector3(0, 0, 0));

        this.camera.matrixWorld.set(
          ci_vm[0],
          ci_vm[4],
          ci_vm[8],
          ci_vm[12],
          ci_vm[1],
          ci_vm[5],
          ci_vm[9],
          ci_vm[13],
          ci_vm[2],
          ci_vm[6],
          ci_vm[10],
          ci_vm[14],
          ci_vm[3],
          ci_vm[7],
          ci_vm[11],
          ci_vm[15]
        );
        this.camera.matrixWorldInverse.set(
          cvm[0],
          cvm[4],
          cvm[8],
          cvm[12],
          cvm[1],
          cvm[5],
          cvm[9],
          cvm[13],
          cvm[2],
          cvm[6],
          cvm[10],
          cvm[14],
          cvm[3],
          cvm[7],
          cvm[11],
          cvm[15]
        );

        this.camera.updateProjectionMatrix();
        this.renderer.clear();
        this.renderer.render(this.scene, this.camera);
      }
    };
    this.updateCamera = () => {};
    this.postCameraState = (cameraState: CameraState) => {
      axios.post("/cameraState", cameraState).then((response) => {
        this.cameraMatrix = response.data;
      });
    };
    this.render = () => {
      //获取谷歌地球相机数据
      let cameraState: CameraState = this.GetCameraState();
      //发送谷歌地球相机数据到数据交换服务器并获取计算返回值
      // this.postCameraState(cameraState);
      this.cameraMatrix =
        this.cesiumCamera.getCurrentCameraPosition(cameraState);
      //设置Play3d中的目标朝向
      this.Play3d.setPlaneOrientedToCamera(cameraState);

      //更新Three.js相机
      this.updateThreeCamera();
    };

    this.setCameraMatrix = (camera_matrix: string) => {
      this.cameraMatrix = JSON.parse(camera_matrix);
    };
    setTimeout(() => {
      let cesium_credit_expand_link = document.querySelector(
        ".cesium-credit-expand-link"
      );
      if (cesium_credit_expand_link) {
        cesium_credit_expand_link.setAttribute("style", "display: none");
      }
    }, 3000);
  }
}

export default Play;
