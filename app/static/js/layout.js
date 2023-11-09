document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("myForm");

    // Manejar el evento de cambio en los radio buttons
    form.addEventListener("change", function() {
      // Enviar el formulario automáticamente al cambiar la opción
      form.submit();
    });
  });