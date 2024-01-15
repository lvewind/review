///<reference path = "Interface/Module.d.ts" />

class Control {
  static getCurrentCameraStateUrl() {
    // return window.Module.StateUrlPresenter_GetCurrentCameraStateUrl();
    let urlPath = window.localStorage.getItem("earth.CameraStateUrlPath");
    if (urlPath) {
      return urlPath;
    }
    return "";
  }

  static showEarthUi(opacity = "0") {
    let ui = <HTMLElement>(
      document.querySelector(
        "flt-scene-host > flt-scene > flt-canvas-container:nth-child(5) > canvas"
      )
    );
    if (ui) {
      ui.style.opacity = opacity;
    }
  }

  static getCameraPosition(): any {
    let sr = document.getElementsByTagName("Earth-app")[0].shadowRoot;
    let coordinates = sr!
      .getElementById("earth-relative-elements")!
      .children[4].shadowRoot!.getElementById("coordinates");
    if (coordinates) {
      let cameraAltitude = coordinates.children[0].innerHTML;
      let pointerCoordinates = coordinates.children[2].children[0].innerHTML;
      let pointerElevation = coordinates.children[2].children[2].innerHTML;
      return {
        camera_altitude: cameraAltitude,
        pointer_coordinates: pointerCoordinates,
        pointer_elevation: pointerElevation,
      };
    }
  }

  static openSearch() {
    document
      .getElementsByTagName("Earth-app")[0]
      .shadowRoot!.getElementById("toolbar")!
      .shadowRoot!.getElementById("search")!
      .click();
  }

  static searchPlace(place: any) {
    if (place !== null) {
      let search_omnibox = document
        .getElementsByTagName("Earth-app")[0]
        .shadowRoot!.getElementById("drawer-container")!
        .shadowRoot!.getElementById("search")!
        .shadowRoot!.getElementById("omnibox");

      let input_el = search_omnibox!
        .shadowRoot!.querySelector(".layout.horizontal.flex")!
        .querySelector("input");
      let evt = document.createEvent("HTMLEvents");
      evt.initEvent("input", true, true);
      input_el!.value = place;
      input_el!.dispatchEvent(evt);

      search_omnibox!
        .shadowRoot!.getElementById("search-button")!
        .shadowRoot!.getElementById("ripple")!
        .click();
    }
  }

  static clearSearchInput() {
    let search_omnibox = document
      .getElementsByTagName("Earth-app")[0]
      .shadowRoot!.getElementById("drawer-container")!
      .shadowRoot!.getElementById("search")!
      .shadowRoot!.getElementById("omnibox");
    search_omnibox!
      .shadowRoot!.getElementById("trailing-buttons")!
      .querySelector("#clear-button")!
      .shadowRoot!.getElementById("ripple")!
      .click();
    search_omnibox!
      .shadowRoot!.getElementById("trailing-buttons")!
      .querySelector("#hide-button")!
      .shadowRoot!.getElementById("ripple")!
      .click();
  }

  static flyToLla(longitude: number, latitude: number, altitude: number) {
    window.Module.NavGlobePresenter_FlyToLatLng(latitude, longitude, altitude);
  }

  static closeCurrentSearch() {
    let knowledgeCard = document
      .getElementsByTagName("Earth-app")[0]
      .shadowRoot!.getElementById("knowledge-card");
    if (knowledgeCard) {
      knowledgeCard.hidden = true;
      // knowledgeCard.parentNode.removeChild(knowledgeCard)
      knowledgeCard
        .shadowRoot!.getElementById("top-card")!
        .shadowRoot!.getElementById("close")!
        .shadowRoot!.getElementById("ripple")!
        .click();
    }

    this.clearSearchInput();
  }

  static playTour() {
    // document.querySelector("earth-app")
    //     .shadowRoot.getElementById("tour-player")
    //     .shadowRoot.getElementById("play")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.TourPresenter_PlayTour();
  }

  static pauseTour() {
    // document.querySelector("earth-app")
    //     .shadowRoot.getElementById("tour-player")
    //     .shadowRoot.getElementById("play")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.TourPresenter_PauseTour();
  }

  static restartTour() {
    // document.querySelector("earth-app")
    //     .shadowRoot.getElementById("tour-player")
    //     .shadowRoot.getElementById("play")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.TourPresenter_RestartTour();
  }

  static getTourCurrentTime() {
    // document.querySelector("earth-app")
    //     .shadowRoot.getElementById("tour-player")
    //     .shadowRoot.getElementById("play")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.TourPresenter_GetCurrentTime();
  }

  static getTourDuration() {
    // document.querySelector("earth-app")
    //     .shadowRoot.getElementById("tour-player")
    //     .shadowRoot.getElementById("play")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.TourPresenter_GetTourDuration();
  }

  static playNextPage() {
    // document.querySelector("earth-app")
    //     .shadowRoot.getElementById("play-mode-controller")
    //     .shadowRoot.getElementById("next-button")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.PlayModePresenter_ShowNextFeature();
  }

  static playPrevPage() {
    // document.querySelector("earth-app")
    //     .shadowRoot.getElementById("play-mode-controller")
    //     .shadowRoot.getElementById("prev-button")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.PlayModePresenter_ShowPreviousFeature();
  }

  static stopPlay() {
    // document.querySelector("earth-app")
    //     .shadowRoot.getElementById("play-mode-controller")
    //     .shadowRoot.getElementById("prev-button")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.PlayModePresenter_Stop();
  }

  static restartPlay() {
    // document.querySelector("earth-app")
    //     .shadowRoot.getElementById("play-mode-controller")
    //     .shadowRoot.getElementById("prev-button")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.PlayModePresenter_Restart();
  }

  static setView3d() {
    // document.querySelector("earth-app")!.shadowRoot.getElementById("hover-button")
    //     .shadowRoot.getElementById("hover-button")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.HoverButtonPresenter_TransitionViewTo3D();
  }

  static setView2d() {
    // document.querySelector("earth-app")!.shadowRoot.getElementById("hover-button")
    //     .shadowRoot.getElementById("hover-button")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.HoverButtonPresenter_TransitionViewTo2D();
  }

  static isView3d(): any {
    let svg_2d =
      "M11.142 17v-1.73H6.496l2.456-2.59c.673-.737 1.148-1.382 1.425-1.937.277-.554.416-1.098.416-1.632 0-.975-.308-1.73-.924-2.264-.616-.535-1.48-.802-2.594-.802-.727 0-1.378.155-1.952.464a3.322 3.322 0 00-1.332 1.28 3.543 3.543 0 00-.471 1.804h2.152c0-.544.14-.983.42-1.317.279-.334.661-.501 1.146-.501.45 0 .797.137 1.039.412.242.274.364.651.364 1.131 0 .352-.115.723-.345 1.114-.23.39-.586.848-1.066 1.373L3.735 15.53V17h7.407zm4.89 0c.946-.005 1.794-.223 2.547-.653a4.438 4.438 0 001.747-1.818c.414-.782.62-1.675.62-2.68v-.497c0-1.004-.21-1.901-.63-2.69a4.477 4.477 0 00-1.756-1.826c-.75-.428-1.6-.642-2.55-.642h-3.324V17h3.347zm-.044-1.789h-1.076V7.997h1.099c.875 0 1.54.284 1.996.85.455.567.683 1.4.683 2.498v.571c-.01 1.059-.245 1.873-.705 2.442-.46.569-1.126.853-1.997.853z";
    if (
      document
        .getElementsByTagName("earth-app")[0]
        .shadowRoot!.getElementById("hover-button")!
        .shadowRoot!.getElementById("hover-button")!
        .shadowRoot!.getElementById("icon")!
        .shadowRoot!.querySelector("path")!
        .getAttribute("a") === svg_2d
    ) {
      return true;
    }
  }

  static zoomToSpace() {
    // document.querySelector("earth-app")!.shadowRoot.getElementById("nav-globe")
    //     .shadowRoot.getElementById("globe")!.click()
    window.Module.NavGlobePresenter_ResetToSpaceView();
  }

  static setCompassAllReset() {
    // document.querySelector("earth-app")!.shadowRoot.getElementById("compass")
    //     .shadowRoot.getElementById("compass-icon")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.CompassPresenter_ResetAll();
  }

  static setCompassHeadingReset() {
    window.Module.CompassPresenter_ResetHeading();
  }

  static setCompassTiltReset() {
    window.Module.CompassPresenter_ResetTilt();
  }

  static setCompassHeading(a: any, b: number) {
    window.Module.CompassPresenter_SetHeading(a, b);
  }

  static setCompassTitle(a: any, b: number) {
    window.Module.CompassPresenter_SetTilt(a, b);
  }

  static showStreetView() {
    // document.querySelector("earth-app")!.shadowRoot.getElementById("street-view")
    //     .shadowRoot.getElementById("pegman-icon")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.StreetViewPresenter_SetCoverageOverlayVisible(1);
  }

  static hideStreetView() {
    // document.querySelector("earth-app")!.shadowRoot.getElementById("street-view")
    //     .shadowRoot.getElementById("pegman-icon")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.StreetViewPresenter_SetCoverageOverlayVisible(0);
  }

  static leaveStreetView() {
    // document.querySelector("earth-app")!.shadowRoot.getElementById("street-view")
    //     .shadowRoot.getElementById("pegman-icon")
    //     .shadowRoot.getElementById("icon")!.click()
    window.Module.StreetViewPresenter_LeaveStreetView();
  }

  static KeyboardEnterStreetView(lat: any, lon: any) {
    window.Module.StreetViewPresenter_KeyboardEnterStreetView(lat, lon);
  }

  static SetMemoryCacheSize(cacheSize = "4096") {
    window.Module.SettingsPresenter_SetValue("MemoryCacheSize", cacheSize);
  }

  static SetLatLngFormatting(format = "decimal") {
    window.Module.SettingsPresenter_SetValue("LatLngFormatting", format);
  }

  static SetFlySpeed(speed = "2") {
    window.Module.SettingsPresenter_SetValue("FlySpeed", speed);
  }

  static EarthSettingSync() {
    window.Module.SettingsPresenter_Sync();
  }

  static setEarthStyle(style = 0) {
    window.Module.BaseLayerPresenter_SetBaseLayerStyle(style);
  }

  static load_kml(kml_uri = "") {
    if (kml_uri) {
      window.Module.MyPlacesPresenter_OpenKmlFromUri(kml_uri);
      setTimeout(window.Module.NavGlobePresenter_StopCameraMotion, 60);
      setTimeout(window.Module.NavGlobePresenter_StopCameraMotion, 100);
      setTimeout(window.Module.NavGlobePresenter_StopCameraMotion, 150);
    }
  }
}

export default Control;
