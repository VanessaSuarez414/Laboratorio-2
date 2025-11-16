# MATRIZ con los registros de actividad (usuario, hora de entrada, hora de salida)
logs = [
    ["ana", "08:00", "09:00"],
    ["pedro", "08:15", "09:30"],
    ["ana", "10:00", "11:00"],
    ["maria", "09:00", "10:00"],
    ["pedro", "13:00", "14:00"],
    ["ana", "15:00", "16:00"]
]

usuarios = []   # lista de usuarios únicos

i = 0
while i < len(logs):
    usuario = logs[i][0]

    if usuario not in usuarios:
        usuarios.append(usuario)

    i += 1


resultados = []  # [usuario, numero_de_accesos, lista_de_horas]

for u in usuarios:
    contador = 0
    horas = []   # aquí guardamos las horas de entrada y salida

    for registro in logs:
        if registro[0] == u:
            contador += 1
            horas.append((registro[1], registro[2]))  # (entrada, salida)

    resultados.append([u, contador, horas])


# Mostrar resultados completos
print("Resultados finales:")
for r in resultados:
    usuario = r[0]
    accesos = r[1]
    horas = r[2]

    print(f"\nUsuario: {usuario}")
    print(f"Total accesos: {accesos}")
    print("Horas registradas:")
    for h in horas:
        print(f" - Entrada: {h[0]} | Salida: {h[1]}")
