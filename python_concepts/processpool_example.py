from concurrent.futures import ProcessPoolExecutor


def square_number(n):
    return n * n


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    with ProcessPoolExecutor() as executor:
        # Execute the square_number function in parallel
        results = executor.map(square_number, numbers)

    print(list(results))  # Output: [1, 4, 9, 16, 25]
