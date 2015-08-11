import sys
from pybtex.database.input import bibtex
from pybtex.database import Person


def checkauthor():
    global missingflag, missingfields
    if not 'author' in entry.persons:
        missingflag = True; missingfields.append('author(s)')
    return

def checkyear():
    global missingflag, missingfields
    if not 'year' in fields:
        missingflag = True; missingfields.append('year')
    return

def checktitle():
    global missingflag, missingfields
    if not 'title' in fields:
        missingflag = True; missingfields.append('title')
    return

def checkbooktitle():
    global missingflag, missingfields
    if not 'booktitle' in fields:
        missingflag = True; missingfields.append('booktitle')
    return

def checkeditor():
    global missingflag, missingfields
    if not 'editor' in entry.persons:
        missingflag = True; missingfields.append('editor(s)')
    return

def checklocation():
    global missingflag, missingfields
    if not 'location' in fields:
        missingflag = True; missingfields.append('conference location')
    return

def checkdate():
    global missingflag, missingfields
    if not 'eventdate' in fields:
        missingflag = True; missingfields.append('conference date(s)')
    return

def checkpublisher():
    global missingflag, missingfields
    if not 'publisher' in fields:
        missingflag = True; missingfields.append('publisher')
    return

def checkaddress():
    global missingflag, missingfields
    if not 'address' in fields:
        missingflag = True; missingfields.append('publisher\'s location')
    return

def checkjournal():
    global missingflag, missingfields
    if not 'journal' in fields:
        missingflag = True; missingfields.append('journal')
    return

def checkschool():
    global missingflag, missingfields
    if not 'school' in fields:
        missingflag = True; missingfields.append('university')
    return

def checkvolume():
    global missingflag, missingfields
    if not 'volume' in fields:
        missingflag = True; missingfields.append('volume')
    return

def checkpages():
    global missingflag, missingfields
    if not 'pages' in fields:
        missingflag = True; missingfields.append('pages')
    return


# Globals
entry = None
fields = []
missingflag = False
missingfields = []

# Read the bib file
parser = bibtex.Parser()
bib_data = parser.parse_file(sys.argv[1])

# Check each entry for missing fields
for key, entry in bib_data.entries.iteritems():

    entrytype = entry.type
    fields = entry.fields
    missingflag = False
    missingfields = []

    # General fields
    # if not 'year' in fields:
    #     missingflag = True; missingfields.append('year')
    checkyear()

    # Type-specific fields
    if entrytype == 'book':
        checkpublisher()
        checkaddress()

    elif entrytype == 'incollection':
        checkbooktitle()
        checkeditor()
        checkpublisher()
        checkaddress()
        checkpages()

    elif entrytype == 'article':
        checkjournal()
        checkvolume()
        checkpages()

    elif entrytype in ['inproceedings', 'conference']:
        checkeditor()
        checklocation()
        checkdate()
        checkpublisher()
        checkaddress()
        checkpages()

    elif entrytype == 'phdthesis':
        checkschool()

    if missingflag:
        # Write a query

        # Build a string to identify the reference in any query
        if 'author' in entry.persons:
            author = entry.persons['author'][0].last()[0]
        else:
            author = '(no author provided)'

        if 'year' in fields:
            year = '(' + entry.fields['year'] + ')'
        else:
            year = '(no year provided)'

        # Write the query
        print '\query{For', author, year, 'please provide:', ', '.join(map(str, missingfields)) + '}'
