import tkinter as tk

callculation = ""

# Opeartions 
def add_to_callculation(symbol):
    global callculation
    callculation += str(symbol)
    title.delete(1.0, "end")
    title.insert(1.0, callculation)

def evaluate_callculation():
    global callculation
    print(callculation)
    try : 
        result = str(eval(callculation))
        callculation = ""
        title.delete(1.0, "end")
        title.insert(1.0, result)
    except:
        clear_callculation
        title.delete(1.0, "Error")
        pass

# clear callculation
def clear_callculation():
    global callculation
    callculation = ""
    title.delete(1.0, "end")


# Grapichal User Interface
root = tk.Tk()
root.geometry("300x275")
# Title
title = tk.Text(root, height=2, width=16, font=("Arial", 24))
title.grid(columnspan=5)

# Buttons
button1 = tk.Button(root, text="1", command=lambda: add_to_callculation(1),width=5, font=("Arial",14))
button1.grid(row=2,column=1)
button2 = tk.Button(root, text="2", command=lambda: add_to_callculation(2),width=5, font=("Arial",14))
button2.grid(row=2,column=2)
button3 = tk.Button(root, text="3", command=lambda: add_to_callculation(3),width=5, font=("Arial",14))
button3.grid(row=2,column=3)
button4 = tk.Button(root, text="4", command=lambda: add_to_callculation(4),width=5, font=("Arial",14))
button4.grid(row=3,column=1)
button5 = tk.Button(root, text="5", command=lambda: add_to_callculation(5),width=5, font=("Arial",14))
button5.grid(row=3,column=2)
button6 = tk.Button(root, text="6", command=lambda: add_to_callculation(6),width=5, font=("Arial",14))
button6.grid(row=3,column=3)
button7 = tk.Button(root, text="7", command=lambda: add_to_callculation(7),width=5, font=("Arial",14))
button7.grid(row=4,column=1)
button8 = tk.Button(root, text="8", command=lambda: add_to_callculation(8),width=5, font=("Arial",14))
button8.grid(row=4,column=2)
button9 = tk.Button(root, text="9", command=lambda: add_to_callculation(9),width=5, font=("Arial",14))
button9.grid(row=4,column=3)
button0 = tk.Button(root, text="0", command=lambda: add_to_callculation(0),width=5, font=("Arial",14))
button0.grid(row=5,column=2)
buttonplus = tk.Button(root, text="+", command=lambda: add_to_callculation("+"),width=5, font=("Arial",14))
buttonplus.grid(row=2,column=4)
buttonminus = tk.Button(root, text="-", command=lambda: add_to_callculation("-"),width=5, font=("Arial",14))
buttonminus.grid(row=3,column=4)
buttonmultiplication = tk.Button(root, text="x", command=lambda: add_to_callculation("*"),width=5, font=("Arial",14))
buttonmultiplication.grid(row=4,column=4)
buttondivision = tk.Button(root, text="/", command=lambda: add_to_callculation("/"),width=5, font=("Arial",14))
buttondivision.grid(row=5,column=4)
buttonopen = tk.Button(root, text="(", command=lambda: add_to_callculation("("),width=5, font=("Arial",14))
buttonopen.grid(row=5,column=1)
buttonclose = tk.Button(root, text=")", command=lambda: add_to_callculation(")"),width=5, font=("Arial",14))
buttonclose.grid(row=5,column=3)
buttonclear = tk.Button(root, text="C", command= clear_callculation, width=11, font=("Arial",14))
buttonclear.grid(row=6,column=1, columnspan=2)
buttonequals = tk.Button(root, text="=", command= evaluate_callculation, width=11, font=("Arial",14))
buttonequals.grid(row=6,column=3, columnspan=2)

# Grapichal User Interface End
root.mainloop()