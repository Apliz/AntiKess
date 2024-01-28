import * as THREE from 'three';

//create scene and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);


//earth geometry
const geometry = new THREE.SphereGeometry(15, 32, 16);
// const material = new THREE.MeshDepthMaterial();
const material = new THREE.MeshBasicMaterial();
const earth = new THREE.Mesh(geometry, material);
scene.add(earth);

const light = new THREE.AmbientLight(0x404040); // soft white light
scene.add(light);
const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
scene.add(directionalLight);

camera.position.z = 50;
//render animate loop
function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
animate();