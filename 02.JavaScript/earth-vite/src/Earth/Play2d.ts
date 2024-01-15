import { DataMedia, DataMedia2dProp } from "./Interface/DataMedia";

class Play2d {
  public displayImage: (media?: string, media_prop?: string) => void;
  public displayVideo: (media?: string, media_prop?: string) => void;
  public displayText: (media?: string, media_prop?: string) => void;
  public createMediaContainer: (
    dataMedia: DataMedia,
    dataMediaProp: DataMedia2dProp
  ) => HTMLDivElement;
  protected moveToSideOrRemove: (
    dataMedia: DataMedia,
    dataMediaProp: DataMedia2dProp,
    mediaContainer: Element
  ) => void;

  constructor() {
    this.createMediaContainer = (dataMedia, dataMediaProp) => {
      let mediaContainer = document.createElement("div");
      mediaContainer.style.display = "block";
      mediaContainer.style.position = "absolute";
      mediaContainer.style.textAlign = "center";
      mediaContainer.style.pointerEvents = "None";
      mediaContainer.style.opacity = dataMediaProp.opacity.toString();
      if (dataMediaProp.full_screen === 1) {
        mediaContainer.style.width = window.outerWidth.toString().concat("px");
        mediaContainer.style.height = window.outerHeight
          .toString()
          .concat("px");
        mediaContainer.style.backgroundColor = "#000000";
      } else {
        mediaContainer.style.left = dataMediaProp.left + "%";
        if (dataMedia.media_type !== "text") {
          mediaContainer.style.top = dataMediaProp.top + "%";
        }
        mediaContainer.style.width = (
          (window.outerWidth / 100) *
          dataMediaProp.width
        )
          .toString()
          .concat("px");
        mediaContainer.style.height = (
          (window.outerHeight / 100) *
          dataMediaProp.height
        )
          .toString()
          .concat("px");
        mediaContainer.style.marginLeft = (
          -((window.outerWidth / 100) * dataMediaProp.width) / 2
        )
          .toString()
          .concat("px");
        if (dataMedia.media_type === "image") {
          mediaContainer.style.marginTop = (
            -((window.outerWidth / 100) * dataMediaProp.width) /
            dataMediaProp.aspect /
            2
          )
            .toString()
            .concat("px");
        }
      }
      let mediaIdAttr = document.createAttribute("id");
      mediaContainer.setAttributeNode(mediaIdAttr);
      return mediaContainer;
    };
    this.moveToSideOrRemove = (dataMedia, dataMediaProp, mediaContainer) => {
      let media_time = dataMedia.media_time;
      if (!media_time) {
        media_time = dataMedia.subtitle_time;
      }
      window.setTimeout(() => {
        if (mediaContainer.parentElement) {
          let toSideElement =
            mediaContainer.parentElement.removeChild(mediaContainer);
          if (dataMediaProp.keep) {
            console.log(toSideElement);
          }
        }
      }, media_time * 1000);
    };
    this.displayImage = (media = "", media_prop = "") => {
      if (media && media_prop) {
        let dataMedia: DataMedia = JSON.parse(media);
        let dataMediaProp: DataMedia2dProp = JSON.parse(media_prop);
        let image = document.createElement("img");
        if (dataMediaProp.full_screen) {
          image.style.width = ((window.outerWidth / 100) * dataMediaProp.width)
            .toString()
            .concat("px");
          image.style.top = "50%";
          image.style.position = "relative";
          image.style.marginTop = (
            -((window.outerWidth / 100) * dataMediaProp.width) /
            dataMediaProp.aspect /
            2
          )
            .toString()
            .concat("px");
        } else {
          image.style.width = "100%";
        }

        image.style.overflow = "visible";
        image.src = dataMediaProp.file;
        let mediaContainer = this.createMediaContainer(
          dataMedia,
          dataMediaProp
        );
        mediaContainer.appendChild(image);
        const bodyElement = document.querySelector("body");
        if (bodyElement) {
          bodyElement.appendChild(mediaContainer);
        }
        this.moveToSideOrRemove(dataMedia, dataMediaProp, mediaContainer);
      } else {
        console.log("displayImage data is Empty");
      }
    };
    this.displayVideo = (media = "", media_prop = "") => {
      if (media && media_prop) {
        let dataMedia: DataMedia = JSON.parse(media);
        let dataMediaProp: DataMedia2dProp = JSON.parse(media_prop);
        let mediaContainer = this.createMediaContainer(
          dataMedia,
          dataMediaProp
        );
        let video = document.createElement("video");
        video.autoplay = true;
        video.muted = true;
        video.loop = true;
        video.style.width = "100%";
        video.src = dataMediaProp.file;
        mediaContainer.appendChild(video);
        const bodyElement = document.querySelector("body");
        if (bodyElement) {
          bodyElement.appendChild(mediaContainer);
        }
        if (dataMediaProp.full_screen === 0) {
          let marginTop = -mediaContainer.clientHeight / 2;
          video.style.marginTop = marginTop.toString().concat("px");
        } else {
          let clientHeight = video.clientHeight;
          let paddingTop = window.outerHeight - clientHeight;
          console.log(clientHeight, window.outerHeight, paddingTop);
          video.style.paddingTop = paddingTop.toString().concat("px");
        }

        this.moveToSideOrRemove(dataMedia, dataMediaProp, mediaContainer);
      } else {
        console.log("displayVideo data is Empty");
      }
    };
    this.displayText = (media = "", media_prop = "") => {
      if (media && media_prop) {
        let dataMedia: DataMedia = JSON.parse(media);
        let dataMediaProp: DataMedia2dProp = JSON.parse(media_prop);
        let text = document.createElement("span");
        text.style.color = "#".concat(dataMediaProp.font_color);
        text.style.fontSize = dataMediaProp.font_size;
        text.style.fontFamily = dataMediaProp.font;
        text.style.position = "relative";
        text.style.textShadow = "1px 1px 1px black";
        text.style.top = dataMediaProp.top + "%";
        text.innerText = dataMediaProp.file;
        let mediaContainer = this.createMediaContainer(
          dataMedia,
          dataMediaProp
        );
        mediaContainer.appendChild(text);
        mediaContainer.style.height = "100%";
        document.body.appendChild(mediaContainer);

        this.moveToSideOrRemove(dataMedia, dataMediaProp, mediaContainer);
      } else {
        console.log("displayText data is Empty");
      }
    };
  }
}

export default Play2d;
