# فروشگاه لباس
# اطلاعات کالاها در یک لیست از دیکشنری‌ها نگهداری می‌شود.

clothes = []


def choose_size():
    size = input("سایز را وارد کنید (XS, S, M, L, XL, XXL, 3XL, 4XL): ").upper()
    match size:
        case "XS" | "S" | "M" | "L" | "XL" | "XXL" | "3XL" | "4XL":
            return size
        case _:
            print("سایز نامعتبر است.")
            return None


def choose_model():
    model = input("مدل لباس (پیراهن، شلوار، کت): ")
    match model:
        case "پیراهن" | "شلوار" | "کت":
            return model
        case _:
            print("مدل نامعتبر است.")
            return None


def add_cloth():
    name = input("نام محصول: ")
    color = input("رنگ: ")
    size = choose_size()
    if size is None:
        return
    model = choose_model()
    if model is None:
        return
    stock_text = input("موجودی (عدد صحیح): ")
    price_text = input("قیمت: ")
    try:
        stock = int(stock_text)
        price = float(price_text)
        if stock < 0 or price < 0:
            print("موجودی و قیمت نمی‌توانند منفی باشند.")
            return
    except ValueError:
        print("موجودی و قیمت باید عدد باشند.")
        return

    clothes.append({
        "name": name, "color": color, "size": size,
        "model": model, "stock": stock, "price": price
    })
    print("کالا اضافه شد.")


def show_cloth(cloth):
    print("نام:", cloth["name"], "| رنگ:", cloth["color"],
          "| سایز:", cloth["size"], "| مدل:", cloth["model"],
          "| موجودی:", cloth["stock"], "| قیمت:", cloth["price"])


def find_cloth():
    name = input("نام محصول برای جستجو: ")
    found = False
    for cloth in clothes:
        if cloth["name"] == name:
            show_cloth(cloth)
            found = True
    if not found:
        print("کالایی پیدا نشد.")


def delete_cloth():
    name = input("نام محصول برای حذف: ")
    for cloth in clothes:
        if cloth["name"] == name:
            clothes.remove(cloth)
            print("کالا حذف شد.")
            return
    print("کالایی پیدا نشد.")


def edit_cloth():
    name = input("نام محصول برای ویرایش: ")
    for cloth in clothes:
        if cloth["name"] == name:
            print("اطلاعات جدید را وارد کنید:")
            color = input("رنگ جدید: ")
            size = choose_size()
            if size is None:
                return
            model = choose_model()
            if model is None:
                return
            try:
                stock = int(input("موجودی جدید: "))
                price = float(input("قیمت جدید: "))
                if stock < 0 or price < 0:
                    print("موجودی و قیمت نمی‌توانند منفی باشند.")
                    return
            except ValueError:
                print("موجودی و قیمت باید عدد باشند.")
                return
            cloth["color"] = color
            cloth["size"] = size
            cloth["model"] = model
            cloth["stock"] = stock
            cloth["price"] = price
            print("اطلاعات ویرایش شد.")
            return
    print("کالایی پیدا نشد.")


# منوی اصلی تا زمان انتخاب خروج تکرار می‌شود.
while True:
    print("\n--- فروشگاه لباس ---")
    print("1) اد (افزودن)")
    print("2) پیدا (جستجو)")
    print("3) حذف کالا")
    print("4) ادیت (ویرایش)")
    print("5) خروج")
    choice = input("انتخاب شما: ")

    match choice:
        case "1":
            add_cloth()
        case "2":
            find_cloth()
        case "3":
            delete_cloth()
        case "4":
            edit_cloth()
        case "5":
            print("برنامه تمام شد.")
            break
        case _:
            print("گزینه نامعتبر است.")
