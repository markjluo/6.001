# Merge sort complexity: nlogn where n is len(L)

def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    # Base case: when the length of the list if smaller than 2
    # it is already  sorted
    if len(L) < 2:
        return L
    else:
        # Divide the list successively in halves

        # Depth-first such that conquer smallest
        # pieces down one branch first before
        # moving to larger pieces
        mid = len(L)//2
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        return merge(left, right)


a = [3, 4, 2, 1,5 ,213, 1, .001]
print(merge([3,4], [2, 1]))
print(merge_sort(a))