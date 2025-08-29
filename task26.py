user_str = input('user name: ')

if user_str.replace('-','').lower().isalnum():
    print(True)
else:
    print(False)