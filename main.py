print(f'Запуск Homework1\main.py')

from application.__salary import calculate_salary
from application.db.__people import get_employees
from datetime import datetime

def work():
    calculate_salary()
    get_employees()

if __name__ == '__main__':
    current_date = datetime.now().date()
    print(f'>>>>>>>>>[{current_date}] Точка входа: Homework1\main.py')
    work()



    # print(f'Запуск Homework1\main.py')
    # from datetime import datetime
    # if __name__ == '__main__':
    #     current_date = datetime.now().date()
    #     print(f'>>>>>>>>>[{current_date}] Точка входа: Homework1\main.py')