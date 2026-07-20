# Assignment: Search in a Rotated Decreasing Array

## Problem Statement
Given an integer array `nums` that was originally sorted in **strictly descending (reverse) order** and then rotated at an unknown pivot index `k` (`0 <= k < nums.length`), and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with $O(\log n)$ runtime complexity.

---

### Examples

#### Example 1:
- **Input:** `nums = [2, 1, 0, 7, 6, 5, 4]`, `target = 6`
- **Output:** `4`
- **Explanation:** The array was originally `[7, 6, 5, 4, 2, 1, 0]` and rotated. `6` is located at index 4.

#### Example 2:
- **Input:** `nums = [2, 1, 0, 7, 6, 5, 4]`, `target = 3`
- **Output:** `-1`
- **Explanation:** `3` is not present in `nums`.

#### Example 3:
- **Input:** `nums = [5, 4, 3, 2, 1]`, `target = 4`
- **Output:** `1`

#### Example 4:
- **Input:** `nums = []`, `target = 5`
- **Output:** `-1`
- **Explanation:** The array is empty, so target cannot be found.

---

### Constraints:
- `0 <= nums.length <= 5 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**.
- `nums` is an array sorted in descending order that has been rotated.
- `-10^4 <= target <= 10^4`
