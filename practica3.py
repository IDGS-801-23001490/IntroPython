x = int(input("Dame el numero del cual quieres la tabla de multiplicar: "))

for i in range(1,11,1):
    resultado = (i*x)
    print(x, "x", i, "=", resultado)