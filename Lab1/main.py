import re
import customtkinter
import fitz
import spacy
from tkinter import *

nlp = spacy.load(r"C:\Users\cawap\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\en_core_web_sm\en_core_web_sm-3.5.0")
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

    tokens = customtkinter.CTkButton(master=show_page, text="Tokens", command=tokenize)
    tokens.grid(row=0, column=3)

    search_request = customtkinter.CTkEntry(master=show_page, placeholder_text="Input search key")
    search_request.grid(row=1, column=1)

    search = customtkinter.CTkButton(master=show_page, text="Search", command=search_sentence)
    search.grid(row=1, column=2)

    update = customtkinter.CTkButton(master=show_page, text="Update", command=update_data)
    update.grid(row=1, column=3)

    save = customtkinter.CTkButton(master=show_page, text="Save")
    save.grid(row=2, column=1)

    delete = customtkinter.CTkButton(master=show_page, text="Delete")
    delete.grid(row=2, column=2)

    filter_btn = customtkinter.CTkButton(master=show_page, text="Filter")
    filter_btn.grid(row=2, column=3)

    widgets_for_destroy.append(show_page)

def tokenize():
    destroy_all()
    def tokens_maker():  # -> spacy work
        sentence_info_page = customtkinter.CTkFrame(master=main_page, width=width, height=height)
        list_view = Listbox(master=sentence_info_page, height=10, width=85)
        for item in range(len(data)):
            list_view.insert(item, data[item])
        sentence_info_page.grid(row=2, column=0)
        list_view.grid(row=2, column=0)
        if tokenize_sentence.get():
            doc = nlp(tokenize_sentence.get())
        for token in range(len(doc)):
            if doc[token].pos_ == 'NOUN':
                list_view.insert(token, f'{doc[token].text} {doc[token].lemma_} {doc[token].pos_} {doc[token].suffix_}  {doc[token].morph}')
            else:
                list_view.insert(token, f'{doc[token].text} {doc[token].lemma_} {doc[token].pos_} {doc[token].suffix_} ')

        del doc
        widgets_for_destroy.append(sentence_info_page)
        widgets_for_destroy.append(list_view)

    tokenize_page = customtkinter.CTkFrame(master=main_page, width=width, height=height)
    tokenize_page.grid(row=1, column=0)

    tokenize_sentence = customtkinter.CTkEntry(master=tokenize_page, placeholder_text="Input sentence", width=280, height=10)
    tokenize_sentence.grid(row=0, column=0)

    tokenize_btn = customtkinter.CTkButton(master=tokenize_page, text="tokenize", command=tokens_maker)
    tokenize_btn.grid(row=0, column=2)



def generate_lexeme_logic():
    destroy_all()

    def generate():
        pass

    show_page = customtkinter.CTkFrame(master=main_page, width=width, height=height)
    show_page.grid(row=1, column=0)

    word = customtkinter.CTkEntry(master=show_page, placeholder_text="Input word")
    word.grid(row=0, column=0)

    number_of = customtkinter.CTkComboBox(master=show_page, values=["Number of", "Singular", "Plural"])
    number_of.grid(row=1, column=0)

    kind = customtkinter.CTkComboBox(master=show_page, values=["Kind", "Masculine", "Feminine", "Neuter"])
    kind.grid(row=1, column=1)

    kind = customtkinter.CTkComboBox(master=show_page,
                                     values=["Case", "Subjective Case", "Objective Case", "Possessive Case"])
    kind.grid(row=1, column=2)

    generate_btn = customtkinter.CTkButton(master=show_page, text="Generate", command=generate)
    generate_btn.grid(row=0, column=1)

    widgets_for_destroy.append(show_page)


def help_logic():
    destroy_all()

    show_page = customtkinter.CTkFrame(master=main_page, width=width, height=height)
    show_page.grid(row=1, column=0)

    help_doc = (
        "vocabulary: has some methods to process some text",
        "input field for file - search some file in project by the name",
        "View - generate icon for read and view file",
        "Tokens - get some lexemes and parsers words according to the rules",
        "Search - search word in text",
        "Update - regenerate window",
        "Save - save file from processed data",
        "Delete - delete some sentences from text",
        "Filter - filter sentences by the dictionary",
        "generate lexeme: generate lexeme with the some choice rules",
        "input word field - for input some word which need generate with some rule",
        "generate button - start generate lexeme",
        "number of - choice singular word of plural",
        "kind - choice Masculine/Feminine etc.",
        "case - choice Subjective Case etc."
    )

    list_view = Listbox(master=show_page, height=17, width=85)
    for item in range(len(help_doc)):
        list_view.insert(item, help_doc[item])
    list_view.grid(row=2, column=1)
    widgets_for_destroy.append(list_view)
    widgets_for_destroy.append(show_page)


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
