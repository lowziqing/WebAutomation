from Tkinter import Label, Button, FALSE, Tk, Entry
import tkMessageBox as messagebox

username = 0
password = 0

def getLogin():

    def try_login():
        if password_guess.get() == retype_password_guess.get():
            global username, password
            username = username_guess.get()
            password = password_guess.get()
            messagebox.showinfo("-- COMPLETE --", "Password Matched", icon="info")
            window.destroy()
        else:
            messagebox.showinfo("-- ERROR --", "Password doesn't match!", icon="warning")

    # Gui Things
    window = Tk()
    window.resizable(width=FALSE, height=FALSE)
    window.title("Log-In")
    window.geometry("250x175")

    # Creating the username & password entry boxes
    username_text = Label(window, text="Username:")
    username_guess = Entry(window)
    password_text = Label(window, text="Password:")
    password_guess = Entry(window, show="*")
    retype_password_text = Label(window, text="Re-type Password:")
    retype_password_guess = Entry(window, show="*")


    # attempt to login button
    attempt_login = Button(text="Login", command=try_login)

    username_text.pack()
    username_guess.pack()
    password_text.pack()
    password_guess.pack()
    retype_password_text.pack()
    retype_password_guess.pack()
    attempt_login.pack()
    # Main Starter
    window.mainloop()
    return {'username': username, 'password': password}
