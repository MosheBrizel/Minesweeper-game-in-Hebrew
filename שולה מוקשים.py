import time
import tkinter
import tkinter as Tk
from tkinter import *
from tkinter import messagebox
from random import choice
from random import randint

window = Tk()
window.title("שולה מוקשים")  # Set the title of the window
window.configure(bg="#F5F5DC")  # Set the background color of the window

# Define a class to store row, column, bomb, and high letter data
class row_col_bomb_letter:
    def __init__(self, len_row=0, len_col=0, sum_bomb=0, high_letter=0):
        self.high_letter = high_letter
        self.sum_bomb = sum_bomb
        self.len_col = len_col
        self.len_row = len_row

# Initialize variables
num_level = row_col_bomb_letter()
counter_open_next = 0
number_open = 0
list_bomb_positions = []
list_move_button = []
list_press_button = []
game_over = False
label_play = None
clear_button = None
window_buttons = None
level_button = None
label_win = False
label_lose = False

# Function to retrieve the value from the dictionary based on row and column indices
def value_in_dict(row_int, col_int):
    return dict_numbers[row_int][col_int]

# Function to add numbers and bombs to the game grid
def add_numbers_bomb():
    counter_bomb = 0
    while counter_bomb != num_level.sum_bomb:
        rundom_row = randint(0, num_level.len_row - 1)
        rundom_col = randint(0, num_level.len_col - 1)
        if value_in_dict(rundom_row, rundom_col) != "💣":
            counter_bomb += 1
            dict_numbers[rundom_row][rundom_col] = "💣"
            list_bomb_positions.append((rundom_row, rundom_col))

    for position_bomb in list_bomb_positions:
        for plus_row in range(3):
            for plus_col in range(3):
                if position_bomb[1] - 1 + plus_col != -1:

                    try:
                        if value_in_dict((position_bomb[0] - 1) + plus_row, (position_bomb[1] - 1) + plus_col) != "💣":
                            dict_numbers[(position_bomb[0] - 1) + plus_row][(position_bomb[1] - 1) + plus_col] += 1
                    except:
                        pass

# Function to open all buttons on the grid
def open_all():
    for row_button in range(num_level.len_row):
        for col_button in range(num_level.len_col):
            button_open = dict_buttons[row_button][col_button]
            button_open["state"] = "disabled"
            if dict_numbers[row_button][col_button] == 0:
                button_open["bg"] = "#FFFFFF"
            else:
                button_open["bg"] = "#FFFFFF"
                button_open["text"] = dict_numbers[row_button][col_button]
                button_open["disabledforeground"] = "black"
            if len(list_press_button) == num_level.len_row * num_level.len_col - num_level.sum_bomb and \
                    dict_numbers[row_button][col_button] == "💣":
                button_open["bg"] = "#8FF67D"  # green

            elif dict_numbers[row_button][col_button] == "💣":
                button_open["bg"] = "#F67D7D"  # red

# Function to open adjacent buttons when a button with 0 bombs nearby is pressed
def open_next(int_row, int_col):
    try:
        if dict_numbers[int_row - 1][int_col] != "💣" \
                and dict_buttons[int_row - 1][int_col] not in list_move_button:
            list_move_button.append(dict_buttons[int_row - 1][int_col])
            press_button(int_row - 1, int_col, dict_buttons[int_row - 1][int_col])

    except:
        pass
    try:
        if dict_numbers[int_row][int_col - 1] != "💣" \
                and dict_buttons[int_row][int_col - 1] not in list_move_button:
            list_move_button.append(dict_buttons[int_row][int_col - 1])
            press_button(int_row, int_col - 1, dict_buttons[int_row][int_col - 1])
    except:
        pass
    try:
        if dict_numbers[int_row][int_col + 1] != "💣" and dict_buttons[int_row][int_col + 1] not in list_move_button:
            list_move_button.append(dict_buttons[int_row][int_col + 1])
            press_button(int_row, int_col + 1, dict_buttons[int_row][int_col + 1])
    except:
        pass
    try:

        if dict_numbers[int_row + 1][int_col] != "💣" and dict_buttons[int_row + 1][int_col] not in list_move_button:
            list_move_button.append(dict_buttons[int_row + 1][int_col])
            press_button(int_row + 1, int_col, dict_buttons[int_row + 1][int_col])
    except:
        pass
    return

# Function to handle button press event
def press_button(row_int, col_int, name_button):
    global counter_open_next, number_open, game_over, label_win, label_lose

    if name_button not in list_press_button and dict_numbers[row_int][col_int] != "💣":
        list_press_button.append(name_button)
    if name_button["text"] != "🚩":
        if dict_numbers[row_int][col_int] == 0:
            name_button["bg"] = "#FFFFFF"
        else:
            name_button["text"] = dict_numbers[row_int][col_int]
            name_button["bg"] = "#FFFFFF"
            name_button["disabledforeground"] = "black"

    # Check if the game is over (win or lose conditions)
    if dict_numbers[row_int][col_int] == "💣":
        game_over = True
        label_lose = Label(window, text=f"הפסדת !", bg="#F5F5DC", fg="red", font=("Helvetica", 50))
        label_lose.place(relx=0.5, rely=0.5, anchor=CENTER)
    if len(list_press_button) == num_level.len_row * num_level.len_col - num_level.sum_bomb:
        game_over = True
        label_win = Label(window, text=f"אתה ניצחת !", bg="#F5F5DC", fg="green", font=("Helvetica", 50))
        label_win.place(relx=0.5, rely=0.5, anchor=CENTER)

    # If the pressed button has no bombs nearby, open adjacent buttons
    if dict_numbers[row_int][col_int] == 0:
        open_next(row_int, col_int)

    name_button["state"] = "disabled"
    if game_over:
        open_all()

    return

# Function to handle right-click event on buttons
def right_click(event,button_):
    global counter_flay
    if button_["text"] == "" and counter_flay > 0:
        button_["text"] = "🚩"
        button_["state"] = "disabled"
        button_["disabledforeground"] = "#FA0E03"
        counter_flay -= 1
        label_play["text"] = f"מספר הפצצות שנותר למצוא הוא : {counter_flay}"

    elif button_["text"] == "🚩":
        button_["text"] = ""
        button_["state"] = "normal"
        counter_flay += 1
        label_play["text"] = f"מספר הפצצות שנותר למצוא הוא : {counter_flay}"

    else:
        pass

# Function to output the game grid based on the selected level.
def level_output():
    global button_game, label_play, window_buttons, clear_button, dict_buttons, dict_numbers, counter_flay, level_button
    dict_numbers = {x: [0 for i in range(num_level.len_col)] for x in range(num_level.len_row)}
    dict_buttons = {x: ["" for m in range(num_level.len_col)] for x in range(num_level.len_row)}
    counter_flay = num_level.sum_bomb

    add_numbers_bomb()
    label_play = Label(window, text=f"מספר הפצצות שנותר למצוא הוא : {counter_flay}", bg="#F5F5DC",
                       font=("Helvetica", 20), fg="#17B5F5")
    label_play.pack()
    window_buttons = tkinter.Frame(window, bg="#F5F5DC")
    window_buttons.pack(padx=20, pady=20)

    for y in range(num_level.len_row):
        for x in range(num_level.len_col):
            button_game = Button(window_buttons, fg='black', bg="#17B5F5", text="",
                                 font=("Helvetica", num_level.high_letter),
                                 width=2, height=0)
            button_game.configure(
                command=lambda row=y, col=x, button_num=button_game: press_button(row, col, button_num))
            button_game.bind("<Button-3>",
                             lambda button_r, button_right=button_game: right_click(button_r, button_right))
            button_game.grid(row=y, column=x)
            button_game["state"] = "normal"
            dict_buttons[y][x] = button_game

    clear_button = Button(window, text="אפס את המשחק", command=lambda: clear_screen("clear"))
    clear_button.pack()
    level_button = Button(window, text="רמה אחרת", command=lambda: clear_screen("level"))
    level_button.pack()


def clear_screen(level_or_clin):
    global game_over
    global counter_bomb, counter_open_next, number_open, dict_numbers, list_bomb_positions, list_move_button, \
        dict_buttons
    global counter_all_open, list_press_button, clear_button, window_buttons, level_button
    if not game_over:
        answer = messagebox.askokcancel("massage", "אתה בטוח שאתה רוצה לאפס את המשחק ?")
        if not answer:
            return
    list_press_button = []
    counter_bomb = 0
    counter_open_next = 0
    number_open = 0
    dict_numbers = {x: [0 for i in range(num_level.len_col)] for x in range(num_level.len_row)}
    list_bomb_positions = []
    list_move_button = []
    dict_buttons = {x: ["" for m in range(num_level.len_col)] for x in range(num_level.len_row)}
    game_over = False
    label_play.destroy()
    clear_button.destroy()
    window_buttons.destroy()
    level_button.destroy()
    if label_win:
        label_win.destroy()
    if label_lose:
        label_lose.destroy()
    if level_or_clin == "level":
        first_output()
        return
    level_output()

# Function to open the game grid based on the user's personal choices
def personal_choice():
    label_chose.destroy()
    window_chose_label.destroy()
    label_chose_personal = Label(window, text=f"בחר את השורות ועמודות ופצצות", bg="#F5F5DC", font=("Helvetica", 20))
    label_chose_personal.pack()
    window_personal_choice = tkinter.Frame(window, bg="#F5F5DC")
    window_personal_choice.pack(padx=20, pady=20)

    label_row = Label(window_personal_choice, text=f"שורת : ", bg="#F5F5DC", font=("Helvetica", 30))
    label_row.grid(row=0, column=0, rowspan=2, padx=0, pady=20)
    label_col = Label(window_personal_choice, text=f"עמודות : ", bg="#F5F5DC", font=("Helvetica", 30))
    label_col.grid(row=3, column=0, rowspan=2, padx=0, pady=20)
    label_bomb = Label(window_personal_choice, text=f"פצצות : ", bg="#F5F5DC", font=("Helvetica", 30))
    label_bomb.grid(row=6, column=0, rowspan=2, padx=0, pady=20)
    label_row_max = Label(window_personal_choice, text=f"מקסימום 14", bg="#F5F5DC", font=("Helvetica", 30))
    label_row_max.grid(row=0, column=2, rowspan=2, padx=0, pady=20)
    label_col = Label(window_personal_choice, text=f"מקסימום 38", bg="#F5F5DC", font=("Helvetica", 30))
    label_col.grid(row=3, column=2, rowspan=2, padx=0, pady=20)
    label_bomb = Label(window_personal_choice, text=f" מקסימום 531", bg="#F5F5DC", font=("Helvetica", 30))
    label_bomb.grid(row=6, column=2, rowspan=2, padx=0, pady=20)

    def increment_row():
        value_row = entry_row.get()
        if not value_row.isdigit():
            value_row = 2
            entry_row.delete(0, END)
            entry_row.insert(0, str(value_row))
            return

        value_row = int(value_row)
        value_row += 1
        if value_row > 14:
            value_row = 1
        entry_row.delete(0, END)
        entry_row.insert(0, str(value_row))

    def decrement_row():
        value = entry_row.get()
        if not value.isdigit():
            value = 2
            entry_row.delete(0, END)
            entry_row.insert(0, str(value))
            return

        value = int(value)
        value -= 1
        if value < 1:
            value = 14
        if value > 14:
            value = 14
        entry_row.delete(0, END)
        entry_row.insert(0, str(value))

    def increment_col():
        value = entry_col.get()
        if not value.isdigit():
            value = 2
            entry_col.delete(0, END)
            entry_col.insert(0, str(value))
            return

        value = int(value)
        value += 1
        if value > 38:
            value = 1
        entry_col.delete(0, END)
        entry_col.insert(0, str(value))

    def decrement_col():
        value = entry_col.get()
        if not value.isdigit():
            value = 2
            entry_col.delete(0, END)
            entry_col.insert(0, str(value))
            return

        value = int(value)
        value -= 1
        if value < 1:
            value = 38
        if value > 38:
            value = 38

        entry_col.delete(0, END)
        entry_col.insert(0, str(value))

    def increment_bomb():
        value = entry_bomb.get()
        if not value.isdigit():
            value = 1
            entry_bomb.delete(0, END)
            entry_bomb.insert(0, str(value))
            return

        value = int(value)
        value += 1
        if value > 531:
            value = 1

        if value > 531:
            value = 531
        entry_bomb.delete(0, END)
        entry_bomb.insert(0, str(value))

    def decrement_bomb():
        value = entry_bomb.get()
        if not value.isdigit():
            value = 1
            entry_bomb.delete(0, END)
            entry_bomb.insert(0, str(value))
            return

        value = int(value)
        value -= 1
        if value < 1:
            value = 531
        entry_bomb.delete(0, END)
        entry_bomb.insert(0, str(value))

    initial_value = 2
    entry_row = Entry(window_personal_choice, width=10, justify='center', font=("Helvetica", 30))
    entry_row.insert(0, str(initial_value))
    entry_row.grid(row=0, column=1, rowspan=2, padx=0, pady=20)

    increment_button_row = Button(entry_row, text="▲", command=increment_row)
    increment_button_row.place(relx=1.0, rely=0.25, anchor='e')

    decrement_button_row = Button(entry_row, text="▼", command=decrement_row)
    decrement_button_row.place(relx=1.0, rely=0.5, anchor='ne')

    entry_col = Entry(window_personal_choice, width=10, justify='center', font=("Helvetica", 30))
    entry_col.insert(0, str(initial_value))
    entry_col.grid(row=3, column=1, rowspan=2, padx=0, pady=20)

    increment_button_col = Button(entry_col, text="▲", command=increment_col)
    increment_button_col.place(relx=1.0, rely=0.25, anchor='e')

    decrement_button_col = Button(entry_col, text="▼", command=decrement_col)
    decrement_button_col.place(relx=1.0, rely=0.5, anchor='ne')

    entry_bomb = Entry(window_personal_choice, width=10, justify='center', font=("Helvetica", 30))
    entry_bomb.insert(0, str(initial_value))
    entry_bomb.grid(row=7, column=1, rowspan=2, padx=0, pady=20)

    increment_button_bomb = Button(entry_bomb, text="▲", command=increment_bomb)
    increment_button_bomb.place(relx=1.0, rely=0.25, anchor='e')

    decrement_button_bomb = Button(entry_bomb, text="▼", command=decrement_bomb)
    decrement_button_bomb.place(relx=1.0, rely=0.5, anchor='ne')

    def start_personal_game():
        get_row = entry_row.get()
        get_col = entry_col.get()
        get_bomb = entry_bomb.get()

        if get_row.isdigit() and int(get_row) <= 14 and get_col.isdigit() and int(get_col) <= 38 and get_bomb.isdigit()\
                and int(get_bomb) <= int(get_row) * int(get_col) - 1 and int(get_bomb) > 0:
            window_personal_choice.destroy()
            label_chose_personal.destroy()
            button_personal_start_game.destroy()
            input_level(int(get_row), int(get_col), int(get_bomb), 15)

        if get_row.isdigit():
            if int(get_row) > 14:
                value = 14
                entry_row.delete(0, END)
                entry_row.insert(0, str(value))
        else:
            value = 1
            entry_row.delete(0, END)
            entry_row.insert(0, str(value))

        if get_col.isdigit():
            if int(get_col) > 38:
                value = 38
                entry_col.delete(0, END)
                entry_col.insert(0, str(value))
        else:
            value = 1
            entry_col.delete(0, END)
            entry_col.insert(0, str(value))

        if get_bomb.isdigit() and get_row.isdigit() and get_col.isdigit():
            if int(get_bomb) > int(get_row) * int(get_col) - 1:
                value = int(get_row) * int(get_col) - 1
                entry_bomb.delete(0, END)
                entry_bomb.insert(0, str(value))

        else:
            value = 1
            entry_bomb.delete(0, END)
            entry_bomb.insert(0, str(value))

    button_personal_start_game = Button(window_personal_choice, fg='black', text="התחל משחק", font=("Helvetica", 20),
                                        command=lambda: start_personal_game())
    button_personal_start_game.grid(row=9, column=1, padx=0, pady=20)

# Function to handle level selection
def input_level(len_row, len_col, sum_bomb, high_letter):
    global num_level
    num_level = row_col_bomb_letter(len_row=len_row, len_col=len_col, sum_bomb=sum_bomb, high_letter=high_letter)
    label_chose.destroy()
    window_chose_label.destroy()
    level_output()

# Function to display the level selection options
def first_output():
    global label_chose,window_chose_label,game_over,label_play ,clear_button, window_buttons, level_button
    game_over = False
    label_chose = Label(window, text=f"בחר את הרמה", bg="#F5F5DC", font=("Helvetica", 20))
    label_chose.pack()
    window_chose_label = tkinter.Frame(window, bg="#F5F5DC")
    window_chose_label.pack(padx=20, pady=20)

    button_low_level = Button(window_chose_label, fg='black', text="נמוך", font=("Helvetica", 20)
                              , command=lambda: input_level(5, 6, 3, 40))
    button_low_level.grid(row=0, column=0, padx=30, pady=30)
    button_high_level = Button(window_chose_label, fg='black', text="גבוה", font=("Helvetica", 20)
                               , command=lambda: input_level(10, 25, 20, 20))
    button_high_level.grid(row=0, column=1, padx=30, pady=30)
    button_personal_choice_level = Button(window_chose_label, fg='black', text="בחירה אישית", font=("Helvetica", 20)
                                          , command=lambda: personal_choice())
    button_personal_choice_level.grid(row=0, column=2, padx=30, pady=30)


first_output()
window.mainloop()
