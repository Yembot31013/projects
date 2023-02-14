const webCamElement = document.getElementById("webcam");
const canvasElement = document.getElementById("canvas");
const link = document.getElementById("snap");

const webcams = new Webcam(webCamElement, "user", canvasElement);

webcams.start();

function snapWithCam() {
  var picture = webcams.snap();
  link.href = picture;
}

