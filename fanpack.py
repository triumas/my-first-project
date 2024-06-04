from customtkinter import *
import PIL
from PIL import Image
import time
import random
from wallpaper import set_wallpaper
import ctypes
from pathlib import Path
from io import StringIO
import sys
import webbrowser 

app = CTk()
app.geometry("350x400")
app.resizable(width=False, height=False)
app.title = "Time battles fan pack"
set_appearance_mode("light")

mainsize = CTkFont("", size= 18)
altsize1 = CTkFont("", size= 22)
altsize2 = CTkFont("", size= 15)

working_space = Path.cwd()

bg_path = str(Path.cwd() /"wallpaper_for_App.png")

extra_button = CTkCheckBox(master=app, text="Follow me?", font=altsize2)
extra_button.place(y=95, x=7)

def on_clicked():
     rndtime=random.randint(0, 0)
     btn.configure(text="Installed")
     btn.configure(state="disabled")
     btn.configure(fg_color="#1c3798")
     ctypes.windll.user32.SystemParametersInfoW(20, 0, bg_path, 0)
     openwebsite = extra_button.get()
     extra_button.configure(state="disabled")
     if openwebsite == 1:
          webbrowser.open('https://www.roblox.com/users/1448958151/profile', new = 2)

bgsize = CTkFont("", size= 350)
bgopener = Image.open("chat_screenshot_refined.png")
bg_label = CTkLabel(master=app, text="", image=CTkImage(bgopener, size=(200,400)))
bg_label.place(x=254, rely=0.5, anchor="center")

toplabel = CTkLabel(master=app, text="Skytru fanpack", fg_color="transparent", font=altsize1)
toplabel.place(y=5, x=7)

extra_text = CTkLabel(master=app, text="(made by tum)", fg_color="transparent", font=altsize2)
extra_text.place(y=30, x=7)

small_text = CTkLabel(master=app, text="(Wallpaper + more)", fg_color="transparent", font=altsize2)
small_text.place(y=370, x=7)

btn = CTkButton(master=app, text="Install", font=mainsize, fg_color="#284ed7", hover_color="#1c3798", command=on_clicked)
btn.place(y=59, x=7)

app.mainloop()
