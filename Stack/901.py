# Online Stock Span - Medium
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span

def main():
    # [100, 80, 60, 70, 60, 75, 85] -> Finding prev bigger value, so decreasing monotonic stack
    stockSpanner = StockSpanner()
    
    # Test Case 1
    print(stockSpanner.next(100)) # return 1
    print(stockSpanner.next(80))  # return 1
    print(stockSpanner.next(60))  # return 1
    print(stockSpanner.next(70))  # return 2 [60, 70]
    print(stockSpanner.next(60))  # return 1
    print(stockSpanner.next(75))  # return 4 [60, 70, 60, 75]
    print(stockSpanner.next(85))  # return 6 [80, 60, 70, 60, 75, 85]
    
    # Test Case 2
    # print(stockSpanner.next(31)) # return 1
    # print(stockSpanner.next(41)) # return 2
    # print(stockSpanner.next(48)) # return 3
    # print(stockSpanner.next(59)) # return 4
    # print(stockSpanner.next(79)) # return 5

if __name__ == "__main__":
    main()