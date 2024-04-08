//Efecto de Code de texto de navbar

const text = "<Soy Francisco Clavería.....</>"; // Texto a escribir
const speed = 100; // Velocidad de escritura (en milisegundos)
let i = 0;

function typeWriter() {
  if (i < text.length) {
    document.getElementById("typed-text").innerHTML += text.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  } else {
    // Reiniciar la animación después de 10 segundos
    setTimeout(function() {
      // Reiniciar el índice y limpiar el contenido del elemento
      i = 0;
      document.getElementById("typed-text").innerHTML = "";
      // Volver a llamar a typeWriter para iniciar la animación nuevamente
      typeWriter();
    }, 10000); // 10 segundos en milisegundos
  }
}

// Iniciar la animación cuando el documento esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
  typeWriter();
});



document.addEventListener("DOMContentLoaded", function() {
  window.onscroll = function() {scrollFunction()};

  function scrollFunction() {
      var scrollToTopBtn = document.getElementById("scrollToTopBtn");
      if (scrollToTopBtn) {
          if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
              scrollToTopBtn.style.display = "block";
          } else {
              scrollToTopBtn.style.display = "none";
          }
      }
  }

  var scrollToTopBtn = document.getElementById("scrollToTopBtn");
  if (scrollToTopBtn) {
      scrollToTopBtn.addEventListener("click", function() {
          document.body.scrollTop = 0;
          document.documentElement.scrollTop = 0;
      });
  }
});
