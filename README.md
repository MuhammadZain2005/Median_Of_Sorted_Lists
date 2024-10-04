# Median of Two Sorted Lists

## Description

This project implements a function to find the median of two sorted arrays. The solution uses a binary search approach, making it efficient even for larger arrays. The goal is to demonstrate how binary search can be applied to solve median-related problems in logarithmic time.

## Features

- **Binary Search Algorithm**: Utilizes binary search to partition two arrays for an efficient solution.
- **Handles Various Input Sizes**: Works correctly even when the arrays have different lengths.
- **Efficient Complexity**: Achieves O(log(min(n, m))) time complexity, where n and m are the lengths of the two input arrays.

## How It Works

A step-by-step explanation of how the program operates:

1. **Input**: The function takes in two sorted arrays (`nums1` and `nums2`).
2. **Initialization**: The smaller array is selected as the basis for binary search, reducing time complexity.
3. **Process**: The arrays are partitioned to find the correct median by comparing the left and right partitions of both arrays.
4. **Output**: The median value is returned based on the combined partition results.

## Usage

### Prerequisites

- Python 3.x

### Running the Program

1. Clone the repository or download the script file `MedLists.py`.
2. Run the script using the command:

    ```bash
    python MedLists.py
    ```

3. The program will print the median for different example inputs.

### Example

```bash
$ python MedLists.py

2.5
16.0
13.5
```
## Program Structure

- **`find_median_sorted_arrays(nums1, nums2)`**: This function takes two sorted arrays and applies binary search to partition them into halves. Based on the partition values, it calculates the median.
- **`main()`**: The script demonstrates usage by providing sample sorted arrays and printing the resulting median.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

