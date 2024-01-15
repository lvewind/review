interface Subtitle {
  id: number;
  episode_id: number;
  name: string;
  audio_file: string;
  audio_time: number;
  ext_time: number;
  font: string;
  font_size: string;
  font_color: string;
  media_count: number;
  sort: number;
  is_empty: number;
  voice_local_name: string;
  voice_name: string;
  voice_role: string;
  voice_style: string;
  voice_rate: number;
  voice_volume: number;
  voice_pitch: number;
  subtitle_action: DataSubtitleAction;
}

interface DataSubtitleAction {
  id: number;
  subtitle_id: number;
  name: string;
  fly_type: string;
  fly_to_place: string;
  fly_to_longitude: number;
  fly_to_latitude: number;
  fly_to_altitude: number;
  heading: number;
  tilt: number;
  set_2d_view: number;
  set_3d_view: number;
  fly_speed: number;
  start_x: number;
  start_y: number;
  end_x: number;
  end_y: number;
  slide_speed: number;
  zoom_times: number;
}

export type { Subtitle, DataSubtitleAction };
