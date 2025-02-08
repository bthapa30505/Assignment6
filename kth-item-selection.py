import random
import time


#Implementing the medians of medians algorithm.
def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    # Divides the array into groups of 5 elements
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    # Finds the median of medians recursively
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k <= len(low):
        return median_of_medians(low, k)
    elif k <= len(low) + len(pivots):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - len(pivots))
    

#Implementation of the quick sort algorithm.
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Choose a random pivot
    pivot = random.choice(arr)

    # Partition the array into three parts
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k <= len(low):
        return quickselect(low, k)
    elif k <= len(low) + len(pivots):
        return pivot
    else:
        return quickselect(high, k - len(low) - len(pivots))


# Function to print time difference
def print_difference(start_time, end_time, data_type):
    print(f"Time taken for {data_type}: {end_time - start_time:.6f} seconds")


def run_tests(n):
    sorted_data = list(range(1, n + 1))
    sorted_descending = list(range(n, 0, -1))
    random_data = random.sample(range(1, n + 1), n)
    random_data_duplicate = random.choices(range(1, n + 1), k=n)
    
    k = n // 2  # Find the median element
    
    print("Testing Median of Medians:")
    start_time = time.time()
    median_of_medians(sorted_data, k)
    end_time = time.time()
    print_difference(start_time, end_time, "sorted data")
    
    start_time = time.time()
    median_of_medians(sorted_descending, k)
    end_time = time.time()
    print_difference(start_time, end_time, "sorted descending data")
    
    start_time = time.time()
    median_of_medians(random_data, k)
    end_time = time.time()
    print_difference(start_time, end_time, "random data")
    
    start_time = time.time()
    median_of_medians(random_data_duplicate, k)
    end_time = time.time()
    print_difference(start_time, end_time, "random data with duplicates")
    
    print("\nTesting Quickselect:")
    start_time = time.time()
    quickselect(sorted_data, k)
    end_time = time.time()
    print_difference(start_time, end_time, "sorted data")
    
    start_time = time.time()
    quickselect(sorted_descending, k)
    end_time = time.time()
    print_difference(start_time, end_time, "sorted descending data")
    
    start_time = time.time()
    quickselect(random_data, k)
    end_time = time.time()
    print_difference(start_time, end_time, "random data")
    
    start_time = time.time()
    quickselect(random_data_duplicate, k)
    end_time = time.time()
    print_difference(start_time, end_time, "random data with duplicates")

# Run tests for both 10,000 and 20,000 elements
for size in [10000, 20000]:
    print(f"\nRunning tests for input size: {size}")
    run_tests(size)