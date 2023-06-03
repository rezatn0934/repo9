def add(number):
    sum = 0
    if number > 0:
        for i in range(0, number + 1):
            sum += i
        else:
            sum += number
        return sum
if __name__ == "__main__":
    number = int(float(input("Enter Number: ")))
    result: int = add(number)
print(result)
