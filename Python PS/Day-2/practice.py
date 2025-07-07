# program 1 : max largest or highest number in a list
# list = [-1,-15,-25-35] #max = -1
# max = list[0]  

# for ele in list: 
#     if ele>max: 
#         max = ele


# for i in range(0,len(list)):
#     if list[i]>max:

# print("max:",max)

# max using while 
# list = [5,6,8,10,15,1] 
# i = 0 
# max = list[0] 
# while i<len(list):# length of list
#     if list[i] > max: 
#         max = list[i] 
#     i+=1 
# print("max:",max)


#program - 2 : second max

#methods approach
num_list = [5,6,8,10,15,14,15,1] # max =15 sec = 14

num_list = list(set(num_list)) #convert into set and again convert into list

num_list.sort(reverse=True) #sort the list (set are unordered collection)
# print("max", num_list[0])
# print("sec_max", num_list[1])


#logic approach
# num_list = [5,6,15,15,2] 
# num_list = list(set(num_list))
# max = num_list[0] 
# sec_max = num_list[0] 

# for ele in num_list:
#     if ele > max :  
#         sec_max = max 
#         max = ele  

# print("max", max)
# print("sec_max", sec_max )


#recursion : a function which calls itself unless a condition is met to break
# sum of a number 10 - 1 55
def factorial(n):
    if n==1: #loop break
        return 1
    return n * factorial(n-1)  

print("factorial: ",factorial(10))

#1 - 10 for, while  recursion  #stack - last in first out (push/pop)

def printNum(n): #n - 10 9 8 7 6 5 4 3 2 1
    if n==0: #break
        return 
    # print(n, end=" ") #before function calling  # printing when ele is pushed into stack
    printNum(n-1) 
    print(n, end=" ")

printNum(5) # 5 4 3 2 1 when printing after pushing phase 1 2 3 4 5 
    