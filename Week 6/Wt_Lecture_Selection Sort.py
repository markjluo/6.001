# Keep selecting the smallest element to place in the beginning of the list


def selection_sort(L):
    suffixSt = 0
    # O(len(L))
    while suffixSt != len(L):
        # O(len(L)-i)
        # Gets smaller on each step, but still O(len(L))
        for i in range(suffixSt, len(L)):
            if L[suffixSt] > L[i]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1


a = [3, 1, 7, 9, 5]
selection_sort(a)
print(a)
