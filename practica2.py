opcion = 0

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def salir():
    return "Saliendo.."

def main():
   n1 = int(input("Ingrese su primer número: "))
   n2 = int(input("Ingrese su segundo número: "))
   opcion = int(input("Seleccione una de las opciones \n1.Suma\n2.Resta\n3.Multiplicación\n4.Division\n5.Salir\n"))
   if opcion == 1:
       print("El resultado es: ",sumar(n1,n2))
   if opcion == 2:
       print("El resultado es: ",restar(n1,n2))
   if opcion == 3:
       print("El resultado es: ",multiplicar(n1,n2))
   if opcion == 4:
      print("El resultado es: ",dividir(n1,n2))
   if opcion == 5:
       print(salir())


main()