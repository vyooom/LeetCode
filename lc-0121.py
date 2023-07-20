'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve
any profit, return 0.
eg: Input: prices = [7,1,5,3,6,4]
Output: 5

'''
'''
# The below code is very basic and has two loops. So it fails on the time consumed test
# Hence we have to design a different algo

def maxProfit(prices: list[int]) -> int:
    max = 0
    i = 0
    while i < len(prices):
        d = 0
        for n in range(i + 1, len(prices)):
            d = prices[n] - prices[i]
            max = d if d > max else max
        i += 1
    return max

'''

def maxProfit(prices: list[int]) -> int:
    if not prices or len(prices) == 1:
        return 0
    maximum_profit = 0
    minimum_price = prices[0]

    for price in prices[1:]:
        maximum_profit = max(maximum_profit, price - minimum_price)
        minimum_price = min(minimum_price, price)

    return maximum_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
