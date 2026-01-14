balance = 0.0
kyc_documents = {}
def check_balance():
    print(f"Your current balance is {balance}.")
    print("======================")

    def check_balance(self):
        print(f"Your current balance is {self.balance}.")
        print("======================")

    def deposit(self,amount):
        if amount <= 0:
            print("Please enter a valid amount to deposit.")
            print("======================")
            return
        self.balance += amount
        print(f"The amount {amount} is deposited Successfully.")
        print(f"Your current balance is {balance}.")
        print("======================")


    def withdraw(self,amount):
        if amount <= 0:
            print("Please enter a valid amount to withdraw.")
            print("======================")
        elif amount > self.balance:
            print("Insufficient balance.")
            print("======================")
        else:
            self.balance -= amount
            print(f"The amount {amount} is withdrawn Successfully.")
            print("======================")

    def update_kyc(self,docs):
        self.kyc_documents.update(docs)

    def check_kyc(self):
        if not self.kyc_documents:
            print("No kyc documents found.")
        else:
            for key, value in self.kyc_documents.items():
                print(f"{key}: {value}")

def save_account(account):
    with open("account.json", "w") as file:
        json.dump({
            "balance": account.balance,
            "kyc": account.kyc_documents
        }, file)

def load_account():
    try:
        with open("account.json", "r") as file:
            data = json.load(file)
            account=BankAccount()
            account.balance=data["balance"]
            account.kyc_documents=data["kyc"]
            return account
    except FileNotFoundError:
        return BankAccount()

if __name__ == "__main__":
    account = load_account()
    print("****** Welcome to the Banking System ******")

    while True:
        print("1. Check Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Check KYC Documents")
        print("5. Update KYC Documents")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account.check_balance()

        elif choice == '2':
            try:
                amt = float(input("Enter amount to deposit: "))
                account.deposit(amt)
                save_account(account)
            except ValueError:
                print("Please enter a numeric value.")

        elif choice == '3':
            try:
                amt = float(input("Enter amount to withdraw: "))
                account.withdraw(amt)
                save_account(account)
            except ValueError:
                print("Please enter a numeric value.")

        elif choice == '4':
            account.check_kyc()

        elif choice == '5':
            kyc_docs = {}
            n = int(input("Number of documents: "))
            for _ in range(n):
                key = input("Document name: ")
                value = input("Document value: ")
                kyc_docs[key] = value
            account.update_kyc(kyc_docs)
            save_account(account)

        elif choice == '6':
            print("Thank you for using Banking System!")
            break

        else:
            print("Invalid choice. Please try again.")
