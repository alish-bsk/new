  window.addEventListener('scroll', function () {
    const item = document.getElementById('scrollItem');
    const scrollY = window.scrollY;

    if (scrollY > 100) { // Adjust this value as needed
      item.classList.add('visible');
    } else {
      item.classList.remove('visible');
    }
    
  });

  window.addEventListener('scroll', function () {
    const item = document.getElementById('scrollItemBar');
    const scrollY = window.scrollY;

    if (scrollY > 1400) { // Adjust this value as needed
      item.classList.add('visible');
    } else {
      item.classList.remove('visible');
    }
    
  });

  window.addEventListener('scroll', function () {
    const item = document.getElementById('scrollItemInf');
    const scrollY = window.scrollY;

    if (scrollY > 2200) { // Adjust this value as needed
      item.classList.add('visible');
    } else {
      item.classList.remove('visible');
    }
    
  });