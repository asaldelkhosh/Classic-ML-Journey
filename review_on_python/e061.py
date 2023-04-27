num_list = input('Enter elements of a list separated by space: ').split()
new_list = []

# compare numbers
def compare(x, y):
    return float(x) < float(y)
    
# checking numbers from the list
while num_list:
    min = num_list[0]  
    for x in num_list: 
        if compare(x, min):
            min = x
    new_list.append(min)
    num_list.remove(min)    

print(*new_list)
