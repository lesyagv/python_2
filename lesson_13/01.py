from typing import List, Dict

def add_book() -> None:
    "This function takes no arguments and returns nothing, so the result is None."
    title: str = input("Title: ").strip().title()
    author: str = input("Author: ").strip().title()
    year: str = input("Year of publication: ").strip()

    with open("books.csv", "a") as reading_list:
        reading_list.write(f"{title},{author},{year},Not Read\n")

def delete_book(books: List[Dict[str, str]], book_to_delete: Dict[str, str]) -> None:
    "A dictionary representing the book to be deleted. The function returns nothing (None)."
    books.remove(book_to_delete)

def find_books() -> List[Dict[str, str]]:
    "The function takes no arguments. Returns a list of dictionaries where each dictionary represents a book with attributes of type str"
    reading_list: List[Dict[str, str]] = get_all_books()
    matching_books: List[Dict[str, str]] = []

    search_term: str = input("Please enter a book title: ").strip().lower()

    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)

    return matching_books

# Helper function for retrieving data from the csv file
def get_all_books() -> List[Dict[str, str]]:
    "The function takes no arguments. Returns a list of dictionaries where each dictionary represents a book with attributes of type str."
    books: List[Dict[str, str]] = []

    with open("books.csv", "r") as reading_list:
        for book in reading_list:
            # Extracts the values from the CSV data
            title, author, year, read_status = book.strip().split(",")

            # Creates a dictionary from the csv data and adds it to the books list
            books.append({
                "title": title,
                "author": author,
                "year": year,
                "read": read_status
            })

    return books

def mark_book_as_read(books: List[Dict[str, str]], book_to_update: Dict[str, str]) -> None:
    "books: a list of dictionaries, where each dictionary represents a book with attributes of type str. book_to_update: a dictionary representing the book to be marked as read. the function returns nothing (None)."
    index: int = books.index(book_to_update)
    books[index]['read'] = "Read"

def update_reading_list(operation: callable) -> None:
    "operation: A function that takes two arguments (a list of books and a single book) and returns nothing. The function returns nothing (None)."
    books: List[Dict[str, str]] = get_all_books()
    matching_books: List[Dict[str, str]] = find_books()

    if matching_books:
        operation(books, matching_books[0])

        with open("books.csv", "w") as reading_list:
            for book in books:
                reading_list.write(",".join(book.values()) + "\n")
    else:
        print("Sorry, we didn't find any books matching that title.")

def show_books(books: List[Dict[str, str]]) -> None:
    "books: a list of dictionaries, where each dictionary represents a book with attributes of type str.The function returns nothing (None)."
    # Adds an empty line before the output
    print()

    for book in books:
        print(f"{book['title']}, by {book['author']} ({book['year']}) - {book['read']}")

    print()

menu_prompt: str = """Please enter one of the following options:
"menu_prompt: variable of type str."
- 'a' to add a book
- 'd' to delete a book
- 'l' to list the books
- 'r' to mark a book as read
- 's' to search for a book
- 'q' to quit

What would you like to do? """

# Get a selection from the user
selected_option: str = input(menu_prompt).strip().lower()
"selected_option: variable of type str."
# Run the loop until the user selected 'q'
while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "d":
        update_reading_list(delete_book)
    elif selected_option == "l":
        # Retrieves the whole reading list for printing
        reading_list: List[Dict[str, str]] = get_all_books()

        # Check that reading_list contains at least one book
        if reading_list:
            show_books(reading_list)
        else:
            print("Your reading list is empty.")
    elif selected_option == "r":
        update_reading_list(mark_book_as_read)
    elif selected_option == "s":
        matching_books: List[Dict[str, str]] = find_books()

        # Checks that the seach returned at least one book
        if matching_books:
            show_books(matching_books)
        else:
            print("Sorry, we didn't find any books for that search term")
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")

    # Allow the user to change their selection at the end of each iteration
    selected_option = input(menu_prompt).strip().lower()
