  window.addEventListener('scroll', function () {
    const item = document.getElementById('carouselExampleAutoplaying');

    const scrollY = window.scrollY;
    

    if (scrollY > 100) { // Adjust this value as needed
      item.classList.add('visible');

    } else {
      item.classList.remove('visible');

    }
    



  });


window.addEventListener('scroll', function () {
    const itemre = document.getElementById('recomendation');

    const sectionTop = document.querySelector("#choose-us").offsetTop;
    const scrollY = window.scrollY;

if (window.scrollY >100) {      

      itemre.classList.add('visible');

    } else {
      itemre.classList.remove('visible');

    }
  

  });
