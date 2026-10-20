from typing import List


def remove_element(arr: List[int], element: int) -> List[int]:
    c_arr = arr.copy()

    if element in c_arr:
        c_arr.remove(element)
    
    return c_arr




# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
