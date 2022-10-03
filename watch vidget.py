from tkinter import Label, Tk
import time
import math
app_window = Tk()
app_window.title("Время без лиги")
app_window.geometry("400x100")
app_window.resizable(1,1)

text_font= ("Lato", 35, 'bold')
background = '#15253c'
foreground = "#c9991e"
border_width = 35


label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

TIME_GRIND= time.strptime('02/10/2022 20:00', '%d/%m/%Y %H:%M')
TIME_GRIND_epoch=time.mktime(TIME_GRIND)

now=math.floor(time.time())
diff=int(now-TIME_GRIND_epoch)

def kal(diff):
    sec=diff%60
    diff=diff//60
    min=diff%60
    diff=diff//60
    hour=diff%24
    diff=diff//24
    day=diff
    return f"{day} d:{hour} h:{min} m:{sec} s"

def dclock():
    now=math.floor(time.time())
    diff=int(now-TIME_GRIND_epoch)
    label.config(text=kal(diff))
    label.after(200, dclock)

dclock()
app_window.mainloop()