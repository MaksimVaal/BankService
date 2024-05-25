class OperationAmount:

    def __init__(self, **kwargs):
        self.amount = kwargs.get('amount')
        self.currency = Currency(**kwargs.get('currency'))


class Operation:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.state = kwargs.get('state')
        self.date = kwargs.get('date')
        self.operation_amount = OperationAmount(
            **kwargs.get('operationAmount')
        )
        self.description = kwargs.get('description')
        self.from_ = kwargs.get('from')
        self.to = kwargs.get('to')


class Currency:

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.code = kwargs.get('code')
