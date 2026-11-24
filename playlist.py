# مدیریت پلی‌لیست آهنگ
# هر آهنگ یک دیکشنری است و همه آهنگ‌ها در یک لیست قرار می‌گیرند.

songs = []


def add_song():
    artist = input("اسم خواننده: ")
    title = input("اسم آهنگ: ")
    genre = input("سبک آهنگ: ")
    album = input("نام آلبوم: ")
    songs.append({
        "artist": artist, "title": title,
        "genre": genre, "album": album
    })
    print("آهنگ اضافه شد.")


def show_songs():
    if len(songs) == 0:
        print("پلی‌لیست خالی است.")
    else:
        for song in songs:
            print("خواننده:", song["artist"],
                  "| آهنگ:", song["title"],
                  "| سبک:", song["genre"],
                  "| آلبوم:", song["album"])


def find_song():
    title = input("نام آهنگ برای جستجو: ")
    found = False
    for song in songs:
        if song["title"] == title:
            print("خواننده:", song["artist"],
                  "| آهنگ:", song["title"],
                  "| سبک:", song["genre"],
                  "| آلبوم:", song["album"])
            found = True
    if not found:
        print("آهنگی پیدا نشد.")


def delete_song():
    title = input("نام آهنگ برای حذف: ")
    for song in songs:
        if song["title"] == title:
            songs.remove(song)
            print("آهنگ حذف شد.")
            return
    print("آهنگی پیدا نشد.")


def edit_song():
    title = input("نام آهنگ برای ویرایش: ")
    for song in songs:
        if song["title"] == title:
            song["artist"] = input("اسم خواننده جدید: ")
            song["title"] = input("اسم آهنگ جدید: ")
            song["genre"] = input("سبک جدید: ")
            song["album"] = input("نام آلبوم جدید: ")
            print("اطلاعات آهنگ ویرایش شد.")
            return
    print("آهنگی پیدا نشد.")


# منوی اصلی در حلقه اجرا می‌شود.
while True:
    print("\n--- پلی‌لیست آهنگ ---")
    print("1) اد")
    print("2) شو (نمایش)")
    print("3) حذف")
    print("4) پیدا کردن")
    print("5) ادیت")
    print("6) خروج")
    choice = input("انتخاب شما: ")

    match choice:
        case "1":
            add_song()
        case "2":
            show_songs()
        case "3":
            delete_song()
        case "4":
            find_song()
        case "5":
            edit_song()
        case "6":
            print("برنامه تمام شد.")
            break
        case _:
            print("گزینه نامعتبر است.")
