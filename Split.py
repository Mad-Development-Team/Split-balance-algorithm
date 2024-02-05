#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os


class Split:
    ''' Class representing an instance of the problem, focusing on splitting expenses. '''

    def __init__(self, expenses=None):
        if expenses is None:
            expenses = []
        self.expenses = expenses  # Use a list of expenses instead of a file
        self.balancelist = []
        self.netowned = []
        self.transactions = []

    def add_expense(self, payer, amount, receivers):
        ''' Method to add an expense to the list '''
        self.expenses.append([payer, amount] + receivers)

    def balance(self):
        ''' Returns a list of transactions which set the current accounts to zero in the format ["Payer", amount, "Receiver"]. '''

        # Process the list of expenses directly
        for expense in self.expenses:
            length = len(expense)
            amount_per_person = round(float(expense[1]) / float(length - 2), 2)
            for receiver in expense[2:]:
                if expense[0] == receiver:
                    continue  # Skip if the payer is also listed as a receiver for the same expense
                else:
                    # Add or subtract the amount from each person's balance
                    self.balancelist.append([expense[0], round(-amount_per_person, 2)])
                    self.balancelist.append([receiver, round(amount_per_person, 2)])

        # Consolidate balances
        balance_dict = {}
        for entry in self.balancelist:
            person, amount = entry
            if person in balance_dict:
                balance_dict[person] += amount
            else:
                balance_dict[person] = amount

        self.netowned = [[person, round(balance, 2)] for person, balance in balance_dict.items()]
        # Sort by net balance to optimize transactions
        self.netowned.sort(key=lambda x: x[1])

        # Calculate the minimum transactions to balance the debts
        while self.netowned and self.netowned[0][1] < 0:
            debtor = self.netowned[0]
            creditor = self.netowned[-1]

            amount = round(min(-debtor[1], creditor[1]), 2)
            self.transactions.append([debtor[0], amount, creditor[0]])

            debtor[1] += amount
            creditor[1] -= amount

            if debtor[1] == 0:
                self.netowned.pop(0)
            if creditor[1] == 0:
                self.netowned.pop()

        return self.transactions


if __name__ == '__main__':
    # Create a list with the expenses
    # [payer, quantity, receptor1, receptor2, ...]
    expenses = [
        ['Alice', 125, 'Alice', 'Bob', 'Charlie'],  # Alice paid 120 for Bob and Charlie
        ['Bob', 150, 'Alice', 'Charlie'],  # Bob paid 150 for Alice and Charlie
        ['Charlie', 180, 'Bob'],
        ['Alice', 30, 'Bob', 'Alice']
    ]

    # Create a split instance with the expenses
    split_instance = Split(expenses)

    # Calculate the needed transactions to balance the account
    transactions = split_instance.balance()

    print("\nThe following transactions are needed to balance the accounts:")
    for transaction in transactions:
        # Each transaction is a list with the following format [payer, quantity, receptor]
        print(transaction)

    print("\nTotal transactions needed: {}".format(len(transactions)))
