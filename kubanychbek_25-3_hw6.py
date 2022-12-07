def first_word(words):
    if type(words) == str:
        first_word = words.split()
        return  first_word[0]
    if type(words) != str:
        return  False
print(first_word('Hello world'))
print(first_word(13))

def count_average(*args):
    count_average = sum(args) / len(args)
    return count_average
print(count_average(4,6,7, 8,9))


def password_true(password):
     if len(password) >= 6 and not password.isdigit() and not password.isalpha():
         return  True
     else:
         return  False
print(password_true('hgkueq419'))
print(password_true('qwer'))
