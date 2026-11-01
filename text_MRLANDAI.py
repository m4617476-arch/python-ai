
# def MRLANDAI():
#     print('Hello! I am MRLAND AI!')

#     # اطلاعات اولیه‌ای که برنامه در حافظه دارد
#     data = ["mohammad", "18", "python"]

#     # دریافت ورودی از کاربر
#     user = input('Enter: ')

#     # اگر کاربر چیزی وارد نکرد
#     if user == '':
#         print('You entered nothing!')

#     # اگر ورودی از قبل در حافظه باشد
#     elif user in data:
#         print('I already know:', user)

#     # اگر ورودی جدید باشد، آن را ذخیره کن
#     else:
#         data.append(user)
#         print('OK, I learned:', user)

#     # نمایش اطلاعات فعلی حافظه
#     print('My memory:', data)


# MRLANDAI()
#############################################################################################################################################

# # نام پروژه را مشخص می‌کنیم
# # تابع اصلی برنامه را تعریف می‌کنیم
# def MRLANDAI():

#     # پیام خوشامدگویی را نمایش می‌دهیم
#     print("Hello! I am MR LAND AI.")

#     # روش خروج از برنامه را به کاربر اعلام می‌کنیم
#     print("Type 'exit' to stop the conversation.")

#     # تلاش می‌کنیم حافظه قبلی برنامه را از فایل بخوانیم
#     try:

#         # فایل حافظه را با پشتیبانی از متن انگلیسی و فارسی باز می‌کنیم
#         with open("data.txt", "r", encoding="utf-8") as file:

#             # تمام خط‌های فایل را می‌خوانیم و در فهرست ذخیره می‌کنیم
#             data = file.read().splitlines()

#     # اگر فایل حافظه وجود نداشت، این قسمت اجرا می‌شود
#     except FileNotFoundError:

#         # یک فهرست خالی برای حافظه ایجاد می‌کنیم
#         data = []

#     # گفتگو را تا زمان خروج کاربر ادامه می‌دهیم
#     while True:

#         # پیام کاربر را دریافت می‌کنیم و فاصله‌های اضافی را حذف می‌کنیم
#         # حروف انگلیسی را نیز به حروف کوچک تبدیل می‌کنیم
#         user = input("You: ").strip().lower()

#         # بررسی می‌کنیم که آیا کاربر قصد خروج دارد
#         if user == "exit":

#             # پیام خداحافظی را نمایش می‌دهیم
#             print("MR LAND AI: Goodbye!")

#             # اجرای حلقه را متوقف می‌کنیم
#             break

#         # بررسی می‌کنیم که آیا ورودی کاربر خالی است
#         if user == "":

#             # از کاربر می‌خواهیم پیامی وارد کند
#             print("MR LAND AI: You entered nothing!")

#             # به ابتدای حلقه برمی‌گردیم
#             continue

#         # اگر پیام کاربر سلام باشد، پاسخ مناسب می‌دهیم
#         if user == "hello":
#             print("MR LAND AI: Hello! Nice to meet you!")

#         # اگر کاربر درباره حال برنامه بپرسد، پاسخ می‌دهیم
#         elif user == "how are you":
#             print("MR LAND AI: I'm fine! How are you?")

#         # اگر کاربر نام برنامه را بپرسد، آن را اعلام می‌کنیم
#         elif user == "what is your name":
#             print("MR LAND AI: I am MR LAND AI!")

#         # اگر کاربر درباره سن برنامه بپرسد، پاسخ می‌دهیم
#         elif user == "how old are you":
#             print("MR LAND AI: I don't have a human age!")

#         # بررسی می‌کنیم که آیا پیام قبلاً در حافظه ذخیره شده است
#         if user not in data:

#             # پیام جدید را به حافظه اضافه می‌کنیم
#             data.append(user)

#             # ذخیره پیام جدید را به کاربر اعلام می‌کنیم
#             print("MR LAND AI: I saved this message to memory.")

#         # اگر پیام قبلاً ذخیره شده باشد، این قسمت اجرا می‌شود
#         else:

#             # به کاربر می‌گوییم که پیام را از قبل می‌شناسیم
#             print("MR LAND AI: I already know this message.")

#     # پس از پایان گفتگو، فایل حافظه را برای نوشتن باز می‌کنیم
#     with open("data.txt", "w", encoding="utf-8") as file:

#         # پیام‌های حافظه را با جداکننده خط جدید در فایل ذخیره می‌کنیم
#         file.write("\n".join(data))

#     # موفقیت‌آمیز بودن ذخیره حافظه را اعلام می‌کنیم
#     print("MR LAND AI: Memory saved successfully!")


# # تابع اصلی را اجرا می‌کنیم
# MRLANDAI()

###################################################################################################################


import json # کتابخانه json را وارد می‌کنیم تا بتونیم داده‌ها را در فایل ذخیره و بازخوانی کنیم

# نام فایلی که قرار است داده‌ها در آن ذخیره شوند را در یک متغیر ثابت نگه می‌داریم
MEMORY_FILE = "data.json" 

# ==========================================
# تابع ۱: خواندن حافظه از فایل
# ==========================================
def load_memory():
    try:
        # فایل را در حالت خواندن ("r") با انکودینگ utf-8 باز می‌کنیم
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file) # محتوای فایل را به یک دیکشنری پایتون تبدیل می‌کنیم

        # بررسی می‌کنیم که آیا داده خوانده شده واقعا یک دیکشنری است یا نه
        if isinstance(data, dict):
            return data # اگر دیکشنری بود، آن را برمی‌گردانیم

        print('AI >> New memory file created.') # اگر دیکشنری نبود، پیام می‌دهیم
        return {} # و یک دیکشنری خالی برمی‌گردانیم

    except FileNotFoundError:
        # اگر فایل وجود نداشت (اولین بار اجرا)، خطا نمی‌دهیم و دیکشنری خالی برمی‌گردانیم
        return {}

    except json.JSONDecodeError:
        # اگر فایل وجود داشت ولی محتوایش خراب بود (مثلا دستی تغییرش داده بودیم)
        print("AI >> Memory file is invalid. Starting with empty memory.")
        return {} # دیکشنری خالی برمی‌گردانیم تا برنامه کرش نکند

# ==========================================
# تابع ۲: ذخیره حافظه در فایل
# ==========================================
def save_memory(data):
    try:
        # فایل را در حالت نوشتن ("w") باز می‌کنیم
        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            # داده‌ها را با فرمت زیبا (indent=4) و بدون تبدیل کاراکترهای فارسی به کد (ensure_ascii=False) ذخیره می‌کنیم
            json.dump(data, file, ensure_ascii=False, indent=4)
        return True # اگر ذخیره موفق بود، True برمی‌گردانیم

    except OSError:
        # اگر مشکلی در نوشتن روی فایل پیش آمد (مثلا کمبود فضای دیسک)
        print("AI >> Could not save memory.")
        return False # False برمی‌گردانیم

# ==========================================
# تابع ۳: جستجوی جواب در حافظه
# ==========================================
def get_answer(question, data):
    # فاصله‌های اضافی ابتدا و انتهای سوال را حذف می‌کنیم
    question = question.strip()
    
    # حروف را کوچک می‌کنیم تا مثلا Hello و hello یکی باشند
    question = question.lower()

    # اگر سوال در حافظه بود، جواب آن را برمی‌گردانیم
    if question in data:
        return data[question]

    # اگر سوال در حافظه نبود، None برمی‌گردانیم (یعنی نمی‌دانم)
    return None

# ==========================================
# تابع ۴: حلقه اصلی برنامه (مغز ربات)
# ==========================================
def MRLANDAI():
    # در شروع برنامه، حافظه را از فایل می‌خوانیم
    data = load_memory()

    print('AI >> Hello, I am MR LAND AI. How can I help you?')
    print('AI >> Type "exit" to stop the app.')
    print('#################################################')

    while True: # حلقه بی‌نهایت تا زمانی که کاربر دستور خروج بدهد
        user = input('YOU >> ').strip().lower() # ورودی کاربر را می‌گیریم و همزمان تمیزش می‌کنیم

        # ۱. بررسی دستور خروج
        if user == 'exit':
            print('AI >> Goodbye!')
            break # از حلقه خارج می‌شویم

        # ۲. بررسی اینکه کاربر چیزی تایپ کرده یا فقط اینتر زده
        if not user:
            print('AI >> Please enter a message.')
            continue # برمی‌گردیم به اول حلقه و از کاربر دوباره می‌پرسیم

        # ۳. جستجوی جواب در حافظه
        answer = get_answer(user, data)

        # ۴. اگر جواب پیدا شد
        if answer is not None:
            print('AI >>', answer)

        # ۵. اگر جواب پیدا نشد (ربات نمی‌داند)
        else:
            print('AI >> I don\'t know the answer yet.')
            
            # از کاربر می‌پرسیم آیا می‌خواهد به ما یاد بدهد
            teach = input('AI >> Do you like to teach me? (yes/no): ').strip().lower()

            if teach == 'yes':
                # از کاربر جواب را می‌پرسیم (بدون split تا جمله کامل ذخیره شود)
                new_answer = input('Enter the answer >> ').strip()

                # اگر کاربر جواب خالی وارد نکرده بود
                if new_answer:
                    data[user] = new_answer # سوال و جواب را در دیکشنری ذخیره می‌کنیم
                    save_memory(data)      # 👈 مهم‌ترین خط: بلافاصله در فایل json ذخیره می‌کنیم
                    print('AI >> I learned it!')
                else:
                    print('AI >> Empty answers cannot be saved.')
            else:
                print('AI >> Okay, maybe next time.')

# اجرای برنامه
MRLANDAI()
#################################################################################################################