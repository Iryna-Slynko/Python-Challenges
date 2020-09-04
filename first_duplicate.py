'''For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

For a = [2, 2], the output should be firstDuplicate(a) = 2;

For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.
'''
def firstDuplicate(a):
    values_set=set()
    for elem in a:
        if elem in values_set:
            return elem
        else:
            values_set.add(elem)
    
    return -1
