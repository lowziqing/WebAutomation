from Tkinter import *
import tkMessageBox as messagebox
import time
from pygame import mixer
username = 0
password = 0


def reminder():
    w = '2170'
    h = '250'

    window = Tk()
    window.geometry('{}x{}'.format(w, h))
    window.configure(bg='lightgreen')
    window.resizable(width=FALSE, height=FALSE)
    window.title("Stretching Break!")

    display = Label(window, text="Prepare for Stretching @ 3pm", font="Serif 140", bg="lightgreen")
    display.grid(column=0, row=0)
    display.columnconfigure(0, weight=1)
    display.rowconfigure(0, weight=1)

    mixer.init()
    mixer.music.load("C:\Users\LowZiQing\PycharmProjects\Test1\SeleniumScript\Music.mp3")

    abort_after = 1 * 115
    start = time.time()

    window.lift()
    window.call('wm', 'attributes', '.', '-topmost', True)
    window.after_idle(window.call, 'wm', 'attributes', '.', '-topmost', False)

    while True:
        delta = time.time() - start
        window.after(115000, lambda: window.destroy())
        mixer.music.play()
        window.mainloop()
        if delta >= abort_after:
            mixer.music.stop()
            print "break"
            break


def get_login():

    def try_login():
        if password_guess.get() and username_guess.get:
            global username, password
            username = username_guess.get()
            password = password_guess.get()
            window.destroy()
        else:
            messagebox.showerror("Error!", "No Empty Fields!")

    # Gui Things
    window = Tk()
    window.resizable(width=FALSE, height=FALSE)
    window.title("Log-In")
    window.geometry("400x400")

    # Creating the username & password entry boxes
    username_text = Label(window, text="Username:", font="Serif 25")
    username_guess = Entry(window, font="Serif 25")
    password_text = Label(window, text="Password:", font="Serif 25")
    password_guess = Entry(window, show="*", font="Serif 25")

    # attempt to login button
    attempt_login = Button(text="Login", command=try_login, height=30, width=150)

    username_text.pack()
    username_guess.pack()
    password_text.pack()
    password_guess.pack()
    attempt_login.pack()

    # Main Starter
    window.mainloop()
    return {'username': username, 'password': password}
