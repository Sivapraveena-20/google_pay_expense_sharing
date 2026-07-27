from data_model import DataModelMixin
from balances import BalancesMixin
from settlement import SettlementMixin
from edge_cases import EdgeCasesMixin
from analytics import AnalyticsMixin
from visualization import VisualizationMixin

class ExpenseSharing(
    DataModelMixin,
    BalancesMixin,
    SettlementMixin,
    EdgeCasesMixin,
    AnalyticsMixin,
    VisualizationMixin
):
    def __init__(self, friends):
        self._init_ledger(friends)
