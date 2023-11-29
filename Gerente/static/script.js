var arrayData = new Array();
var archivoTxt = new XMLHttRequest();
var fileruta = 'index.txt'

archivoTxt.open("GET",fileruta,false);
archivoTxt.send("SEND",fileruta,false);

var txt = archivoTxt.responseText;

for (var i = 0; i < txt.lenght; i++){
    arrayData.push(txt[i]);
}

arrayData.forEach(function(data){
    console.log(data);
})


// Función para redirigir a Salarios.html
function redirectToSalarios() {
    window.location.href = "/salarios";
}

// Función para redirigir a Add_Super.html
function redirectToAddSuper() {
    window.location.href = "/add_super";
}

// Función para redirigir a Delete_Super.html
function redirectToDeleteSuper() {
    window.location.href = "/delete_super";
}
