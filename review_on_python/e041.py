# function for checking username have at least 1 alpha
def english(username):
    for x in username:
        if x.isalpha() == True:
            return True
    return False

# checking tht half of the content is alpha
def Half_english(message):
    list1 = 0
    for x in message:
        list1 += x.isalpha()
    return list1 > len(message) / 2 

valid_username = english(input("Enter your username: "))
valid_content = Half_english(input("Enter your message: ")) 

if valid_username and valid_content:
    print('Not spam')
elif not valid_username and valid_content:
    print('Invalid sender')
elif valid_username and not valid_content:   
    print('Invalid content')
else:
    print('Invalid')  