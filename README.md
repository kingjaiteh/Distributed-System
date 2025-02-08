ABC Bank Distributed System
Overview

This project simulates a distributed banking system using a client-server model. The system allows multiple clients to concurrently perform various banking operations such as deposits, withdrawals, money transfers, and loan repayments. The project leverages Python's threading and socket libraries to simulate concurrency and TCP connections.
Features

The server supports the following operations:

    Create Account: Allows creating new accounts.
    Show Account Holders: Displays a list of all account holders (Audit-only access).
    Show Transaction History: Displays transaction history for all accounts (Audit-only access).
    Deposit: Deposits funds into a specified account.
    Withdraw: Withdraws funds from a specified account.
    Transfer Money: Transfers funds between accounts.
    Pay Loan with Check: Repays a loan using a direct payment.
    Pay Loan by Transfer: Transfers funds from a checking account to repay a loan.

Synchronization Mechanisms

The system uses threading.Lock to ensure thread safety during account operations. Each account is associated with a lock to prevent race conditions when multiple threads access the same account.
Challenges and Solutions
Challenges

    Concurrency Issues: Ensuring thread safety when multiple clients access the same account.
    Data Integrity: Preventing errors in operations such as double withdrawals or incorrect balance updates.

Solutions

    Threading Locks: Used locks to synchronize access to shared resources.
    Error Handling: Implemented robust error checks for invalid inputs and account operations.

How to Run
Prerequisites

    Operating System: Debian Linux
    Python Version: 3.x
    Dependencies: Install the tabulate library for formatted output:

    sudo apt update
    sudo apt install python3-pip
    pip install tabulate

Running the Server

    Open a terminal and navigate to the project directory.
    Start the server:

    python3 server.py

Running the Client

    Open another terminal for client operations.
    Use the following command format to interact with the server:

python3 client.py [user] [command] [account_number] [amount]

Examples:

Create an account:

    python3 client.py Alice create_account 1001 500

Deposit funds:

    python3 client.py Alice deposit 1001 200

View all account holders (Audit-only):

    python3 client.py Audit show_accountholders

Running Bash Scripts

Grant execute permissions to the scripts:

    chmod +x short_script.sh run_bank.sh

Run the short script for testing:

    ./short_script.sh

Run the full script for final testing:

    ./run_bank.sh

Performance Analysis

    The system can handle concurrent operations efficiently due to proper locking mechanisms.
    Potential improvement areas include optimizing lock to minimize contention.
