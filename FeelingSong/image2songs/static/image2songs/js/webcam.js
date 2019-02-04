var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var video = document.getElementById('video');
var snap = document.getElementById('snap');
var confirmar = document.getElementById("confirmar")

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({
        video: true
    }).then(function (stream) {
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
        confirmar.style.display = "none";
    } else {
        canvas.style.display = "block";
        video.style.display = "none";
        confirmar.style.display = "block";

    }
});

confirmar.addEventListener("click", function () {
    var dataURL = canvas.toDataURL("image/png;base64");
    var canvasImg=document.getElementById('canvasImg');
    canvasImg.src = dataURL;
    confirmar.href=dataURL;
    /*$(document).ready(function() {
        $.ajax({
            method: 'POST',
            url: 'process_image/',
            data: {'imageUrl': dataURL},
        });
    });*/   
});