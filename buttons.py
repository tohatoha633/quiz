from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu():
    # Asosiy menyu tugmalari yangilandi
    kb = [
        [KeyboardButton(text="🐍 Python savol"), KeyboardButton(text="🌐 JavaScript savol")],
        [KeyboardButton(text="📊 Мой рейтинг"), KeyboardButton(text="⚙️ Помощь")]
    ]
    # resize_keyboard=True tugmalarni ixcham qiladi
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def get_quiz_info():
    # Savol tagida chiquvchi inline tugma
    inline_kb = [
        [InlineKeyboardButton(text="💡 Объяснить решение", callback_data="explain")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb)
