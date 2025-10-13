from tkinter import *

def calculate():
    miles = float(input.get())
    km = round(miles * 1.609344, 1)
    my_label3.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Entry
input = Entry(width=7)
print(input.get())
input.grid(column=1, row=0)

#Label 1 (Miles)
my_label1 = Label(text="Miles")
my_label1.grid(column=2, row=0)
my_label1.config(padx=30, pady=30)

#Label 2 (is equal to)
my_label2 = Label(text="is equal to")
my_label2.grid(column=0, row=1)
my_label2.config(padx=30, pady=30)

#Label 3 (Result)
my_label3 = Label(text="0")
my_label3.grid(column=1, row=1)
my_label3.config(padx=30, pady=30)

#Label 4 (Km)
my_label4 = Label(text="Km")
my_label4.grid(column=2, row=1)
my_label4.config(padx=30, pady=30)

#Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()




