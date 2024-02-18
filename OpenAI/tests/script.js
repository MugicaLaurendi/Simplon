function allowDrop(ev) {
  ev.preventDefault();
  console.log(ev);
  console.log("allowdrop");
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
  console.log("drag");
}

function drop(ev) {
  ev.preventDefault();
  console.log("ok");
  var data = ev.dataTransfer.getData();
  console.log(data);

}

function translator(file){

  localStorage.file = file;

  document.getElementById("result").innerHTML = localStorage.file;
}
