import customtkinter
from tkinter import *
import tksheet

from app import *


if __name__ == '__main__':
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    width = 600
    height = 400
    root = customtkinter.CTk()
    root.title("Vocabulary")
    root.geometry(f'{width}x{height}+300+300')

    start_page = customtkinter.CTkFrame(master=root,
                                        width=width,
                                        height=height,
                                        corner_radius=4)
    start_page.place(relx=0.5, rely=0.5, anchor=CENTER)

    customtkinter.CTkButton(start_page, text="Download Data", command=lambda: raise_frame(download_page)).place(
                                                                                                        relx=0.5,
                                                                                                        rely=0.4,
                                                                                                        anchor=CENTER)
    customtkinter.CTkButton(start_page, text="Work with Vocabulary", command=lambda: raise_frame(work_with_vocab)).place(
                                                                                                        relx=0.5,
                                                                                                        rely=0.5,
                                                                                                        anchor=CENTER)
    customtkinter.CTkButton(start_page, text="Generate Lexeme Form", command=lambda: raise_frame(making_word_form)).place(
                                                                                                        relx=0.5,
                                                                                                        rely=0.6,
                                                                                                        anchor=CENTER)
######################################################################
    download_page = customtkinter.CTkFrame(master=root,
                                           width=width,
                                           height=height,
                                           corner_radius=4)
    download_page.place(relx=0.5, rely=0.55, anchor=CENTER)

    input_data = customtkinter.CTkEntry(download_page, placeholder_text="input PDF name")
    input_data.place(relx=0.5, rely=0.4, anchor=CENTER)

    # TO DO: change raise_frame(...) to appropriate function
    customtkinter.CTkButton(download_page, text="Download Data", command=lambda: raise_frame(start_page)).place(
                                                                                                        relx=0.5,
                                                                                                        rely=0.5,
                                                                                                        anchor=CENTER)
    customtkinter.CTkButton(download_page, text="Main Page", command=lambda: raise_frame(start_page)).place(
                                                                                                        relx=0.5,
                                                                                                        rely=0.9,
                                                                                                        anchor=CENTER)

#########################################################################
    data = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13],
            [3, 4, 'jjdkd', 'ksks', 6, 6, 7, 8, 9, 10, 11, 13],
            [1, 1, 1, 1, 1, 6, 7, 8, 9, 10, 11, 13]]
    x_size = len(data)
    y_size = len(data[0])

    work_with_vocab = customtkinter.CTkFrame(master=root,
                                             width=width,
                                             height=height,
                                             corner_radius=4)
    work_with_vocab.place(relx=0.5, rely=0.5, anchor=CENTER)

    table = tksheet.Sheet(work_with_vocab, width=width, height=0.7*height)
    table.place(relx=0.5, rely=0.1, anchor=N)

    table.set_sheet_data([[f"{data[ri][cj]}" for cj in range(y_size)] for ri in range(x_size)])
    table.enable_bindings(("single_select",
                           "row_select",
                           "column_width_resize",
                           "arrowkeys",
                           "right_click_popup_menu",
                           "rc_select",
                           "rc_insert_row",
                           "rc_delete_row",
                           "copy",
                           "cut",
                           "paste",
                           "delete",
                           "undo",
                           "edit_cell"))
    customtkinter.CTkButton(work_with_vocab, text="Main Page", command=lambda: raise_frame(start_page)).place(
        relx=0.5,
        rely=0.9,
        anchor=CENTER)
    customtkinter.CTkButton(work_with_vocab, text="Save Data", command=lambda: raise_frame(upload_page)).place(
        relx=0.5,
        rely=0.8,
        anchor=CENTER)

########################################################################
    upload_page = customtkinter.CTkFrame(master=root,
                                           width=width,
                                           height=height,
                                           corner_radius=4)
    upload_page.place(relx=0.5, rely=0.55, anchor=CENTER)

    input_data = customtkinter.CTkEntry(upload_page, placeholder_text="input PDF name")
    input_data.place(relx=0.5, rely=0.4, anchor=CENTER)

    customtkinter.CTkButton(upload_page, text="Download Data", command=lambda: raise_frame(start_page)).place(
        relx=0.5,
        rely=0.5,
        anchor=CENTER)
    customtkinter.CTkButton(download_page, text="Main Page", command=lambda: raise_frame(start_page)).place(
        relx=0.5,
        rely=0.9,
        anchor=CENTER)

#######################################################################
    # TO DO: filters
    filter_page = customtkinter.CTkFrame(master=root,
                                         width=width,
                                         height=height,
                                         corner_radius=4)
    filter_page.place(relx=0.5, rely=0.5, anchor=CENTER)

    customtkinter.CTkButton(filter_page, text="Filter", command=lambda: filter_records(
        data,
        frame=work_with_vocab
    )).place(
        relx=0.5,
        rely=0.8,
        anchor=CENTER)
    customtkinter.CTkButton(filter_page, text="Main Page", command=lambda: raise_frame(start_page)).place(
        relx=0.5,
        rely=0.9,
        anchor=CENTER)

########################################################################
    # TO DO: special form for different lexemes
    making_word_form = customtkinter.CTkFrame(master=root,
                                              width=width,
                                              height=height,
                                              corner_radius=4)
    making_word_form.place(relx=0.5, rely=0.5, anchor=CENTER)

    button4 = customtkinter.CTkButton(making_word_form, text="Main Page", command=lambda: raise_frame(start_page)).place(
        relx=0.5,
        rely=0.9,
        anchor=CENTER)

########################################################################
    raise_frame(start_page)
    root.mainloop()

