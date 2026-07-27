from expense_sharing import ExpenseSharing


def main():
    friends = ["Alice", "Bob", "Carol"]
    es = ExpenseSharing(friends)

    # Normal equal-split expenses
    es.add_expense("Alice", 900, ["Alice", "Bob", "Carol"], category="Accommodation")
    es.add_expense("Bob", 300, ["Alice", "Bob", "Carol"], category="Food")

    # Weighted split: Carol paid for fuel, but Alice used the car twice as much
    es.add_expense("Carol", 300, ["Alice", "Carol"],
                    split_type="weighted", weights={"Alice": 2, "Carol": 1},
                    category="Fuel")

    # Edge case 1: refund
    es.add_refund("Alice", 90, ["Alice", "Bob", "Carol"], category="Accommodation Refund")

    # Edge case 2: partial/direct payment
    es.record_partial_payment("Bob", "Alice", 100)

    print("---- Ledger ----")
    print(es.ledger[["expense_id", "payer", "amount", "participants", "split_type", "category"]])

    print("\n---- Net Balances ----")
    print(es.calculate_balances())

    print("\n---- Final Settlement ----")
    es.calculate_settlement()

    print("\n---- Per-Person Summary ----")
    print(es.per_person_summary())

    print("\n---- Spend by Category ----")
    print(es.spend_by_category())

    es.plot_spend_by_person()
    es.plot_spend_by_category()
    es.plot_net_balances()
    print("\nCharts saved: spend_by_person.png, spend_by_category.png, net_balances.png")


if __name__ == "__main__":
    main()
