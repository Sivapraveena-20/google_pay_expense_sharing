import pandas as pd

class AnalyticsMixin:
    def spend_by_payer(self):
        
        """Total amount each person has paid before splitting."""
        return self.ledger.groupby("payer")["amount"].sum().round(2)

    def spend_by_category(self):
        """Total group spend per category"""
        return self.ledger.groupby("category")["amount"].sum().round(2)

    def spend_over_time(self):
        """Total spend per date - useful for a trip-spending timeline."""
        return self.ledger.groupby("date")["amount"].sum().round(2)

    def per_person_summary(self):
        """Combines spend-by-payer with net balance into one table."""
        balances = self.calculate_balances()
        paid = self.spend_by_payer().reindex(self.friends, fill_value=0)
        summary = pd.DataFrame({
            "total_paid": paid,
            "net_balance": pd.Series(balances)
        })
        summary["status"] = summary["net_balance"].apply(
            lambda b: "to be reimbursed" if b > 0
            else ("owes" if b < 0 else "settled")
        )
        return summary
