from tkinter import *

dc = Tk()

dc.geometry("700x500")
dc.title("Billing Process :)")
dc.resizable(False, False)


def calculator():
    Pizza = e1.get()
    PaniPuri = e2.get()
    Samosa = e3.get()
    FiredRise = e4.get()
    total = ((int(Pizza)*100)+(int(PaniPuri)*20) +
             (int(Samosa)*30)+(int(FiredRise)*150))
    Label(dc, text=total, font="times 30 ").place(x=150, y=400)

    # print(total)


Label(dc, text="Snack - Time :)",
      font="times 30 bold ").place(x=350, y=20, anchor="center")


# Menu section
Label(dc, text="Menu", font="times 28 bold").place(x=550, y=70)

Label(dc, text="Pizza             Rs 100",
      font="times 18 ").place(x=500, y=120)

Label(dc, text="Pani-Puri       Rs 20", font="times 18 ").place(x=500, y=150)

Label(dc, text="Samosa          Rs 30", font="times 18 ").place(x=500, y=180)

Label(dc, text="Fried Rice      Rs 150", font="times 18 ").place(x=500, y=210)


#  Billing section

Label(dc, text="Pizza", font="times 18 ").place(x=20, y=120)
e1 = Entry(dc)
e1.place(x=20, y=150)

Label(dc, text="Pani-Puri", font="times 18 ").place(x=20, y=210)
e2 = Entry(dc)
e2.place(x=20, y=240)

Label(dc, text="Samosa", font="times 18 ").place(x=250, y=210)
e3 = Entry(dc)
e3.place(x=250, y=240)

Label(dc, text="Fired Rice", font="times 18 ").place(x=250, y=120)
e4 = Entry(dc)
e4.place(x=250, y=150)


Button(dc, text="Your Bill :) ", width=20,
       command=calculator).place(x=100, y=300)


dc.mainloop()
