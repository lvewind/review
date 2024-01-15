// The URL on your server where CesiumJS's static files are hosted.

import {
  Cartesian3,
  createOsmBuildingsAsync,
  Ion,
  Math as CesiumMath,
  Terrain,
  Viewer,
} from "cesium";
import "cesium/Build/Cesium/Widgets/widgets.css";

window.CESIUM_BASE_URL = "/Cesium";

// Your access token can be found at: https://ion.cesium.com/tokens.
// This is the default access token from your ion account

Ion.defaultAccessToken =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIxZDM4Nzg4OC02NDcyLTQ3YTEtYjljZC0zOTlkMDM1MDc2MjMiLCJpZCI6NjU1NjcsImlhdCI6MTY4MTIxMjExNX0.Bop3BlrXOdF6I4n88o7-nOyn3u4leFIy1kbBdXurl1o";

// Initialize the Cesium Viewer in the HTML element with the `cesiumContainer` ID.
const viewer = new Viewer("cesiumContainer", {
  terrain: Terrain.fromWorldTerrain(),
});

// Fly the camera to San Francisco at the given longitude, latitude, and height.
viewer.camera.flyTo({
  destination: Cartesian3.fromDegrees(-122.4175, 37.655, 400),
  orientation: {
    heading: CesiumMath.toRadians(0.0),
    pitch: CesiumMath.toRadians(-15.0),
  },
});

// Add Cesium OSM Buildings, a global 3D buildings layer.
const buildingTileset = await createOsmBuildingsAsync();
viewer.scene.primitives.add(buildingTileset);
