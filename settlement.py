class SettlementMixin:
    def calculate_settlement(self, verbose=True):
        balances = self.calculate_balances()

        creditors = [(p, bal) for p, bal in balances.items() if bal > 0]
        debtors = [(p, -bal) for p, bal in balances.items() if bal < 0]

        # settle largest amounts first -> fewer transactions
        creditors.sort(key=lambda x: -x[1])
        debtors.sort(key=lambda x: -x[1])

        transactions = []
        i, j = 0, 0
        while i < len(debtors) and j < len(creditors):
            debtor, debt_amount = debtors[i]
            creditor, credit_amount = creditors[j]

            payment = round(min(debt_amount, credit_amount), 2)
            if payment > 0:
                transactions.append((debtor, creditor, payment))

            debt_amount -= payment
            credit_amount -= payment

            if debt_amount <= 0.01:
                i += 1
            else:
                debtors[i] = (debtor, debt_amount)

            if credit_amount <= 0.01:
                j += 1
            else:
                creditors[j] = (creditor, credit_amount)

        if verbose:
            if not transactions:
                print("Everyone is settled up!")
            for debtor, creditor, amount in transactions:
                print(f"{debtor} pays {creditor}: Rs.{amount:.2f}")

        return transactions
