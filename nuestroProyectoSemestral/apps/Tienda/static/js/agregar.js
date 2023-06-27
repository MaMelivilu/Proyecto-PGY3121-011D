/* var selectedRow = null;

//show alerts
function showAlert(message, className){
    const div = document.createElement("div");
    div.className = `alert alert-${className}`;
    
    div.appendChild(document.createTextNode(message));
    const container = document.querySelector(".container");
    const main = document.querySelector(".main");
    container.insertBefore(div, main);

    setTimeout(() => document.querySelector(".alert").remove(), 3000);

}

function clearFields(){
    document.querySelector("#idProducto").value = "";
    document.querySelector("#producto").value = "";
    document.querySelector("#precio").value = "";
}

document.querySelector("#product-form").addEventListener("submit", (e) =>{
    e.preventDefault();

    const idProducto = document.querySelector("#idProducto").value;
    const producto = document.querySelector("#producto").value;
    const precio = document.querySelector("#precio").value;

    if(idProducto == "" || producto == "" || precio == ""){
        showAlert("Por favor, rellene todas las casillas.", "danger");
    }
    else{
        if(selectedRow == null){
            const list = document.querySelector("#product-list");
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${idProducto}</td>
                <td>${producto}</td>
                <td>${precio}</td>
                <td>
                <a href="#" class="btn btn-warning btn-sm edit">Edit</a>
                <a href="#" class="btn btn-danger btn-sm delete">Delete</a> 
            `;
            list.appendChild(row);
            selectedRow = null;
            showAlert("Producto agregado", "success");
        }
        else{
            selectedRow.children[0].textContent = idProducto;
            selectedRow.children[1].textContent = producto;
            selectedRow.children[2].textContent = precio;
            selectedRow = null;
            showAlert("Informacion del producto editada", "info");
        }
        clearFields();
    }
});

document.querySelector("#product-list").addEventListener("click", (e) =>{
    target = e.target;
    if(target.classList.contains("edit")){
        selectedRow = target.parentElement.parentElement;
        document.querySelector("#idProducto").value = selectedRow.children[0].textContent;
        document.querySelector("#producto").value = selectedRow.children[1].textContent;
        document.querySelector("#precio").value = selectedRow.children[2].textContent;
    }
});

document.querySelector("#product-list").addEventListener("click", (e) =>{
    target = e.target;
    if(target.classList.contains("delete")){
        target.parentElement.parentElement.remove();
        showAlert("Datos del producto eliminados", "danger");
    }
});

 */




const formulario = document.getElementById("formularioAgregarProducto");

formulario.addEventListener('submit',function(evento){
    evento.preventDefault();

    if (document.getElementById("txtSku").value.length == 0) {
        alert("Debe ingresar el codigo del producto.")
        return;
    }else{
        this.submit();
    }

})