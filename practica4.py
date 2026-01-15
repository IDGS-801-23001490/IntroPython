lista = []
sin_repetir = []
pares = []
impares = []

print("Ingresa 20 numeros:")
for i in range(20):
    num = int(input("Numero: "))
    lista.append(num)

lista.sort()

for numero in lista:
    es_nuevo = True
    for x in sin_repetir:
        if numero == x:
            es_nuevo = False
    
    if es_nuevo:
        sin_repetir.append(numero)

for numero in sin_repetir:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista ordenada menor a mayor:")
print(sin_repetir)
print("Pares:")
print(pares)
print("Impares:")
print(impares)
print("Repetidos:")
for numero in sin_repetir:
    contador = 0
    for original in lista:
        if numero == original:
            contador += 1
    
    if contador > 1:
        print(str(numero) + " se repite " + str(contador) + " veces")