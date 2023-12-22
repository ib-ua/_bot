from collections import UserDict
from typing import List
import re

from .data_transfer import DataTransferService
from .note import Note


class NoteBook(UserDict[str, Note], DataTransferService):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.filename = f'{name}_{self.__class__.__name__}.bin'
        data = self.load_data()
        if data:
            self.data.update(data)

    def add_note(self, new_note: Note) -> None:
        self.data[new_note.title.value] = new_note

    def find_note_by_title(self, title: str) -> Note:
        note = self.data.get(title)
        if not note:
            raise ValueError({'message': 'No note was found'})
        return note

    def find_notes_by_tag(self, tag_term: str) -> List[Note]:
        found_notes = []
        for note in self.data.values():
            for tag in note.tags:
                if tag_term == tag.value:
                    found_notes.append(note)
                    break
        return found_notes

    def delete_note(self, note):
        try:
            del self.data[note.title.value]
        except:
            raise ValueError({'message': 'No note was found'})

    def find_note_by_term(self, term):
        found_notes = []
        for note in self.data.values():
            for field in [note.title, note.content, *note.tags]:
                if re.search(term, field.value, re.IGNORECASE):
                    found_notes.append(note)
                    break
        return found_notes

    def close(self) -> None:
        self.save_data(self.data)
