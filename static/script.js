
function startProgressBar() {
    var progressBar = document.getElementById('progressBar');
    var width = 1;
    var interval = setInterval(frame, 30);

    function frame() {
        if (width >= 100) {
            clearInterval(interval);
        } else {
            width++;
            progressBar.style.width = width + '%';
        }
    }
}
