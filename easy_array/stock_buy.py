arr = [3,4,6,7,9,6,1,3,6,3,5,8]


def stock_price(arr):
    min_price = arr[0]
    profit = 0
    sell_price = 0
    for i in range(len(arr)):
        if arr[i] < min_price:
            min_price = arr[i]
        else:
            current_profit = arr[i]-min_price
            if current_profit > profit:
                profit = current_profit
                sell_price = arr[i]
                
    return min_price, sell_price


if __name__ == "__main__":
    print(stock_price(arr))



