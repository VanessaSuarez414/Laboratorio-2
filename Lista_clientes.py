#Se crea una funcion para la simulacion de cola de atención 
def procesar_cliente(cliente):
  
    nombre, operacion, monto, cuenta = cliente
    print(f"\nAtendiendo a: {nombre}")

    if operacion == "deposito":
        cuenta.depositar(monto)
    elif operacion == "retiro":
        cuenta.retirar(monto)
    elif operacion == "consulta":
        cuenta.consultar_saldo()
    else:
        print("¡ERROR! Operación no válida.")


def procesar_cola(clientes):
    """
    Simula la cola del banco 
    
    """
    print("\n========== INICIO ATENCIÓN DE CLIENTES ==========")

    while clientes:
        cliente_actual = clientes.pop(0)
        procesar_cliente(cliente_actual)

    print("========== FIN DE ATENCIÓN ==========\n")
