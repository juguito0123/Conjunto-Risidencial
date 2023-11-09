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

function agregarPersona() {
  // Obtener los datos del formulario
  var tipoPersona = document.querySelector('input[name="tipoPersona"]:checked').value;
  var tipoIdentificacion = document.getElementById('tipoIdentificacion').value;
  var nombres = document.getElementById('nombres').value;
  var apellidos = document.getElementById('apellidos').value;
  var razonSocial = document.getElementById('razonSocial').value;
  var numeroContacto = document.getElementById('contacto').value;
  var correoElectronico = document.getElementById('email').value;
  var ciudad = document.getElementById('ciudad').value;
  var apartamento = document.getElementById('apartamento').value;

  // Crear un objeto con los datos del formulario
  var datosResidente = {
      tipoPersona: tipoPersona,
      tipoIdentificacion: tipoIdentificacion,
      nombres: nombres,
      apellidos: apellidos,
      razonSocial: razonSocial,
      numeroContacto: numeroContacto,
      correoElectronico: correoElectronico,
      ciudad: ciudad,
      apartamento: apartamento
  };

  // Enviar los datos al servidor mediante una solicitud AJAX
  fetch('/procesar_formulario', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(datosResidente),
  })
  .then(response => response.json())
  .then(data => {
      // Hacer algo con la respuesta del servidor, si es necesario
      console.log(data);
  })
  .catch((error) => {
      console.error('Error:', error);
  });
}