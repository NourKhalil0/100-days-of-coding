# Bubble Sort (Descending Order)

**Bubble Sort** is a fundamental sorting algorithm based on repeated comparison and swapping of adjacent elements.  
This implementation sorts an array in **descending order** using JavaScript.
![Bubble Sort Diagram](https://d3e8mc9t3dqxs7.cloudfront.net/wp-content/uploads/sites/11/2022/10/bubble-sort-in-data-structures-diagram.png)
---


## Features

- Sorts numeric arrays in **descending** order
- Simple, readable two-loop structure
- Demonstrates classic **bubble sort** logic
- Logs the sorted array to the console

---

## How It Works

The `bubbleSort` function compares adjacent elements and swaps them if the left one is **smaller** than the right one.  
Each iteration "bubbles" the largest unsorted value to the front.

---
## Function example
    array = bubbleSort([1, 2, 3, 4, 5, 6, 7, 8, 9]);
## Output
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

## Run
    node bubblesort.js
--You can run this code in any browser console or JavaScript runtime 

## Educational Notes
1. Time Complexity: O(n²) in worst and average case

2. In-place sorting, no extra memory

3. Great for learning, but inefficient for large datasets

![Bubble Sort](https://media1.tenor.com/m/h78xhYVtmgUAAAAd/sort-graph.gif)