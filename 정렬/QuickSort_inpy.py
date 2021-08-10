#quicksort를 파이썬 방식으로 비교횟수증가하여 비효율적이지만 코드가 간결하다
array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array)<=1:
        return array

    pivot=array[0]
    tail=array[1:]

    left_side=[x for x in tail if x <= pivot]
    right_side=[x for x in tail if x> pivot]

    return quick_sort(left_side)+ [pivot] + quick_sort(right_side)

print(quick_sort(array))
    
