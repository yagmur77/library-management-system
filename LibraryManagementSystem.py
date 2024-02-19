class Library:
    def __init__(self, file_path="books.txt"):
        self.file_path = file_path
        self.file = open(self.file_path, "a+")

    def __del__(self):
         self.file.close()

    def list_books(self):     
            self.file.seek(0)
            file_contents = self.file.read()
            books_list = file_contents.splitlines()
        
            for book_info in books_list:
                book_details = book_info.split(',')
                book_name, author = book_details[:2]
                print(f"Book Name: {book_name}, Author: {author}")

    def add_book(self):
            book_name = input("Enter the book title: ")
            author = input("Enter the author: ")
            release_year = input("Enter the release year: ")
            num_pages = input("Enter the number of pages: ")

            book_info = f"{book_name},{author},{release_year},{num_pages}\n"
            self.file.write(book_info)

    def remove_book(self, title_to_remove):
            self.file.seek(0)
            file_contents = self.file.read()
            books_list = file_contents.splitlines()

            index_to_remove = -1
            for i, book_info in enumerate(books_list):
                if title_to_remove.lower() in book_info.lower():
                    index_to_remove = i
                    break

            if index_to_remove != -1:
                removed_book = books_list.pop(index_to_remove)
                
            self.file.truncate(0)

            for book_info in books_list:
                self.file.write(book_info + '\n')
lib = Library()

while True:
    print("Welcome to the library!")
    print("Choose from the following options:")
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("Q) Quit")

    user_input = input("Enter your choice (1-4): ")

    if user_input == "1":
        lib.list_books()
    elif user_input == "2":
        lib.add_book()
    elif user_input == "3":
        book_to_remove = input("Enter the title of the book to remove: ")
        lib.remove_book(book_to_remove)
    elif user_input == "Q":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
