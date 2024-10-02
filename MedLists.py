"""
MEDIAN OF TWO SORTED LISTS

Difficulty: 3/10

Comments: Basic concepts and minor code to be thought of
"""


def find_median_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minX = float('inf') if partitionX == x else nums1[partitionX]

        maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minY = float('inf') if partitionY == y else nums2[partitionY]

        if maxX <= minY and maxY <= minX:
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1

    raise ValueError("Input arrays are not sorted")


# Example usage:
nums1 = [1, 2, 5, 8]
nums2 = [3, 4, 6, 7]
print(find_median_sorted_arrays(nums1, nums2))

nums1 = [1, 3, 8, 9, 15]
nums2 = [7, 11, 18, 19, 21, 25]
print(find_median_sorted_arrays(nums1, nums2))

nums1 = [23, 26, 31, 35]
nums2 = [3, 5, 7, 9, 11, 16]
print(find_median_sorted_arrays(nums1, nums2))
