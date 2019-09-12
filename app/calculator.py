def add(*numbers):
    if len(numbers) == 1:
        return numbers
    else:
        result = 0
        for num in numbers:
            result += num
        return result

def multiply(*numbers):
    if len(numbers) == 1:
        return numbers
    else:
        result = 1
        for num in numbers:
            result = result * num
        return result