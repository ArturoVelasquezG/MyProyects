//Practica, concentrate y sigue :D
var miVariable = "Hola soy una variable";
console.log(miVariable);
miVariable = 1;
//las variables pueden cambiar
console.log(miVariable); 


var a = 5; //iniciar la variable es: darle valor al inicio de asignarla
var b = a;
//las variables pueden ser asignadas a otras variables
console.log(a);
console.log(b);

var x; //esta es una variable no inicializada y dara "undefine"
x = 1;
console.log(x);

/*las variables se diferencian entre si por como se escribe, es decir,
en programación no es lo mismo SoyUnaVariable a soyunavariable.
Esto se conoce como: "Case-sencitive*/

var Var1;
Var1 = 5;
console.log(Var1); //se dejo igual nombre para evitar errores

/*en operaciones o al declarar valores o en ciclos deja un pequeño espacio
para una facil lectura*/

/*Operaciones*/
//suma
var suma = 7 + 12;
console.log("var suma: " + suma);

//restas
var resta = 15 - 5; //restas positivas
console.log("var resta: " + resta + " (valor positivo)");
resta = 5 -15; //restas negativas
console.log("var resta: " + resta + " (valor negativo)");
resta = 15 - 15; //restas a cero
console.log("var resta: " + resta + " (valor 0)");

//multiplicacion
var producto = 5 * 3;
console.log("var producto: " + producto);
producto = -5 * 6;
console.log("var producto: " + producto + " (producto negativa)");

//division
var cociente = 10 / 2;
console.log("var cociente: " + cociente);
cociente = 17 / 31;
console.log("var cociente: " + cociente + " (valor decimal)" );

//resto de una divisioo
var resto = 13 % 2;
console.log("var resto: " + resto);
