class Fibnocci():
    def fibnocciSeries(self, n, store_value):
        if n == 0 or n == 1:
            store_value[n]=n
            return n

        if not store_value and store_value[n]!=-1:
            return store_value[n]

        store_value[n] = self.fibnocciSeries(n - 1, store_value) + self.fibnocciSeries(n - 2, store_value)

        return store_value[n]

if __name__ == "__main__":
    fibnocciObj = Fibnocci()
    n=10
    store_value=[-1]*(n+1)
    fibnocciObj.fibnocciSeries(n, store_value)
    print(f"fibnocci for {n}: {store_value}")
