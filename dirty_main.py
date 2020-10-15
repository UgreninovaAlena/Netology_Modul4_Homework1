print('Запуск Homework1\dirty_main.py')
from datetime import datetime
from main import *

if __name__ == '__main__':
     current_date = datetime.now().date()
     print(f'>>>>>>>>>[{current_date}] Точка входа: Homework1\dirty_main.py')
     calculate_salary()
     get_employees()