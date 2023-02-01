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


# to do: read and load data from pdf
def download_data(file_from, *args, **kwargs):
    pass


# to do: save data in file
def upload_data(file_to, data, *args, **kwargs):
    pass


# to do: display vocabulary records on the screen
def show_records(vocabulary, *args, **kwargs):
    pass


# to do: edit and save existing record
def edit_record(old_record, *args, **kwargs):
    pass


# to do: save edited record
def save_record(record, *args, **kwargs):
    pass


# to do: filter records by parameters
def filter_records(*args, **kwargs):
    pass


# to do: search records by parameters
def search_records(*args, **kwargs):
    pass


# to do: make new word form by given rules
def generate_lexeme_form(base_lexeme, *args, **kwargs):
    pass


if __name__ == '__main__':
    input_data = customtkinter.CTkEntry(root, placeholder_text="input text")
    input_data.pack()
    button = customtkinter.CTkButton(root, text="Update", command=print_data).pack()

    root.mainloop()
