import json
import logging

from BankService.dto.OperationAmount import Operation

logger = logging.getLogger(__name__)

def get_operations(json_file):
    with open(json_file, 'r', encoding="utf-8") as file:
        data = file.read()

    jsons = json.loads(data)
    operation_list = []

    for j in jsons:
        try:
            operation_list.append(Operation(**j))
        except Exception as t:
            logger.error('Ошибка при разборе json\n')

    return operation_list

def get_last_operations(list_operations):
    executed_constant = 'EXECUTED'
    execute_operations = []

    for operation in list_operations:
        if operation.state == executed_constant:
            execute_operations.append(operation)

    sorted_operations = sorted(execute_operations, key=lambda x: x.date, reverse=True)

    logger.info('Последние 5 переводов:\n')

    for operation in sorted_operations[:5]:
        print(f'{operation.date} {operation.description}\n'
              f'{operation.from_ if operation.from_ is None else 'Null'} {operation.to}\n'
              f'{operation.operation_amount.amount} {operation.operation_amount.currency.name}\n')
