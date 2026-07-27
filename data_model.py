import pandas as pd

class DataModelMixin:
    def _init_ledger(self, friends):
        self.friends = friends
        self.ledger = pd.DataFrame(columns=[
            "expense_id", "payer", "amount", "participants",
            "split_type", "weights", "category", "date"
        ])
        self._next_id = 1

    def add_expense(self, payer, amount, participants,
                     split_type="equal", weights=None,
                     category="General", date=None):
       
        # ---- basic validation (preprocessing step) ----
        if payer not in self.friends:
            raise ValueError(f"Payer '{payer}' is not part of the group.")
        for p in participants:
            if p not in self.friends:
                raise ValueError(f"Participant '{p}' is not part of the group.")
        if len(participants) == 0:
            raise ValueError("An expense must have at least one participant.")
        if split_type == "weighted":
            if not weights:
                raise ValueError("weights must be provided for a weighted split.")
            missing = set(participants) - set(weights.keys())
            if missing:
                raise ValueError(f"Missing weights for: {missing}")

        if date is None:
            date = pd.Timestamp.today().strftime("%Y-%m-%d")

        row = {
            "expense_id": self._next_id,
            "payer": payer,
            "amount": amount,
            "participants": participants,
            "split_type": split_type,
            "weights": weights,
            "category": category,
            "date": date
        }
        self.ledger.loc[len(self.ledger)] = row
        self._next_id += 1
