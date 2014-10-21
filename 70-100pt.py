from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
# walls for da house
rectangle = drawpad.create_rectangle(100,200,400,500)

#roof
line1 = drawpad.create_line(100,200,250,40)
line2 = drawpad.create_line(400,200,250,40)
root.mainloop()

