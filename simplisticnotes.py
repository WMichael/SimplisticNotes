import os

# Used to clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Note Collection holds each note in a list.
class Note_Collection:
    def __init__(self,name):
        self.name = name
        self.notes = list()

    def add_note(self,Note):
        self.notes.append(Note)

    def remove_note(self,noteNum):
        self.notes.pop(noteNum)

# Note object holds the title and content of the note.
class Note:
    def __init__(self,title,content):
        self.title = title
        self.content = content

# Interface
def Menu():
    clear()
    print("\nSimplistic notes:\n---------------- \n1.General Notes\n2.Note Collections\n3.About\n4.Exit\n")
    select = input("What's your selection? ")
    if select == "1":
        NotesList(0)
    elif select == "2":
        NoteCollections()
    elif select == "3":
        About()

    elif select == "4":
        return

    else:
        Menu()

# Shows list of note collections
def NoteCollections():
    clear()
    print("\nNote Collections:")
    print("----------------")
    for x in range(0, len(gCollection)):
        print("{0}.{1}".format(x + 1,gCollection[x].name))

    select = input("\na - Add collection, 1-{} - View collection, b - Go back  ".format(len(gCollection)))
    try:
        if select == "b":
            Menu()

        elif int(select) > 0 and int(select) <= len(gCollection):
            NotesList(int(select) - 1)
    except:
        NoteCollections()


# Shows list of notes of a particular collection
def NotesList(collectionNo):
    clear()
    print("\n{} Notes:".format(gCollection[collectionNo].name))
    print("----------------")
    for x in range(0, len(gCollection[collectionNo].notes)):
        print("{0}.{1}".format(x + 1,gCollection[collectionNo].notes[x].title))

    select = input("\na - Add note, 1-{} - View note, b - Go back ".format(len(gCollection[collectionNo].notes)))
    try:
        if select == "b":
            NoteCollections()

        elif select == "a":
            AddNote(gCollection[collectionNo])

        elif int(select) > 0 and int(select) <= len(gCollection[collectionNo].notes):
            ViewNote(gCollection[collectionNo],int(select) - 1)
    except:
        NotesList(collectionNo)

# Views a note of a particular collection and noteNo
def ViewNote(collection,noteNo):
    clear()
    print("\nNote {0}: {1}".format(noteNo + 1,collection.notes[noteNo].title))
    print("----------------")
    print("{}".format(collection.notes[noteNo].content))

    select = input("\nb - Go back, d - Delete ")
    if select == "b":
        NotesList(gCollection.index(collection))
    elif select == "d":
        collection.remove_note(noteNo)
        NotesList(gCollection.index(collection))
    else:
        ViewNote(collection,noteNo)

# Adds a note
def AddNote(collection):
    clear()
    print("\nAdd Note: ")
    print("----------------")
    title = input("Title: ")
    note = input("Note: ")
    completedNote = Note(title,note)
    collection.add_note(completedNote)
    NotesList(gCollection.index(collection))

# Talks about program
def About():
    clear()
    print("\nAbout: ")
    print("----------------")
    print("A simple program for taking notes on the command line. \nCreated by Michael.W")

    select = input("\nb - Go back ")
    if select == "b":
        Menu()
    else:
        About()

#Example notes
gCollection = list() #Used for holding all note collections.
general = Note_Collection("General")
animals = Note_Collection("Animals")
gCollection.append(general)
gCollection.append(animals)

note1 = Note("Hello","Hello World!")
note2 = Note("Shopping List","Bread, Milk, Ham")
note3 = Note("Favourite Colour","Blue")

general.add_note(note1)
general.add_note(note2)
general.add_note(note3)

Menu()
