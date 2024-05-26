from BankService.service.Main import get_operations, print_last_operations

if __name__ == '__main__':
    print_last_operations(get_operations('operations.json'))