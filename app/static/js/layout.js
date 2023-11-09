document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("myForm");

    // Manejar el evento de cambio en los radio buttons
    form.addEventListener("change", function() {
      // Enviar el formulario automáticamente al cambiar la opción
      form.submit();
    });
  });

  document.getElementById("personaNatural").addEventListener("change", function() {
    document.getElementById("naturalForm").style.display = "block";
    document.getElementById("juridicaForm").style.display = "none";
});

document.getElementById("personaJuridica").addEventListener("change", function() {
    document.getElementById("naturalForm").style.display = "none";
    document.getElementById("juridicaForm").style.display = "block";
});

function agregarPersona() {
    // Lógica para agregar persona según el formulario visible
    const tipoPersona = document.querySelector('input[name="tipoPersona"]:checked').value;

    if (tipoPersona === 'natural') {
        // Lógica para agregar persona natural
        const tipoIdentificacion = document.getElementById("tipoIdentificacion").value;
        // Resto de la lógica para persona natural
    } else {
        // Lógica para agregar persona jurídica
        const razonSocial = document.getElementById("razonSocial").value;
        // Resto de la lógica para persona jurídica
    }

    // Actualizar la lista en la interfaz de usuario
    mostrarPersonasRegistradas();

    // Limpiar el formulario
    document.getElementById("personForm").reset();
}

function mostrarPersonasRegistradas() {
    const personList = document.getElementById("personList");
    personList.innerHTML = "";

    // Lógica para mostrar personas registradas
}