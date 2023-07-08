'''
You are given a large integer represented as an integer array digits, where each digits[i]
is the ith digit of the integer. The digits are ordered from most significant to least
significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
'''
def plusOne(digits: list[int]) -> list[int]:
    c = 1
    for i in range(len(digits)-1, -1, -1):
        r = (digits[i] + c)%10
        c = (digits[i] + c)//10
        digits[i] = r
        if i == 0 and c == 1:
            digits.insert(0, 1)

    return digits

digits = [4,3,2]
print(plusOne(digits))
digits = [4,3,2,9]
print(plusOne(digits))
digits = [9,9]
print(plusOne(digits))
