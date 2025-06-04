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

main()