import time
from random import choice
from tkinter import *

root = Tk()
global sentence_list
sentence_list = [["Я", "люблю", "гулять", "по", "парку", "в", "воскресенье"],
                ["Сегодня", "я", "пойду", "в", "кино", "с", "друзьями"],
                ["Мои", "любимые", "цветы", "-", "розы"],
                ['Я', 'очень', 'люблю', 'слушать', 'музыку', 'перед', 'сном'],
                ["Вчера", "я", "приготовил", "очень", "вкусный", "ужин"],
                ["Я", "хочу", "научиться", "играть", "на", "гитаре"],
                ["Мой", "любимый", "фильм", "-", "Звездные", "войны"],
                ["Я", "хочу", "посетить", "Лондон", "и", "Париж"]]
def start_game():

    def compare_sentence(event):
        nonlocal errors, correct_sentences
        user_input = input_field.get()
        if user_input == ' '.join(sentence_list[sentence_index]):
            correct_sentences += 1
        else:
            errors += 1
        update_stat_labels()
        next_sentence()

    def update_stat_labels():
        correct_sentences_label.config(text=f"Правильно: {correct_sentences}")
        errors_label.config(text=f"Ошибки: {errors}")

    def next_sentence():
        nonlocal sentence_index
        sentence_index = (sentence_index + 1) % len(sentence_list)
        random_sentence = ' '.join(choice(sentence_list))
        sentence_label.config(text=random_sentence)
        input_field.delete(0, END)

    start_button.destroy()
    sentence_index = 0
    random_sentence = ' '.join(choice(sentence_list))
    sentence_label = Label(root, text=random_sentence)
    sentence_label.pack()

    input_field = Entry(root)
    input_field.pack()
    input_field.bind("<Return>", compare_sentence)

    correct_sentences = 0
    errors = 0
    correct_sentences_label = Label(root, text="Правильно: 0")
    correct_sentences_label.pack()
    errors_label = Label(root, text="Ошибки: 0")
    errors_label.pack()

    next_sentence()

start_button = Button(root, text="Начать игру", command=start_game)
start_button.pack()

root.mainloop()