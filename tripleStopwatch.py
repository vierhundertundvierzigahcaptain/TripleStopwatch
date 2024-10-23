import tkinter as tk
import json
import os

from time import sleep
from threading import Thread
from winsound import PlaySound, SND_ASYNC
from tkinter import font

script_dir = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(script_dir, 'sound.wav')

with open('db.json', 'r') as db:
    data = json.load(db)

counter_1_1 = data['counter_1_1']
counter_1_2 = data['counter_1_2']
counter_2_1 = data['counter_2_1']
counter_2_2 = data['counter_2_2']
counter_3_1 = data['counter_3_1']
counter_3_2 = data['counter_3_2']


def thread(func):  # Decorator for separating functions into threads
    def wrapper(*args, **kwargs):
        current_thread = Thread(target=func, args=args, kwargs=kwargs, daemon=True)
        current_thread.start()
    return wrapper


@thread
def start(quantity_entry, radiobutton, counter_1, counter_2, label_count_1, label_count_2, timer_label):
    global counter_1_1, counter_1_2, counter_2_1, counter_2_2, counter_3_1, counter_3_2
    __duration = 0
    if (quantity_entry.get()).isdigit() is True:
        __duration = int(quantity_entry.get())

        selected_counter = radiobutton.get()
        if selected_counter == 1:
            counter_1[0] += 1
            label_count_1['text'] = str(counter_1[0])
            label_count_1.update()
        elif selected_counter == 2:
            counter_2[0] += 1
            label_count_2['text'] = str(counter_2[0])
            label_count_2.update()

        while __duration >= 0:
            if __duration > 0:
                timer_label['foreground'] = '#1f1'

            timer_label['text'] = __duration
            timer_label.update()
            if __duration <= 0:
                timer_label['foreground'] = '#f11'
                PlaySound(sound_path, SND_ASYNC)
            sleep(1)
            __duration -= 1

        data['counter_1_1'] = counter_1_1
        data['counter_1_2'] = counter_1_2
        data['counter_2_1'] = counter_2_1
        data['counter_2_2'] = counter_2_2
        data['counter_3_1'] = counter_3_1
        data['counter_3_2'] = counter_3_2

        with open('db.json', 'w') as file:
            json.dump(data, file)


def key_start(event):
    if event.keysym == 'Left':
        start(quantityEntry1, rb1, counter_1_1, counter_1_2, labelCount1_1, labelCount1_2, timerLabel1)
    if event.keysym == 'Down':
        start(quantityEntry2, rb2, counter_2_1, counter_2_2, labelCount2_1, labelCount2_2, timerLabel2)
    if event.keysym == 'Right':
        start(quantityEntry3, rb3, counter_3_1, counter_3_2, labelCount3_1, labelCount3_2, timerLabel3)


def reset(counter, label):
    global counter_1_1, counter_1_2, counter_2_1, counter_2_2, counter_3_1, counter_3_2
    counter[0] = 0

    data['counter_1_1'] = counter_1_1
    data['counter_1_2'] = counter_1_2
    data['counter_2_1'] = counter_2_1
    data['counter_2_2'] = counter_2_2
    data['counter_3_1'] = counter_3_1
    data['counter_3_2'] = counter_3_2

    label['text'] = counter
    with open('db.json', 'w') as file:
        json.dump(data, file)


# Creating a window
root = tk.Tk()

root['bg'] = '#111'
root.title('Triple stopwatch')
root.geometry('1200x1000')

root.resizable(width=False, height=False)

canvas = tk.Canvas(root, width=1200, height=1000)
canvas.pack()

# Window Marking
frame1 = tk.Frame(root, bg='#111', width=400, height=1000)
frame2 = tk.Frame(root, bg='#111', width=400, height=1000)
frame3 = tk.Frame(root, bg='#111', width=400, height=1000)
frame1.place(relwidth=0.33, relheight=1)
frame2.place(relx=0.33, relwidth=0.34, relheight=1)
frame3.place(relx=0.67, relwidth=0.33, relheight=1)

# Filling the first area
font1 = font.Font(family='Arial', size=16, weight='bold')
font2 = font.Font(family='Arial', size=150, weight='bold')

title1 = tk.Label(frame1, text='Number of products:', background='#111', foreground='#fff', font=font1)
title1.place(relx=0.5, rely=0.025, anchor=tk.N)

rb1 = tk.IntVar()

radiobutton1_1 = tk.Radiobutton(frame1, text='', variable=rb1, value=1, background='#111')
radiobutton1_1.place(relx=0.26, rely=0.06, anchor=tk.N)

radiobutton1_2 = tk.Radiobutton(frame1, text='', variable=rb1, value=2, background='#111')
radiobutton1_2.place(relx=0.26, rely=0.1, anchor=tk.N)

labelCount1_1 = tk.Label(frame1, text='0', background='#111', foreground='#fff', font=font1)
labelCount1_1.place(relx=0.5, rely=0.06, anchor=tk.N)

labelCount1_2 = tk.Label(frame1, text='0', background='#111', foreground='#fff', font=font1)
labelCount1_2.place(relx=0.5, rely=0.1, anchor=tk.N)

btnReset1_1 = tk.Button(frame1, text='Reset', background='#111', foreground='#fff', font=font1, command=lambda: reset(counter_1_1, labelCount1_1))
btnReset1_1.place(relx=0.75, rely=0.055, anchor=tk.N)

btnReset1_2 = tk.Button(frame1, text='Reset', background='#111', foreground='#fff', font=font1, command=lambda: reset(counter_1_2, labelCount1_2))
btnReset1_2.place(relx=0.75, rely=0.1, anchor=tk.N)

timerLabel1 = tk.Label(frame1, text='000', background='#111', foreground='#1f1', font=font2)
timerLabel1.place(relx=0.5, rely=0.4, anchor=tk.N)

quantityLabel1 = tk.Label(frame1, text='Enter time:', background='#111', foreground='#fff', font=font1)
quantityLabel1.place(relx=0.5, rely=0.8, anchor=tk.N)

quantityEntry1 = tk.Entry(frame1, width=5, bg="white", font=font1)
quantityEntry1.place(relx=0.5, rely=0.85, anchor=tk.N)

startBtn1 = tk.Button(frame1, text='Press ← to start', background='#111', foreground='#fff', font=font1, command=lambda: start(quantityEntry1, rb1, counter_1_1, counter_1_2, labelCount1_1, labelCount1_2, timerLabel1))
startBtn1.place(relx=0.5, rely=0.9, anchor=tk.N)
canvas.bind_all("<KeyPress-Left>", key_start)

# Filling the second area
title2 = tk.Label(frame2, text='Number of products:', background='#111', foreground='#fff', font=font1)
title2.place(relx=0.5, rely=0.025, anchor=tk.N)

rb2 = tk.IntVar()

radiobutton2_1 = tk.Radiobutton(frame2, text='', variable=rb2, value=1, background='#111')
radiobutton2_1.place(relx=0.26, rely=0.06, anchor=tk.N)

radiobutton2_2 = tk.Radiobutton(frame2, text='', variable=rb2, value=2, background='#111')
radiobutton2_2.place(relx=0.26, rely=0.1, anchor=tk.N)

labelCount2_1 = tk.Label(frame2, text='0', background='#111', foreground='#fff', font=font1)
labelCount2_1.place(relx=0.5, rely=0.06, anchor=tk.N)

labelCount2_2 = tk.Label(frame2, text='0', background='#111', foreground='#fff', font=font1)
labelCount2_2.place(relx=0.5, rely=0.1, anchor=tk.N)

btnReset2_1 = tk.Button(frame2, text='Reset', background='#111', foreground='#fff', font=font1, command=lambda: reset(counter_2_1, labelCount2_1))
btnReset2_1.place(relx=0.75, rely=0.055, anchor=tk.N)

btnReset2_2 = tk.Button(frame2, text='Reset', background='#111', foreground='#fff', font=font1, command=lambda: reset(counter_2_2, labelCount2_2))
btnReset2_2.place(relx=0.75, rely=0.1, anchor=tk.N)

timerLabel2 = tk.Label(frame2, text='000', background='#111', foreground='#1f1', font=font2)
timerLabel2.place(relx=0.5, rely=0.4, anchor=tk.N)

quantityLabel2 = tk.Label(frame2, text='Enter time:', background='#111', foreground='#fff', font=font1)
quantityLabel2.place(relx=0.5, rely=0.8, anchor=tk.N)

quantityEntry2 = tk.Entry(frame2, width=5, bg="white", font=font1)
quantityEntry2.place(relx=0.5, rely=0.85, anchor=tk.N)

startBtn2 = tk.Button(frame2, text='Press ↓ to start', background='#111', foreground='#fff', font=font1, command=lambda: start(quantityEntry2, rb2, counter_2_1, counter_2_2, labelCount2_1, labelCount2_2, timerLabel2))
startBtn2.place(relx=0.5, rely=0.9, anchor=tk.N)
canvas.bind_all("<KeyPress-Down>", key_start)

# Filling the third area
title3 = tk.Label(frame3, text='Number of products:', background='#111', foreground='#fff', font=font1)
title3.place(relx=0.5, rely=0.025, anchor=tk.N)

rb3 = tk.IntVar()

radiobutton3_1 = tk.Radiobutton(frame3, text='', variable=rb3, value=1, background='#111')
radiobutton3_1.place(relx=0.26, rely=0.06, anchor=tk.N)

radiobutton3_2 = tk.Radiobutton(frame3, text='', variable=rb3, value=2, background='#111')
radiobutton3_2.place(relx=0.26, rely=0.1, anchor=tk.N)

labelCount3_1 = tk.Label(frame3, text='0', background='#111', foreground='#fff', font=font1)
labelCount3_1.place(relx=0.5, rely=0.06, anchor=tk.N)

labelCount3_2 = tk.Label(frame3, text='0', background='#111', foreground='#fff', font=font1)
labelCount3_2.place(relx=0.5, rely=0.1, anchor=tk.N)

btnReset3_1 = tk.Button(frame3, text='Reset', background='#111', foreground='#fff', font=font1, command=lambda: reset(counter_3_1, labelCount3_1))
btnReset3_1.place(relx=0.75, rely=0.055, anchor=tk.N)

btnReset3_2 = tk.Button(frame3, text='Reset', background='#111', foreground='#fff', font=font1, command=lambda: reset(counter_3_2, labelCount3_2))
btnReset3_2.place(relx=0.75, rely=0.1, anchor=tk.N)

timerLabel3 = tk.Label(frame3, text='000', background='#111', foreground='#1f1', font=font2)
timerLabel3.place(relx=0.5, rely=0.4, anchor=tk.N)

quantityLabel3 = tk.Label(frame3, text='Enter time:', background='#111', foreground='#fff', font=font1)
quantityLabel3.place(relx=0.5, rely=0.8, anchor=tk.N)

quantityEntry3 = tk.Entry(frame3, width=5, bg="white", font=font1)
quantityEntry3.place(relx=0.5, rely=0.85, anchor=tk.N)

startBtn3 = tk.Button(frame3, text='Press → to start', background='#111', foreground='#fff', font=font1, command=lambda: start(quantityEntry3, rb3, counter_3_1, counter_3_2, labelCount3_1, labelCount3_2, timerLabel3))
startBtn3.place(relx=0.5, rely=0.9, anchor=tk.N)
canvas.bind_all("<KeyPress-Right>", key_start)

# Assigning values to counters when opening a program
labelCount1_1['text'] = str(counter_1_1[0])
labelCount1_1.update()
labelCount1_2['text'] = str(counter_1_2[0])
labelCount1_2.update()
labelCount2_1['text'] = str(counter_2_1[0])
labelCount2_1.update()
labelCount2_2['text'] = str(counter_2_2[0])
labelCount2_2.update()
labelCount3_1['text'] = str(counter_3_1[0])
labelCount3_1.update()
labelCount3_2['text'] = str(counter_3_2[0])
labelCount3_2.update()

root.mainloop()

# Compilation
# pyinstaller --onefile --icon=icon.ico tripleStopwatch.py
# python -m nuitka --follow-imports --windows-icon-from-ico=icon.ico tripleStopwatch.py
