class StockSpanner:
    
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        counter = 1
        #print(self.prices)
        if len(self.prices) >= 2:
            #print(f'{price},{self.prices}')
            for i in range(len(self.prices)-2,-1,-1):
                #print(f'{price},{self.prices[i]}')
                if self.prices[i] <= price:
                    counter += 1
                else:
                    break
        return counter



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)