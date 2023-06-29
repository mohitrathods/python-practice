""""""
"""
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""
class bank():
    def __init__(self):
        self.deposit = 100
        self.withdrawal = 0
        # self.net = self.deposit - self.withdrawal

    def depositfun(self,d):
        self.deposit += d #addmoney and update existing

    def withdrawfun(self,w):
         self.deposit -= w
         self.withdrawal += w

o = bank()

while True:
    print("Enter 1 to withdraw money,'\n' Enter 2 to deposit money,'\n' Press enter to exit")
    ip = int(input("Enter value : "))
    if ip == 1:
        w = float(input("enter amount to withdraw money : "))
        if w > o.deposit:
            print(f"you have not sufficient balance your balance : {o.deposit}")
        else:
            o.withdrawfun(w)
            print(f"total withdraw amount : {o.withdrawal} , total deposit amount : {o.deposit}")
    elif ip == 2:
        d = float(input("enter amount to add money : "))
        o.depositfun(d)
        print(f"total withdraw amount : {o.withdrawal} , total deposit amount : {o.deposit}")
    else:
        break