def histogram(lst):
    for num in lst:
        print("*" * num)
nums = list(map(int, input("Inuput numbers separated by spaces:").split()))
histogram(nums)