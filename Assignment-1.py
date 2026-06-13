print("****************************PROBLEM - 1****************************")
num = 5
list = []

if (num >= 0):
    print(num)

    for i in range(0, num):
        list.append(i**2)

print(list)


print("****************************PROBLEM - 2****************************")

b = []
a = "aaaabbbbbbccccddddd"
for i in a:
    
    b.append(i)


b = dict.fromkeys(b)
b = [*b]



print(b)



print("****************************PROBLEM - 3****************************")

a = [12, 75, 150, 180, 145, 525, 50]
print(a)

for i in a:
    
    if (i % 5 == 0 ):
        
        if (i > 500):
            break

        if (i <= 150):
            
            print(i)


print("****************************PROBLEM - 4****************************")

num = 654
count = 0

while (num > 0):

    rem = num % 10
    num = num // 10
    count += 1

print(count)


print("****************************PROBLEM - 5****************************")

num = 5
temp = 0
ans = 0

for i in range(0, num):
    temp = temp + (2 * 10**i)
    ans = temp + ans
    print(temp)

print(ans)


print("****************************PROBLEM - 6****************************")

num = 65346
rev = 0

while (num > 0):

    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10

print(rev)


print("****************************PROBLEM - 7****************************")

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


for i in range(len(numbers)):

    if (i % 2 != 0 ):
        print(numbers[i])


print("****************************PROBLEM - 8****************************")

numbers = [10, 20, 5]
print(sorted(numbers))
ans = int(len(numbers)/2)

print(numbers[ans])


print("****************************PROBLEM - 9****************************")

def fact(num):

    if (num <=0 ):
        print ("Not a Valid number")
        
    else: 
        ans = 1
        for i in range(1, num + 1):
            
            ans = ans * i

        print(ans)

fact(4)


print("****************************PROBLEM - 10****************************")

word = "pythonlobby"
vowels = 0
consonants = 0

for i in word:

    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):

        vowels += 1

    else:

        consonants += 1

print("Vowels: ", vowels)
print("Consonants: ", consonants)