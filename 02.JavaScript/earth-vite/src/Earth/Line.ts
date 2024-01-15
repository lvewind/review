import { CatmullRomCurve3 } from "three";
import * as THREE from "three";
import { LineData } from "./Interface/DataMedia";

class MotionLine {
  private readonly curve: CatmullRomCurve3;

  lineMoving = () => {
    console.log(this.curve);
  };

  constructor(lineData: LineData) {
    let lineVector3: Array<THREE.Vector3> = [];
    // 地球坐标转换为Vector3
    for (const coordinate in lineData.coordinateList) {
      lineVector3.push(
        new THREE.Vector3(
          lineData.coordinateList[coordinate][0],
          lineData.coordinateList[coordinate][1],
          lineData.coordinateList[coordinate][2]
        )
      );
    }
    //使用Vector3生成CatmullRomCurve3
    this.curve = new THREE.CatmullRomCurve3(lineVector3);

    // 创建线条
    const points = this.curve.getPoints(lineData.lineDivide);
    const geometry = new THREE.BufferGeometry().setFromPoints(points);
    const material = new THREE.ShaderMaterial({
      uniforms: {
        time: { value: 0 },
        lineWidth: { value: 0.5 },
        color: { value: new THREE.Color("#00ff00") },
      },
      vertexShader: `
            uniform float time;
            uniform float lineWidth;
            attribute float linePos;

            void main() {
              vec4 mvPosition = modelViewMatrix * vec4( position, 1.0 );
              gl_Position = projectionMatrix * mvPosition;
              gl_Position.xy += gl_Position.w *  linePos * 1.0 + time * 0.5  * vec2( lineWidth * 0.5 );
            }
          `,
      fragmentShader: `
            uniform vec3 color;

            void main() {
              gl_FragColor = vec4( color, 1.0 );
            }
          `,
    });

    //线条运动函数
    console.log(geometry, material);
  }
}

export default MotionLine;
