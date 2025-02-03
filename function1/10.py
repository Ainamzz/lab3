def unique_elements(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result

numbers = list(map(int, input("Enter numbers: ").split()))
print(unique_elements(numbers))
