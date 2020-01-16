''' 

Bubble sort compares the current element with the 
next element on the list and if the next element is greater than the
current element, it swaps it

'''
def bubble_sort(sort_list):
    for j in range (len(sort_list)):
        for k in range (len(sort_list) -1):
            if sort_list[k] > sort_list[k+1]:
                 sort_list[k],sort_list[k+1] = sort_list[k+1],sort_list[k]
    print(sort_list) 


list = []
size = int(input("Enter the size of the list "))

for i in range(size):
    elements = input("Enter the elements ")
    list.append(elements)
bubble_sort(list)


