#Ben Cradick
#cs3130
#10-19-18
from random import randint
import math

import sys
import time
#super danger don't do this if you can't afford to crash
sys.setrecursionlimit(20000)
sys.stdout =  open("CRAB2A.py", "a")

def selection_sort(arr):
    for i in range(len(arr)): 
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
                
        # Swap the found minimum element with  
        # the first element         
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 


def bubble_sort_counting(arr):
    n = len(arr) 
   
    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
  
        # Last i elements are already 
        #  in place 
        for j in range(0, n-i-1): 
   
            # traverse the array from 0 to 
            # n-i-1. Swap if the element  
            # found is greater than the 
            # next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break
    


def bubble_sort_no_counting(arr):
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    

def quick_sort(arr, low, high):
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quick_sort(arr, pi+1, high) 
        quick_sort(arr, low, pi-1)

def merge_sort(arr, l, r):
    if l < r: 
  
        # Same as (l+r)/2, but avoids overflow for 
        # large l and h 
        m = math.floor((l+(r-1))/2)
  
        # Sort first and second halves 
        merge_sort(arr, l, m) 
        merge_sort(arr, m+1, r) 
        merge(arr, l, m, r) 

def partition(arr, low, high):
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     
    j = 0      
    k = l      
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
def generate_sorted_arr(size):
    
    #max value for integer in array
    UPPER = 10000
    #initialize lower so that we can initialize arrray with first value so index in range for loops.
    lower = randint(1,51)
    #arr is uninitialized list
    arr = [lower]
    #initialize x to 0 for array initialization.
    while lower + 50 <= UPPER and len(arr) <= size:
        #generate random value to be the lower bound for random generated number within +50 range of last lower.
        lower = randint(lower, lower+50)
        #append next value to list
        arr.append(lower)
    while len(arr) <= size:
        try:
            #select random initialized element that is not the last one
            element = randint(1, len(arr) - 1)

            #generate integer value that is >arr[element - 1] and <arr[element]
            inserted_val = randint(arr[element - 1], arr[element])

            #insert inserted_val into the list at element, list shifts right
            arr.insert(element, inserted_val)
        #used to debug the issue but only seeing the problem cases
        except IndexError:
            print("IndexError: line 179 ",element, inserted_val, len(arr))
    return arr


def generate_random_arr(size):
    arr = [randint(0,10000) for x in range(0,size)]
    return arr

#every 10th element of array will be random.
def generate_semi_sorted_arr(size):
    #generate sorted array which will become semi sorted
    source_arr = generate_sorted_arr(size)
    arr = source_arr.copy()
    length = len(source_arr)
    for x in range(0,size):
        if x%10 == 0:
            rand_element = randint(0,length-1)
            arr[x] = source_arr[rand_element]
            source_arr.pop(rand_element)
            length = length - 1
    return arr
#tests that array is sorted
def test_list_ordered(arr):
    for x in range(1,len(arr) - 1):
        if(arr[x - 1] > arr[x]):
            return False
        
    return True
#function for testing to make sure arrays get sorted properly
def test_each_method():
    sorted_array = "sorted array"
    random_array = "random array"
    semi_sorted= "semi-sorted array"

    insert = "Insertion Sort"
    select = "Selection Sort"
    bubswith = "Bubble Sort w/ counting"
    bubswithout = "Bubble Sort w/o counting"
    merge = "Merge Sort"
    quick = "Quick Sort"
    size = [100,1000,10000]
    for x in range(0,3):
        
        arr1 = generate_sorted_arr(size[x])
        arr2 = generate_random_arr(size[x])
        arr3 = generate_semi_sorted_arr(size[x])

        copy1 = arr1.copy()
        copy2 = arr2.copy()
        copy3 = arr3.copy()

        insertion_sort(copy1)
        insertion_sort(copy2)
        insertion_sort(copy3)

        print(f'{insert:25}', f'{sorted_array:20}', "sorted: ", test_list_ordered(copy1))
        print(f'{insert:25}', f'{random_array:20}', "sorted: ", test_list_ordered(copy2))
        print(f'{insert:25}', f'{semi_sorted:20}', "sorted: ", test_list_ordered(copy3))

        copy1 = arr1.copy()
        copy2 = arr2.copy()
        copy3 = arr3.copy()

        selection_sort(copy1)
        selection_sort(copy2)
        selection_sort(copy3)

        print(f'{select:25}', f'{sorted_array:20}', "sorted: ", test_list_ordered(copy1))
        print(f'{select:25}', f'{random_array:20}', "sorted: ", test_list_ordered(copy2))
        print(f'{select:25}', f'{semi_sorted:20}', "sorted: ", test_list_ordered(copy3))

        copy1 = arr1.copy()
        copy2 = arr2.copy()
        copy3 = arr3.copy()

        bubble_sort_counting(copy1)
        bubble_sort_counting(copy2)
        bubble_sort_counting(copy3)

        print(f'{bubswith:25}', f'{sorted_array:20}', "sorted: ", test_list_ordered(copy1))
        print(f'{bubswith:25}', f'{random_array:20}', "sorted: ", test_list_ordered(copy2))
        print(f'{bubswith:25}', f'{semi_sorted:20}', "sorted: ", test_list_ordered(copy3))

        copy1 = arr1.copy()
        copy2 = arr2.copy()
        copy3 = arr3.copy()

        bubble_sort_no_counting(copy1)
        bubble_sort_no_counting(copy2)
        bubble_sort_no_counting(copy3)

        print(f'{bubswithout:25}', f'{sorted_array:20}', "sorted: ", test_list_ordered(copy1))
        print(f'{bubswithout:25}', f'{random_array:20}', "sorted: ", test_list_ordered(copy2))
        print(f'{bubswithout:25}', f'{semi_sorted:20}', "sorted: ", test_list_ordered(copy3))

        copy1 = arr1.copy()
        copy2 = arr2.copy()
        copy3 = arr3.copy()

        merge_sort(copy1, 0, size[x] - 1)
        merge_sort(copy2, 0, size[x] - 1)
        merge_sort(copy3, 0, size[x] - 1)

        print(f'{merge:25}', f'{sorted_array:20}', "sorted: ", test_list_ordered(copy1))
        print(f'{merge:25}', f'{random_array:20}', "sorted: ", test_list_ordered(copy2))
        print(f'{merge:25}', f'{semi_sorted:20}', "sorted: ", test_list_ordered(copy3))

        copy1 = arr1.copy()
        copy2 = arr2.copy()
        copy3 = arr3.copy()

        quick_sort(copy1, 0, size[x] - 1)
        quick_sort(copy2, 0, size[x] - 1)
        quick_sort(copy3, 0, size[x] - 1)

        print(f'{quick:25}', f'{sorted_array:20}', "sorted: ", test_list_ordered(copy1))
        print(f'{quick:25}', f'{random_array:20}', "sorted: ", test_list_ordered(copy2))
        print(f'{quick:25}', f'{semi_sorted:20}', "sorted: ", test_list_ordered(copy3))


        print("\n")

def time_each_method():
    sorted_array = "sorted array"
    random_array = "random array"
    semi_sorted= "semi-sorted array"

    insert = "Insertion Sort"
    select = "Selection Sort"
    bubswith = "Bubble Sort w/ counting"
    bubswithout = "Bubble Sort w/o counting"
    merge = "Merge Sort"
    quick = "Quick Sort"
    size = [100,1000,10000]
    for x in range(0,3):
        
        arr1 = generate_sorted_arr(size[x])
        arr2 = generate_random_arr(size[x])
        arr3 = generate_semi_sorted_arr(size[x])

        copy1 = arr1.copy()
        copy2 = arr2.copy()
        copy3 = arr3.copy()

        z = time.process_time()
        insertion_sort(copy1)
        y = time.process_time()
        time1 = y - z
        
        z = time.process_time()
        insertion_sort(copy2)
        y = time.process_time()
        time2 = y - z

        z = time.process_time()
        insertion_sort(copy3)
        y = time.process_time()
        time3 = y - z

        print(f'{insert:25}', f'{sorted_array:20}', "runtime:", time1)
        print(f'{insert:25}', f'{random_array:20}', "runtime:", time2)
        print(f'{insert:25}', f'{semi_sorted:20}', "runtime:", time3)

        copy1 = arr1.copy()
        copy2 = arr2.copy()
        copy3 = arr3.copy()

        z = time.process_time()
        selection_sort(copy1)
        y = time.process_time()
        time1 = y - z
        z = time.process_time()
        selection_sort(copy2)
        y = time.process_time()
        time2 = y - z
        z = time.process_time()
        selection_sort(copy3)
        y = time.process_time()
        time3 = y - z

        print(f'{select:25}', f'{sorted_array:20}', "runtime:", time1)
        print(f'{select:25}', f'{random_array:20}', "runtime:", time2)
        print(f'{select:25}', f'{semi_sorted:20}', "runtime:", time3)

        copy1 = arr1.copy()
        copy2 = arr2.copy()
        copy3 = arr3.copy()

        z = time.process_time()
        bubble_sort_counting(copy1)
        y = time.process_time()
        time1 = y - z
        z = time.process_time()
        bubble_sort_counting(copy2)
        y = time.process_time()
        time2 = y - z
        z = time.process_time()
        bubble_sort_counting(copy3)
        y = time.process_time()
        time3 = y - z

        print(f'{bubswith:25}', f'{sorted_array:20}', "runtime:", time1)
        print(f'{bubswith:25}', f'{random_array:20}', "runtime:", time2)
        print(f'{bubswith:25}', f'{semi_sorted:20}', "runtime:", time3)

        copy1 = arr1.copy()
        copy2 = arr2.copy()
        copy3 = arr3.copy()

        z = time.process_time()
        bubble_sort_no_counting(copy1)
        y = time.process_time()
        time1 = y - z
        z = time.process_time()
        bubble_sort_no_counting(copy2)
        y = time.process_time()
        time2 = y - z
        z = time.process_time()
        bubble_sort_no_counting(copy3)
        y = time.process_time()
        time3 = y - z

        print(f'{bubswithout:25}', f'{sorted_array:20}', "runtime:", time1)
        print(f'{bubswithout:25}', f'{random_array:20}', "runtime:", time2)
        print(f'{bubswithout:25}', f'{semi_sorted:20}', "runtime:", time3)

        copy1 = arr1.copy()
        copy2 = arr2.copy()
        copy3 = arr3.copy()

        z = time.process_time()
        merge_sort(copy1, 0, size[x] - 1)
        y = time.process_time()
        time1 = y - z
        z = time.process_time()
        merge_sort(copy2, 0, size[x] - 1)
        y = time.process_time()
        time2 = y - z
        z = time.process_time()
        merge_sort(copy3, 0, size[x] - 1)
        y = time.process_time()
        time3 = y - z

        print(f'{merge:25}', f'{sorted_array:20}', "runtime:", time1)
        print(f'{merge:25}', f'{random_array:20}', "runtime:", time2)
        print(f'{merge:25}', f'{semi_sorted:20}', "runtime:", time3)

        copy1 = arr1.copy()
        copy2 = arr2.copy()
        copy3 = arr3.copy()

        z = time.process_time()
        quick_sort(copy1, 0, size[x] - 1)
        y = time.process_time()
        time1 = y - z
        z = time.process_time()
        quick_sort(copy2, 0, size[x] - 1)
        y = time.process_time()
        time2 = y - z
        z = time.process_time()
        quick_sort(copy3, 0, size[x] - 1)
        y = time.process_time()
        time3 = y - z

        print(f'{quick:25}', f'{sorted_array:20}', "runtime:", time1)
        print(f'{quick:25}', f'{random_array:20}', "runtime:", time2)
        print(f'{quick:25}', f'{semi_sorted:20}', "runtime:", time3)


        print("\n")
time_each_method()




# arr2 = generate_random_arr(100)

# print(arr2)
# selection_sort(arr2)
# print(arr2)

