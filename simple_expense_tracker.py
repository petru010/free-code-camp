def add_expense(expenses, amount, category):
    expenses.append({
        'amount': amount,
        'category': category
    })

def print_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    
    print("Expenses:")
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}")

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add Expense')
        print('List all expenses')
        print('3. Show Total Expenses')
        print('4. Filter Expenses by Category')
        print('5. Exit')
        choice = input('Choose an option: ')
        if choice == '1':
            amount = float(input('Enter expense amount: '))
            category = input('Enter expense category: ')
            add_expense(expenses, amount, category)
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
        elif choice == '3':
            print(f"\nTotal Expenses: {total_expenses(expenses)}")
        elif choice == '4':
            category = input('Enter category to filter: ')
            filtered = filter_expenses_by_category(expenses, category)
            print_expenses(filtered)
        elif choice == '5':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')
