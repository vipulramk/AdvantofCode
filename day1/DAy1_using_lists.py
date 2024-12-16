list1 = [3, 4, 2, 1, 3, 3]
list2 = [4, 3, 5, 3, 9, 3]
list1 = sorted(list1)
list2 = sorted(list2)
list3 = []
for i in range(len(list1)):
    list3.append(abs(list1[i]-list2[i]))
print(sum(list3))

list4 = []
list5 =[]
for val in range(len(list2)):
    # Use list1[val] to access the element correctly and count its occurrences in list2
    list4.append(list2.count(list1[val]))
    list5.append(list4[val] * list1[val])

print(sum(list5))

