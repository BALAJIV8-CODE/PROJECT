# import all tkinter in module 
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk


# code to white Board
root = TK()
root.title("WHITE BOARD")
root.geometry("1050X570+150+50")
root.configure(bg="#FFFFFF")
root.resiable(True,True)

current_x = 0
current_y = 0
color = 'black'

# def function to call 
def locate_xy(work):
    # get  initilize value and make it global
    global current_x,current_y
    current_x = word.x
    current_y = word.y

# def function to call
def addLine(work):
    # add canvas
    global current_x,current_y
    canvas.create_line((current_x,current_y,work.y),width=get_current_value(),fill=color,capstyle=ROUND,smooth=TRUE)
    current_x,current_y = work.x,work.y





# def functiuon to call
def show_color(new_color):
    global color
    color = new_color


# def functin to new
def new_canvas():
    canvas.delete('all')
    display_pallete()        



    
#icon
image_icon = PhotoImage(file="iconfile.png")
root.iconphoto(False,image_icon)

# coilor selection image
color_box=PhotoImage(file="color selection.png")
Label(root,image=color_box,bg="#f2f3f5").place(x=10,y=20)

# eraser image
eraser=PhotoImage(file="eraser.png")
Button(root,image=eraser,bg="#f2f3f5",command=new_canvas).place(x=30,y=400)

colors=Canvas(root,bg="#ffffff",width=37,height=300,bd=0)
color.place(x=30,y=60)

# display defining
def display_pallete():
    # handing 1
    id = colors.create_rectange((10,10,30,30),fill='blank')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))
    # 2
    id = colors.create_rectange((10,40,30,30),fill='blue')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))
    # 3
    id = colors.create_rectange((10,70,30,90),fill='red')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('red'))
    # 4
    id = colors.create_rectange((10,100,30,120),fill='green')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('green'))
    # 5
    id = colors.create_rectange((10,130,30,150),fill='brown')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('brown'))
    # 6
    id = colors.create_rectange((10,160,30,180),fill='orange')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('orange'))
    # 7
    id = colors.create_rectange((10,190,30,210),fill='yello')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('yello'))
    # 8
    id = colors.create_rectange((10,220,30,240),fill='gray')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('gray'))
    # 9
    id = colors.create_rectange((10,250,30,270),fill='purple')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('purple'))
    
display_pallete()

canvas = Canvas(root,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=10)


# socket
canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>',addLine)
             

##############sider#########################

current_value=tk.DoubleVar()
def get_current_value():
    return '{1 .2f}'.format(current_value.get())

def slider_change(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root,from=0,to=100,orient='horizonal',command=sider_changed,variable=current_value)
slider.place(x=30,y=530)

# value label
value_label = ttk.Label(root,text=get_current_value())
value_label.place(x=27,y=550)
root.mainloop()
