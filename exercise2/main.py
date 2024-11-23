# Створення запису
from exercise2.DBConnect import DBConnect


def create_cat(collection, name, age, features):
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        result = collection.insert_one(cat)
        print(f"Кіт доданий з _id: {result.inserted_id}")
    except Exception as e:
        print(f"Помилка при створенні запису: {e}")


# Читання всіх записів
def read_all_cats(collection):
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Помилка при читанні записів: {e}")


# Читання запису за ім'ям
def read_cat_by_name(collection, name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кіт із ім'ям '{name}' не знайдений.")
    except Exception as e:
        print(f"Помилка при пошуку кота: {e}")


# Оновлення віку кота за ім'ям
def update_cat_age(collection, name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print(f"Вік кота '{name}' оновлено до {new_age}.")
        else:
            print(f"Кіт із ім'ям '{name}' не знайдений.")
    except Exception as e:
        print(f"Помилка при оновленні віку: {e}")


# Додавання нової характеристики коту за ім'ям
def add_feature_to_cat(collection, name, new_feature):
    try:
        result = collection.update_one({"name": name}, {"$addToSet": {"features": new_feature}})
        if result.modified_count > 0:
            print(f"Характеристика '{new_feature}' додана коту '{name}'.")
        else:
            print(f"Кіт із ім'ям '{name}' не знайдений або характеристика вже існує.")
    except Exception as e:
        print(f"Помилка при додаванні характеристики: {e}")


# Видалення запису за ім'ям
def delete_cat_by_name(collection, name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кіт із ім'ям '{name}' видалений.")
        else:
            print(f"Кіт із ім'ям '{name}' не знайдений.")
    except Exception as e:
        print(f"Помилка при видаленні кота: {e}")


# Видалення всіх записів
def delete_all_cats(collection):
    try:
        result = collection.delete_many({})
        print(f"Видалено {result.deleted_count} записів.")
    except Exception as e:
        print(f"Помилка при видаленні всіх записів: {e}")


# Головна функція
if __name__ == "__main__":
    db = DBConnect()
    collection = db.collection

    while True:
        print("\nМеню:")
        print("1. Додати кота")
        print("2. Показати всіх котів")
        print("3. Показати кота за ім'ям")
        print("4. Оновити вік кота за ім'ям")
        print("5. Додати характеристику коту за ім'ям")
        print("6. Видалити кота за ім'ям")
        print("7. Видалити всіх котів")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("Введіть ім'я кота: ")
            age = int(input("Введіть вік кота: "))
            features = input("Введіть характеристики кота через кому: ").split(", ")
            create_cat(collection, name, age, features)

        elif choice == "2":
            read_all_cats(collection)

        elif choice == "3":
            name = input("Введіть ім'я кота: ")
            read_cat_by_name(collection, name)

        elif choice == "4":
            name = input("Введіть ім'я кота: ")
            new_age = int(input("Введіть новий вік кота: "))
            update_cat_age(collection, name, new_age)

        elif choice == "5":
            name = input("Введіть ім'я кота: ")
            new_feature = input("Введіть нову характеристику: ")
            add_feature_to_cat(collection, name, new_feature)

        elif choice == "6":
            name = input("Введіть ім'я кота: ")
            delete_cat_by_name(collection, name)

        elif choice == "7":
            delete_all_cats(collection)

        elif choice == "0":
            print("До побачення!")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")
