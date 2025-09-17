import csv
import json
import time

def load_books_csv(filename):
    books = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append({'title': row['title'], 'author': row['author']})
    return books

def load_books_json(filename):
    with open(filename, encoding='utf-8') as f:
        books = json.load(f)
    return books

def linear_search(books, keyword):
    keyword = keyword.lower()
    results = []
    for book in books:
        if keyword in book['title'].lower() or keyword in book['author'].lower():
            results.append(book)
    return results

def binary_search(books_sorted, keyword):
    # books_sorted must be sorted by title
    keyword = keyword.lower()
    left, right = 0, len(books_sorted) - 1
    results = []
    while left <= right:
        mid = (left + right) // 2
        title = books_sorted[mid]['title'].lower()
        if keyword in title:
            # Find all matches around mid
            l, r = mid, mid+1
            while l >= 0 and keyword in books_sorted[l]['title'].lower():
                l -= 1
            while r < len(books_sorted) and keyword in books_sorted[r]['title'].lower():
                r += 1
            results.extend(books_sorted[l+1:r])
            break
        elif keyword < title:
            right = mid - 1
        else:
            left = mid + 1
    return results

def build_hash_table(books):
    # Hash by lowercased words in title and author
    hash_table = {}
    for book in books:
        words = set(book['title'].lower().split() + book['author'].lower().split())
        for word in words:
            if word not in hash_table:
                hash_table[word] = []
            hash_table[word].append(book)
    return hash_table

def hash_search(hash_table, keyword):
    keyword = keyword.lower()
    return hash_table.get(keyword, [])

def print_results(results):
    if not results:
        print("No matching entries found.")
    else:
        print(f"Found {len(results)} matching entries:")
        for book in results:
            print(f"Title: {book['title']} | Author: {book['author']}")

def main():
    print("SR University Digital Library Search System")
    print("Loading books from CSV file: C:\\Users\\manic\\OneDrive\\Desktop\\AIAC\\LAB12\\books.csv")
    filename = r"C:\Users\manic\OneDrive\Desktop\AIAC\LAB12\books.csv"
    books = load_books_csv(filename)

    keyword = input("Enter a keyword to search (title or author): ")

    # Linear Search
    start = time.time()
    linear_results = linear_search(books, keyword)
    end = time.time()
    linear_time = end - start
    print("\n[Linear Search Results]")
    print_results(linear_results)
    print(f"Linear Search Time: {linear_time:.6f} seconds\n")

    # Binary Search (on title)
    books_sorted = sorted(books, key=lambda x: x['title'].lower())
    start = time.time()
    binary_results = binary_search(books_sorted, keyword)
    end = time.time()
    binary_time = end - start
    print("[Binary Search Results] (on title only)")
    print_results(binary_results)
    print(f"Binary Search Time: {binary_time:.6f} seconds\n")

    # Hash-based Search (by word)
    hash_table = build_hash_table(books)
    start = time.time()
    hash_results = hash_search(hash_table, keyword)
    end = time.time()
    hash_time = end - start
    print("[Hash-based Search Results] (by word in title/author)")
    print_results(hash_results)
    print(f"Hash-based Search Time: {hash_time:.6f} seconds\n")

    print("Efficiency Comparison:")
    print(f"Linear Search: {linear_time:.6f} s, Binary Search: {binary_time:.6f} s, Hash-based Search: {hash_time:.6f} s")

if __name__ == "__main__":
    main()

