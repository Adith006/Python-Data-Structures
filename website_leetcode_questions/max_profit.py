# WRITE MAX_PROFIT FUNCTION HERE #
#                                #
#                                #
#                                #
#                                #
##################################
    
    
def max_profit(prices):
    if len (prices) < 2:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        profit = price - min_price
        
        if profit > max_profit:
            max_profit = profit
        
        if price < min_price:
            min_price = price 
            
    return max_profit
            
    

    

prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [7, 6, 4, 3, 1]
profit = max_profit(prices)
print("Test with descending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [1, 2, 3, 4, 5, 6]
profit = max_profit(prices)
print("Test with ascending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


"""
    EXPECTED OUTPUT:
    ----------------
    Test with mixed prices:
    Prices: [7, 1, 5, 3, 6, 4]
    Maximum profit: 5
    -----------------------------
    Test with descending prices:
    Prices: [7, 6, 4, 3, 1]
    Maximum profit: 0
    -----------------------------
    Test with ascending prices:
    Prices: [1, 2, 3, 4, 5, 6]
    Maximum profit: 5
    -----------------------------

"""