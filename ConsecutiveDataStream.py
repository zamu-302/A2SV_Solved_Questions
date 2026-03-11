class DataStream:

    def __init__(self, value: int, k: int):
        self.q=[value]
        self.k=k
        self.start=0
        
        

    def consec(self, num: int) -> bool:
        if num==self.q[0]:
            self.start+=1
        else:
            self.start=0
        return self.start>=self.k


# obj = DataStream(value, k)
# param_1 = obj.consec(num)