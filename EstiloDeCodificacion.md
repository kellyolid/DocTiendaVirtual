# DocTiendaVirtual
Estilo de codificación 
•	Clases
La primera letra del nombre de todas las clases debe estar escrita con mayúscula.
Si existiese la necesidad de utilizar más de una palabra para nombrar la clase, las palabras serán unidas y todas las palabras despues de la primera seran diferenciadas por tener la primera letra en mayúscula. (Ej.: NombreClase)
•	Variables globales
La primera letra de las variables deben ser en mayúscula y si se necesita el uso de más de una palabra, estas serán separadas por un guion bajo.
•	Funciones
Las funciones deben ir en minúsculas, si se necesitase el uso de más de una palabra, se escribiran juntas y todas las palabras despues de la primera seran diferenciadas por tener la primera letra en mayúscula. (Ej.: getNombre)
•	Estructuras de control
•	Ciclos
•	Comentarios
•	Importaciones
Las importaciones de librerías deben ir en líneas separadas.
•	Salto de línea 
Antes de un operador binario y no después para que los operadores coincidan con los operandos.
Ej.:
ingresos = (gross_wages
          + taxable_interest
          + (dividendos - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
•	Comillas
Las cadenas de caracteres estarán siempre entre comillas simples.
•	Espacios en blanco en expresiones y declaraciones
Evitar los espacios en blanco extraños en las siguientes situaciones:
-	Inmediatamente dentro paréntesis, corchetes o llaves.
Yes: spam(ham[1], {eggs: 2})
No:  spam( ham[ 1 ], { eggs: 2 } )

-	Entre una coma final y un siguiente paréntesis cerca.
Yes: foo = (0,)
No:  bar = (0, )

-	Inmediatamente antes de una coma o punto y coma,:
Yes: if x == 4: print x, y; x, y = y, x
No:  if x == 4 : print x , y ; x , y = y , x

-	Inmediatamente antes del paréntesis de apertura que se inicia la lista de argumentos de una llamada de función:
Yes: spam(1)
No:  spam (1)

-	Inmediatamente antes del paréntesis de apertura que se inicia una indexación o el corte:
Yes: dct['key'] = lst[index]
No:  dct ['key'] = lst [index]

-	Más de un espacio alrededor de una asignación (u otro) del operador para alinear con otro.
Sí:
x = 1
y = 2
long_variable = 3
No:
x             = 1
y             = 2
long_variable = 3

-	Si se utilizan los operadores con diferentes prioridades, considerar la adición de un espacio en blanco alrededor de los operadores con la prioridad más baja (es). Use su propio juicio; Sin embargo, nunca utilice más de un espacio, y siempre tienen la misma cantidad de espacio en blanco en ambos lados de un operador binario.

Sí:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
No:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

