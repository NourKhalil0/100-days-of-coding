#  Quick Sort Algorithm
![](https://upload.wikimedia.org/wikipedia/commons/9/9c/Quicksort-example.gif?20110419161403)
---

##  Overview

This project contains an implementation of the Quick Sort algorithm written in Java. Quick Sort is an efficient, comparison based, divide and conquer sorting algorithm that is widely used in practice due to its excellent performance on average.

---

##  How Quick Sort Works

1. Pivot Selection: Choose a pivot element from the array (commonly the last element).
2. Partitioning: Rearrange elements so that all items smaller than the pivot are on the left, and all greater are on the right.
3. Recursive Sorting: Recursively apply the same logic to the sub-arrays on the left and right of the pivot.
4. In-Place Sorting: The algorithm sorts the array in place, using no additional memory for another array.

---

##  Time Complexity

| Scenario        | Time Complexity |
|------------------|------------------|
| Best Case        | O(n log n)       |
| Average Case     | O(n log n)       |
| Worst Case       | O(n²)            |

> **Note**: Worst case performance occurs when the pivot is always the smallest or largest element ( in already sorted arrays.). This can be mitigated using better pivot strategies like median of three.

---

## Input

A single unsorted array of integers.
 ````java
[10, 7, 8, 9, 1, 5]
````
---
## Output
The same array, sorted in ascending order.
````java
[1, 5, 7, 8, 9, 10]
````
---
## Run
To compile and run from terminal:
````bash
javac QuickSort.java
java QuickSort
