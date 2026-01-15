import os

def saludar(nombre):
    """Función que saluda a la persona cuyo nombre se pasa como argumento"""
    return f"Hola, {nombre}!"
def sumar(a, b):
    """Función que devuelve la suma de dos números"""
    return a + b
os.system("cls")
saludar("Ana")
os.system("pause")


def main():
    os.system("cls")
    saludar("Juan")
    resultado_suma = sumar(5,7)
    print("La suma de 5 y 7 es:", resultado_suma)

if __name__ == "__main__":
    main()

