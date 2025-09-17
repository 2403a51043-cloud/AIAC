import random
import time

def simulate_stock_data(n):
    stocks = []
    used_symbols = set()
    while len(stocks) < n:
        symbol = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))
        if symbol in used_symbols:
            continue
        used_symbols.add(symbol)
        open_price = round(random.uniform(100, 1000), 2)
        close_price = round(open_price * random.uniform(0.95, 1.05), 2)
        stocks.append({
            'Symbol': symbol,
            'Open': open_price,
            'Close': close_price,
            'Change': ((close_price - open_price) / open_price) * 100
        })
    return stocks

def heapify(arr, n, i, key):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l][key] > arr[largest][key]:
        largest = l
    if r < n and arr[r][key] > arr[largest][key]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heap_sort(arr, key):
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, key)
    arr.reverse()  # For descending order

def build_stock_hashmap(stocks):
    return {stock['Symbol']: stock for stock in stocks}

def print_stocks(stocks, top_n=10):
    print(f"\n{'Symbol':<8}{'Open':>10}{'Close':>10}{'%Change':>12}")
    for stock in stocks[:top_n]:
        print(f"{stock['Symbol']:<8}{stock['Open']:>10.2f}{stock['Close']:>10.2f}{stock['Change']:>12.2f}")

def main():
    print("SR University FinTech Lab - Real-Time Stock Data Sorting & Searching")
    while True:
        try:
            n = int(input("Enter number of stocks to simulate: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    stocks = simulate_stock_data(n)

    # Heap Sort by percentage change
    stocks_for_heap = [dict(stock) for stock in stocks]
    start = time.time()
    heap_sort(stocks_for_heap, 'Change')
    heap_time = time.time() - start

    print("\nTop 10 Stocks by Daily % Gain (Heap Sort):")
    print_stocks(stocks_for_heap, top_n=min(10, n))

    # Standard library sort
    start = time.time()
    stocks_sorted = sorted(stocks, key=lambda x: x['Change'], reverse=True)
    std_sort_time = time.time() - start

    print("\nTop 10 Stocks by Daily % Gain (sorted()):")
    print_stocks(stocks_sorted, top_n=min(10, n))

    # Build hash map for instant search
    stock_map = build_stock_hashmap(stocks)

    # Search for a stock symbol
    while True:
        symbol = input("\nEnter a stock symbol to search (or 'exit' to quit): ").strip().upper()
        if symbol == 'EXIT':
            break
        if not symbol:
            print("Please enter a valid stock symbol.")
            continue

        # Hash map search
        start = time.time()
        stock = stock_map.get(symbol)
        hash_time = time.time() - start

        # Standard dict lookup (same as above, but for comparison)
        start = time.time()
        stock_std = stock_map.get(symbol)
        std_lookup_time = time.time() - start

        if stock:
            print(f"\n[Hash Map Search] Found: Symbol: {stock['Symbol']}, Open: {stock['Open']:.2f}, Close: {stock['Close']:.2f}, %Change: {stock['Change']:.2f}")
            print(f"Hash Map Search Time: {hash_time:.8f} seconds")
            print(f"Standard Dict Lookup Time: {std_lookup_time:.8f} seconds")
        else:
            print("Stock symbol not found.")

    print("\n--- Performance Comparison ---")
    print(f"Heap Sort Time: {heap_time:.6f} seconds")
    print(f"sorted() Time: {std_sort_time:.6f} seconds")
    print("Hash map search and dict lookup times are both nearly instantaneous for single lookups.")

if __name__ == "__main__":
    main()


