class SwapTwoNumbers():
    def swapTwoNumbers(self):
        a=8
        b=3
        b=a+b
        a=b-a
        b=b-a
        print(f"after swap: {a}, {b}")

if __name__ == "__main__":
    swapTwoNumbersObj = SwapTwoNumbers()
    swapTwoNumbersObj.swapTwoNumbers()


