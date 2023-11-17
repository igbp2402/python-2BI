class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}')
        else:
            print('Saldo insuficiente. Operação de saque não realizada.')

    def ver_saldo(self):
        print(f'Saldo atual da conta de {self.titular}: R${self.saldo}')


conta_exemplo = ContaBancaria("Igor")

conta_exemplo.depositar(1000)
conta_exemplo.sacar(500)
conta_exemplo.ver_saldo()
conta_exemplo.sacar(800) 
conta_exemplo.depositar(300)
conta_exemplo.ver_saldo()
