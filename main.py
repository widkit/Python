# Finding most frequent list index
# Start
from typing import Any, Callable

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
copy_of_numbers = numbers  # holding numbers in copy
numbers.sort()
sorted_value = []

# taking frequency number and value in list
# and deleting calculated values in array
sorted_value.append([numbers.count(numbers[0]), numbers[0]])
del numbers[:numbers.count(numbers[0])]
sorted_value.append([numbers.count(numbers[0]), numbers[0]])
del numbers[:numbers.count(numbers[0])]
sorted_value.append([numbers.count(numbers[0]), numbers[0]])
del numbers[:numbers.count(numbers[0])]
sorted_value.append([numbers.count(numbers[0]), numbers[0]])
del numbers[:numbers.count(numbers[0])]
sorted_value.append([numbers.count(numbers[0]), numbers[0]])
del numbers[:numbers.count(numbers[0])]
sorted_value.append([numbers.count(numbers[0]), numbers[0]])
del numbers[:numbers.count(numbers[0])], numbers
max_freq = max(sorted_value)
print(f"the most frequent number is {max_freq[1]} and it was {max_freq[0]} times repeated")
print("------------------------------------")


def frequent_calc(lst: list):
    lst.sort()
    sorted_value = []
    for item in range(0, len(lst)):
        sorted_value.append([lst.count(lst[0]), lst[0]])
        del lst[:lst.count(lst[0])]
        if len(lst) == item + 1:
            max_freq = max(sorted_value)
            return f"the most frequent number is {max_freq[1]} and it was {max_freq[0]} times repeated"


print(frequent_calc([1, 3, 7, 4, 3, 0, 3, 6, 3]))
print("------------------------------------")

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
print(f"the most frequent number is {max(numbers, key=numbers.count)} and "
      f"it was {numbers.count(max(numbers, key=numbers.count))} times repeated")
# End

# Comfortable Word
# Start
word = set(input('Enter a word(it can contain Turkish words too) :'))
left_hand_words, right_hand_words = set('qazwsxedcrfvtgb'), set('yhnujmıköolçpşğiü')
# print("sağ el kelimesi: ", word - left_hand_words)
# print("sol el kelimesi: ", word - right_hand_words)
print((word - left_hand_words != set()) and (word - right_hand_words != set()))
# End

# Password Reminder
# Start
name = input('Please enter your name :')
if name == 'ahmet':
    print(f"Hello, {name}! The password is : W@12")
else:
    print(f"Hello, {name}! See you later.")
# End

# Covid-19 Risk
# Start
age = input("Are you a cigarette addict older than 75 years old?").strip().lower() == "yes"
chronic = input("Do you have a severe chronic disease?").strip().lower() == "yes"
immune = input("Is your immune system too weak?").strip().lower() == "yes"
# print(f"age: {age} , chronic: {chronic}, immune: {immune}")
if age or chronic or immune:
    print("You are in risky group")
else:
    print("You are not in risky group")

# End

# Changes

