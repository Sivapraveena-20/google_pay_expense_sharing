import matplotlib.pyplot as plt


class VisualizationMixin:
    def plot_spend_by_person(self, save_path="spend_by_person.png"):
        paid = self.spend_by_payer().reindex(self.friends, fill_value=0)
        plt.figure(figsize=(6, 4))
        paid.plot(kind="bar", color="#4C8BF5")
        plt.title("Total Amount Paid per Person")
        plt.ylabel("Rs.")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

    def plot_spend_by_category(self, save_path="spend_by_category.png"):
        cat = self.spend_by_category().abs()
        cat = cat[cat > 0]
        plt.figure(figsize=(6, 6))
        cat.plot(kind="pie", autopct="%1.1f%%", startangle=90)
        plt.title("Spending by Category")
        plt.ylabel("")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

    def plot_net_balances(self, save_path="net_balances.png"):
        import pandas as pd
        balances = pd.Series(self.calculate_balances())
        colors = ["#2ecc71" if v >= 0 else "#e74c3c" for v in balances]
        plt.figure(figsize=(6, 4))
        balances.plot(kind="bar", color=colors)
        plt.axhline(0, color="black", linewidth=0.8)
        plt.title("Net Balance per Person (Green = owed, Red = owes)")
        plt.ylabel("Rs.")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
