// recuperation du fichier en drag and drop
const dropZone = document.getElementById('drop-zone');

dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.style.backgroundColor = '#e2e2e2';
});

dropZone.addEventListener('dragleave', (e) => {
  e.preventDefault();
  dropZone.style.backgroundColor = '#f8f8f8';
});

dropZone.addEventListener('drop', (e) => {
  console.log("ok");
  e.preventDefault();
  dropZone.style.backgroundColor = '#f8f8f8';

  const files = e.dataTransfer.files;
  const file = files[0];
  console.log(file.type);
  console.log(file.name);
  
  //transformation du fichier pour le trnasmettre a l'api

  

  // transmission du fichier a l'api

  fetch('http://127.0.0.1:8000/traductor/${file}')
  .then(function(response) {
    if (response.ok) {
      return response.json();
    }
    throw new Error('Erreur de réseau.');
  })
  .then(function(data) {
    // Traitez la réponse de l'API ici
    console.log(data);
  })
  .catch(function(error) {
    // Gérez les erreurs ici
    console.log(error);
  });


});
