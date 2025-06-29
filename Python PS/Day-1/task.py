# program to print only primes from a given list 
num_list = [2,3,4,55,72,51,23]

# prime logic
def checkPrime(num):
    fact=0
    for i in range(2,num):
        if num%i==0:
            fact+=1
            break
    if fact==0:
        return num
    else:
        return

# execution
newList = []
for ele in num_list:
    val = checkPrime(ele)
    if val is not None: #corrected logic for None error
        newList.append(val)

print(newList)


# program to digits in a number
num = 526 
sum = 0 
while num!=0: 
    last_digit = num % 10  
    sum+=last_digit 
    num = num//10
print(sum)

# program to reverse a number
num = 721  
temp = num
rev = 0
while num!=0:
    last_digit = num%10
    rev = rev*10 + last_digit
    num = num//10

print(temp)
print(rev)   
