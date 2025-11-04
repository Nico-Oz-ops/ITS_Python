'''
Progettare un semplice sistema bancario con i seguenti requisiti:

1. Classe del Account:
* Attributi:
    * account_id: str - identificatore univoco per l'account.
    * balance: float - il saldo attuale del conto.

* Metodi:
    * deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
    * get_balance(): restituisce il saldo corrente del conto.


2. Classe Bank:
* Attributi:
    * accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.

* Metodi:
    * create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0. 
    Solleva il seguente KeyError "Account with this ID already exists" se l'account con l'ID specificato esiste già.
    * deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
    * get_balance(account_id): restituisce il saldo del conto con l'ID specificato. Solleva il seguente 
    KeyError "Account not found" se l'account non esiste.
'''
class Account:
    def __init__(self, account_id: str, balance: float) -> None:
        self.account_id = account_id
        self.balance = balance
    
    def deposit(self, amount: float):
        self.balance += amount
    
    def get_balance(self) -> float:
        return self.balance

class Bank:
    def __init__(self):
        self.accounts: dict[str, Account] = {}
    
    def create_account(self, account_id: str):
        if account_id in self.accounts:
            raise KeyError("Account with this ID already exists")
        self.accounts[account_id] = Account(account_id, 0)
    
    def deposit(self, account_id: str, amount: float):
        if account_id not in self.accounts:
            raise KeyError("Account with this ID already exists")
        account = self.accounts[account_id]
        account.deposit(amount)
    
    def get_balance(self, account_id: str):
        if account_id not in self.accounts:
            raise KeyError("Account not found") 
        return self.accounts[account_id].get_balance()

# Test
	
bank = Bank()
account1 = bank.create_account("123")
print(bank.get_balance('123'))
	
bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))

bank = Bank()
account1 = bank.create_account("123")
try:
    bank.create_account("123")
except KeyError as e:
    print(e)

bank = Bank()
try:
    bank.get_balance("456")
except KeyError as e:
    print(e)