# Divide the unsorted array in it's lowest form where they cannot be further divided and become a single element (DIVIDE AND CONQUER RULE) big notation -> (nlogn)

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_sort_two_lists(left, right)


def merge_sort_two_lists(a, b):
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    sorted_arr = []

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_arr.append(a[i])
            i+=1
        else:
            sorted_arr.append(b[j])
            j+=1

    while i < len_a:
        sorted_arr.append(a[i])
        i+=1
    
    while j < len_b:
        sorted_arr.append(b[j])
        j+=1
    
    return sorted_arr


if __name__ == '__main__':
    # l1 = [5, 8, 12, 56, 89, 100]
    # l2 = [7, 9, 45, 51]
    l3 = [10, 3, 15, 7, 8, 23, 98, 29]

    # print(merge_sort_two_lists(l1, l2))
    print(merge_sort(l3))