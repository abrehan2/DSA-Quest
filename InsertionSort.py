def insertion_sort(elem):
    for i in range(1, len(elem)):
        anchor=elem[i]
        j = j - 1
        while j >=0 and anchor < elem[j]:
            elem[j+1] = elem[j]
            j = j - 1
        
        elem[j+1] = anchor


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(elements)
    print(elements)
