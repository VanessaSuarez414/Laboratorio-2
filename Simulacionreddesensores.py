import random

n = 5
m = 6

matriz_sensores = []

for i in range(n):
    fila = []
    for j in range(m):
        temperatura = random.randint(20, 100)
        fila.append(temperatura)
    matriz_sensores.append(fila)

def detectar_criticos(matriz):
    criticos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > 80:
                criticos.append([i, j, matriz[i][j]])
    return criticos

criticos = detectar_criticos(matriz_sensores)

print("Matriz de sensores (temperaturas):")
for fila in matriz_sensores:
    print(fila)

print("\nSensores en estado crítico (> 80°C):")
for c in criticos:
    print(f"Fila {c[0]}, Columna {c[1]} → {c[2]}°C")
