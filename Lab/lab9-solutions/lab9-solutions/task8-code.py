def some_sort(L):
     '''(list)->list
     Returns a sorted version of the given list L
     '''
     sorted_list = []
     while L!=[]:
          if L[0] == min(L):
               sorted_list.append(L[0])
               L.pop(0)
          else:
               L.append(L[0])
               L.pop(0)
     return sorted_list


lst=[10,9,8,7,6,5,4,3,2,1]
print(lst)
new_list=some_sort(lst)
print(new_list)
