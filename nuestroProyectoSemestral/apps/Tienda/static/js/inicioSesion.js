document.getElementById("valUsuario").style.display = "none";
document.getElementById("valContraseña").style.display = "none";

function validar(){
    if (document.getElementById("txtUsuario").value.length == 0) {
        document.getElementById("valUsuario").style.display = "inline";
        document.getElementById("txtUsuario").classList.add("is-invalid");
    }else{
        document.getElementById("valUsuario").style.display = "none";
        document.getElementById("txtUsuario").classList.remove("is-invalid");
        document.getElementById("txtUsuario").classList.add("is-valid");
    }


    if (document.getElementById("txtContraseña").value.length == 0) {
        document.getElementById("valContraseña").style.display = "inline";
        document.getElementById("txtContraseña").classList.add("is-invalid");
    }else{
        document.getElementById("valContraseña").style.display = "none";
        document.getElementById("txtContraseña").classList.remove("is-invalid");
        document.getElementById("txtContraseña").classList.add("is-valid");
    }


    
}