#User function Template for python3
def distinct(arr):
    # Your Code here
    counter = 0
    freq_set = set()
    for num in arr:
        if num not in freq_set:
            freq_set.add(num)
            counter += 1
    return counter