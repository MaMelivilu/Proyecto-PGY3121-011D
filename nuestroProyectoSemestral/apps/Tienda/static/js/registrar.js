$(function(){
    $("#registrarse").validate({
        rules:{
            nombre:{
                required: true,
                minlength: 3
            },
            apellido:{
                required: true,
                minlength: 4
            },
            usuario:{
                required: true,
                minlength: 5
            },
            correo:{
                required: true,
                minlength: 7
            },
            contraseña:{
                required: true,
                minlength: 10
            },
            confirmar:{
                required: true,
                minlength: 10
            }
        },
        messages:{
            nombre:{
                required: "Debe ingresar su Nombre.",
                minlength: "Debe ingresar minimo 3 caracteres."
            },
            apellido:{
                required: "Debe ingresar su Apellido.",
                minlength: "Debe ingresar minimo 4 caracteres."
            },
            usuario:{
                required: "Debe ingresar un Usuario.",
                minlength: "Debe ingresar minimo 5 caracteres."
            },
            correo:{
                required: "Debe ingresar un Correo.",
                minlength: "Debe ingresar minimo 7 caracteres."
            },
            contraseña:{
                required: "Debe ingresar su Contraseña.",
                minlength: "Debe ingresar minimo 10 caracteres."
            },
            confirmar:{
                required: "Debe confirmar su Contraseña.",
                minlength: "Debe ingresar minimo 10 caracteres."
            }
        }
    })
})

