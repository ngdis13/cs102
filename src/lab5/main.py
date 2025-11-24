from file_manager import FileManager
from validators import OrderValidator
from processing import OrderProcessor


def main():
    """Функция запуска всего приложения"""
    fm = FileManager()
    validator = OrderValidator()

    processor = OrderProcessor(
        all_orders=[],
        valid_orders=[],
        invalid_errors=[],
        validator=validator,
        file_manager=fm
    )

    processor.process(
        input_file="orders.txt",
        valid_output="order_country.txt",
        invalid_output="non_valid_orders.txt"
    )

    print("\nОбработка завершена.")
    print(f"Валидные заказы сохранены в order_country.txt")
    print(f"Ошибки сохранены в non_valid_orders.txt")


if __name__ == "__main__":
    main()