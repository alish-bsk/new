document.addEventListener('DOMContentLoaded', function() {
    let image = document.getElementById("ad-imageone"); 

    let images = [
        image.getAttribute('data-img1'),
        image.getAttribute('data-img2'),
        image.getAttribute('data-img3'),
    ];
    setInterval(function () {
        let rnd = Math.floor(Math.random() * images.length);
        image.src = images[rnd]; 
        console.log(`Changing image to: ${images[rnd]}`);
    }, 6000); 
});
