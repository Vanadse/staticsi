

class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props == None:
            return None
        for prop in self.props:
            result = result + f' {prop}="{self.props[prop]}"'
        return result
    
    def __repr__(self):
        return "HTMLNode(" + f"<{self.tag}>, " + f"{self.value}" + f", {self.children}" + f",{self.props_to_html()})"

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError
        
        if self.tag == None:
            return self.value
        
        if self.tag == "p" or self.tag == "b" or self.tag == "i":
            return f"<{self.tag}>{self.value}</{self.tag}>"
    
        if self.tag == "a":
            return f"<{self.tag}{self.props_to_html()}<{self.tag}>"
        
    def __repr__(self):
        return "LeafNode(" + f"{self.to_html()})"