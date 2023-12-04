
(function() {
    
const btnEliminacion = document.querySelectorAll(".btnEliminacion");

btnEliminacion.forEach(btn=>{
    btn.addEventListener('click', (e)=>{

        const confirmacion = confirm('¿seguro que quieres eliminar el libro?');
        if(!confirmacion){
            e.preventDefault();
            }   

        });
    });
})();