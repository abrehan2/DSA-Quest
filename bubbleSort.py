def bubbleSort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
        
        if not swapped:
            break



if __name__ == "__main__":
   values = [5, 9, 2, 1, 67, 34, 88, 34]
   bubbleSort(values)
   print(values)
