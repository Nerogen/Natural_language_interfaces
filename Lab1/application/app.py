import re

import fitz


def raise_frame(frame):
    frame.tkraise()


# regular expression without numbers in words \b[^\W\d]+\b
# regular expression with numbers in end of word \b[^\W\d]+\d*\b
def convert_text_to_set(text):
    result = re.findall(r'\w+\b', text)
    return set(result)


# to do: read and load data from pdf
def download_data(file_from, *args, **kwargs):
    # use frame as kwarg to move from one page to another
    doc = fitz.open(file_from)
    text = ''
    for i in range(doc.page_count):
        page = doc.load_page(i)
        page_text = page.get_text("text")
        text += page_text
    raise_frame(kwargs['frame'])
    return text


# to do: save data in file
def upload_data(file_to, data, *args, **kwargs):
    with open(file_to, "w") as txt:
        txt.write(data)
    raise_frame(kwargs['frame'])


# to do: display vocabulary records on the screen
def show_records(vocabulary, *args, **kwargs):
    raise_frame(kwargs['frame'])
    pass


# to do: edit and save existing record
def edit_record(old_record, *args, **kwargs):
    pass


# to do: save edited record
def save_record(record, *args, **kwargs):
    pass


# to do: filter records by parameters
def filter_records(data, *args, **kwargs):
    raise_frame(kwargs['frame'])
    pass


# to do: search records by parameters
def search_records(*args, **kwargs):
    pass


# to do: make new word form by given rules
def generate_lexeme_form(base_lexeme, *args, **kwargs):
    raise_frame(kwargs['frame'])
    pass


def main():
    pass


if __name__ == "__main__":
    main()
