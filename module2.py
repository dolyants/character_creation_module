# Из модуля module1.py импортируем функцию special_calculation.
from module import special_calculation

print("Основной модуль")
# Производим расчёты. 
coef = special_calculation(2, 5)
print(coef) 