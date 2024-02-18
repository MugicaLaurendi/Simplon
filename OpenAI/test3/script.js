const form = document.getElementById("bob")
//const form = document.querySelector("#form")
form.addEventListener("click",(event)=>{
    event.preventDefault();
    console.log("coucou");
    new formData = 
    const myImage = document.querySelector('img');

    fetch(file)
    .then(function(response) {
      return response.blob();
    })
    .then(function(myBlob) {
      const objectURL = URL.createObjectURL(myBlob);
      myImage.src = objectURL;
    });
    
    //new formData
    //poster avec fetch dans mon dossier
    // fcth sur mon api
        // insertadjacenthtml before end
})
