def computeAverage(numbers):
    total = 0
    count = 0
    for i in range(0, 9 + 1, 1):
        num = numbers[i]
        if num == 0:
            pass
        else:
            total = total + num
            count = count + 1
    average = float(total) / count
    
    return average

# Main
numbers = [0] * (10)

i = 0
while i < 10:
    numbers[i] = int(input())
    i = i + 1
average = computeAverage(numbers)
print("The average is: " + str(average))
