import time


def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 10 ** 6 #мкс
        formatted_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
        print(f"Старт метода {func.__name__} в {formatted_start_time}.")
        print(f"Выполнение метода {func.__name__} завершилось. Время выполнения: {execution_time:.3f} мкс.")
        return result
    return wrapper

class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = {drink.title: drink for drink in wines} if wines is not None else {}
        self.beers = {drink.title: drink for drink in beers} if beers is not None else {}

    @log_time
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        if title in self.wines or title in self.beers:
            return True
        else:
            return False

    @log_time
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        drinks = list(self.wines.values()) + list(self.beers.values())
        sorted_drinks = sorted(drinks, key=lambda drink: drink.title)
        return sorted_drinks

    @log_time
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        drinks = list(self.wines.values()) + list(self.beers.values())

        filtered_drinks = list(filter(
            lambda drink: (from_date is None or drink.production_date >= from_date) and
                          (to_date is None or drink.production_date <= to_date),
            drinks
        ))
        sorted_filtered_drinks = sorted(filtered_drinks, key=lambda drink: drink.production_date)

        return sorted_filtered_drinks

