def get_distinct_letters(str1, str2):
    unique_str = ''
    for c in str1:
        unique_str += (c if c not in str2 else '')
    for c in str2:
        unique_str += (c if c not in str1 else '') 
    return ''.join(sorted(unique_str))
    
# print(get_distinct_letters('hello', 'world'))
