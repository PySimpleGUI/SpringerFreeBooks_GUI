
## PySimpleGUI based GUI to download all Springer books released for free during the 2020 COVID-19 quarantine

This repo has the code that dowhnloads the files:

https://github.com/alexgand/springer_free_books

It lacks a GUI and control of where to save the files which is what this new program provides.

## Using

Run the program `PSG_Download_Springer_Books.py`

You will be prompted for a folder to save the books to.  In that folder a subfolder named "springer_books" will be created.

Books will be downloaded to this subfolder and categorized by subject.

The books are organized according to the subject ("English Package Name" column).

If you want just one or two specific books, get the excel file from the folowing link and download the titles you seek:

https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v4

## The GUI Additions

The addition of the GUI was not a difficult one to add to this program.  You will find that converting most command line programs into a GUI program are easy when using PySimpleGUI.  There were 2 primary changes.

1. Where the code previously had a path that was hard coded, replace with a call to `popup_get_folder`
2. Added a "smarter progress meter".  TQDM is OK.  It's better than nothing

Each of these changes amounted to 7 lines of code.  The result is a program that could be make into an EXE file and distributed to anyone.  Previously you had to modify the source code to change the download folder so creating an EXE file wouldn't have helped.  You would also have to continue to run as a command line program as the TQDM output is to the console.

If you're just getting into GUIs, try converting somee of your programs like this.  

## Information about Springer Books' Generous Gestrure

* https://group.springernature.com/gp/group/media/press-releases/freely-accessible-textbook-initiative-for-educators-and-students/17858180?utm_medium=social&utm_content=organic&utm_source=facebook&utm_campaign=SpringerNature_&sf232256230=1
* https://www.springernature.com/gp/librarians/news-events/all-news-articles/industry-news-initiatives/free-access-to-textbooks-for-institutions-affected-by-coronaviru/17855960

## Spreadsheet listinging available books

* https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v4

## Screenshots

![image](https://user-images.githubusercontent.com/46163555/80296779-c70c7200-874b-11ea-94b1-1d7a8a1b550e.png)

One thing that the original program did not provide you was the ability to **safely** abort the download.  Nor were you informed about the estimated download time.

![image](https://user-images.githubusercontent.com/46163555/80307414-f3011500-8796-11ea-8db8-1783956af026.png)


## This softwared is licensed using LGPL3

## Requires

PySimpleGUI
