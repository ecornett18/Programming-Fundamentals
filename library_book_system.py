# Author: Ebony Cornett
# Date: October 4, 2026
# Description: Library Book Management System using object-oriented programming to create, display, check out, and return library books.
# Tier Level Attempted: Base Level

# Test Results:
# The program successfully displayed the full collection of 6 books.
# Wicked was successfully checked out to Lauren.
# The Great Gatsby was successfully checked out to Essence.
# A second checkout attempt for Wicked was correctly rejected.
# The Great Gatsby was successfully returned and became available again.
# The collection was successfully sorted alphabetically by title.
# The available books list correctly displayed only books that were available.

# Represents a book in the library.
class Book:
    # Initializes a new Book object with its information.
    def __init__(self, title, author, isbn, year, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self.available = True
        self.borrower = None
    # Checks out the book to a borrower.
    def check_out(self, borrower_name):
        if self.available:
            self.available = False
            self.borrower = borrower_name
            return True
        else:
            return False
    # Returns the book and provides a confirmation message.
    def return_book(self):
        self.available = True
        self.borrower = None
        return f"'{self.title}' has been returned and is now available."  
    # Returns the current availability status of the book.
    def get_status(self):
        if self.available:
            return "Available"
        else:
            return f"Checked out to {self.borrower}"
    # Returns a formatted string with the book's information and status.
    def __str__(self):
        return (
            f"{self.isbn:<18} "
            f"{self.title:<25} "
            f"by {self.author:<20} "
            f"{self.year:<6} "
            f"{self.genre:<18} "
            f"{self.get_status()}"
        )
# Create the starter book collection.
collection = [
    Book("Wicked", "Gregory Maguire", "978-0061350962", 1995, "Fantasy"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 1925, "Classic Fiction"),
    Book("A Wrinkle in Time", "Madeleine L'Engle", "978-0312367541", 1962, "Science Fiction"),
    Book("The Fault in Our Stars", "John Green", "978-0525478812", 2012, "Young Adult"),
    Book("My Sister's Keeper", "Jodi Picoult", "978-0743454537", 2004, "Fiction"),
    Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", 1960, "Classic Fiction")
] 
# Display the full collection.
print("\n=== Full Collection ===")
for book in collection:
    print(book)
# Check out the first book.
if collection[0].check_out("Lauren"):
    print(f"\n'{collection[0].title}' checked out to Lauren.")
else:
    print(f"\n'{collection[0].title}' is already checked out.")
# Check out the second book.
if collection[1].check_out("Essence"):
    print(f"'{collection[1].title}' checked out to Essence.")
else:
    print(f"'{collection[1].title}' is already checked out.")    
# Attempt to check out the first book again.
if collection[0].check_out("Taylor"):
    print(f"'{collection[0].title}' checked out successfully.")
else:
    print(f"'{collection[0].title}' is already checked out.")    
# Return the second checked-out book.
print(collection[1].return_book())
# Display the collection sorted alphabetically by title.
print("\n=== Collection Sorted by Title ===")
sorted_collection = sorted(collection, key=lambda b: b.title)
for book in sorted_collection:
    print(book)  
# Display only the books that are currently available.
print("\n=== Available Books ===")
available_books = [book for book in collection if book.available is True]
for book in available_books:
    print(book)    