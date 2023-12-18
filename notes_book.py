from note import Note

class Note_book:
    def __init__(self):
        self.__notes = {}
    
    @property
    def notes(self):
        return self.__notes
    
    @notes.setter
    def set_notes(self, notes):
        if notes is not None and type(notes) is dict:
            self.__notes = notes
        else:
            raise ValueError("Invalid type for notes or notes are empty")
        
    def add_note(self, new_note, new_author):
        if new_note is None or new_author is None:
            raise ValueError("Arguments are empty")

        if new_author in self.__notes:
            self.__notes[new_author].append(new_note)
        else:
            self.__notes[new_author] = [new_note]
        return self
    
    def find_notes_by_author(self, author):
        found_notes = self.__notes.get(author, [])
        if(not found_notes):
            return None
        return found_notes

        
    def find_notes_by_author_title(self, author, title):
        notes_by_author = self.find_notes_by_author(author)
        if notes_by_author is not None:
            found_notes = [note for note in notes_by_author if note.title.lower() == title.lower()]
            if not found_notes:
                return None
            return found_notes
        else:
            return None
        
    def find_notes_by_title(self, title):
        all_notes = [note for notes_list in self.__notes.values() for note in notes_list]
        found_notes = [note for note in all_notes if note.title.lower() == title.lower()]
        if not found_notes:
            return None
        return found_notes
    
    def find_notes_by_tag(self, tag):
        all_notes = [note for notes_list in self.__notes.values() for note in notes_list]
        found_notes = [note for note in all_notes if note.tag.lower() == tag.lower()]
        if not found_notes:
            return None
        return found_notes
    
    def sort_notes_by_tags(self):
        sorted_book = Note_book()

        for author, notes in self.__notes.items():
            sorted_notes = sorted(notes, key=lambda note: tuple(note.tags))
            for note in sorted_notes:
                sorted_book.add_note(note, author)

        return sorted_book

    def delete_note(self, note):
        for author, notes in self.__notes.items():
            for existing_note in notes:
                if existing_note == note:
                    notes.remove(existing_note)
                    return True
        return False 
    
