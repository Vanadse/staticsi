

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
        for prop in self.props:
            result = result + f' {prop}="{self.props[prop]}"'
        return result
    
    def __repr__(self):
        return "HTMLNode(" + f"{self.tag}, " + f"{self.value}" + f", {self.children}" + f",{self.props_to_html()})"

