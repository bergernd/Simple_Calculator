import tkinter as tk




def press(num):
    value = str(lbl_value["text"])
    if value =='0':
        if str(num).isnumeric() == False:
            lbl_value["text"] = '0'
        else:
            lbl_value["text"] = str(num)
    else:
        lbl_value["text"] = value + str(num)

def press_equal():
    value = str(lbl_value["text"])
    lbl_value["text"] = eval(value)

def press_back():
    value = str(lbl_value["text"])
    if len(value) == 1:
        lbl_value["text"] = '0'
    else:
        lbl_value["text"] = value[:-1]

def press_clear():
    lbl_value["text"] = '0'
    



root = tk.Tk()

root.title("Calculate 3000")
root.columnconfigure([0,1,2,3], minsize=50, weight=1)
root.rowconfigure([0, 1,2,3,4,5,6], minsize=50, weight=1)






lbl_value = tk.Label(text = 0, bg = 'black', fg = 'green', anchor = 'e')
lbl_value.grid(row=0, column=0, columnspan=4, sticky = 'nsew')

but_0 = tk.Button(text = '0', command = lambda: press(0))
but_0.grid(row=6, column=0, columnspan=2, sticky = 'nsew')
but_1 = tk.Button(text = '1', command = lambda: press(1))
but_1.grid(row=5, column=0,sticky = 'nsew')
but_2 = tk.Button(text = '2', command = lambda: press(2))
but_2.grid(row=5, column=1, sticky = 'nsew')
but_3 = tk.Button(text = '3', command = lambda: press(3))
but_3.grid(row=5, column=2, sticky = 'nsew')
but_4 = tk.Button(text = '4', command = lambda: press(4))
but_4.grid(row=4, column=0,sticky = 'nsew')
but_5 = tk.Button(text = '5', command = lambda: press(5))
but_5.grid(row=4, column=1, sticky = 'nsew')
but_6 = tk.Button(text = '6', command = lambda: press(6))
but_6.grid(row=4, column=2, sticky = 'nsew')
but_7 = tk.Button(text = '7', command = lambda: press(7))
but_7.grid(row=3, column=0,sticky = 'nsew')
but_8 = tk.Button(text = '8', command = lambda: press(8))
but_8.grid(row=3, column=1, sticky = 'nsew')
but_9 = tk.Button(text = '9', command = lambda: press(9))
but_9.grid(row=3, column=2, sticky = 'nsew')
but_dot = tk.Button(text = '.', command = lambda: press('.'))
but_dot.grid(row=6, column=2, sticky = 'nsew')
but_ent = tk.Button(text = '=', command = press_equal)
but_ent.grid(row=5, column=3, rowspan=2, sticky = 'nsew')
but_plus = tk.Button(text = '+', command =lambda: press('+'))
but_plus.grid(row=3, column=3, rowspan=2, sticky = 'nsew')
but_minus = tk.Button(text = '-', command = lambda: press('-'))
but_minus.grid(row=2, column=1,sticky = 'nsew')
but_times = tk.Button(text = '*', command = lambda: press('*'))
but_times.grid(row=2, column=3, sticky = 'nsew')
but_divide = tk.Button(text = '/', command = lambda: press('/'))
but_divide.grid(row=2, column=2, sticky = 'nsew')
but_back = tk.Button(text = '<-', command = press_back)
but_back.grid(row = 2, column = 0, sticky = 'nsew')
but_clear = tk.Button(text = 'C', command = press_clear)
but_clear.grid(row=1, column = 0, sticky = 'nwes')




root.mainloop()