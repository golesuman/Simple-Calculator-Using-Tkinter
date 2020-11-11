from tkinter import *
root=Tk()
root.title('Simple Calculator')
en=Entry(root, width=40)
en.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
en.get()
# en.insert(0, 'Enter Your name')
# root.geometry('445x324')
def addButton(number):
    curr=en.get()
    en.delete(0, END)
    en.insert(0, str(curr)+str(number))
def clearButton():
    en.delete(0, END)
def sumButton():
    first_number=en.get()
    global f_num
    f_num=int(first_number)
    en.delete(0, END)
def eqButton():
    second_num=en.get()
    en.delete(0,END)
    en.insert(0, f_num+int(second_num))
button1= Button(root, text='1', padx=40, pady=10, command=lambda : addButton(1))
button2= Button(root, text='2', padx=40, pady=10, command=lambda : addButton(2))
button3= Button(root, text='3', padx=40, pady=10, command=lambda : addButton(3))
button4= Button(root, text='4', padx=40, pady=10, command=lambda : addButton(4))
button5= Button(root, text='5', padx=40, pady=10, command=lambda : addButton(5))
button6= Button(root, text='6', padx=40, pady=10, command=lambda : addButton(6))
button7= Button(root, text='7', padx=40, pady=10, command=lambda : addButton(7))
button8= Button(root, text='8', padx=40, pady=10, command=lambda : addButton(8))
button9= Button(root, text='9', padx=40, pady=10, command=lambda : addButton(9))
button0= Button(root, text='0', padx=40, pady=10, command=lambda : addButton(0))
buttonSum=Button(root, text='+', padx=40, pady=10, command=sumButton)
buttonEqual=Button(root, text='=', padx=40, pady=10, command=eqButton)
buttonClear=Button(root, text='Clear', padx=29, pady=10, command=clearButton)
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
#create the button for addion and equal sign
buttonSum.grid(row=4, column=2)
buttonEqual.grid(row=4, column=1)
buttonClear.grid(row=5, column=0)

# mybutton=Button(root, text='Enter the numbers',command=clickMe,fg='red',bg='pink')
# mybutton.pack()
root.mainloop()