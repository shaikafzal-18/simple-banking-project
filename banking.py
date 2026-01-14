balance = 0.0
kyc_documents = {}
def check_balance():
    print(f"Your current balance is {balance}.")
    print("======================")

def deposit(amount):
    if amount == 0:
        print("Please enter a valid amount to deposit.")
        print("======================")
    elif amount < 0:
        print("Please enter a valid amount to deposit.")
        print("======================")
    else:
        global balance
        balance += amount
        print(f"The amount {amount} is deposited Successfully.")
        print(f"Your current balance is {balance}.")
        print("======================")

def withdraw(amount):
    global balance
    if amount == 0:
        print("Please enter a valid amount to withdraw.")
        print("======================")
    elif amount > balance:
        print("Insufficient balance.")
        print("======================")
    else:
        balance -= amount
        print(f"The amount {amount} is withdrawn Successfully.")
        print("======================")

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("You have no kyc documents.")
        print("======================")

    else:
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")
            print("======================")


if __name__ == "__main__":
    print("******Welcome to the Banking System******")
    while True:
        print("1. Check your balance")
        print("2. Deposit an amount")
        print("3. Withdraw an amount")
        print("4. Check your kyc documents")
        print("5. Update your kyc documents")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            check_balance()
        elif choice == '2':
            amt = float(input("Enter the amount to deposit: "))
            deposit(amt)
        elif choice == '3':
            amt = float(input("Enter the amount to withdraw: "))
            withdraw(amt)
        elif choice == '4':
            check_kyc()
        elif choice == '5':
            kyc_docs = {}
            n_documents = int(input("Enter the number of documents you want to add: "))
            for i in range(n_documents):
                key = input("Enter the document's key: ")
                value = input("Enter the document's value: ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print(f"====KYC Updated Successfully!!!====")

        elif choice == '6':
            print("Quitting. Have a Nice day!")
            break
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
