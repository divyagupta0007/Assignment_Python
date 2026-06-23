
print("****************************PROBLEM - 1****************************")

nums = [-1, 0, 1, 2, -1, -4]
nums.sort() 
result = []
    
for i in range(len(nums) - 2):
    
    if i > 0 and nums[i] == nums[i-1]:
        continue
            
    left = i + 1
    right = len(nums) - 1
        
    while left < right:
        total = nums[i] + nums[left] + nums[right]
            
        if total == 0:
            result.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1
                
            while left < right and nums[left] == nums[left - 1]: left += 1
            while left < right and nums[right] == nums[right + 1]: right -= 1
                
        elif total < 0:
            left += 1  
        else:
            right -= 1

print(result)


print("****************************PROBLEM - 2****************************")

num = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

for i in range(len(num)):

    for j in range(len(num) - 1 - i):

        if ((num[j] > 0) and (num[j+1] < 0)):

            temp = num[j]
            num[j] = num[j+1]
            num[j+1] = temp


print(num)


print("****************************PROBLEM - 3****************************")

num = [1, 5, 7, -1]
sum = 6
count = 0
n = len(num)

for i in range(len(num)):

    for j in range(i + 1, n):


        if (((num[i] + num[j]) == sum)):

            print(num[i], num[j])
            count += 1

print(count)


print("****************************PROBLEM - 4****************************")

num = [3, 4, 1, 9, 56, 7, 9, 12] 
m = 5
n = len(num)

min_diff = 9999
print(min_diff)

num.sort()
print(num)

for i in range(n - m + 1):

        
    diff = num[i + m - 1] - num[i]
    if (diff < min_diff):
        min_diff = diff

print(min_diff)


print("****************************PROBLEM - 5****************************")

num = 3749

roman_mapping = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]
    
result = ""

for value, symbol in roman_mapping:

    while num >= value:

        result += symbol
        num -= value
            
   

print(result)


print("****************************PROBLEM - 6****************************")

symbol = "MCMXCIV"

roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
total = 0
    
for i in range(len(symbol)):
    
    if i + 1 < len(symbol) and roman_values[symbol[i]] < roman_values[symbol[i+1]]:
        
        total -= roman_values[symbol[i]]
    
    else:
    
        total += roman_values[symbol[i]]
            

print(total)


print("****************************PROBLEM - 7****************************")

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matrix)
n = len(matrix)

print("\n\n")

for i in range(n):

    for j in range(i + 1, n):

        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix[j])

print("\n\n")

for i in range(n):
    matrix[i].reverse()

print("\n\n")

for i in matrix:
    print(i)

# 7 4 1
# 8 5 2
# 9 6 3