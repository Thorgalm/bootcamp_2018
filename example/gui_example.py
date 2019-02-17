import tkinter
from tkinter import messagebox


def suma():
    print("Nacisnieto przycisk")
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
        wynik = a + b
        wynik_label.configure(text=f"Wynik: {wynik}")
    except ValueError:
        messagebox.showerror("Błędne dane", "Popraw dane na liczby")


root = tkinter.Tk()

# etykieta
a_label = tkinter.Label(master=root, text="argument a")
# przypina etykiete do naszego okienka
a_label.pack()
# elementy
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="argument b")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

button = tkinter.Button(master=root, text="Sum", command=suma)
button.pack()

wynik_label = tkinter.Label(master=root, text=" - ")
wynik_label.pack()

root.mainloop()
