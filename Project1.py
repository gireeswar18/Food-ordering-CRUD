import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from tkinter import ttk

def project():
    try:
        a = Tk()
        a.state("zoomed")
        a.resizable(0, 0)


        def mainpage(un):
            try:
                main = Tk()
                main.state("zoomed")
                main.resizable(0, 0)
                main.title("Order Now")
                main.config(bg="white")
                head = Label(main, text="Order Now", font=("Sans Seriff", 24, "bold"), bg="white")
                head.place(x=650, y=50)


                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="gireeswar@18",
                    database="users"
                )

                cursor = db.cursor()

                def order1():
                    try:
                        data = cb.get()
                        make_order = messagebox.askyesnocancel("Confirm Order", "Do you want to order a cup of coffee?")
                        if make_order:
                            cursor.execute("insert into orders(username, location, item, price) values (%s, %s, %s, %s)",
                                           (un, data, "Coffee",20))
                            db.commit()
                            messagebox.showinfo("Done!", "Ordered Successfully!")

                    except Exception as e:
                        messagebox.showerror("Error", e)
                        main.destroy()
                        project()

                def order2():
                    try:
                        data = cb.get()
                        make_order = messagebox.askyesnocancel("Confirm Order", "Do you want to order 2 Idlis with Sambar and Chutney?")
                        if make_order:
                            cursor.execute(
                                "insert into orders(username, location, item, price) values (%s, %s, %s, %s)",
                                (un, data, "Idli", 25))
                            db.commit()
                            messagebox.showinfo("Done!", "Ordered Successfully!")
                    except Exception as e:
                        messagebox.showerror("Error", e)

                def order3():
                    try:
                        data = cb.get()
                        make_order = messagebox.askyesnocancel("Confirm Order", "Do you want to order a Dosa with Sambar and Chutney?")
                        if make_order:
                            cursor.execute(
                                "insert into orders(username, location, item, price) values (%s, %s, %s, %s)",
                                (un, data, "Dosa", 40))
                            db.commit()
                            messagebox.showinfo("Done!", "Ordered Successfully!")
                    except Exception as e:
                        messagebox.showerror("Error", e)

                def order4():
                    try:
                        data = cb.get()
                        make_order = messagebox.askyesnocancel("Confirm Order", "Do you want to order a Chicken Biriyani?")
                        if make_order:
                            cursor.execute(
                                "insert into orders(username, location, item, price) values (%s, %s, %s, %s)",
                                (un, data, "Chicken Biriyani", 180))
                            db.commit()
                            messagebox.showinfo("Done!", "Ordered Successfully!")
                    except Exception as e:
                        messagebox.showerror("Error", e)

                def order5():
                    try:
                        data = cb.get()
                        make_order = messagebox.askyesnocancel("Confirm Order", "Do you want to order 2 Parottas with Veg Curry?")
                        if make_order:
                            cursor.execute(
                                "insert into orders(username, location, item, price) values (%s, %s, %s, %s)",
                                (un, data, "Parotta", 30))
                            db.commit()
                            messagebox.showinfo("Done!", "Ordered Successfully!")
                    except Exception as e:
                        messagebox.showerror("Error", e)

                deliver = Label(main, text="Select Delivery Location", bg="white", padx=30, pady=30,
                                font=("Sans Seriff", 18))
                deliver.place(x=300, y=100)
                cb = ttk.Combobox(main, width=40, state="readonly")
                cb["value"] = ['Nagercoil', 'Thuckalay', 'Marthandam', 'Kanniyakumari', 'Kaliyakkavilai']
                cb.current(0)
                cb.place(x=625, y=134)
                img1 = Image.open("pexels-spotwizardlee-7333831.jpg")
                img1 = img1.resize((200, 200))
                coffee = ImageTk.PhotoImage(img1)
                cofLabel = Label(image=coffee)
                cofLabel.image = coffee
                cofLabel.place(x=50, y=220)
                item1 = Label(main, text="Coffee", font=("Sans Seriff", 15), bg="white")
                item1.place(x=115, y=435)
                b1 = Button(main, text="Rs.20", font=("Sans Seriff", 12), padx="25", activebackground="light green",
                            relief=FLAT, bd="0", command=order1)
                b1.place(x=96, y=475)

                img2 = Image.open("Idli-2Pieces.jpg")
                img2 = img2.resize((200, 200))
                idli = ImageTk.PhotoImage(img2)
                idliLabel = Label(image=idli)
                idliLabel.image = idli
                idliLabel.place(x=350, y=220)
                item2 = Label(main, text="Idli", font=("Sans Seriff", 15), bg="white")
                item2.place(x=430, y=432)
                b2 = Button(main, text="Rs.25", font=("Sans Seriff", 12), padx="25", activebackground="light green",
                            relief=FLAT, bd="0", command=order2)
                b2.place(x=397, y=475)

                img3 = Image.open("dosa.jpg")
                img3 = img3.resize((200, 200))
                dosa = ImageTk.PhotoImage(img3)
                dosaLabel = Label(image=dosa)
                dosaLabel.image = dosa
                dosaLabel.place(x=650, y=220)
                item3 = Label(main, text="Dosa", font=("Sans Seriff", 15), bg="white")
                item3.place(x=723, y=430)
                b3 = Button(main, text="Rs.40", font=("Sans Seriff", 12), padx="25", activebackground="light green",
                            relief=FLAT, bd="0", command=order3)
                b3.place(x=701, y=475)

                img4 = Image.open("hyderbadi-biriyani-1.jpg")
                img4 = img4.resize((200, 200))
                bry = ImageTk.PhotoImage(img4)
                bryLabel = Label(image=bry)
                bryLabel.image = bry
                bryLabel.place(x=950, y=220)
                item4 = Label(main, text="Chicken Biriyani", font=("Sans Seriff", 15), bg="white")
                item4.place(x=980, y=430)
                b4 = Button(main, text="Rs.180", font=("Sans Seriff", 12), padx="25", activebackground="light green",
                            relief=FLAT, bd="0", command=order4)
                b4.place(x=1000, y=475)

                img5 = Image.open("wp8365304.jpg")
                img5 = img5.resize((200, 200))
                prt = ImageTk.PhotoImage(img5)
                prtLabel = Label(image=prt)
                prtLabel.image = prt
                prtLabel.place(x=1250, y=220)
                item5 = Label(main, text="Parotta", font=("Sans Seriff", 15), bg="white")
                item5.place(x=1315, y=430)
                b5 = Button(main, text="Rs.30", font=("Sans Seriff", 12), padx="25", activebackground="light green",
                            relief=FLAT, bd="0", command=order5)
                b5.place(x=1305, y=475)

                contact = Label(main, text="Contact no: 9150944212", font=("Sans Seriff", 20, "italic"), bg="white")
                contact.place(x=590, y=600)

                address = Label(main, text="Address: 18, Veppamoodu,\nNagercoil-629001", font=("Sans Seriff", 18, "bold"),
                                bg="white")
                address.place(x=590, y=650)
                main.mainloop()

            except Exception as e:
                messagebox.showerror("Error", e)

        def register():
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="gireeswar@18",
                database="users"
            )

            cursor = db.cursor()

            def reg():
                try:
                    username = entry1.get().strip()
                    email = entry2.get().strip()
                    password = entry3.get().strip()
                    if (email == '' or username == '' or password == ''):
                        messagebox.showwarning("Warning", "Fill all the fields!")
                        p1.destroy()
                        return
                    cursor.execute("insert into users (email, username, password) values (%s, %s, %s)",
                                   (email, username, password))
                    db.commit()
                    db.close()
                    messagebox.showinfo("SUCCESS", "Registered Successfully!")
                    p1.destroy()
                except Exception as e:
                    messagebox.showerror("Error", "Something went wrong!")
                    p1.destroy()

            p1 = Tk()
            p1.geometry('600x600')
            p1.resizable(0, 0)
            p1.title("Register")
            p1.config(bg="pink")
            head = Label(p1, text="Registration", font=("Sans Seriff", 25, "bold"), fg="black", bg="pink")
            head.place(x=200, y=10)
            username = Label(p1, text="Username", font=("Sans Seriff", 18), bg="pink")
            username.place(x=90, y=100)
            email = Label(p1, text="Email", font=("Sans Seriff", 18), bg="pink")
            email.place(x=90, y=180)
            password = Label(p1, text="Password", font=("Sans Seriff", 18), bg="pink")
            password.place(x=90, y=260)
            entry1 = Entry(p1, font=(12), bd=3)
            entry1.place(x=250, y=100)
            entry2 = Entry(p1, bd=3, font=(12))
            entry2.place(x=250, y=180)
            entry3 = Entry(p1, bd=3, font=(12), show="*")
            entry3.place(x=250, y=260)
            regButton = Button(p1, text="Register", font=("Sans Seriff", 15), command=reg)
            regButton.place(x=260, y=340)
            p1.mainloop()


        def login():
            def log():
                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="gireeswar@18",
                    database="users"
                )

                cursor = db.cursor()

                try:
                    email = entry1.get().strip()
                    password = entry3.get().strip()
                    if (email == '' or password == ''):
                        messagebox.showwarning("Warning", "Fill all the fields!")
                        p2.destroy()
                        return
                    cursor.execute("select * from users where email= %s and password=%s", (email, password))
                    a1 = cursor.fetchall()
                    if a1:
                        messagebox.showinfo("Done", "Login Successful")
                        cursor.execute("select username from users where email= %s and password=%s", (email, password))
                        un = cursor.fetchone()

                        p2.destroy()
                        a.destroy()
                        mainpage(un[0])

                    else:
                        messagebox.showwarning("Failed", "Invalid Credentials")
                        p2.destroy()

                    cursor.close()


                except Exception as e:
                    messagebox.showerror("Error", e)

            p2 = Tk()
            p2.geometry('600x600')
            p2.resizable(0, 0)
            p2.title("Login")
            p2.config(bg="skyblue")
            head = Label(p2, text="Login", font=("Sans Seriff", 25, "bold"), fg="black", bg="skyblue")
            head.place(x=250, y=10)
            username = Label(p2, text="Email", font=("Sans Seriff", 18), bg="skyblue")
            username.place(x=90, y=150)
            password = Label(p2, text="Password", font=("Sans Seriff", 18), bg="skyblue")
            password.place(x=90, y=260)
            entry1 = Entry(p2, font=(12), bd=3)
            entry1.place(x=250, y=150)
            entry3 = Entry(p2, bd=3, font=(12), show="*")
            entry3.place(x=250, y=260)
            logbutton = Button(p2, text="Login", font=("Sans Seriff", 15), command=log)
            logbutton.place(x=260, y=360)
            p2.mainloop()

        a.title("Food Ordering System")
        image = Image.open("Backgrounds-Food-0532.jpg")
        test = ImageTk.PhotoImage(image)
        label = tkinter.Label(image = test)
        label.image = test
        label.grid(row=0, column=0)
        head = Label(a, text = "Foodie Store", font = ("Sans Seriff", 50, "bold"),fg = "black", bg = "brown")
        head.place(x = 550, y = 25)
        button1 = Button(a, text="New User?",font=("Times New Roman", 20, "bold"), bg = "sky blue", relief=RAISED, command=register)
        button1.config(height=2, width=10)
        button1.place(x = 660, y = 300)
        button2 = Button(a, text="Login", font=("Times New Roman", 20, "bold"), bg = "sky blue", relief=RAISED, command=login)
        button2.config(height=2, width=10)
        button2.place(x=660, y=450)
        a.mainloop()

    except Exception as e:
        print(e)

project()