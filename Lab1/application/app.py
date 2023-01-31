import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
width = 300
height = 150
root = customtkinter.CTk()
root.title("Vocabulary")
root.geometry(str(width) + "x" + str(height) + "+300+300")


def print_data():
    print(input_data.get())


input_data = customtkinter.CTkEntry(root, placeholder_text="input text")
input_data.pack()
button = customtkinter.CTkButton(root, text="Update", command=print_data).pack()

root.mainloop()
