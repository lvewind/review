import * as THREE from "three";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);
camera.position.z = 5;

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const geometry = new THREE.BufferGeometry();
const numPoints = 100;
const positions = new Float32Array(numPoints * 3);
const colors = new Float32Array(numPoints * 3);

const color = new THREE.Color();

for (let i = 0; i < numPoints; i++) {
  const t = i / numPoints;

  positions[i * 3] = Math.sin(t * Math.PI * 2) * 2;
  positions[i * 3 + 1] = Math.cos(t * Math.PI * 2) * 2;
  positions[i * 3 + 2] = 0;

  color.setHSL(t, 1.0, 0.5);
  colors[i * 3] = color.r;
  colors[i * 3 + 1] = color.g;
  colors[i * 3 + 2] = color.b;
}

geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
geometry.setAttribute("color", new THREE.BufferAttribute(colors, 3));

const material = new THREE.LineBasicMaterial({
  vertexColors: THREE.VertexColors,
  linewidth: 2,
});

const line = new THREE.Line(geometry, material);
scene.add(line);

function animate() {
  requestAnimationFrame(animate);

  // 循环移动最后一个点到起点
  const positions = line.geometry.attributes.position.array;
  for (let i = 0; i < numPoints - 1; i++) {
    positions[i * 3] = positions[(i + 1) * 3];
    positions[i * 3 + 1] = positions[(i + 1) * 3 + 1];
    positions[i * 3 + 2] = positions[(i + 1) * 3 + 2];
  }
  positions[(numPoints - 1) * 3] =
    Math.sin((Date.now() / 1000) * Math.PI * 2) * 2;
  positions[(numPoints - 1) * 3 + 1] =
    Math.cos((Date.now() / 1000) * Math.PI * 2) * 2;

  line.geometry.attributes.position.needsUpdate = true;

  renderer.render(scene, camera);
}

// 调用动画函数
animate();
