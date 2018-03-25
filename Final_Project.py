"""CSC 161: Final Project

Algorithmithic Trading Program
      --This programme traces through stock price of Apple Corp. and decides to buy or sell stocks accordingly.

Shuyu Zhou
ID#: 28376996
Lab Section TR 2:00-3:15pm
Fall 2015
"""

def first_last(balance, Close_rev, Open_rev):
        stock = balance/eval(Close_rev[0])
        balance = stock*eval(Open_rev[3663])
        return balance

def reverse(List):
        i = len(List) - 1
        l2 = []
        while i > 0:
                l2.append(List[i])
                i -= 1
        return l2


def mean(days, Close_rev):
        n = days
        sum_close = 0
        average_close = []
        while n < 3664: # 3665-1
                for i in range(n-days, n):
                        sum_close = sum_close + eval(Close_rev[i])
                mean = sum_close/days
                average_close.append(mean)
                n += 1
                sum_close = 0
        return average_close

#####################################################################
def mean_return(days, Close_rev):
        n = days
        sum_return = 0
        average_return = []
        while n < 3664:
                for i in range(n-days+1, n):
                        r = (eval(Close_rev[i])-eval(Close_rev[i-1]))/eval(Close_rev[i-1])
                        sum_return = sum_return + r
                aver = sum_return/(days-1)
                average_return.append(aver)
                n+=1
                sum_return = 0
        return average_return

#####################################################################
def year(date):
    b = []
    for i in range(len(date)):
        x = date[i]
        a = x.split('-')
        b.append(eval(a[0]))
    return b

def removeDuplicates(myList):
    w = []
    i = 1
    w.append(myList[0])
    while i < len(myList)-1:
        if myList[i] != myList[i-1]:
            w.append(myList[i])
        elif myList[i-1] == myList[i]:
            w.append('')
        i += 1
    w.append(myList[len(myList)-1])
    return w

def graph_average_close(days,Date_rev,average_close):
        import numpy as np
        import matplotlib.pyplot as plt
        
        date = Date_rev[days:]
        yrs = year(date)
        y = removeDuplicates(yrs)
        x = range(len(y))
        plt.xticks(x,y)
        plt.figure(1)
        plt.xlabel('Date')
        plt.ylabel('Average Price')
        plt.plot(x, average_close)
        plt.show()
        
def graph_average_return(days,Date_rev,average_return):
        import numpy as np
        import matplotlib.pyplot as plt
        
        date = Date_rev[days:]
        yrs = year(date)
        y = removeDuplicates(yrs)
        x = range(len(y))
        plt.xticks(x,y)
        plt.figure(1)
        plt.xlabel('Date')
        plt.ylabel('Average Return')
        plt.plot(x, average_return)
        plt.show()
        
#####################################################################
class Stock_1:
        def __init__(self, days, average_close, Open, balance, stock, date):
                self.days = days
                self.average_close = average_close
                self.Open = Open
                self.balance = balance
                self.stock = stock
                self.date = date
                self.balance_list = []
                self.stock_list = []

        def get_days(self):
                return self.days
        def get_average_close(self):
                return self.average_close
        def get_Open(self):
                return self.Open
        def get_balance(self):
                return self.balance
        def get_stock(self):
                return self.stock
        def get_date(self):
                return self.date
                
        def compare_1(self):
                
                for i in range(self.days,3663):# list range(1-3665), delete first row gives range(2-3665), transfer to python list range(0,3663)
                        #buy
                        if (eval(self.Open[i]) - self.average_close[i-self.days])/self.average_close[i-self.days] < -0.03 and self.balance != 0:
                                self.stock = self.stock + self.balance/eval(self.Open[i])
                                self.stock_list.append(self.stock)
                                self.balance = 0
                                self.balance_list.append(self.balance)
                        #sell
                        elif (eval(self.Open[i]) - self.average_close[i-self.days])/self.average_close[i-self.days] > 0.025 and self.stock != 0:
                                self.balance = self.balance + self.stock*eval(self.Open[i])
                                self.balance_list.append(self.balance)
                                self.stock = 0
                                self.stock_list.append(self.stock)
                        #no action
                        else:
                                if i == self.days:
                                        self.stock_list.append(self.stock)
                                        self.balance_list.append(self.balance)
                                else:
                                        self.stock_list.append(None)
                                        self.balance_list.append(None)

                                        
                self.balance_list.append(self.balance + self.stock*eval(self.Open[3663]))
                self.stock_list.append(0.0)
                # sell all stocks on the last day
                

                for k in range(self.days,3664):
                        if self.stock_list[k-self.days] != None or self.balance_list[k-self.days] != None:
                            # Skip days without purchasing or selling actions happened
                                s = round(self.stock_list[k-self.days],1)
                                b = round(self.balance_list[k-self.days],1)
                                print("{0}              {1}              {2}".format(self.date[k], s, b))
                return self.balance_list[3663-self.days]


                                
#####################################################################
class Stock_2:
        def __init__(self, days, average_return, Open, balance, stock, date, Close):
                self.days = days
                self.average_return = average_return
                self.Open = Open
                self.balance = balance
                self.stock = stock
                self.date = date
                self.Close = Close
                self.balance_list = []
                self.stock_list = []

        def get_days(self):
                return self.days
        def get_average_return(self):
                return self.average_return
        def get_Open(self):
                return self.Open
        def get_balance(self):
                return self.balance
        def get_stock(self):
                return self.stock
        def get_date(self):
                return self.date
        def get_Close(self):
                return self.Close

        def compare_2(self):

                for i in range(self.days, 3663):
                        daily_return = eval(self.Open[i])/eval(self.Close[i-1])-1
                        # buy
                        if daily_return < self.average_return[i-self.days] and self.balance > 0:
                                # it means that at i, the close price is likely to rise to achieve the past average return, so we buy.

                                if eval(self.Open[i]) > eval(self.Close[i-1]):
                                        # to make sure that buying stocks can have positive returns
                                        self.stock = self.stock + self.balance/eval(self.Open[i])
                                        self.stock_list.append(round(self.stock, 1))
                                        self.balance = self.balance - self.balance
                                        self.balance_list.append(round(self.balance,1))

                                else:
                                        # this means that even though the current return is less than past average return, but since the past average return is negative, we believe that even if we buy stocks at this moment, we will lose money too.
                                        if i == self.days:
                                                self.stock_list.append(round(self.stock,1))
                                                self.balance_list.append(round(self.balance,1))
                                        else:
                                                self.stock_list.append(None)
                                                self.balance_list.append(None)


                        # sell
                        elif daily_return > self.average_return[i-self.days] and self.stock != 0: 
                        # this means that the current day's open price is even higher than the last day's close price, so we sell.
                                if eval(self.Open[i]) > eval(self.Close[i-1]):
                                        # we expect two things here: 
                                        # 1. the future stock price is going up so we want to keep some stocks 
                                        # 2. At this moment, we can make a profit from selling stocks but we don't want to sell all because of reason 1. So we only sell a certain portion of stocks
                                        percent = eval(self.Open[i])/eval(self.Close[i-1]) - 1
                                        sell = self.stock * percent
                                        self.stock = self.stock - sell
                                        self.stock_list.append(round(self.stock,1))
                                        money = sell * eval(self.Open[i])
                                        self.balance = self.balance + money
                                        self.balance_list.append(round(self.balance,1))
                                else:
                                        if i == self.days:
                                                self.stock_list.append(round(self.stock,1))
                                                self.balance_list.append(round(self.balance,1))
                                        else:
                                                self.stock_list.append(None)
                                                self.balance_list.append(None)

                        # no action
                        else:
                                if i == self.days:
                                        self.stock_list.append(round(self.stock,1))
                                        self.balance_list.append(round(self.balance,1))
                                else:
                                        self.stock_list.append(None)
                                        self.balance_list.append(None)

                self.balance = self.balance + self.stock*eval(self.Open[3663])
                self.balance = round(self.balance,1)
                self.balance_list.append(self.balance)
                self.stock_list.append(0.0)


                for k in range(self.days,3664):
                        if self.stock_list[k-self.days] != None or self.balance_list[k-self.days] != None:
                                # Skip days without purchasing or selling actions happened
                                print("{0}              {1}              {2}".format(self.date[k], self.stock_list[k-self.days], self.balance_list[k-self.days]))
                return self.balance_list[3663-self.days]

#####################################################################
def printintro_1():
    print("[Method 1]\nIt calculates the moving average of the data in which the number of days is chosen by you.\nIf the current day stock price is 3.0%  lower than the average of the previous days,\nwe buy stocks with all the money we have.\nIf the current day stock price is 2.5%  higher than the average of the previous days,\nwe sell all stocks we have.\nWe sell all remaining stocks on the last day of data.\n")

def printintro_2():
    print("[Method 2]\nIt uses the concept of average return.\nWe firstly calculate each day’s return based on the previous day.\n(use Close price for both)\nThen we calculate the average return by the number of days you choose.\n(all use Close prices)\nFor example, if 20 days are chosen, it calculates the average return of these 20days.\nThen it calculates the 21st day’s return with 21st day’s Open price and 20th day’s Close price.\nThen it compares the average return with 21st day’s return.\nIf the 21st day’s return is lower than the average return,it means that on current day the close price is likely to rise to achieve the past average return.\nSo we buy stocks with all the money.\nNote:\nThe purchase only happens when the average return is positive.\nBecause if the past average return is negative,we believe that even if we buy stocks at this moment, we will lose money too.\n")
    print("If the 21st day’s return is higher than the average return,it means that the current day's open price is even higher than the last day's close price, so we sell.\nWe expect two things here:\n1. the future stock price is going up so we want to keep some stocks.\n2. At this moment, we can make a profit from selling stocks but we don't want to sell all because of reason 1.\nSo we only sell a certain portion of stocks.\nWe use the 21st day’s return as the percentage to calculate the portion of stocks we use to sell.\nWe make a deal in this way each day since 21st day.\nWe sell all remaining stocks on the last day of data.\n")

def printintro_3():
    print("[Method 3]\nWe purchase as much stock as possible on the first day and sell on the last.\nWe use the result of this method as comparison to above two methods.\n")
#####################################################################
def operate_1(days, average_close, Open_rev, balance, stock, Date_rev):
    s1 = Stock_1(days, average_close, Open_rev, balance, stock, Date_rev)
    print("Date                  # of stocks        Balance")
    print("---------------------------------------------------")
    x = s1.compare_1()
    return x

def operate_2(days, average_return, Open_rev, balance, stock, Date_rev, Close_rev):
    s2 = Stock_2(days, average_return, Open_rev, balance, stock, Date_rev, Close_rev)
    print("Date                  # of stocks        Balance")
    print("---------------------------------------------------")
    y = s2.compare_2()
    return y
                
#####################################################################
def main():
        
        import csv
        f = open('/Users/JoshuaZhou/Documents/2015 FALL/CSC 161/project/InterDayAAPL_2015_07_28to2001_01_03.csv')
        Open = []
        Close = []
        Date = []
        AppleData_f = csv.reader(f)
        for row in AppleData_f:
                Open.append(row[1])
                Close.append(row[4])
                Date.append(row[0])

        Open_rev = reverse(Open)
        Close_rev = reverse(Close)
        Date_rev = reverse(Date)
        f.close()

    #####################################################################  
        print("There are three methods for you to buy and sell stocks: Method 1, Method 2, Method 3.\n")
        printintro_1()
        printintro_2()
        printintro_3()
        days = int(input("How many days you want to use to calculate the past average stock price: "))
        average_close = mean(days, Close_rev)
        average_return = mean_return(days, Close_rev)
        balance = 1000
        stock = 0
    #####################################################################
        # first purchase and last sell
        first_purchase_last_sell = first_last(balance, Close_rev, Open_rev)
        z = first_purchase_last_sell
    #####################################################################
        ask_1 = input("Do you want to try method 1 ('yes' or 'no'):")
        if ask_1 in ['yes','ye','yeah','y','Yes','Ye','Y','Yeah','Of course','sure','why not']:
            x = operate_1(days, average_close, Open_rev, balance, stock, Date_rev)
            ask_2 = input("Do you want to try method 2 ('yes' or 'no'):")
            if ask_2 in ['yes','ye','yeah','y','Yes','Ye','Y','Yeah','of course','sure','why not']:
                y = operate_2(days, average_return, Open_rev, balance, stock, Date_rev, Close_rev)
                print("you earned ${0:0.2f} by method 1".format(x))
                print("you earned ${0:0.2f} by method 2".format(y))
                print("you earned ${0:0.2f} by method 3".format(z))
                print("Method 1 earned ${0:0.2f} more(less) than purchasing as much stock as possible on the first day and selling on the last.".format(x-z))
                print("Method 2 earned ${0:0.2f} more(less) than purchasing as much stock as possible on the first day and selling on the last.".format(y-z))
            else:
                print("you earned ${0:0.2f} by method 1".format(x))
                print("you earned ${0:0.2f} by method 3".format(z))
                print("Method 1 earned ${0:0.2f} more(less) than purchasing as much stock as possible on the first day and selling on the last.".format(x-z))
        else:
            ask_2 = input("Do you want to try method 2 ('yes' or 'no'):")
            if ask_2 in ['yes','ye','yeah','y','Yes','Ye','Y','Yeah','Of course','sure','why not']:
                y = operate_2(days, average_return, Open_rev, balance, stock, Date_rev, Close_rev)
                print("you earned ${0:0.2f} by method 2".format(y))
                print("you earned ${0:0.2f} by method 3".format(z))
                print("Method 2 earned ${0:0.2f} more(less) than purchasing as much stock as possible on the first day and selling on the last.".format(y-z))
            else:
                print('Goodbye!')
  #####################################################################
        # Plot the average price of Close price.
        # The overall trend of stock price is increasing. But we also see a large drop in 2014, which was likely the time to buy a large amount of stocks.
        # However, Method 1 doesn't earn more money than simply purchasing stocks at the beginning and sell them as the end. 
        # It may imply that the slope of average Close price may be flatter than the slope of the beginning and the end.
        # But when the number of days is decreasing (say 20 to 2), the profit from Method 1 is increasing.
        # It may imply that the slope of average Close price is exceeding the slope of the beginning and the end.
        graph_average_close(days,Date_rev,average_close)

        # Plot the average return. The average return is quite stable (in between (-20% to 20%)).
        # The Plot can imply that Method 2 based on average return is relatively conservative than Method 1 and Method 3 as well.
        # Therefore, the profit we earn based on the analysis of average return is not as much as that based on method 1.
        # It is the case especially when the number of days to calculate the average is increasing.
        # But when the days are around 20, Method 2 is over Method 1
        # The reason might be Method 2 which is based on the average return is more conservative than Method 1, so it doesn't earn much money and it doesn't lose a lot of money too.
        graph_average_return(days,Date_rev,average_return)
    
        
if __name__=='__main__':
        main()

    






        
