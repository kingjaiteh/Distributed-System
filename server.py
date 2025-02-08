import socket
import threading
import time
from tabulate import tabulate # type: ignore

# ['Alice', 'Bob', 'Charlie', 'Dave', 'Frank', 'Grace', 'Heidi','Ivan', 'John', 'Kate', 'James',
#  'Michael', 'Robert', 'William', 'David','Thomas', 'Mark', 'Steven', 'Paul', 'Kevin', 'Jason',
#  'Gary', 'Larry','Justin','Raymond','Adam','Henry','Eve']

class Bank:
    def __init__(self):
        self.accounts = [
            {'acct_num': 1001, 'acct_type': 'checking', 'init_acct_holder': 'Alice',
             'acct_holder': ['Alice', 'Jason', 'David'], 'balance': 2100, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1002, 'acct_type': 'loan', 'init_acct_holder': 'Alice',
             'acct_holder': ['Alice', 'Jason', 'David'], 'balance': -300, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1003, 'acct_type': 'checking', 'init_acct_holder': 'Bob',
             'acct_holder': ['Bob', 'Ivan', 'Kevin'], 'balance': 3500, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1004, 'acct_type': 'loan', 'init_acct_holder': 'Bob',
             'acct_holder': ['Bob', 'Ivan', 'Paul'], 'balance': -900, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1005, 'acct_type': 'checking', 'init_acct_holder': 'Charlie',
             'acct_holder': ['Charlie', 'Dave'], 'balance': 9100, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1006, 'acct_type': 'loan', 'init_acct_holder': 'Charlie',
             'acct_holder': ['Charlie', 'Dave', 'Gary'], 'balance': -3200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1007, 'acct_type': 'checking', 'init_acct_holder': 'Dave',
             'acct_holder': ['Dave', 'Thomas', 'Henry'], 'balance': 200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1008, 'acct_type': 'loan', 'init_acct_holder': 'Dave',
             'acct_holder': ['Dave', 'James', 'Gary'], 'balance': -300, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1009, 'acct_type': 'checking', 'init_acct_holder': 'Frank',
             'acct_holder': ['Frank', 'Grace', 'Charlie'], 'balance': 4000, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1010, 'acct_type': 'loan', 'init_acct_holder': 'Frank',
             'acct_holder': ['Frank', 'Adam', 'Steven'], 'balance': -900, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1011, 'acct_type': 'checking', 'init_acct_holder': 'Grace',
             'acct_holder': ['Grace', 'Adam', 'Heidi'], 'balance': 3000, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1012, 'acct_type': 'loan', 'init_acct_holder': 'Grace',
             'acct_holder': ['Grace', 'Robert', 'Larry'], 'balance': -100, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1013, 'acct_type': 'checking', 'init_acct_holder': 'Heidi',
             'acct_holder': ['Heidi', 'Mark', 'Kate'], 'balance': 500, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1014, 'acct_type': 'loan', 'init_acct_holder': 'Heidi',
             'acct_holder': ['Heidi', 'Ivan', 'Dave'], 'balance': -200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1015, 'acct_type': 'checking', 'init_acct_holder': 'Ivan',
             'acct_holder': ['Ivan', 'Charlie', 'Bob'], 'balance': 5000, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1016, 'acct_type': 'loan', 'init_acct_holder': 'Ivan',
             'acct_holder': ['Ivan', 'Michael', 'Mark'], 'balance': -2100, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1017, 'acct_type': 'checking', 'init_acct_holder': 'John',
             'acct_holder': ['John', 'Raymond', 'Dave'], 'balance': 6200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1018, 'acct_type': 'loan', 'init_acct_holder': 'John',
             'acct_holder': ['John', 'Frank', 'Justin'], 'balance': -2000, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1019, 'acct_type': 'checking', 'init_acct_holder': 'Kate',
             'acct_holder': ['Kate', 'Kevin', 'Justin'], 'balance': 5200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1020, 'acct_type': 'loan', 'init_acct_holder': 'Kate',
             'acct_holder': ['Kate', 'Thomas', 'James'], 'balance': -1800, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1021, 'acct_type': 'checking', 'init_acct_holder': 'James',
             'acct_holder': ['James', 'John', 'Grace'], 'balance': 8700, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1022, 'acct_type': 'loan', 'init_acct_holder': 'James',
             'acct_holder': ['James', 'Larry', 'Alice'], 'balance': -700, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1023, 'acct_type': 'checking', 'init_acct_holder': 'Michael',
             'acct_holder': ['Michael', 'Jason', 'Eve'], 'balance': 7400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1024, 'acct_type': 'loan', 'init_acct_holder': 'Michael',
             'acct_holder': ['Michael', 'Ivan', 'Gary'], 'balance': -4900, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1025, 'acct_type': 'checking', 'init_acct_holder': 'Robert',
             'acct_holder': ['Robert', 'Frank', 'Grace'], 'balance': 8400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1026, 'acct_type': 'loan', 'init_acct_holder': 'Robert',
             'acct_holder': ['Robert', 'Ivan', 'Justin'], 'balance': -400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1027, 'acct_type': 'checking', 'init_acct_holder': 'William',
             'acct_holder': ['William', 'Alice', 'Heidi'], 'balance': 6600, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1028, 'acct_type': 'loan', 'init_acct_holder': 'William',
             'acct_holder': ['William', 'Justin', 'Henry'], 'balance': -5000, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1029, 'acct_type': 'checking', 'init_acct_holder': 'David',
             'acct_holder': ['David', 'Raymond', 'Bob'], 'balance': 2400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1030, 'acct_type': 'loan', 'init_acct_holder': 'David',
             'acct_holder': ['David', 'Kate', 'Mark'], 'balance': -200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1031, 'acct_type': 'checking', 'init_acct_holder': 'Thomas',
             'acct_holder': ['Thomas', 'Charlie', 'Dave'], 'balance': 8700, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1032, 'acct_type': 'loan', 'init_acct_holder': 'Thomas',
             'acct_holder': ['Thomas', 'Grace', 'Robert'], 'balance': -2900, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1033, 'acct_type': 'checking', 'init_acct_holder': 'Mark',
             'acct_holder': ['Mark', 'Steven', 'Justin'], 'balance': 7800, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1034, 'acct_type': 'loan', 'init_acct_holder': 'Mark',
             'acct_holder': ['Mark', 'Paul', 'Bob'], 'balance': -5900, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1035, 'acct_type': 'checking', 'init_acct_holder': 'Steven',
             'acct_holder': ['Steven', 'Grace', 'William'], 'balance': 2400, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1036, 'acct_type': 'loan', 'init_acct_holder': 'Steven',
             'acct_holder': ['Steven', 'David', 'Justin'], 'balance': -1900, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1037, 'acct_type': 'checking', 'init_acct_holder': 'Paul',
             'acct_holder': ['Paul', 'Charlie', 'Steven'], 'balance': 7800, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1038, 'acct_type': 'loan', 'init_acct_holder': 'Paul',
             'acct_holder': ['Paul', 'Eve', 'Dave'], 'balance': -2500, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1039, 'acct_type': 'checking', 'init_acct_holder': 'Kevin',
             'acct_holder': ['Kevin', 'Kate', 'Larry'], 'balance': 4400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1040, 'acct_type': 'loan', 'init_acct_holder': 'Kevin',
             'acct_holder': ['Kevin', 'Ivan', 'James'], 'balance': -800, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1041, 'acct_type': 'checking', 'init_acct_holder': 'Jason',
             'acct_holder': ['Jason', 'Adam', 'Henry'], 'balance': 1400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1042, 'acct_type': 'loan', 'init_acct_holder': 'Jason',
             'acct_holder': ['Jason', 'Raymond', 'William'], 'balance': -200, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1043, 'acct_type': 'checking', 'init_acct_holder': 'Gary',
             'acct_holder': ['Gary', 'Larry', 'Ivan'], 'balance': 3400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1044, 'acct_type': 'loan', 'init_acct_holder': 'Gary',
             'acct_holder': ['Gary', 'Frank', 'James'], 'balance': -900, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1045, 'acct_type': 'checking', 'init_acct_holder': 'Larry',
             'acct_holder': ['Larry', 'Frank', 'Heidi'], 'balance': 5400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1046, 'acct_type': 'loan', 'init_acct_holder': 'Larry',
             'acct_holder': ['Larry', 'William', 'David'], 'balance': -300, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1047, 'acct_type': 'checking', 'init_acct_holder': 'Justin',
             'acct_holder': ['Justin', 'John', 'Dave'], 'balance': 3400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1048, 'acct_type': 'loan', 'init_acct_holder': 'Justin',
             'acct_holder': ['Justin', 'Charlie', 'Alice'], 'balance': -1500, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1049, 'acct_type': 'checking', 'init_acct_holder': 'Raymond',
             'acct_holder': ['Raymond', 'Henry', 'James'], 'balance': 9400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1050, 'acct_type': 'loan', 'init_acct_holder': 'Raymond',
             'acct_holder': ['Raymond', 'Steven', 'Mark'], 'balance': -6900, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1051, 'acct_type': 'checking', 'init_acct_holder': 'Adam',
             'acct_holder': ['Adam', 'Charlie', 'Michael'], 'balance': 5400, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1052, 'acct_type': 'loan', 'init_acct_holder': 'Adam',
             'acct_holder': ['Adam', 'Larry', 'Jason'], 'balance': -4600, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1053, 'acct_type': 'checking', 'init_acct_holder': 'Henry',
             'acct_holder': ['Henry', 'Henry', 'James'], 'balance': 8300, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1054, 'acct_type': 'loan', 'init_acct_holder': 'Henry',
             'acct_holder': ['Henry', 'Steven', 'Mark'], 'balance': -1800, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1055, 'acct_type': 'checking', 'init_acct_holder': 'Eve',
             'acct_holder': ['Eve', 'Michael', 'Justin'], 'balance': 2200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1056, 'acct_type': 'loan', 'init_acct_holder': 'Eve',
             'acct_holder': ['Eve', 'William', 'Alice'], 'balance': -400, 'history': [], 'lock': threading.Lock()}
        ]

    def create_account(self, data_dict):
        # Check if the user already has an account
        for account in self.accounts:
            if account['init_acct_holder'] == data_dict['user']:
                return "One person can only create one account"

        # Check if the account number specified by the user is already in use
        for account in self.accounts:
            if int(account['acct_num']) == int(data_dict['acct_num']):
                return f"The account number has been used by {account['init_acct_holder']}"

        # Create new account
        new_account = {
            'acct_num': int(data_dict['acct_num']),
            'acct_type': 'checking',
            'init_acct_holder': data_dict['user'],
            'acct_holder': [data_dict['user']],
            'balance': int(data_dict.get('amount', 0)),
            'history': [],
            'lock': threading.Lock()
        }

        # Add new account to the list
        self.accounts.append(new_account)
        return f"Successfully created checking account for {data_dict['user']} with account number {int(data_dict['acct_num'])}。"

    def show_bank(self, data_dict):
        # Check if the user is 'Audit'
        if data_dict['user'] != 'Audit':
            return "Access denied: only Audit can view all bank accounts"

        # Prepare data for table format
        table_data = []
        for account in self.accounts:
            row = [
                account['acct_num'],
                account['acct_type'],
                account['init_acct_holder'],
                ', '.join(account['acct_holder']),
                account['balance'],
                account['history']
            ]
            table_data.append(row)

        # Format the table
        headers = ["acct_num", "acct_type", "init_holder", "acct_holder", "balance", "history"]
        formatted_table = tabulate(table_data, headers=headers, tablefmt="plain")
        return f"All account information is as follows:\n{formatted_table}"

   
    

    def show_accountholders(self, data_dict):
        user = data_dict['user']

        # Check if the user is 'Audit'
        if user == 'Audit':
            accountholder_data = []
            for account in self.accounts:
                accountholders = ', '.join(account['acct_holder']) if account['acct_holder'] else "no holders"
                accountholder_data.append((account['acct_num'], accountholders))

            # Format the output
            headers = ["Account Number", "Account Holders"]
            formatted_table = tabulate(accountholder_data, headers=headers, tablefmt="plain")
            return f"All accounts' holders:\n{formatted_table}"

        # If not 'Audit', deny access
        return f"Access denied: Only 'Audit' can view all account holders."



    def deposit(self, data_dict):
        acct_num = int(data_dict['acct_num'])
        amount = int(data_dict['amount'])
        user = data_dict['user']

        # Check if the account number exists
        for account in self.accounts:
            if account['acct_num'] == acct_num:
                with account['lock']:  # Acquire lock for thread safety
                    if amount < 0:
                        # if deposit amount <0
                        return "Error: Deposit amount must be greater than or equal to 0."
                    if amount == 0:
                        # if deposit amount=0, return current balance
                        return f"Deposit amount is 0. Current balance: {account['balance']}."
                    
                    # Deposit the amount
                    account['balance'] += amount
                    account['history'].append(f"({user}, deposited, {amount})")
                    return f"Successfully deposited {amount}. New balance: {account['balance']}."

        return f"Error: Account {acct_num} not found."



    def withdraw(self, data_dict):
        acct_num = int(data_dict['acct_num'])
        amount = int(data_dict['amount'])
        user = data_dict['user']

        # Check if the account number exists
        for account in self.accounts:
            if account['acct_num'] == acct_num:
                if user not in account['acct_holder']:
                    return f"Access denied: {user} is not an account holder for account {acct_num}"

                with account['lock']:

                    if amount < 0:
                        # if withdraw amount <0
                        return "Withdrawal amount must be greater than 0."
                    if amount == 0:
                        # if withdraw amount=0, return current balance
                        return f"Withdrawal amount is 0. Current balance: {account['balance']}."
                        # check if account balance is sufficient
                    if account['balance'] < amount:
                        return f"Insufficient funds. Current balance: {account['balance']}"

                    # Subtract amount from remaining balance and append
                    account['balance'] -= amount
                    account['history'].append(f"({user}, withdrew, {amount})")
                    return f"Successfully withdrew {amount}. New balance: {account['balance']}"

        return f"Account {acct_num} not found."


    def transfer_to(self, data_dict):
        source_acct_num = next(
            (account['acct_num'] for account in self.accounts 
            if account['init_acct_holder'] == data_dict['user'] and account['acct_type'] == 'checking'), None)
        target_acct_num = int(data_dict['acct_num'])
        amount = int(data_dict.get('amount', 0))

        # Transfer only from checking account
        if source_acct_num is None:
            return f"Error: User {data_dict['user']} does not have a checking account."
        
        # Verify that amount is positive
        if amount <= 0:
            return "Error: Transfer amount must be greater than zero."
        
        # Initialize account doing the transfer and account receiving transfer
        source_account = next((acct for acct in self.accounts if acct['acct_num'] == source_acct_num), None)
        target_account = next((acct for acct in self.accounts if acct['acct_num'] == target_acct_num), None)

        # Verify that user is an init_acct_holder for an account in the bank.

        # Verify that the target account acct_num exists
        if not source_account or not target_account:
            return f"Error: Either source ({source_acct_num}) or target ({target_acct_num}) account does not exist."

        # get mutex lock and consider deadlock
        with source_account['lock'], target_account['lock']:
            if source_account['balance'] < amount:
                return "Error: Insufficient funds in the source account."
            
            # transfer and append
            source_account['balance'] -= amount
            target_account['balance'] += amount
            source_account['history'].append((data_dict['user'], 'transfer_to', -amount))
            target_account['history'].append((data_dict['user'], 'received_transfer', amount))
        return f"Transfer of {amount} from {source_acct_num} to {target_acct_num} successful. New balance: {source_account['balance']}."

    
        
    def pay_loan_check(self, data_dict):
        # Get account number and repayment amount
        acct_num = int(data_dict['acct_num'])
        amount = int(data_dict['amount'])
        user = data_dict['user']

        # Check if the repayment amount is positive
        if amount <= 0:
            return "Repayment amount must be greater than 0."

        # Find Target Loan Accounts
        for account in self.accounts:
            # Confirm that the account is a loan account
            if account['acct_num'] == acct_num and account['acct_type'] == 'loan':

                # Check if the user is the holder of the account
                if user not in account['acct_holder']:
                    return f"Access denied: {user} is not an account holder for account {acct_num}."
                
                # get mutex lock and pay loan
                with account['lock']:
                    account['balance'] += amount
                    account['history'].append(f"({user} paid {amount} towards loan)")
                    return f"Successfully paid {amount} towards loan. Remaining loan balance: {account['balance']}"

        return f"Loan account {acct_num} not found."


    def pay_loan_transfer_to(self, data_dict):
        loan_acct_num = int(data_dict['acct_num'])
        amount = int(data_dict.get('amount', 0))

        if amount <= 0:
            return "Error: Payment amount must be greater than zero."

        # Locate the user's checking and loan accounts
        checking_account = next(
            (acct for acct in self.accounts
            if acct['acct_type'] == 'checking' and acct['init_acct_holder'] == data_dict['user']), None)
        loan_account = next(
            (acct for acct in self.accounts
            if acct['acct_type'] == 'loan' and acct['acct_num'] == loan_acct_num), None)

        # Ensure the user has a checking account
        if not checking_account:
            return f"Error: User {data_dict['user']} does not have a checking account."

        # Ensure the loan account exists
        if not loan_account:
            return f"Error: Loan account {loan_acct_num} does not exist."

        # Ensure the user is the owner of the loan account
        if loan_account['init_acct_holder'] != data_dict['user']:
            return f"Error: User {data_dict['user']} is not the owner of loan account {loan_acct_num}."

        # Perform the transaction under lock
        with checking_account['lock'], loan_account['lock']:
            if checking_account['balance'] < amount:
                return "Error: Insufficient funds in the checking account."
            # Update balances
            checking_account['balance'] -= amount
            loan_account['balance'] += amount  # Loans have negative balances

            # Record transactions in histories
            checking_account['history'].append((data_dict['user'], 'pay_loan_transfer_to', -amount))
            loan_account['history'].append((data_dict['user'], 'received_loan_payment', amount))

        return (f"Loan payment of {amount} from checking account {checking_account['acct_num']} "
                f"to loan account {loan_acct_num} successful. "
                f"New balances: Checking {checking_account['balance']}, Loan {loan_account['balance']}.")

    
    
    def show_history(self, data_dict):
        user = data_dict['user']

        # If the user is 'Audit', display all accounts' histories
        if user == 'Audit':
            history_data = []
            for account in self.accounts:
                history = account['history'] if account['history'] else "no history"
                history_data.append((account['acct_num'], history))

            # Format the output
            headers = ["Account Number", "Transaction History"]
            formatted_table = tabulate(history_data, headers=headers, tablefmt="plain")
            return f"All accounts' transaction histories:\n{formatted_table}"

        # For non-Audit users, show only the history of accounts they are holders of
        history_data = []
        for account in self.accounts:
            if user in account['acct_holder']:
                history = account['history'] if account['history'] else "no history"
                history_data.append((account['acct_num'], history))

        if not history_data:
            return f"Error: User {user} does not hold any accounts."

        # Format the output
        headers = ["Account Number", "Transaction History"]
        formatted_table = tabulate(history_data, headers=headers, tablefmt="plain")
        return f"Transaction history for accounts held by {user}:\n{formatted_table}"


    
def handle_client(client_socket, bank):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        # Parse the command line format [user] [command] [account] [amount]
        pairs = data.decode().split()
        data_dict = dict(pair.split('=') for pair in pairs)

        if len(data_dict) < 3:
            response = "Invalid request format."
            client_socket.send(response.encode())
            continue

        print(f"Request received: user={data_dict['user']} command={data_dict['command']}  account={data_dict['acct_num']}, "
              f"amount={data_dict.get('amount', 0)}")

        # Execute the corresponding command
        if data_dict['command'] == 'create_account':
            response = bank.create_account(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'show_bank':
            response = bank.show_bank(data_dict)
            # Sending show_bank data in segments
            for i in range(0, len(response), 1024):
                client_socket.send(response[i:i + 1024].encode())
            client_socket.send(b"END")
            continue

        elif data_dict['command'] == 'show_accountholders':
            response = bank.show_accountholders(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'deposit':
            response = bank.deposit(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'withdraw':
            response = bank.withdraw(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'transfer_to':
            response = bank.transfer_to(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'pay_loan_check':
            response = bank.pay_loan_check(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'pay_loan_transfer_to':
            response = bank.pay_loan_transfer_to(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'show_history':
            response = bank.show_history(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")


        else:
            response = "Invalid command."
            client_socket.send(response.encode())
            client_socket.send(b"END")


        print(f"Request handled: {data_dict['command']}")
        # print(f"Current bank state: {bank.accounts}\n")
        time.sleep(1)  # Slight delay for better client-server interaction

    client_socket.close()

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9876
ADDR = (HOST, PORT)
bank = Bank()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)
server_socket.listen()
print(f"Server listening on host {HOST}...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Client connected from {addr}")

    thread = threading.Thread(target=handle_client, args=(client_socket, bank))
    thread.start()
    print(f"{threading.active_count() - 1} thread connections running...")








