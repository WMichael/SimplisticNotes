
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

#Example notes
noteCollection = Note_Collection("General")

note1 = Note("Hello","Hello World!")
note2 = Note("Shopping List","Bread, Milk, Ham")
note3 = Note("Favourite Colour","Blue")

noteCollection.add_note(note1)
noteCollection.add_note(note2)
noteCollection.add_note(note3)

print("{0}: {1}".format(noteCollection.notes[0].title,noteCollection.notes[0].content))
print("{0}: {1}".format(noteCollection.notes[1].title,noteCollection.notes[1].content))
print("{0}: {1}".format(noteCollection.notes[2].title,noteCollection.notes[2].content))
