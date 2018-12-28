// Elements for taking the snapshot
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var video = document.getElementById('video');
var snap = document.getElementById('snap');

// Get access to the camera!
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({
        video: true
    }).then(function (stream) {
        //video.src = window.URL.createObjectURL(stream);
        video.srcObject = stream;
        video.play();
    });
}

// Trigger photo take
document.getElementById("snap").addEventListener("click", function () {
    context.drawImage(video, 0, 0, 640, 480);
    if (canvas.style.display === "block") {
        canvas.style.display = "none";
        video.style.display = "block";
    } else {
        canvas.style.display = "block";
        video.style.display = "none";
    }
});