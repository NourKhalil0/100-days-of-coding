#  Merge Sort algorithm
![](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)
---

##  Overview

This folder contains a simple implementation of the Merge Sort algorithm in Python.

Merge Sort is a classic divide and conquer sorting algorithm with a guaranteed time complexity of O(n log n). It splits the list into halves recursively and then merges the sorted halves.

---

## How It Works

1. Base Case: If the list has 1 or fewer elements, it is already sorted.
2. Divide: The list is split into two halves.
3. Conquer: Recursively apply merge sort on both halves.
4. Combine: Merge the two sorted halves using the merge function.

---

## Input
```java
liste = [4, 1, 7, 3, 9, 2]
 ````
## Output
````java
[1, 2, 3, 4, 7, 9]
````
---
## Run
````bash
sudo python3 merge_sort.py
