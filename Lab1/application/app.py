def raise_frame(frame):
    frame.tkraise()


# to do: read and load data from pdf
def download_data(file_from, *args, **kwargs):
    # use frame as kwarg to move from one page to another
    raise_frame(kwargs['frame'])
    pass


# to do: save data in file
def upload_data(file_to, data, *args, **kwargs):
    raise_frame(kwargs['frame'])
    pass


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
def filter_records(*args, **kwargs):
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
