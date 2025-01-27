class ContaBank:
    def __init__(self, titular: str, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, quantia):
        if quantia > 0:
            self.saldo += quantia
            print(f"Depósito de R${quantia:.2f} realizado com sucesso.")
        else:
            print("A quantia para depósito deve ser positiva.")

    def sacar(self, quantia):
        if 0 < quantia <= self.saldo:
            self.saldo -= quantia
            print(f"Saque de R${quantia:.2f} realizado com sucesso.")
        elif quantia > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            print("A quantia para saque deve ser positiva.")

    def mostrar_saldo(self):
        print(f"O saldo atual da conta de {self.titular} é R${self.saldo:.2f}.")