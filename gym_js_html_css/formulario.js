(function(){
    var formulario = document.getElementsByName('formulario')[0],
      elementos = formulario.elements,
      boton = document.getElementById('btn');
    var validarNombre = function(e) {
      if (formulario.nombre.value == 0){
        alert("Completa el campo Nombre");
        e.preventDefault();
      }
    }

    var validarApellido = function(e) {
      if (formulario.apellido.value == 0){
        alert("Completa el campo Apellido");
        e.preventDefault();
      }
    }

    var validarTelefono = function(e) {
      if (formulario.tel.value == 0){
        alert("Debe dejar un numero de Contacto");
        e.preventDefault();
      }
    }

    var validarMail = function(e) {
      if (formulario.mail.value == 0){
        alert("Debe dejar un mail de Contacto");
        e.preventDefault();
      }
    }

    var validarClase = function(e) {
      if (formulario.clase[0].checked == true || formulario.clase[1].checked == true || formulario.clase[3].checked == true || formulario.clase[4].checked == true || formulario.clase[5].checked == true || formulario.clase[6].checked == true || formulario.clase[7].checked == true){
      }else{
        alert("Debe seleccionar una clase");
        e.preventDefault();
      }
    }

    var validarTerminos = function(e) {
      if (formulario.terminos.checked == true ){
      }else{
        alert("Debe aceptar los Terminos y Condiciones");
        e.preventDefault();
      }
    }

    var validar = function(e) {
      validarNombre(e);
      validarApellido(e);
      validarTelefono(e);
      validarMail(e);
      validarClase(e);
      validarTerminos(e);
    };

    formulario.addEventListener("submit", validar);

  }())