from typing import List

from .tag import Tag
from .title import Title
from .content import Content


class Note:
    def __init__(
            self,
            title: Title,
            content: Content = None,
            tags: List[Tag] = None
    ):
        self.title = title
        self.content = content
        self.tags = tags if tags else []

    def edit_content(self, content):
        self.content = content

    def edit_title(self, title):
        self.title = title

    def add_tag(self, new_tag: Tag):
        for tag in self.tags:
            if tag.value == new_tag.value:
                raise ValueError({'message': 'Tag already exists'})
        self.tags.append(new_tag)

    def delete_tag(self, tag: Tag):
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        raise ValueError({'message': 'Tag does not exist'})

    def __repr__(self) -> str:
        return f'\n{self.title}\n\n{self.content}\n\n{", ".join([tag.value for tag in self.tags])}\n'

    def __eq__(self, note):
        if isinstance(note, Note):
            return self.content == note.content and self.title == note.title
        return False
