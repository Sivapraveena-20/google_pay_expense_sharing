class BalancesMixin:
    def calculate_balances(self):
        """
        Positive balance -> this person is owed money.
        Negative balance -> this person owes money.
        """
        balances = {friend: 0.0 for friend in self.friends}

        for _, row in self.ledger.iterrows():
            payer = row["payer"]
            amount = row["amount"]
            participants = row["participants"]

            balances[payer] += amount

            if row["split_type"] == "weighted":
                weights = row["weights"]
                total_weight = sum(weights[p] for p in participants)
                for p in participants:
                    share = amount * (weights[p] / total_weight)
                    balances[p] -= share
            else:  # equal split
                share = amount / len(participants)
                for p in participants:
                    balances[p] -= share

        return {k: round(v, 2) for k, v in balances.items()}
