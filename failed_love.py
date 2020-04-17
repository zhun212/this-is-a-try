from tkinter import messagebox, Tk
import tkinter as tk
import random
import tkinter
from tkinter import *
from PIL import ImageTk,Image
from 素材_jpg import img as one
import base64,os


def no_close():
    return


def close_all_window():
    window.destroy()


def close_window():
    messagebox.showinfo(title="不要嘛~", message="不选好不许走！")


def Love():
    love = Toplevel(window)
    love.geometry("300x100")
    love.title("喜欢你~")
    btn=tkinter.Button(love, text="在一起！", width=10, height=2, command=close_all_window)
    btn.place(x=100, y=30)
    love.protocol("WM_DELETE_WINDOW", no_close)

def bye():
    bye = Toplevel(window)
    bye.geometry('300x500')
    bye.title('see you')
    show = Label(bye, text="对不起，我又喜欢上了你，", font=("微软雅黑", 10))
    show.place(x=65, y=50)
    show = Label(bye, text="你说两个人突然石沉大海你会伤心。", font=("微软雅黑", 10))
    show.place(x=65, y=100)
    show = Label(bye, text="如果有一天我不见了，", font=("微软雅黑", 10))
    show.place(x=65, y=150)
    show = Label(bye, text="是我不想看到你在别人怀里。", font=("微软雅黑", 10))
    show.place(x=65, y=200)
    btn4 = tkinter.Button(bye, text="对不起。", width=10, height=2, command=close_all_window)
    btn4.place(x=100, y=300)


window=Tk()
window.title("情人节快乐！")
window.geometry("1080x640")
window.protocol("WM_DELETE_WINDOW", close_window)
show = Label(window,text="吴沈燕", font=("微软雅黑", 20))
show.place(x=150, y=10)
show = Label(window, text="我观察你很久了", font=("微软雅黑", 18))
show.place(x=120, y=60)
show = Label(window, text="做我女朋友好不好", font=("微软雅黑", 24))
show.place(x=70, y=100)
show = Label(window, text="一见钟情九分颜", font=("微软雅黑", 15))
show.place(x=820,y=60)
show = Label(window, text='日久生情心相应', font=('微软雅黑', 15))
show.place(x=820,y=100)
btn3 = tk.Button(window,text='我知道了', width=15, height=2, font=('微软雅黑', 10), command=bye)
btn3.place(x=820, y=200)
btn1 = tkinter.Button(window, text="好", width=15, height=2, command=Love)
btn1.place(x=110, y=200)

tmp = open('one.png', 'wb')        #创建临时的文件
tmp.write(base64.b64decode(one))    ##把这个one图片解码出来，写入文件中去。
tmp.close()


# "不好"按钮
pos = [100, 300]
btn2=tkinter.Button(window, text="不好", width=15, height=2)
btn2.place(x=pos[0], y=pos[1])
canvas = tk.Canvas(window, bg='white', width='400', height='300')
img = Image.open('one.png')
img = ImageTk.PhotoImage(img)
image = canvas.create_image(200, 40, anchor='n', image=img)
canvas.pack()

var = tk.StringVar()
lab1 = tk.Label(window, textvariable=var, bg='green', fg='white',
                width=30, height=2, font=('微软雅黑', 12))
lab1.place(x=370,y=300)

hit_me = False
def on_hit():
    global hit_me
    if  hit_me == False:
        hit_me = True
        var.set('接受才能关哦~')
    else:
        hit_me = False
        var.set('')

btn1 = tk.Button(window, text='关闭按钮~', font=('微软雅黑', 12),
                 width=10, height=2, command = on_hit)
btn1.place(x=480,y=400)

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

os.remove('one.png')