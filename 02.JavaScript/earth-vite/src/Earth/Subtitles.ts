import Control from "./Control";
import { Subtitle, DataSubtitleAction } from "./Interface/Subtitle";

class Subtitles {
  static clearSubtitle() {
    let subtitleElement = document.getElementById("earth-subtitle");
    if (subtitleElement) {
      subtitleElement.style.padding = "0px";
      subtitleElement.innerHTML = "";
    }
  }
  static displaySubtitle(data = "") {
    if (data) {
      let dataObject: Subtitle = JSON.parse(data);
      let subtitle_content = dataObject.name.toString();
      if (subtitle_content.search("[blank]") >= 0) {
        let subtitleElement = document.getElementById("earth-subtitle");
        if (subtitleElement) {
          subtitleElement.innerHTML = "";
          subtitleElement.style.backgroundColor = "#00000000";
        }
      } else {
        let subtitleElement = document.getElementById("earth-subtitle");
        if (subtitleElement == null) {
          subtitleElement = document.createElement("div");
          let subtitleId = document.createAttribute("id");
          subtitleId.nodeValue = "earth-subtitle";
          subtitleElement.setAttributeNode(subtitleId);
          subtitleElement.style.color = "#".concat(dataObject.font_color);
          subtitleElement.style.display = "block";
          subtitleElement.style.position = "absolute";
          subtitleElement.style.textAlign = "center";
          subtitleElement.style.width = "inherit";
          subtitleElement.style.zIndex = "999";
          subtitleElement.style.textShadow = "10px 10px 1px black";
          subtitleElement.style.paddingTop = "24px";
          subtitleElement.style.paddingBottom = "24px";
          subtitleElement.style.backgroundColor = "#00000030";
          subtitleElement.style.bottom = "8%";
          subtitleElement.style.pointerEvents = "None";
          subtitleElement.style.fontSize = dataObject.font_size;
          subtitleElement.style.fontFamily = dataObject.font;

          subtitleElement.innerHTML = subtitle_content;

          const bodyElement = document.querySelector("body");
          if (bodyElement) {
            bodyElement.appendChild(subtitleElement);
          }
        } else {
          subtitleElement.style.backgroundColor = "#00000030";
          subtitleElement.style.fontSize = dataObject.font_size;
          subtitleElement.style.color = "#".concat(dataObject.font_color);
          subtitleElement.style.fontFamily = dataObject.font;
          subtitleElement.innerHTML = subtitle_content;
        }
        setTimeout(this.clearSubtitle, dataObject.audio_time * 1000);
        this.runSubtitleAction(dataObject.subtitle_action);
      }
    }
  }
  static runSubtitleAction(action_data: DataSubtitleAction) {
    let speed = action_data.fly_speed;
    Control.SetFlySpeed(speed.toString());
    if (action_data.fly_type === "lla") {
      Control.flyToLla(
        action_data.fly_to_longitude,
        action_data.fly_to_latitude,
        action_data.fly_to_altitude
      );
    } else if (action_data.fly_type === "place_name") {
      Control.searchPlace(action_data.fly_to_place);
    } else if (action_data.fly_type === "heading") {
      Control.setCompassHeading(action_data.heading, 1);
    } else if (action_data.fly_type === "tilt") {
      Control.setCompassTitle(action_data.tilt, 1);
    } else if (action_data.fly_type === "set_view") {
      if (action_data.set_2d_view) {
        Control.setView2d();
      } else if (action_data.set_3d_view) {
        Control.setView3d();
      }
    } else if (action_data.fly_type === "zoom_to_space") {
      Control.zoomToSpace();
    }
  }
}

export default Subtitles;
