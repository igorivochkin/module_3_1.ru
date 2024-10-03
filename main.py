# module_3_1.ru

def count_calls():
   global calls
   calls += 1
   return calls

def string_info(string):
    count_calls()
    tuple_ = tuple([len(string), string.upper(), string.lower()])
    return tuple_

def  is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string.lower():
           return True
        else:
           continue
    return False

calls = 0
str_ = 'Эскалибур'
str1_ = 'Конкистадор'
list1_ = ['ban', 'BaNaN', 'urBAN']
list2_ = ['recycling', 'cyclic']
print(string_info(str_))
print(string_info(str1_))
print(is_contains('Urban', list1_))
print(is_contains('cycle', list2_))
print(calls)
