def bubble_sort(list):
    for i in range(len(list)):
        swapped = False
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                swapped = True
                list[j], list[j+1] = list[j+1], list[j]
        if not swapped:
            break




if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    bubble_sort(lst)  # Calling selection sort function

    # Printing Sorted lst
    print("Sorted lst: ", lst)