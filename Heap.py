import enum
from math import floor as fl


class HeapFy:

    def HeapFy_(Array, i: int, HeapType: enum.Enum = "Min"):
        if (i > fl(len(Array)/2)-1):
            return Array
        value = Array[i]
        left_Size = 2*i+1
        left = Array[2*i+1]
        right = Array[2*i+2]
        right_Size = 2*i+2
        if (left < right):
            if (value > left):
                Array[i] = left
                Array[left_Size] = value
                HeapFy.HeapFy_(Array, left_Size)
        elif (value > right):
            Array[i] = right
            Array[right_Size] = value
            HeapFy.HeapFy_(Array, right_Size)

        return Array

    def Build_Heap(Array: list) -> list:
        for i in range(fl(len(Array)/2)-1, -1, -1):
            Array = HeapFy.HeapFy_(Array, i)
        return Array


print(HeapFy.Build_Heap([8, 5, 20, 4, 6, 3, 10, 2, 5, 4, 1]))

a = [1, 2, 3]
a += [4]

# HeapType is a delage to a function that returns a boolean for the  max heap or a min heap


def HeapType(father, value) -> bool:
    return father > value


def Insert_Heap(Array: list, Value, HeapType) -> list:
    Array += [Value]

    value_index = len(Array)-1
    return HeapUp(Array, value_index, HeapType)


def HeapUp(Array, value_index, HeapType: bool) -> list:
    if (value_index <= 0):
        return Array
    father_index = fl((value_index+1)/2)-1
    value = Array[value_index]
    father = Array[father_index]
    if (HeapType(father, value)):
        Array[father_index] = value
        Array[value_index] = father
        HeapUp(Array, father_index, HeapType)

    return Array


print(Insert_Heap([3, 5, 7], 2, HeapType))
