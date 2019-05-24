# compare consecutive pairs of elements
# swap elements in pair such that smaller is first

# Complexity = O(n^2) where n is the length of L
def bubble_sort(L):
    swap = False
    # O(len(L))
    while not swap:
        swap = True
        # O(len(L))
        for j in range(1, len(L)-1):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

s = [1, 3, 5, 6]
bubble_sort(s)
print(s)