from wine import Wine
from beer import Beer
from market import Market


wine1 = Wine(title="Merlot", production_date="2022-01-01")
wine2 = Wine(title="Chardonnay", production_date="2021-12-15")
wine3 = Wine(title="Cabernet Sauvignon", production_date="2022-02-10")
wine4 = Wine(title="Дербентское", production_date="2023-05-12")

beer1 = Beer(title="Heineken", production_date="2022-03-05")
beer2 = Beer(title="Guinness", production_date="2023-12-05")
beer3 = Beer(title="Corona", production_date="2022-04-30")
beer4 = Beer(title="Carlsberg", production_date="2023-09-16")


market = Market(wines=[wine1, wine2, wine3, wine4], beers=[beer1, beer2, beer3, beer4])
market2 = Market()


print("\n*************** Проверка: в наличие ли Merlot в маркете. Должно быть True")
print(market.has_drink_with_title("Merlot"))  # True
print("\nПроверка: в наличие ли Балтика в маркете:")
print(market.has_drink_with_title("Балтика"))  # False
print("\nПроверка: в наличие ли None в маркете:")
print(market.has_drink_with_title())  # False

print("\n*************** Проверка: в наличие ли Merlot в маркете 2 (пустой):")
print(market2.has_drink_with_title("Merlot"))

print("\n*************** Сортировка напитков по названию:")
sorted_drinks = market.get_drinks_sorted_by_title()
i = 0
for drink in sorted_drinks:
    i += 1
    print(str(i) + ") " + drink.title)

print("\n*************** Получаем список напитков в диапазоне даты производства с 2022-01-01 до 2022-03-31:")
filtered_drinks = market.get_drinks_by_production_date(from_date="2022-01-01", to_date="2022-03-31")
i = 0
for drink in filtered_drinks:
    i += 1
    print(str(i) + ") " + drink.title + ", дата изг. " + drink.production_date)

print("\n*************** Получаем список напитков без указание диапозона дат производства:")
filtered_drinks = market.get_drinks_by_production_date()
i = 0
for drink in filtered_drinks:
    i += 1
    print(str(i) + ") " + drink.title + ", дата изг. " + drink.production_date)


print("\n*************** Сортировка напитков по названию в маркете 2 (пустой):")
sorted_drinks = market2.get_drinks_sorted_by_title()
i = 0
for drink in sorted_drinks:
    i += 1
    print(str(i) + ") " + drink.title)

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""
