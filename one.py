# Question 1.
def hello_name(username):
    print('hello: ' + username)
hello_name('youmoh')


# Question 2.
def first_odds():
    for n in  range(1,100):
        if n % 2 == 1:
            print(n)


# Question 3.
def max_num_in_list(list):
    max_num = list[0]
    for number in list:
        if number > max_num:
            max_num = number
    return max_num
print(max_num_in_list([1,55,90,90.1]))


# Question 4.
def is_leap_year(year):
        if year % 4 != 0:
            return False  
        elif year % 100 != 0:
            return True    
        elif year % 400 != 0:
            return False
        else:
            return True
print(is_leap_year(100))



#Quetion 5.
def is_consecutive(numbers):
    numbers.sort()
    for number in range(1,len(numbers)):
        if numbers[number] != numbers[number-1]+1:
            return False
    return True
print(is_consecutive([1,2,3,4,5]))


    

