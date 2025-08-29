user_str = input('string: ')
if not user_str.startswith('@') and user_str.endswith('.com'):
    print(True)
else:
    print(False)