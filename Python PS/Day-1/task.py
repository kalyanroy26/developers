num_list = [2,3,4,55,72,51,23]

# # prime logic
# def checkPrime(num):
#     fact=0
#     for i in range(2,num):
#         if num%i==0:
#             fact+=1
#             break
#     if fact==0:
#         return num
#     else:
#         return

# # execution i bringing each element from list and checking using prime function
# newList = []
# for ele in num_list:
#     newList.append(checkPrime(ele))

# print(newList)



# problem solving

# 1 strings - string manipulation (index,)
# palindrome,anagram,reverse,substring,longest substring
# number logic - number manipulation
# reverse,palindrome
# 2 prime,armstrong,perfect,fact,fibb
#3 list - element,max,min.sec-max,sort(asc,desc), unique elements, duplicates remove
#4 dict - access 




# number logic
# 146 - 1 oka character 
# how to get a char from a number

# num = 526 

# # name = "kalyan" - it is a collection of characters
# # %

# extraction of a digit - concept
# sum = 0 
# while num!=0: 
#     last_digit = num % 10  
#     sum+=last_digit 
#     num = num//10
# print(sum)

# how you can form a number with a char 1,4,6 - 146

# formation of a number - concept

num = 721  
temp = num
# rev = rev * 10 +last_digit
rev = 0
while num!=0:
    last_digit = num%10
    rev = rev*10 + last_digit
    num = num//10

print(temp)
print(rev)

412 

# sum of a number
# mul of a numer
# reverse a number
# palindrome - 121 

num = num //10 




