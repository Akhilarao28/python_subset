# Check if the list is already sorted or not. Ascending or descending
list1=[1,7,37,56,71,99]
ascending=False
descending=False
for i in range(0,len(list1)-1):
    if list1[i]< list1[i+1]:
        ascending=True
    if list1[i]>list1[i+1]:
        descending=True
if ascending==True:
    print("list1 is sorted in ascending")
elif descending==True:
    print("list1 is sorted in descending")
else:
    print("not sorted ")



# Check if an array is a subset of another or not.
list2=[1,3,4,5,7]
list3=[1,9]
flag=False
for i in list3:
    if i not in list2:
        flag=True
        break
if flag==False:
    print("not a subset")
if flag==True:
    print("subset")            

    
# Check if a + b = target exists in a list
list4 = [20, 5, 7, 8, 4,20,5]
list4=list(set(list4))
target = 25
checked=[]
for i in list4:
    for j in list4:
        if i not in checked  and j not in checked:
            if i + j == target:
              print(i+j)
              checked.append(i)
              checked.append(j)
print(checked)      
            