class Store:
    def __init__(self, name, address):
        # Конструктор класса Store, инициализирующий атрибуты name, address и пустой словарь items
        self.name = name
        self.address = address
        self.items = {}  # Словарь для хранения товаров (ключ - название товара, значение - цена)

    def add_item(self, item_name, price):
        # Метод для добавления товара в ассортимент магазина
        self.items[item_name] = price

    def remove_item(self, item_name):
        # Метод для удаления товара из ассортимента магазина
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        # Метод для получения цены товара по его названию
        return self.items.get(item_name)

    def update_item_price(self, item_name, new_price):
        # Метод для обновления цены товара
        if item_name in self.items:
            self.items[item_name] = new_price

# Создаем несколько магазинов
store1 = Store("Магазин продуктов", "ул. Центральная, 1")
store2 = Store("Магазин электроники", "пр. Солнечный, 10")
store3 = Store("Магазин одежды", "ул. Главная, 5")

# Добавляем товары в магазины
store1.add_item("Яблоки", 0.5)
store1.add_item("Бананы", 0.75)
store2.add_item("Ноутбук", 1000)
store2.add_item("Смартфон", 500)
store3.add_item("Футболка", 15)
store3.add_item("Джинсы", 30)

# Тестирование методов магазина
print("Цена яблок в магазине:", store1.get_item_price("Яблоки"))
store1.update_item_price("Яблоки", 0.6)
print("Новая цена яблок в магазине:", store1.get_item_price("Яблоки"))
store1.remove_item("Бананы")
print("Цена бананов в магазине:", store1.get_item_price("Бананы"))
