class EdgeCasesMixin:
    def add_refund(self, original_payer, amount, participants,
                    split_type="equal", weights=None, category="Refund", date=None):

        self.add_expense(original_payer, -abs(amount), participants,
                          split_type, weights, category, date)

    def record_partial_payment(self, from_person, to_person, amount, date=None):
      
        if from_person not in self.friends or to_person not in self.friends:
            raise ValueError("Both people must be part of the group.")
        self.add_expense(to_person, amount, [from_person],
                          split_type="equal", category="Settlement Payment", date=date)
