import random

def bubble_sort(x):
    for i in range(len(x)):
        for j in range(len(x)-1):
            if (x[j] > x[j+1]):
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
    return x

def selection_sort(x):
    tempLen = len(x)
    for i in range(len(x)):
        max_indice = 0
        for j in range(tempLen):
            if(x[j] > x[max_indice]):
                max_indice = j
        temp = x[tempLen-1]
        x[tempLen-1] = x[max_indice]
        x[max_indice] = temp
        tempLen = tempLen - 1
    return x

def insertion_sort(x):
    for i in range(len(x)-1):
        subArr = x[:i + 1]
        for j in range(i+1):
            if(x[i+1] < subArr[j]):
                x = subArr[:j] + [x[i+1]] + subArr[j:] + x[i+2:]
                break
    return x

def shell_sort(x):
    gap = (int) (len(x)/2)
    while(gap >= 1):
        for i in range(gap, len(x)):
            j=i
            while True:
                if(x[j] < x[j-gap]):
                    temp = x[j]
                    x[j] = x[j-gap]
                    x[j-gap] = temp
                else:
                    break
                if(j - gap < gap):
                    break
                else:
                    j = j - gap
        gap = (int) (gap/2)
    return x


def merge_sort(x):
    """
    size = (int)(len(x) / 2)
    while True:
        size = (int)(size / 2)
        if(size == 2):
            if(x[1]>x[1+1]):
                temp = x[1]
                x[1] = x[1+1]
                x[1+1] = temp
        elif(size == 3):
            if(x[1+1] > x[1+2]):
                temp = x[1+1]
                x[1+1] = x[1+2]
                x[1+2] = temp
            for i in range():
                for j in range():
    """
    return x

def quick_sort(x):

    return x

# main

arr = []
for i in range(5):
    arr.append((int)(random.random()*100))

print(arr)

arr1 = arr[:]
bubSort = bubble_sort(arr1)
print(bubSort)

arr2 = arr[:] # neden arr1, arr2 gibi farklı değişkenler tanımlamama rağmen; arr dizisini de sıralıyor? ✔ [:]
selecSort = selection_sort(arr2)
print(selecSort)

arr3 = arr[:]
insertSort = insertion_sort(arr3)
print(insertSort)

arr4 = arr[:]
shellSort = shell_sort(arr4)
print(shellSort)

# not considered yet..

arr5 = arr[:]
mergeSort = merge_sort(arr5)
print (mergeSort)

arr6 = arr[:]
quickSort = quick_sort(arr6)
print(quickSort)