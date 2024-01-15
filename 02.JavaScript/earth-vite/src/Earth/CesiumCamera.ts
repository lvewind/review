import {
  Ellipsoid,
  Cartesian3,
  HeadingPitchRange,
  Math as CesiumMath,
  PerspectiveFrustum,
  Camera,
  Scene,
} from "cesium";
import CameraState from "./Interface/CameraState";

class CesiumCamera {
  public scene: Scene;
  public camera: Camera;
  public getCurrentCameraPosition: (cameraState: CameraState) => {
    ci_vm: any;
    fov_y: number;
    cvm: any;
  };

  constructor() {
    const canvas = document.createElement("canvas");
    canvas.id = "CesiumCamera";
    document.body.appendChild(canvas);
    this.scene = new Scene({
      canvas: canvas,
    });
    this.camera = new Camera(this.scene);

    this.getCurrentCameraPosition = function (cameraState: CameraState) {
      let center = Cartesian3.fromDegrees(
        cameraState.longitude,
        cameraState.latitude,
        cameraState.altitude,
        Ellipsoid.WGS84
      );
      let _heading = CesiumMath.toRadians(cameraState.heading);
      let pitch = CesiumMath.toRadians(cameraState.tilt - 90);

      if (cameraState.distance == 0) {
        cameraState.distance = 0.001;
      }
      this.camera.lookAt(
        center,
        new HeadingPitchRange(_heading, pitch, cameraState.distance)
      );
      let fov_y = 35;
      if (this.camera.frustum instanceof PerspectiveFrustum) {
        fov_y = CesiumMath.toDegrees(this.camera.frustum.fovy);
      }
      let cvm = this.camera.viewMatrix;
      let ci_vm = this.camera.inverseViewMatrix;
      return {
        fov_y: fov_y,
        cvm: cvm,
        ci_vm: ci_vm,
      };
    };
  }
}

export default CesiumCamera;
