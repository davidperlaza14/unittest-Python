"""     Suma de N números

Escribe una función que pueda sumar números:

* Debe recibir una secuencia de n números.
* Si no se proporciona ningún argumento, devuelve la suma de los números 1..100.
* Fíjese bien en el tipo de argumento predeterminado de la función...


        Unit testing

Escribe dos pruebas al menos para:

* Verifique la salida con argumentos predeterminados
* Verifique la salida con diferentes valores

"""

def sum_numbers(numbers = None):
    if numbers == None:
        return sum(range(1, 101))
    return sum (numbers)

if __name__ == '__main__':
    sum_numbers()