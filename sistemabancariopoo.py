from datetime import datetime
class Cliente:
     def __init__(self, cpf, nome, data_nascimento): 
         self.cpf = cpf
         self.nome = nome 
         self.data_nascimento = data_nascimento 
         self.contas = [] 

     def adicionar_conta(self, conta): 
           self.contas.append(conta) 


     def __init__(self, numero, agencia, cliente):
         self.saldo = 0.0
         self.numero = numero
         self.agencia = agencia
         self.cliente = cliente 
         self.historico = Histórico() # type: ignore

     def depositar(self, valor):
              if valor > 0:
                   self.saldo += valor 

        self.historico.adicionar_transacao (f"Saque de R${valor:.2f}" # type: ignore
                return True 
             return False 
     def sacar(self, valor): 
        if valor > 0 and valor <= self.saldo:
         self.saldo -= valor

         self.historico.adicionar_transacao(f"Saque de R${valor:.2f}") 
               return True 
             return False
     def exibir_extrato(self): 
        print("Extrato da Conta:") 
        for transacao in 
         self.historico.transacoes: 
              print(transacao)

    class ContaCorrente(Conta):
          def __init__(self, numero, agencia, cliente, limite):
              super().__init__(numero, agencia, cliente) 
         self.limite = limite 
         self.limite_saques = 3 
         self.numero_saques = 0
          def sacar(self, valor):
            if self.numero_saques >= self.limite_saques: 
        print("Limite de saques excedido.")
                return False 
            if valor <= self.saldo + self.limite: 
         self.saldo -= valor
         self.numero_saques += 1

         self.historico.adicionar_transacao(f"Saque de R${valor:.2f} com limite")
                return True 
        print("Saldo insuficiente.") 
            return False
    class Historico: 
           def __init__(self):
              self.transacoes = []
            def adicionar_transacao (self, descricao):
                  data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 

          self.transaçõ.append(f"{data_atual}:
                                  {descricao}")

    class Transacao:
            def registrar (self, conta, valor):
            
                #Implementação específica para o tipo de transação  