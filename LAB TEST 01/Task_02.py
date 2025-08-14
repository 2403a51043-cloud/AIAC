def recommend_book():
    books = []
    n = int(input("Enter the number of books: "))
    for i in range(n):
        title = input(f"Enter the title of book {i+1}: ").strip()
        genre = input(f"Enter the genre of book {i+1}: ").strip().lower()
        books.append({'title': title, 'genre': genre})

    preferred_genre = input("Enter your preferred genre: ").strip().lower()
    found_books = [book['title'] for book in books if book['genre'] == preferred_genre]

    if found_books:
        print("Recommended book(s) based on your preferred genre:")
        for book in found_books:
            print(book)
    else:
        print("No books found for your preferred genre.")

if __name__ == "__main__":
    recommend_book()
