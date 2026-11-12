  window.addEventListener('scroll', function () {
    const item = document.getElementById('carouselExampleAutoplaying');
    const scrollY = window.scrollY;

    if (scrollY > 100) { // Adjust this value as needed
      item.classList.add('visible');
    } else {
      item.classList.remove('visible');
    }
    
  });
