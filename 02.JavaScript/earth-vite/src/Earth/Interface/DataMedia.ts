import * as THREE from "three";

interface DataMedia {
  id: number;
  media_id: number;
  name: string;
  media_type: string;
  show_type: string;
  subtitle_time: number;
  media_delay: number;
  media_time: number;
  sort: number;
  subtitle: string;
  subtitle_id: number;
  episode_id: number;
}

interface DataMediaPropBase {
  id: number;
  media_id: number;
  name: string;
  file: string;
}

interface DataMedia2dProp extends DataMediaPropBase {
  font: string;
  font_size: string;
  font_color: string;
  height: number;
  width: number;
  top: number;
  left: number;
  opacity: number;
  aspect: number;
  transaction_to_3d: string;
  full_screen: number;
  keep: number;
}

interface DataMedia3dProp extends DataMediaPropBase {
  font: string;
  font_color: string;
  font_size: string;
  longitude: number;
  latitude: number;
  altitude: number;
  height: number;
  width: number;
  depth: number;
  aspect: number;
  keep: number;
  parallel: number;
  sprite: number;
}

interface DataMedia3dPropKml extends DataMediaPropBase {
  keep: number;
}

interface DataMedia3dPropMotionLine extends DataMediaPropBase {
  coordinate_list: [];
  color: string;
  line_weight: number;
  motion_speed: number;
  motion_time: number;
  line_divide: number;
  height: number;
  is_circle: boolean;
  parallel: number;
}

interface DataMedia3dPropOverlay extends DataMediaPropBase {
  longitude_1: number;
  latitude_1: number;
  longitude_2: number;
  latitude_2: number;
  longitude_3: number;
  latitude_3: number;
  longitude_4: number;
  latitude_4: number;
  keep: number;
}

interface DataMedia3dPropModel extends DataMediaPropBase {
  longitude: number;
  latitude: number;
  altitude: number;
  geometry_type: string;
  sizeX: number;
  sizeY: number;
  sizeZ: number;
}

interface LineData {
  coordinateList: [];
  lineLength: number;
  lineColor: string;
  moveSpeed: number;
  isCircleLine: boolean;
  lineDivide: number;
}

interface LineToMove {
  linePointsArray: [];
  lineObject: THREE.Line;
  lineColor: string;
  moveSpeed: number;
  isCircleLine: boolean;
  lineLength: number;
}

export type {
  DataMedia,
  DataMedia2dProp,
  DataMedia3dProp,
  DataMedia3dPropKml,
  DataMedia3dPropMotionLine,
  DataMedia3dPropOverlay,
  DataMedia3dPropModel,
  LineData,
  LineToMove,
};
