# MATRIZ con los registros de actividad (usuario, hora de entrada, hora de salida)
logs = [
    ["ana", "08:00", "09:00"],
    ["pedro", "08:15", "09:30"],
    ["ana", "10:00", "11:00"],
    ["maria", "09:00", "10:00"],
    ["pedro", "13:00", "14:00"],
    ["ana", "15:00", "16:00"]
]

usuarios = []   # lista para guardar usuarios únicos

i = 0
while i < len(logs):   # leer cada registro de la matriz
    usuario = logs[i][0]

    if usuario not in usuarios:
        usuarios.append(usuario)

    i += 1



resultados = []   # [nombre_usuario, numero_de_accesos]

for u in usuarios:
    contador = 0
    for registro in logs:  # recorrer matriz
        if registro[0] == u:
            contador += 1

    resultados.append([u, contador])



print("Resultados finales:")
for r in resultados:
    print(r)
