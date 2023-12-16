from note import Note

class Note_book:
    def __init__(self):
        self._notes = {}
    
    @property
    def notes(self):
        return self._notes
    
    @notes.setter
    def set_notes(self, notes):
        if notes is not None and type(notes) is dict:
            self._notes = notes
        else:
            raise ValueError("Invalid type for notes or notes are empty")
        
    def add_note(self, new_note, new_author):
        if new_note is None or new_author is None:
            raise ValueError("Arguments are empty")

        if new_author in self._notes:
            self._notes[new_author].append(new_note)
        else:
            self._notes[new_author] = [new_note]
        return self
    
    def find_notes_author(self, author):
        return self._notes.get(author, [])
        
    def find_notes_author_title(self, author, title):
        notes_by_author = self.find_notes_author(author)
        if notes_by_author is not None:
            return [note for note in notes_by_author if note.title.lower() == title.lower()]
        else:
            return []
        
    def find_notes_title(self, title):
        all_notes = [note for notes_list in self._notes.values() for note in notes_list]
        return [note for note in all_notes if note.title.lower() == title.lower()]
    
    def delete_note(self, note):
        for author, notes in self._notes.items():
            for existing_note in notes:
                if existing_note == note:
                    notes.remove(existing_note)
                    return True
        return False 
    
