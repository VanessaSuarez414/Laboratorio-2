#Se crea la clase: Cuenta bancaria para que es usuario 
#pueda realizar operaciones de depósito, retiro y consulta de saldo.

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"[DEPÓSITO] {self.titular} depositó ${monto}. Nuevo saldo: ${self.saldo}")
        else:
            print("¡ERROR! El monto debe ser positivo.")

    def retirar(self, monto):
        if monto <= 0:
            print("¡ERROR! Monto inválido.")
        elif monto > self.saldo:
            print("¡ERROR! Saldo insuficiente.")
        else:
            self.saldo -= monto
            print(f"RETIRO {self.titular} retiró ${monto}. Nuevo saldo: ${self.saldo}")

    def consultar_saldo(self):
        print(f"CONSULTA Saldo actual de {self.titular}: ${self.saldo}")
        return self.saldo
