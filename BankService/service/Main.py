import json
import logging
import re

from BankService.dto.Operation import Operation

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
            logger.error('[CONVERTER-E001] Ошибка при разборе json(Отсутствует информация о переводе)\n')

    return operation_list


def print_last_operations(list_operations):
    executed_constant = 'EXECUTED'
    execute_operations = []

    for operation in list_operations:
        if operation.state == executed_constant:
            execute_operations.append(operation)

    sorted_operations = sorted(execute_operations, key=lambda x: x.date, reverse=True)

    logger.info('[CONVERTER-I001] Последние 5 переводов:\n')

    last_operations = []
    for operation in sorted_operations[:5]:
        last_operations.append(operation)
        print(f'{operation.date.split('T')[0]} {operation.description}\n'
              f'{operation.from_.split(' ')[0] if operation.from_ is not None else 'Нет данных'} -> '
              f'{re.sub('(\d{6}).*(\d{4})', r'\1 ****** \2', operation.to.split(' ')[1])} \n'
              f'{operation.operation_amount.amount} {operation.operation_amount.currency.name}\n')
    return last_operations
