import os
c=1
list_made = input("Enter the things you want to do with comma as the next point: ")
splitted = list_made.split(",")
sorted_list = sorted(splitted)

for i in sorted_list:
    print(c, i)
    c+=1