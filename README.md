# Split - Expense Management Algorithm

Welcome to the GitHub repository for the core algorithm behind "Split", a mobile application designed to simplify group expense management. This algorithm efficiently calculates the minimal number of transactions required to settle debts within a group, making it easier for friends and families to manage shared expenses without the hassle of complex debt chains.

## Features

- **Minimal Transactions**: The algorithm identifies the optimal way to settle all debts with the fewest transactions possible.
- **Simplicity**: It accepts a list of expenses and automatically calculates who owes whom and how much.
- **Flexibility**: You can easily add or modify expenses, accommodating changes in group activities and expenses.
- **Clarity**: Outputs clear, straightforward transactions needed to balance the group's expenses.

## How to Use

1. **Define Expenses**: Start by creating a list of expenses. Each expense should be a list containing the payer's name, the amount paid, and the names of the beneficiaries.

    ```python
    expenses = [
        ["Alice", 120, "Bob", "Charlie"],
        ["Bob", 150, "Alice", "Charlie"],
        ["Charlie", 180, "Alice", "Bob"]
    ]
    ```

2. **Initialize the Algorithm**: Create an instance of the `Split` class with your list of expenses.

    ```python
    split_instance = Split(expenses)
    ```

3. **Calculate Transactions**: Use the `balance` method to calculate the minimal transactions required.

    ```python
    transactions = split_instance.balance()
    ```

4. **Review Transactions**: The output will be a list of transactions, where each transaction indicates who should pay whom and the amount.

    ```python
    for transaction in transactions:
        print(transaction)
    ```

## Example

Given the expenses:

- Alice paid 120 euros for Bob and Charlie.
- Bob paid 150 euros for Alice and Charlie.
- Charlie paid 180 euros for Alice and Bob.

The algorithm might output a single transaction:

- ['Charlie', '45.0', 'Alice'].

This indicates that to settle all debts within the group, only one transaction is necessary.

## Attribution

This algorithm is based on the original work available at [davymariko's Tricount GitHub repository](https://github.com/davymariko/Tricount). We extend our heartfelt gratitude to the original creator for their innovative approach to simplifying group expense management.
