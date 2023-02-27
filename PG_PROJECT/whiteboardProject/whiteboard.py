# project is about whiteboard using python
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

# create root
root = tk.Tk()
root.title('White Board')
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False,False)
 
current_x = 0
current_y = 0
color='black'


def locate_xy(work):
    current_x = work.x
    current_y = work.y


def addLine(work):
    global current_x,current_y
    canvas.create_line((current_x,current_y,work.x,work.y),width=10,fill=color)
    current_x , current_y = work.x,work.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete("all")
    display_pallete()

# icon
image_icon = PhotoImage(file="/home/lenovo/Desktop/pg_project/whiteboardProject/logo.png")
root.iconphoto(False,image_icon)

color_box =PhotoImage(file="/home/lenovo/Desktop/pg_project/whiteboardProject/color_section.png")
Label(root,image=color_box,bg = "#f2f3f5").place(x=10,y=20)

# color canvas
eraser = PhotoImage(file="/home/lenovo/Desktop/pg_project/whiteboardProject/eraser.png")
Button(root, image=eraser,bg = "#f2f3f5",command=new_canvas).place(x=30,y=400)

colors = Canvas(root,bg="#ffffff",width=37,height=300,bd=0)
colors.place(x=30,y=60)

#def canavas
def display_pallete():
    # 1
    id = colors.create_rectangle((10,10,30,30,),fill='black')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))
    # 2
    id = colors.create_rectangle((10,40,30,60,),fill='gray')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('gray'))
    # 3
    id = colors.create_rectangle((10,70,30,90,),fill='brown')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('brown'))
    # 4
    id = colors.create_rectangle((10,100,30,120,),fill='blue')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))
    # 5
    id = colors.create_rectangle((10,130,30,150,),fill='red')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('red'))
    # 6
    id = colors.create_rectangle((10,160,30,180,),fill='purple')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('purple'))
    # 6
    id = colors.create_rectangle((10,190,30,210,),fill='orange')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('orange'))
    # 7
    id = colors.create_rectangle((10,220,30,240,),fill='yellow')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('yellow'))
    # 8
    id = colors.create_rectangle((10,10,30,30,),fill='black')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))
    # 9
    id = colors.create_rectangle((10,10,30,30,),fill='black')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))
    
display_pallete()


canvas = Canvas(root,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addLine)

root.mainloop()
