class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return"[>>Código {} Saldo {}<<]".format(self.codigo, self.saldo)

conta_do_negao = ContaCorrente(20)
print(conta_do_negao)