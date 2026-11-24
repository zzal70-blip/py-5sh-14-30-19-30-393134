# فروشگاه مواد غذایی
# کالاها در یک لیست از دیکشنری‌ها نگهداری می‌شوند.


products = []


def choose_category():
    print("دسته‌ها: پروتئین، تنقلات، نوشیدنی، شوینده")
    category = input("دسته مواد: ")
    match category:
        case "پروتئین":
            return category
        case "تنقلات":
            return category
        case "نوشیدنی":
            return category
        case "شوینده":
            return category
        case _:
            print("دسته نامعتبر است.")
            return None


def add_product():
    name = input("نام محصول: ")
    category = choose_category()
    if category is None:
        return

    weight = None
    if category == "پروتئین":
        weight = input("وزن محصول (مثلاً 500 گرم): ")

    try:
        stock = int(input("موجودی: "))
        price = float(input("قیمت: "))
        if stock < 0 or price < 0:
            print("موجودی و قیمت نمی‌توانند منفی باشند.")
            return
    except ValueError:
        print("موجودی و قیمت باید عدد باشند.")
        return

    products.append({
        "name": name, "category": category,
        "weight": weight, "stock": stock, "price": price
    })
    print("کالا اضافه شد.")


def show_product(product):
    print("نام:", product["name"],
          "| دسته:", product["category"],
          "| وزن:", product["weight"],
          "| موجودی:", product["stock"],
          "| قیمت:", product["price"])


def delete_product():
    name = input("نام محصول برای حذف: ")
    for product in products:
        if product["name"] == name:
            products.remove(product)
            print("کالا حذف شد.")
            return
    print("کالایی پیدا نشد.")


def edit_product():
    name = input("نام محصول برای ویرایش: ")
    for product in products:
        if product["name"] == name:
            new_name = input("نام جدید: ")
            category = choose_category()
            if category is None:
                return

            weight = None
            if category == "پروتئین":
                weight = input("وزن جدید (مثلاً 500 گرم): ")

            try:
                stock = int(input("موجودی جدید: "))
                price = float(input("قیمت جدید: "))
                if stock < 0 or price < 0:
                    print("موجودی و قیمت نمی‌توانند منفی باشند.")
                    return
            except ValueError:
                print("موجودی و قیمت باید عدد باشند.")
                return

            product["name"] = new_name
            product["category"] = category
            product["weight"] = weight
            product["stock"] = stock
            product["price"] = price
            print("اطلاعات کالا ویرایش شد.")
            return
    print("کالایی پیدا نشد.")


# منوی اصلی تا انتخاب خروج تکرار می‌شود.
while True:
    print("\n--- فروشگاه مواد غذایی ---")
    print("1) اد")
    print("2) حذف")
    print("3) ادیت")
    print("4) خروج")
    choice = input("انتخاب شما: ")

    match choice:
        case "1":
            add_product()
        case "2":
            delete_product()
        case "3":
            edit_product()
        case "4":
            print("برنامه تمام شد.")
            break
        case _:
            print("گزینه نامعتبر است.")
