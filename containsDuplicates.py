'''Given an array of integers, write a function that determines whether the array contains any duplicates. Your function should return true if any element appears at least twice in the array, and it should return false if every element is distinct.'''
def containsDuplicates(a):
    numbers_set = set()
    for i in range(len(a)):
        if a[i] not in numbers_set:
            numbers_set.add(a[i])
        else:
            return True
    return False
