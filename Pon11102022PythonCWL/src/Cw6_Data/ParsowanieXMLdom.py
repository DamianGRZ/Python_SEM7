import xml.dom.minidom

def ParseDom():
    #Creating Dom trre out of xml file
    DOMTree = xml.dom.minidom.parse("books.xml")
    # group is the top element
    group = DOMTree.documentElement
    # get collection of books
    books = group.getElementsByTagName("book")
    for book in books:
        print(f"-- Book {book.getAttribute('id')} --")
        author = book.getElementsByTagName('author')[0].childNodes[0].nodeValue #Get get the first one found, and the the value(by child node)
        title = book.getElementsByTagName('title')[0].childNodes[0].nodeValue
        genre = book.getElementsByTagName('genre')[0].childNodes[0].nodeValue
        price = book.getElementsByTagName('price')[0].childNodes[0].nodeValue
        publish_date = book.getElementsByTagName('publish_date')[0].childNodes[0].nodeValue
        description = book.getElementsByTagName('description')[0].childNodes[0].nodeValue
        #Printing
        print(f"author: {author}")
        print(f"title: {title}")
        print(f"genre: {genre}")
        print(f"price: {price}")
        print(f"publish_date: {publish_date}")
        print(f"description: {description}")

    #Changing one tag
    books[0].getElementsByTagName('author')[0].childNodes[0].nodeValue = "snry"
    books[0].setAttribute("id", "200")
    #Writing to the file
    with open('Newbooks.xml', 'w') as file:
        DOMTree.writexml(file)
        #file.write(DOMTree.writexml())

if (__name__ == "__main__"):
    ParseDom()