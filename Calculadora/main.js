const displayValorAnterior = document.getElementById('valor-anterior');
const displayValorActual = document.getElementById('valor-actual');
const botonesNumeros = document.querySelectorAll('.Numero');
const botonesOperadores = document.querySelectorAll('.Operador');

const display = new Display(displayValorAnterior, displayValorActual);
botonesNumeros.forEach(boton =>{
    boton.addEventListener('click',() => display.agregarNumero(boton.innerHTML));
});

botonesOperadores.forEach(boton =>{
    boton.addEventListener('click', () => display.computar(boton.value))
});