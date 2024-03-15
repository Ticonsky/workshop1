# workshop1
Trabajo clase modelos de programación 1

Se requiere hacer un sistema para catalogar vehiculos , para hacerlo se crean 3 clases llamadas engine, propierties y 
vehicles, donde propierties tendra herencia de engine y vehivle tendra herencia de propierties 


__Clase Engine__

se define la clase engine que tendra los atributos ,

_name, typ(type engine), potency and weight_


__Clase propiedades__

se define la clase propiedades que tendra los atributos propios:


_Engine,chasis a o b ,model ,gas comsuption, year_


Ademas esta clase tiene herencia de la clase engine por que dentro de las propiedades de un vehiculo esta el motor 

en esta clase hay un atributo en particular que es chasis, este atributo puede tomar dos valores para lo que 
se hizo un condicional if que igualara una variable a un numero en este caso en 1 , si es asi entonces sera chasis A, de cualquier otra manera sera chasis B
__Clase vehicle__

Por ultimo se define la clase vehicle , que tendra los atributos de la clase properties por medio de herencia, la explicacion es la misma cada vehiculo tiene una serie de propiedades por ende se hereda 

al final se pone el metodo Vehicle.gasCompsuption, que definira cuanta gasolina gasta un vehiculo en particular

