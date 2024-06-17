from collections import deque


def sliding_window_max(nums, k):
    # Edge cases
    if not nums:
        return []
    if k == 0:
        return nums

    deq = deque()
    max_values = []

    for i in range(len(nums)):
        # Remove elements not within the sliding window
        while deq and deq[0] < i - k + 1:
            deq.popleft()

        # Remove elements smaller than the current element from the deque
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        # Add the current element index to the deque
        deq.append(i)

        # The first element in the deque is the largest element for the current window
        if i >= k - 1:
            max_values.append(nums[deq[0]])

    return max_values


# Example usage
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
result = sliding_window_max(num_list, k)
print(result)  # Output: [5, 5, 5, 5, 10, 12, 33, 33]
