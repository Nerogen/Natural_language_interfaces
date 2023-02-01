import customtkinter
from tkinter import *


def raise_frame(frame):
    frame.tkraise()


if __name__ == '__main__':
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    width = 600
    height = 400
    root = customtkinter.CTk()
    root.title("Vocabulary")
    root.geometry(f'{width}x{height}+300+300')

    f1 = customtkinter.CTkFrame(master=root,
                                width=600,
                                height=400,
                                corner_radius=4)
    f1.place(relx=0.5, rely=0.5, anchor=CENTER)
    f2 = customtkinter.CTkFrame(master=root,
                                width=width,
                                height=height,
                                corner_radius=10)
    f2.place(relx=0.5, rely=0.5, anchor=CENTER)
    f3 = customtkinter.CTkFrame(master=root,
                                width=width,
                                height=height,
                                corner_radius=10)
    f3.place(relx=0.5, rely=0.5, anchor=CENTER)
    f4 = customtkinter.CTkFrame(master=root,
                                width=width,
                                height=height,
                                corner_radius=10)
    f4.place(relx=0.5, rely=0.5, anchor=CENTER)

    customtkinter.CTkLabel(master=f1, text="Frame 1").place(relx=0.5, rely=0.4, anchor=CENTER)
    customtkinter.CTkButton(f1, text="to F2", command=lambda: raise_frame(f2)).place(relx=0.5, rely=0.5, anchor=CENTER)

    button2 = customtkinter.CTkButton(f2, text="to F3", command=lambda: raise_frame(f3)).place(relx=0.5, rely=0.5, anchor=CENTER)

    button3 = customtkinter.CTkButton(f3, text="to F4", command=lambda: raise_frame(f4)).pack()

    button4 = customtkinter.CTkButton(f4, text="to F1", command=lambda: raise_frame(f1)).pack()

    raise_frame(f1)
    root.mainloop()

