library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


def library_system(library):
   
    name = input("What is the name of the book? ")
    author = input("Who is the author? ")
    
    for book in library:
        if book == (name, author):
            print("This book is already in library. ")
            return
        
    library.append((name, author))
    print("Book successfully added to the library.")
            
        
library_system(library)

