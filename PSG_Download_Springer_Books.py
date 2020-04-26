#!/usr/bin/env python
import os
import requests
import pandas as pd
import PySimpleGUI as sg

"""
    
    The download code was provided by repo that can be found at:
    https://github.com/alexgand/springer_free_books
    
    This GUI code was first offered to that project.  Since there was no interest in taking
    the code beyond a hard-coded path, command-line bit of code it made sense to create this separate
    repo.

    Copyright 2020 PySimpleGUI.org
    
"""

folder = sg.popup_get_folder('Location to save\nA "springer_books" folder will be created in this location', 'Choose Save Location')
if not folder:
    sg.popup_cancel('Cancelling')
    exit()

folder = os.path.join(folder, 'springer_books')

if not os.path.exists(folder):
    os.mkdir(folder)

if not os.path.exists(os.path.join(folder, "table.xlsx")):
    books = pd.read_excel('https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v4')

    # save table:
    books.to_excel(os.path.join(folder, 'table.xlsx'))
else:
    books = pd.read_excel(os.path.join(folder, 'table.xlsx'), index_col=0, header=0)

sg.popup_quick_message('Download starting....', background_color='red', text_color='white', font='ANY 20', keep_on_top=True)

total_books = len(books[['OpenURL', 'Book Title', 'Author', 'English Package Name']].values)
for i, (url, title, author, pk_name) in enumerate(books[['OpenURL', 'Book Title', 'Author', 'English Package Name']].values):
    if not sg.one_line_progress_meter('Downloading books', i + 1, total_books, 'key', f'{title}'):
        sg.popup('Cancelling....', 'User cancelled download operation')
        exit()

    new_folder = os.path.join(folder, pk_name)

    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

    r = requests.get(url)
    new_url = r.url

    new_url = new_url.replace('/book/', '/content/pdf/')

    new_url = new_url.replace('%2F', '/')
    new_url = new_url + '.pdf'

    final = new_url.split('/')[-1]
    final = title.replace(',', '-').replace('.', '').replace('/', ' ').replace(':', ' ') + ' - ' + author.replace(',', '-').replace('.', '').replace('/',
                                                                                                                                                     ' ').replace(
        ':', ' ') + ' - ' + final
    output_file = os.path.join(new_folder, final)

    if not os.path.exists(output_file.encode('utf-8')):
        myfile = requests.get(new_url, allow_redirects=True)
        try:
            open(output_file.encode('utf-8'), 'wb').write(myfile.content)
        except OSError:
            sg.popup_error("Error: PDF filename is appears incorrect.")

        # download epub version too if exists
        new_url = r.url

        new_url = new_url.replace('/book/', '/download/epub/')
        new_url = new_url.replace('%2F', '/')
        new_url = new_url + '.epub'

        final = new_url.split('/')[-1]
        final = title.replace(',', '-').replace('.', '').replace('/', ' ').replace(':', ' ') + ' - ' + author.replace(',', '-').replace('.', '').replace('/',
                                                                                                                                                         ' ').replace(
            ':', ' ') + ' - ' + final
        output_file = os.path.join(new_folder, final)

        request = requests.get(new_url)
        if request.status_code == 200:
            myfile = requests.get(new_url, allow_redirects=True)
            try:
                open(output_file.encode('utf-8'), 'wb').write(myfile.content)
            except OSError:
                sg.popup_error("Error: EPUB filename is appears incorrect.")

sg.popup('Download finished.', f'Downloaded {i} books')
