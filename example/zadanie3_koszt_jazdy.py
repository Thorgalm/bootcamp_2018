import tkinter
from tkinter import messagebox


def koszt_jazdy():
    print("Nacisnieto przycisk")
    try:
        dystans = int(dystans_entry.get())
        spalanie = int(spalanie_entry.get())
        cena = float(Cena_entry.get())
        koszt = dystans * spalanie * cena*0.01
        wynik_label.configure(text=f"Wynik: {koszt}")
    except ValueError:
        messagebox.showerror("Błędne dane", "Popraw dane na liczby")


root = tkinter.Tk()
# dodanie columnconfigure przesuwa entry przy rozszerzaniu okienka
root.columnconfigure(1, weight=1)

dystans_label = tkinter.Label(master=root, text="Dystans:")
dystans_label.grid(row=0, column=0)
dystans_entry = tkinter.Entry(master=root)
dystans_entry.grid(row=0, column=1)

spalanie_label = tkinter.Label(master=root, text="Spalanie:")
spalanie_label.grid(row=1, column=0)
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.grid(row=1, column=1)

Cena_label = tkinter.Label(master=root, text="cena za 1 litr")
Cena_label.grid(row=2, column=0)
Cena_entry = tkinter.Entry(master=root)
Cena_entry.grid(row=2, column=1)

button = tkinter.Button(master=root, text="Policz koszt", command=koszt_jazdy)
button.grid(row=3, column=1)

wynik_label = tkinter.Label(master=root, text=" - ")
wynik_label.grid(row=4, column=1)

root.mainloop()
