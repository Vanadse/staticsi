from textnode import *
from htmlnode import *

def main():
    test_text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print (test_text_node)


    test_dict = {
                "href": "https://www.google.com",
                "target": "_blank",
                }
    test_HTML_node = HTMLNode("p", "This is a test paragraph", None, test_dict)
    print (test_HTML_node)

    test_Leaf_node = LeafNode("p", "This is a paragraph of text.")
    print (test_Leaf_node)

    test_Leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print (test_Leaf_node)


main()