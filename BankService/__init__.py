from BankService.service.JsonConverter import get_operations, get_last_operations

if __name__ == '__main__':
    get_last_operations(get_operations('operations.json'))