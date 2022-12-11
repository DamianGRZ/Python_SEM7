import xml.sax

#Initialization
class BookHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current = ""
        self.author = ""
        self.title = ""
        self.genre = ""
        self.price = ""
        self.publish_date = ""
        self.description = ""

#  Start element ex <book id="bk101">
    def startElement(self, tag, attrs):
        self.current = tag
        if tag == "book":
            print(f"-- Book {attrs['id']} --")

# Inside elements save
    def characters(self, content):
        if self.current == "author":
            self.author += content

        elif self.current == "title":
            self.title += content

        elif self.current == "genre":
            self.genre += content

        elif self.current == "price":
            self.price += content

        elif self.current == "publish_date":
            self.publish_date += content

        elif self.current == "description":
            self.description += content
# Printing if the text is correct
    def endElement(self, tag):
        if self.current == "author":
            print(f"author: {self.author}")

        elif self.current == "title":
            print(f"title: {self.title}")

        elif self.current == "genre":
            print(f"genre: {self.genre}")

        elif self.current == "price":
            print(f"price: {self.price}")

        elif self.current == "publish_date":
            print(f"publish_date: {self.publish_date}")

        elif self.current == "description":
            print(f"description: {self.description}")

        self.current = ""


if (__name__ == "__main__"):
    # XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    #ContextHandler
    Handler = BookHandler()
    parser.setContentHandler(Handler)

    parser.parse("books.xml")

