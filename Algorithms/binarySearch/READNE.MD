#  Binary Search in Python

![Fibonacci spiral](https://upload.wikimedia.org/wikipedia/commons/c/c1/Binary-search-work.gif)


This project demonstrates the **binary search algorithm**, implemented in Python. It's a fast and efficient way to search for a specific value in a **sorted list**.
            

---

## What Is Binary Search?

Binary search is a **divide-and-conquer** algorithm used to quickly find a target value in a sorted array. Instead of checking each item one by one (like in linear search), binary search cuts the search space in half at each step.

To use binary search, the input list **must be sorted** in ascending order.

---


## Time and Space Complexity

| Operation       | Complexity |
|----------------|------------|
| Best Case      | O(1)       |
| Average Case   | O(log n)   |
| Worst Case     | O(log n)   |
| Space Complexity | O(1)    |

Binary search is **very efficient** for large, sorted datasets.

---

## When to Use Binary Search

Use binary search when:

- You have a **sorted** list or array.
- You need to **quickly** search for the presence or index of a value.
- You want better performance than linear search (O(n)).

## Example input
1. we call the function to insert the value
2. We insert the value and our array as shown below

    ```python
    array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
   target = 15
   binary_search(array, target)
    
## Example output
The value 15 was found at index: 7

---

## How to Run

1. Save the code in a file, for example `binary_search.py`.
2. Open a terminal in the same folder.
3. Run the program using Python:
```bash
python3 binary_search.py


