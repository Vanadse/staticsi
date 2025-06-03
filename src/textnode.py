from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, type: TextType, url=None):
        self.text = text
        self.text_type = type
        self.url = url

    def __eq__(self, other):
        return(self.text == other.text and self.text_type == other.text_type and self.url == other.url)
    
    def __repr__(self):

        if self.url != None:
            return "TextNode(" f"{self.text}, " + f"{self.text_type.value}" + f", {self.url})"

        return "TextNode(" f"{self.text}, " + f"{self.text_type.value})"