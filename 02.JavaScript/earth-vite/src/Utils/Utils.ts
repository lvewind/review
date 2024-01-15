import axios from "axios";

class Utils {
  static parseCameraState(url_path: string) {
    /**
     *
     */
    let start_index = url_path.indexOf("@");
    url_path = url_path.slice(start_index + 1);
    let cameraStateArray: Array<string> = url_path.split(",");
    return {
      latitude: parseFloat(cameraStateArray[0].replace("@", "")),
      longitude: parseFloat(cameraStateArray[1]),
      altitude: parseFloat(cameraStateArray[2]),
      distance: parseFloat(cameraStateArray[3]),
      heading: parseFloat(cameraStateArray[5]),
      tilt: parseFloat(cameraStateArray[6]),
    };
  }

  static initFonts(fontsServer: string) {
    axios({
      method: "get",
      url: "fonts.json",
      baseURL: fontsServer,
    }).then((response) => {
      let fontsList: Array<string> = response.data;
      let code = fontsList.reduce((accumulator, currentValue) => {
        return (
          accumulator +
          "@font-face { font-family:" +
          currentValue +
          ';src: url("' +
          fontsServer +
          currentValue +
          '.TTF"); }'
        );
      }, "");
      let myFont = document.createElement("style");
      myFont.setAttribute("rel", "stylesheet");
      myFont.appendChild(document.createTextNode(code));

      let head = document.getElementsByTagName("head")[0];
      head.appendChild(myFont);
    });
  }
}

export default Utils;
