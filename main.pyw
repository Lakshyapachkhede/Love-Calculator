import ttkbootstrap as tb
from tkinter import *
from tkinter import messagebox
import random
import re
import pygame



root = tb.Window(themename="vapor")
root.geometry("300x460")
try:
    root.iconbitmap('heart.ico')
except:
    pass
root.resizable(False, False)
root.title("Find your Love - Love Calculator")

name_pattern = r'^[a-zA-Z]+(?:[\s\'\-][a-zA-Z]+)*$'
def seed():
    seed_num = random.randint(1, 10000000000000000)
    return seed_num

def play_sound(sound_file):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    except:
        pass

def validate_name(name):
    return re.match(name_pattern, name) is not None

def fill_meter(current_percent, target_percent):
    if current_percent <= target_percent:
        meter.configure(amountused=current_percent)
        current_percent += 1
        root.after(8, fill_meter, current_percent, target_percent)

def clicked():
    global seed
    if validate_name(first_name_entry.get()) and validate_name(second_name_entry.get()):
            random.seed(seed())
            love_percent = random.randint(0, 100)
            fill_meter(0, love_percent)
            play_sound('drumroll.mp3')
                 

    else:
        messagebox.showinfo("Love Calculator", "Enter Valid Names.")

def display_meter():
    global meter
    meter = tb.Meter(root,
                      bootstyle='secondary',
                      subtext="Love",
                    #   interactive=True,
                      textright="%",
                    #  , metertype="semi"
                    #  , stripethickness=50
                    # ,metersize=100
                    #  amounttotal=200,
                    #  amountused=40,
                    subtextfont=('Helvetica', 16)
                
                    )

    meter.grid(row=0, column=0, pady=(15, 10), sticky="ew")  # Set sticky to "nsew" to center the meter
    # root.grid_rowconfigure(0, weight=1)  # Make row 0 expandable
    root.grid_columnconfigure(0, weight=1)  # Make column 0 expandable


heading = tb.Label(root, text="Love Calculator", bootstyle='warning', font=('Comic Sans MS', 20))
heading.grid(row=1, column=0, sticky="we", pady=(0, 10), padx=50)



entry_frame = tb.Frame(root)
first_name_lbl = tb.Label(entry_frame, text="Enter First Name: ", bootstyle='success')
first_name_entry = tb.Entry(entry_frame, bootstyle='primary')
first_name_lbl.grid(row=0, column=0, padx=0, pady=10)
first_name_entry.grid(row=0, column=1, padx=0, pady=10)

second_name_lbl = tb.Label(entry_frame, text="Enter Second Name: ", bootstyle='success')
second_name_entry = tb.Entry(entry_frame, bootstyle='primary')
second_name_lbl.grid(row=1, column=0, padx=0, pady=10)
second_name_entry.grid(row=1, column=1, padx=0, pady=10)




entry_frame.grid(row=2, column=0)

calculate_button = tb.Button(root, text="Calculate", bootstyle='light outline', command=clicked)
calculate_button.grid(row=3, column=0, sticky="e", padx=20, pady=(20, 10))

warning_lbl = tb.Label(root, text="We are not responible for any damages.", bootstyle='light')
warning_lbl.grid(row=4, column=0, padx=10)


display_meter()

root.mainloop()
