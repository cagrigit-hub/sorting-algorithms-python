import random
def joker_sort(lst):
    # shuffle the list expect to be sorted
    random.shuffle(lst)
    # check if the list is sorted
    while lst != sorted(lst):
        random.shuffle(lst)
# Driver code to test the above code
if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4,3,8,11,23,15,23,44,11,63,234,21,2,3,4,1,2]
    joker_sort(lst)

    print("Sorted list is: ", lst)