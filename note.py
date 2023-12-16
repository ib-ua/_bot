class Note:

    def __init__(self, content, title):
        if content and isinstance(content, str):
            self._content = content
        else:
            self._content = None

        if title and isinstance(title, str):
            self._title = title
        else:
            self._title = None

    @property
    def content(self):
        return self._content
    
    @property
    def title(self):
        return self._title
    
    def set_content(self, content):
        self._content = content if (content and isinstance(content, str)) else None
    
    def set_title(self, title):
        self._title = title if (title and isinstance(title, str)) else None
    
    def edit_content(self, content):
        self.set_content(content)
    
    def edit_title(self, title):
        self.set_title(title)

    def __eq__(self, note):
        if isinstance(note, Note):
            return self.content == note.content and self.title.lower() == note.title.lower()
        return False
        
    