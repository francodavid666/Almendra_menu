
const opciones_button = document.getElementById('opciones_button')

opciones_button.addEventListener('click', ()=>{
  
  Swal.fire({
      'title':'¿Esta que quiere ir al menu de opciones?',
       'text':'Tienes que ser admnistrador para ingresar',
      'icon': 'question',
      'showCancelButton': 'true',
      'confirmButtonText': 'Aceptar',
      'cancelButtonText': 'Cancelar',
      'confirmButtonColor': '#bc3545',
  })
  .then (function(result) {
      if (result.isConfirmed){
          window.location.href = '/opciones/'
      }
  })
})