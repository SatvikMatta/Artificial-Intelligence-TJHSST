def problem1(array):
    return array.count(19) == 2 and array.count(5) > 3
#Write a Python program that accept a list of integers and check the length and the fifth element. Return true if the length of the list is 8 and fifth element occurs thrice in the said list.
def problem2(array):
    return len(array) == 8 and array.count(5) == 3
#Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.
def problem3(num):
    return num > 256 and num % 34 == 4
#Write a Python program to test a list of one hundred integers between 0 and 999, which all differ by ten from one another. Return true or false.
def problem6(array):
    for i in range(len(array)):
        if array[i] % 10 != 0:
            return False
    return True
#Write a Python program to check a given list of integers where the sum of the first i integers is i.
def problem7(array):
    for i in range(len(array)):
        if sum(array[:i]) != i:
            return False
    return True
#Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators
def problem8(string):
    words = string.split(' ')
    for word in words:
        if word.contains(','):
            word.replace(',', '')
    separators = []
    for i in string:
        if i == ' ' or i == ',':
            separators.append(i)
    return words, separators



