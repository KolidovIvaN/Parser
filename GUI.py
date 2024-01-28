import subprocess
from tkinter import *
from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk
from Lexer import Lexer
from SyntaxAnalyzer import Syntax_analyzer

current_file = None
value = True


#  Функции для работы программы
#  Функция "Открытие Word-файла"
def open_word(file_path):
    try:
        subprocess.Popen(['start', 'winword', file_path], shell=True)
    except Exception as e:
        print(f'Произошла ошибка: {e}')


#  Функция "Открыть справку - о программе"
def open_guide():
    try:
        subprocess.Popen(['start', 'winword', './Files_tools/8. Справка (О программе).docx'], shell=True)
    except Exception as e:
        print(f'Произошла ошибка: {e}')


#  Функция "Создание файла"
def create_file():
    global text_editor
    text_editor = Text(window,
                       width=40,
                       height=15,
                       background='white',
                       font=('Calibri', 14),
                       bd=0,
                       highlightthickness=1,
                       highlightbackground='black'
                       )
    text_editor.place(x=10, y=102)


#  Функция "Открыть файл"
def open_file():
    create_file()
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Python files", "*.py")])
    if file_path:
        with open(file_path, "r") as file:
            file_content = file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", file_content)


#  Функция "Сохранить файл"
def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            user_input_text = text_editor.get("1.0", END)
            file.write(user_input_text)
    else:
        save_file_as()


#  Функция "Сохранить файл как"
def save_file_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"),
                                                        ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            user_input_text = text_editor.get("1.0", END)
            file.write(user_input_text)
        current_file = file_path


#  Функция "Увеличение шрифта"
def increase_font():
    current_font = text_editor['font']
    font_specs = str(current_font).split()
    size = int(font_specs[-1])
    new_size = size + 2
    text_editor.configure(font=('Calibri', new_size))


#  Функция "Уменьшение шрифта"
def decrease_font():
    current_font = text_editor['font']
    font_specs = str(current_font).split()
    size = int(font_specs[-1])
    if size > 2:
        new_size = size - 2
        text_editor.configure(font=('Calibri', new_size))
    else:
        pass


#  Функция "Очистить окно редактора"
def delete_text():
    text_editor.delete('1.0', 'end')
    console.configure(text='')


#  Функция "Выбор цвета для шрифта"
def change_color_font():
    color = colorchooser.askcolor(title='Выбор цвета текста')
    if color[1]:
        text_editor.configure(fg=color[1])


#  Функция "Смена темы GUI"
def theme_color():
    global value
    if value == True:
        dark_color_button = '#82877b'
        window.configure(background='#212121')  # темная тема
        console.configure(background='#2c2c2c',
                          highlightthickness=1,
                          highlightbackground='white')
        console_label.configure(background='#FFFFFF')
        text_editor_label.configure(background='#FFFFFF')
        text_editor.configure(background='#2c2c2c',
                              highlightthickness=1,
                              highlightbackground='white',
                              fg='#ff8000')
        button_create_file.configure(background=dark_color_button)
        button_open_file.configure(background=dark_color_button)
        button_save_file.configure(background=dark_color_button)
        button_font_up.configure(background=dark_color_button)
        button_font_down.configure(background=dark_color_button)
        button_clear_text.configure(background=dark_color_button)
        button_color_text.configure(background=dark_color_button)
        button_theme.configure(background=dark_color_button)
        button_start.configure(background=dark_color_button)

        value = False

    else:
        white_color_button = 'light grey'
        window.configure(background='#ecf0f1')
        console.configure(background='white',
                          highlightthickness=1,
                          highlightbackground='black'
                          )
        console_label.configure(background='#ecf0f1')
        text_editor_label.configure(background='#ecf0f1')
        text_editor.configure(background='white',
                              highlightthickness=1,
                              highlightbackground='black',
                              fg='#000000')
        button_create_file.configure(background=white_color_button)
        button_open_file.configure(background=white_color_button)
        button_save_file.configure(background=white_color_button)
        button_font_up.configure(background=white_color_button)
        button_font_down.configure(background=white_color_button)
        button_clear_text.configure(background=white_color_button)
        button_color_text.configure(background=white_color_button)
        button_theme.configure(background=white_color_button)
        button_start.configure(background=white_color_button)
        value = True


#  Функция "Запуск анализатора"
def syntax_analyzer():
    input_code = text_editor.get("1.0", END)
    tokens = Lexer().add_tokens(input_code)
    output = Syntax_analyzer().analyzer(tokens)
    print(f'Входные токены: {tokens}')
    if not output:
        console.config(text='Исходное выражение:' '\n' f'{input_code}' '\n' 'Ошибок не обнаружено',
                       justify='left',
                       anchor='nw',
                       foreground='black')
    else:
        console.config(text='\n'.join(map(lambda x: f'ERROR: {x}', output)),
                       justify='left',
                       anchor='nw',
                       foreground='red')


#  Основное окно программы
window = Tk()
window.title('Объявление целочисленной константы с инициализацией на Java')
window.geometry('855x500')
window.configure(background='#ecf0f1')
window.iconphoto(False, PhotoImage(file='./Icons/Icon_1.png'))
window.wm_attributes('-alpha', 1)
window.resizable(width=False, height=False)

#  "Меню компилятора"
menu = Menu(window)
#  Пункт "Файл" меню компилятора
file_item = Menu(menu, tearoff=0)
file_item.add_command(label='Создать', command=create_file)
file_item.add_separator()
file_item.add_command(label='Открыть', command=open_file)
file_item.add_separator()
file_item.add_command(label='Сохранить', command=save_file)
file_item.add_separator()
file_item.add_command(label='Сохранить как', command=save_file_as)
file_item.add_separator()
file_item.add_command(label='Выход')
file_item.add_separator()
menu.add_cascade(label='Файл', menu=file_item)

#  Пункт "Инструменты" меню компилятора
tools_item = Menu(menu, tearoff=0)
files_tools = [
    ('Постановка задачи', './Files_tools/1. Постановка задачи.docx'),
    ('Порождающая грамматика', './Files_tools/2. Порождающая грамматика.docx'),
    ('Классификация Хомского', './Files_tools/3. Классификация Хомского.docx'),
    ('Метод анализа', './Files_tools/4. Метод.docx'),
    ('Диагностика и нейтрализация', './Files_tools/5. Диагностика и нейтрализация.docx'),
    ('Тестирование', './Files_tools/6. Тестирование.docx'),
    ('Листинг программы', './Files_tools/7. Листинг программы.docx')
]
for file, file_path in files_tools:
    tools_item.add_command(label=file, command=lambda path=file_path: open_word(path))
    tools_item.add_separator()

menu.add_cascade(label='Инструменты', menu=tools_item)

#  Пункт "Справка" меню компилятора
help_item = Menu(menu, tearoff=0)
help_item.add_command(label='О программе', command=open_guide)
help_item.add_separator()
menu.add_cascade(label='Справка', menu=help_item)

#  Пункт "Выход" меню компилятора
for _ in range(43):
    menu.add_separator()
menu.add_command(label='Выход', command=window.quit)
window.config(menu=menu)

#  Разграничение GUI
separator_canvas = Canvas(window, width=853, height=2, bg='grey', highlightthickness=0)
separator_canvas.place(x=1, y=0)

separator_canvas = Canvas(window, width=853, height=2, bg='grey', highlightthickness=0)
separator_canvas.place(x=1, y=65)

#  Кнопки "Панели инструментов"
#  Кнопка "Создать файл"
photo_create_file = Image.open('./Icons/file_create.png')
img_create_file = ImageTk.PhotoImage(photo_create_file)
button_create_file = Button(window, image=img_create_file, width=25, height=25, background='light grey',
                            command=create_file)
button_create_file.place(x=60, y=20)

#  Кнопка "Открыть файл"
photo_open_file = Image.open('./Icons/file_open.png')
img_open_file = ImageTk.PhotoImage(photo_open_file)
button_open_file = Button(window, image=img_open_file, width=25, height=25, background='light grey', command=open_file)
button_open_file.place(x=105, y=20)

#  Кнопка "Сохранить файл"
photo_save_file = Image.open('./Icons/file_save.png')
img_save_file = ImageTk.PhotoImage(photo_save_file)
button_save_file = Button(window, image=img_save_file, width=25, height=25, background='light grey', command=save_file)
button_save_file.place(x=150, y=20)

#  Кнопка "Увеличение шрифта"
photo_font_up = Image.open('./Icons/size_up.png')
img_font_up = ImageTk.PhotoImage(photo_font_up)
button_font_up = Button(window, image=img_font_up, width=25, height=25, background='light grey', command=increase_font)
button_font_up.place(x=270, y=20)

#  Кнопка "Уменьшение шрифта"
photo_font_down = Image.open('./Icons/size_down.png')
img_font_down = ImageTk.PhotoImage(photo_font_down)
button_font_down = Button(window, image=img_font_down, width=25, height=25, background='light grey',
                          command=decrease_font)
button_font_down.place(x=315, y=20)

#  Кнопка "Очистка экрана"
photo_clear_text = Image.open('./Icons/delete_text.png')
img_clear_text = ImageTk.PhotoImage(photo_clear_text)
button_clear_text = Button(window, image=img_clear_text, width=25, height=25, background='light grey',
                           command=delete_text)
button_clear_text.place(x=360, y=20)

#  Кнопка "Очистка экрана"
photo_color_text = Image.open('./Icons/color_font.png')
img_color_text = ImageTk.PhotoImage(photo_color_text)
button_color_text = Button(window, image=img_color_text, width=25, height=25, background='light grey',
                           command=change_color_font)
button_color_text.place(x=405, y=20)

#  Кнопка "Тема"
photo_theme = Image.open('./Icons/theme.png')
img_theme = ImageTk.PhotoImage(photo_theme)
button_theme = Button(window, image=img_theme, width=25, height=25, background='light grey', command=theme_color)
button_theme.place(x=450, y=20)

#  Кнопка "Старт"
photo_start = Image.open('./Icons/start_2.png')
img_start = ImageTk.PhotoImage(photo_start)
button_start = Button(window, image=img_start, width=25, height=25, background='light grey', command=syntax_analyzer)
button_start.place(x=600, y=20)

#  Окно редактирования и консоль
#  Консоль
#  Вывод надписи "Консоль"
console_label = Label(window,
                      text='Консоль (окно вывода сообщений)',
                      font='Calibri 13',
                      background='#ecf0f1')
console_label.place(x=450, y=75)
#  Окно консоли
console = Label(window,
                width=40,
                height=15,
                background='white',
                font='Calibri 14',
                bd=0,
                highlightthickness=1,
                highlightbackground='black',
                wraplength=400)
console.place(x=445, y=102)

#  Вывод надписи "Окно редактирования"
text_editor_label = Label(window,
                          text='Окно редактирования',
                          font='Calibri 13',
                          background='#ecf0f1')
text_editor_label.place(x=30, y=75)

window.mainloop()
