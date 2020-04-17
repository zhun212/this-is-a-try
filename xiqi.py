from tkinter import messagebox, Tk
import random
import tkinter
from tkinter import *


def no_close():
    return


def close_all_window():
    window.destroy()


def close_window():
    messagebox.showinfo(title="不要嘛~", message="不选好不许走！")


def Love():
    love = Toplevel(window)
    love.geometry("300x100+580+250")
    love.title("喜欢你~")
    btn=tkinter.Button(love, text="在一起", width=10, height=2, command=close_all_window)
    btn.place(x=100, y=30)
    love.protocol("WM_DELETE_WINDOW", no_close)


window=Tk()
window.title("嗨，小姐姐")
window.geometry("360x640+550+50")
window.protocol("WM_DELETE_WINDOW", close_window)
show = Label(window, text="观察你很久了", font=("微软雅黑", 18))
show.place(x=120, y=50)
show = Label(window, text="做我女朋友好不好", font=("微软雅黑", 24))
show.place(x=70, y=100)
btn1 = tkinter.Button(window, text="好", width=15, height=2, command=Love)
btn1.place(x=110, y=200)
# "不好"按钮
pos = [100, 300]
btn2=tkinter.Button(window, text="不好", width=15, height=2)
btn2.place(x=pos[0], y=pos[1])


def on_enter(e):
    global pos
    dx = random.randint(100, 200)
    dy = random.randint(100, 300)
    print(pos, dx, dy)
    pos = (pos[0] + dx) % 200, (pos[1] - 250 + dy) % 350 + 250
    btn2.place(x=pos[0], y=pos[1])


btn2.bind("<Enter>", on_enter)
# 显示窗口消息，消息循环
window.mainloop()
