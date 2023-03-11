import re

import customtkinter
import fitz
from tkinter import *

widgets_for_destroy = []
data: list[str] = []


def destroy_all():
    """Destroy all widgets of window"""
    for widget in widgets_for_destroy:
        raise_frame(widget)


def raise_frame(frame):
    frame.destroy()


def vocabulary_logic():
    destroy_all()

    def view_file():
        view_frame = customtkinter.CTkFrame(master=main_page, width=width, height=height)
        show_page.grid(row=1, column=0, sticky="w")
        data.extend(''.join(download_data(file_name.get())).split('\n'))
        list_view = Listbox(master=view_frame, height=10, width=85)
        for item in range(len(data)):
            list_view.insert(item, data[item])
        list_view.grid(row=1, column=1)
        view_frame.grid(row=3, column=0)
        widgets_for_destroy.append(list_view)
        widgets_for_destroy.append(view_frame)

    def tokens_maker():  # -> spacy work
        pass

    def update_data():
        destroy_all()

    def search_sentence():
        list_view = Listbox(master=widgets_for_destroy[2], height=10, width=85)
        for item in range(len(data)):
            if search_request.get() in data[item]:
                list_view.insert(item, data[item])
        list_view.grid(row=2, column=1)
        widgets_for_destroy.append(list_view)

    show_page = customtkinter.CTkFrame(master=main_page, width=width, height=height)
    show_page.grid(row=1, column=0)

    file_name = customtkinter.CTkEntry(master=show_page, placeholder_text="Input PDF name")
    file_name.grid(row=0, column=1)

    view = customtkinter.CTkButton(master=show_page, text="View", command=view_file)
    view.grid(row=0, column=2)

    tokens = customtkinter.CTkButton(master=show_page, text="Tokens")
    tokens.grid(row=0, column=3)

    search_request = customtkinter.CTkEntry(master=show_page, placeholder_text="Input search key")
    search_request.grid(row=1, column=1)

    search = customtkinter.CTkButton(master=show_page, text="Search", command=search_sentence)
    search.grid(row=1, column=2)

    update = customtkinter.CTkButton(master=show_page, text="Update", command=update_data)
    update.grid(row=1, column=3)

    # save = customtkinter.CTkButton(master=show_page, text="Save", command=save_logic)
    # save.grid(row=0, column=4)

    widgets_for_destroy.append(show_page)


def generate_lexeme_logic():
    destroy_all()

    show_page = customtkinter.CTkFrame(master=main_page, width=width, height=height)
    show_page.grid(row=1, column=0)

    file_name = customtkinter.CTkComboBox(master=show_page, values=["hello", 'set'])
    file_name.set('set')
    file_name.grid(row=0, column=1)

    tokens = customtkinter.CTkButton(master=show_page, text="Tokens")
    tokens.grid(row=0, column=2)


def help_logic():
    destroy_all()

    print("Help logic")


def convert_text_to_set(text: str) -> set:
    result = re.findall(r'\w+\b', text)
    return set(result)


# to do: read and load data from pdf
def download_data(file_from: str) -> str:
    # use frame as kwarg to move from one page to another
    doc = fitz.open(file_from)
    text = ''
    for i in range(doc.page_count):
        page = doc.load_page(i)
        page_text = page.get_text("text")
        text += page_text

    return text


# to do: save data in file
def upload_data(file_to: str, data) -> None:
    with open(file_to, "w", encoding="utf-8") as txt:
        txt.write(data)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
width = 600
height = 400
root = customtkinter.CTk()
root.title("Vocabulary")
root.geometry(f"{width}x{height}+300+300")

main_page = customtkinter.CTkFrame(master=root, width=width, height=height, corner_radius=4)

menu = customtkinter.CTkFrame(master=main_page, width=200, height=200, corner_radius=4)

vocabulary = customtkinter.CTkButton(master=menu, text="Vocabulary", command=vocabulary_logic)
vocabulary.grid(row=0, column=0)

generate_lexeme = customtkinter.CTkButton(master=menu, text="Generate lexeme", command=generate_lexeme_logic)
generate_lexeme.grid(row=0, column=1)

help_dox = customtkinter.CTkButton(master=menu, text="Help", command=help_logic)
help_dox.grid(row=0, column=2)

main_page.grid(row=0, column=0)
menu.grid(row=0, column=0)

root.mainloop()
