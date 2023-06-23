const apiKey = 'AIzaSyATQCJZsLQ9OYPoSthIVOlP-dBBdinsrJk'; // Reemplaza 'YOUR_API_KEY' con tu clave de API de YouTube

fetch('https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${videoId}&key=${AIzaSyATQCJZsLQ9OYPoSthIVOlP-dBBdinsrJk}')
  .then(response => response.json())
  .then(data => {
    // Procesar los datos de respuesta (título, descripción, etc.)
    console.log(data); // Puedes imprimir los datos en la consola para verificarlos
  })
  .catch(error => {
    console.error('Error al obtener detalles del video:', error);
  });
// Variable para almacenar el ID del video de YouTube //heeey hola , nada, dice que te asegures que la api este abierta :0
  var videoId = ''; 

document.getElementById('live-link').addEventListener('click', function(event) {
  event.preventDefault(); 

// Crea el reproductor de YouTube después de API
  onYouTubeIframeAPIReady();
});

// Función para crear el reproductor de YouTube
function onYouTubeIframeAPIReady() {
// Crea el reproductor de YouTube en contenedor
  var player = new YT.Player('player-container', {
    height: '360',
    width: '640',
    videoId: videoId,
    playerVars: {
      autoplay: 0, 
      controls: 1, 
      modestbranding: 1, 
      showinfo: 0, 
      rel: 0 
    }
  })};