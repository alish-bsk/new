document.addEventListener('DOMContentLoaded', function() {
    let image = document.getElementById("ad-imageone"); 

    let images = [
        "{% static 'image/samsun02.jpg' %}",
        "{% static 'image/newbal.jpg' %}",
        "{% static 'image/sc.jpg' %}",
    ];

    setInterval(function () {
        let rnd = Math.floor(Math.random() * images.length);
        image.src = images[rnd]; 
        console.log(`Changing image to: ${images[rnd]}`);
    }, 8000); 
});
