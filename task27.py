user_str = input('file name: ')
if user_str.endswith('.pdf') or user_str.endswith('.docx') or user_str.endswith('.txt'):
    print(True)
else:
    print(False)


#tuple -> print(user_str.endswith(('.pdf','docx','txt')))