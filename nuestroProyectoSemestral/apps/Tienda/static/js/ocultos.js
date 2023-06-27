function mostrarAdmin(){
  document.getElementById('ocultoSus').style.display = 'block';
  document.getElementById('ocultoAgregar').style.display = 'block';
  document.getElementById('ocultoUsuarios').style.display = 'block';
  var alertaHTML = '<div class="alert alert-info alert-dismissible fade show" role="alert">' +
                      'Has ingresado como Administrador.' +
                      '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
                        '<span aria-hidden="true">&times;</span>' +
                      '</button>' +
                    '</div>';
    $('#alertContainer').html(alertaHTML);
}
function mostrarUsuario(){
  document.getElementById('ocultoTienda').style.display = 'block';
}

/*Profe a la hora de que se muestren los li de cada usuario al hacerle click y ir a la ruta los otros desaparecen, lo intente arreglar de miles de forma pero 
ninguna me funciono asi que entendi que talvez se bugeo o algo porque minimo lo intente con 5 formas distintas y ninguna me sirvio ese es como el mayor error de 
ocultar los li asi que al ingresar nuevamente en ellos debe ir a iniciar sesion para que se visualizen */