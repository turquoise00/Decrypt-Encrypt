from tkinter import *
from tkinter import messagebox
import base64
import os


def decrypt():
    password=code.get()
    if password=="1234" :
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg=bg_color)
        
        message=text1.get(1.0, END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT",font="arial",fg=text_color, bg=bg_color).place(x=10, y=10)
        text2=Text(screen2,font="Roboto 13",bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)
        text2.config(fg=text_color)

    elif password=="":
        messagebox.showerror("Decryption", "Input Password")
    elif password !="1234":
        messagebox.showerror("Decryption", "Invalid password")

def encrypt():
    password=code.get()

    if password=="1234" :
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg=bg_color)
        
        message=text1.get(1.0,END)
        encode_message=base64.b64encode(message.encode("utf-8")).decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", fg=text_color, bg=bg_color).place(x=10,y=10)
        text2=Text(screen1, font="Roboto 13", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END,encode_message)
        text2.config(fg=text_color)

    elif password=="":
        messagebox.showerror("Encryption", "Input Password")
    elif password !="1234":
        messagebox.showerror("Encryption", "Invalid password")

def toggle_mode():
    global bg_color
    global text_color

    if toggle_button.config('text')[-1] == 'Dark Mode':
        bg_color = "#121212"
        text_color = "#FFFFFF"
        toggle_button.config(text='Light Mode')
    else:
        bg_color = "#FFFFFF"
        text_color = "#000000"
        toggle_button.config(text='Dark Mode')

    # Update background and text colors for existing widgets
    screen.config(bg=bg_color)
    for widget in screen.winfo_children():
        if isinstance(widget, (Label, Text, Button, Entry)):
            widget.config(bg=bg_color, fg=text_color)

    encrypt_button.config(bg=bg_color, fg=text_color)
    decrypt_button.config(bg=bg_color, fg=text_color)
    reset_button.config(bg=bg_color, fg=text_color)

    toggle_button.config(bg=bg_color, fg=text_color)

def reset():
    code.set("")
    text1.delete(1.0,END)

def main_screen():
    global screen
    global code
    global text1
    global bg_color
    global text_color
    global toggle_button
    global encrypt_button
    global decrypt_button
    global reset_button

    screen=Tk()
    screen.geometry("500x500")

    # Light mode configuration
    bg_color="#FFFFFF"
    text_color="#000000"

    # Dark mode configuration
    # bg_color = "#121212"
    # text_color = "#FFFFFF"

     #icon
    image_icon=PhotoImage(file="key.png")
    screen.iconphoto(False, image_icon)
    screen.title('Decryption and Encryption')

    Label(text="Enter text from encryption and decryption", fg=text_color, font=("calbri", 13)).place(x=10, y=10)
    text1=Text(font="Robote 20", bg=bg_color, relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

   
    Label(text="Enter secret key for encryption and decryption", fg=text_color, font=("calibri", 13)).place(x=10, y=170)


    code=StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    encrypt_button = Button(text="ENCRYPT", height="2", width=21, bg=bg_color , fg=text_color ,bd=0, command=encrypt)
    encrypt_button.place(x=10, y=250)

    decrypt_button = Button(text="DECRYPT", height="2", width=21, bg="#00bd56", fg=text_color, bd=0, command=decrypt)
    decrypt_button.place(x=10, y=290)

    reset_button = Button(text="RESET", height="2", width=20, bg=bg_color, fg=text_color, bd=0, command=reset)
    reset_button.place(x=10, y=350)

    toggle_button = Button(text="Dark-Mode", height="2", width="15", fg=text_color, bd=0, bg=bg_color, command=toggle_mode)
    toggle_button.place(x=280, y=10)

    screen.mainloop()

main_screen()