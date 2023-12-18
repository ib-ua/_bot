class Note:

    def __init__(self, content, title, tags):
        if content and isinstance(content, str):
            self.__content = content
        else:
            self.__content = None

        if title and isinstance(title, str):
            self.__title = title
        else:
            self.__title = None

        self.__tags = tags if tags else []

    @property
    def content(self):
        return self.__content
    
    @property
    def title(self):
        return self.__title
    
    @property
    def tags(self):
        return self.__tags
    
    def set_content(self, content):
        self.__content = content if (content and isinstance(content, str)) else None
    
    def set_title(self, title):
        self.__title = title if (title and isinstance(title, str)) else None
    
    def edit_content(self, content):
        self.set_content(content)
    
    def edit_title(self, title):
        self.set_title(title)

    def add_tag(self, tag):
        if tag in self.__tags:
            return False
        self.__tags.append(tag)
        return True

    def delete_tag(self, tag):
        if tag in self.__tags:
            self.__tags.remove(tag)
            return True
        return False

    def __eq__(self, note):
        if isinstance(note, Note):
            return self.content == note.content and self.title.lower() == note.title.lower()
        return False
        
    