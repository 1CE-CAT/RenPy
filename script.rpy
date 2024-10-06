# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    show eileen happy

    e "Это программа для теста"
    menu:
        "Пожалуйста выберете минигру"
        "Три в ряд":
            jump three_in_row
        "Вариант 2":
            "Пока не готово"
            jump start
        "Вариант 3":
            "Пока не готово"
            jump start
        "Вариант 4":
            "Пока не готово"
            jump start
        "Вариант 5":
            "Пока не готово"
            jump start
    
    return

label three_in_row:
    call krix
    pause 1
    centered "{size=52}Поздравляем \n Ваш результат {color=#f2b627}[pointk]"
    if pointk > 100:
        e "Проигрыш"
    else:
        e "Выигрыш"
    return
