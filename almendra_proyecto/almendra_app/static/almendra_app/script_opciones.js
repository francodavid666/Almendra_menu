let listElements = document.querySelectorAll('.list_button--click');

listElements.forEach(listElement =>{
  listElement.addEventListener('click',()=>{
    
    listElement.classList.toggle('arrow');

    let height = 0 ;
    let menu = listElement.nextElementSibling;
    
    if(menu.clientHeight =='0'){
      height = menu.scrollHeight;
    }
    menu.style.height= `${height}px`;
  })
})

const home_button = document.getElementById('home_button')

home_button.addEventListener('click', ()=>{
  
  Swal.fire({
      'title':'¿Esta seguro que quiere ir al menu publico?',
       
      'icon': 'question',
      'showCancelButton': 'true',
      'confirmButtonText': 'Aceptar',
      'cancelButtonText': 'Cancelar',
      'confirmButtonColor': '#008000',
  })
  .then (function(result) {
      if (result.isConfirmed){
          window.location.href = '/inicio/'
      }
  })
}

)


const galeriaContainer = document.querySelector('.galeria-container');
const galeriaControlesContainer = document.querySelector('galeria-controls');
const galeriaControles = ['previous', 'next'];
const galeriaItems =document.querySelectorAll('.galeria-item');


class Carousel{
  constructor(container,items,controls){
    this.carouselContainer  = container;
    this.carrouselControls = controls;
    this.carouselArray = [...items];
  }

  updateGallery(){
    this.carouselArray/forEach(el =>{
      el.classList.remove('galeria-item-1');
      el.classList.remove('galeria-item-2');
      el.classList.remove('galeria-item-3');
      el.classList.remove('galeria-item-4');
      el.classList.remove('galeria-item-5');
    });

  this.carouselArray.slice(0,5).forEach((el, i)=>{
    el.classList.add(`galeria-item-${i+1}`);
   });
  }

  setCurrentState(direction){
    if(direction.className =='galeria-controles-previous'){
      this.carrouselArray.unshift(this.carouselArray.pop());
    }else{
      this.carouselArray.push(this.carouselArray.shift());
    }
    this.updateGallery();
  }
  setControls(){
    this.carrouselControls.forEach(control=>{
      galeriaControlesContainer.appendChild(document.createElement('button')).className=`galeria-controles-${control}`
      document.querySelector(`.galeria-controles-${control}`).innerText = control;
    
    })
  }

  useControls(){
    const triggers = [...galeriaControlesContainer.childNodes];
    triggers.forEach(control =>{
      control.addEventListener('click',e =>{
        e.preventDefault();
        this.setCurrentState(control);
      });
    });
  }

}


const exampleCarousel = new Carousel(galeriaContainer,galeriaItems,galeriaControles);

exampleCarousel.setControls();
exampleCarousel.useControls();