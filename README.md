# Algorithmic Trading Program: A CSC161 Project

## Synopsis
This project attempts, in three methods, to predict Apple's future stock price based on Apple's stock data for the previous 15 years. 

## First Trading Algorithm
The first analysis will be moving average of the stock data. Assume a user is assigned 1,000 US dollars to invest as the initial principle amount. This program will decide to but stock, sell stock, or take no action based on the average of the stock prices for the previous 20 days (Note: when running the project, the length of time to calcuate the average will be decided by the user).

The program will not take any action during the first 20 days so that it can use them to calcualte the first average. The program will use this average to compare to the 21st day. Then the program will recalculate the average of the 20 days starting at 2 and ending at day 21. This pattern will be repeated until the last day of data.

For example, suppose a user uses 20 days as the benchmark. If the current day stock price is 3.0% lower than the average of the previous 20 days, we buy stocks with all the money we have. If the current day stock price is 2.5% higher than the average of the previous days, we sell all stocks we have. When the algorithm reaches the last day of data, have it sell all remaining stock, if we have any. Then the program will report the total amount of money we are left with.

## Second Trading Algorithm
The second analysis uses the concept of average return. We firstly calculate each day’s return based on the previous day (use Close price for both). Then we calculate the average return by the number of days you choose (all use Close prices). For example, if 20 days are chosen, it calculates the average return of these 20 days. Then it calculates the 21st day’s return with 21st day’s Open price and 20th day’s Close price. Then it compares the average return with 21st day’s return. If the 21st day’s return is lower than the average return,it means that on current day the close price is likely to rise to achieve the past average return. So we buy stocks with all the money. 

If the 21st day’s return is higher than the average return, it means that the current day's open price is even higher than the last day's close price, so we sell. We expect two things here: 
1. the future stock price is going up so we want to keep some stocks. 
2. At this moment, we can make a profit from selling stocks but we don't want to sell all because of reason 1. So we only sell a certain portion of stocks. We use the 21st day’s return as the percentage to calculate the portion of stocks we use to sell. We make a deal in this way each day since 21st day. We sell all remaining stocks on the last day of data.

Note: The purchase only happens when the average return is positive. Because if the past average return is negative,we believe that even if we buy stocks at this moment, we will lose money too.

## Third Trading Algorithm
We purchase as many stocks as possible on the first day and sell on the last. We use the result of this method as comparison to above two methods.

## Interpretations on Plots
### The First Graph
This plots the average price of Close price. The overall trend of stock price is increasing. But we also see a large drop in 2014, which was likely the time to buy a large amount of stocks. However, Method 1 doesn't earn more money than simply purchasing stocks at the beginning and sell them as the end. It may imply that the slope of average Close price may be flatter than the slope of the beginning and the end. But when the number of days is decreasing (say 20 to 2), the profit from Method 1 is increasing. It may imply that the slope of average Close price is exceeding the slope of the beginning and the end.

### The Second Graph
This plots the average return. The average return is quite stable (in between (-20% to 20%)). The Plot can imply that Method 2 based on average return is relatively conservative than Method 1 and Method 3 as well. Therefore, the profit we earn based on the analysis of average return is not as much as that based on method 1. It is the case especially when the number of days to calculate the average is increasing. But when the days are around 20, Method 2 is over Method 1. The reason might be Method 2 which is based on the average return is more conservative than Method 1, so it doesn't earn much money and it doesn't lose a lot of money too.

## Acknowledgments
The first trading algorithm was originally designed and written by William Burke (wburke2@u.rochester.edu)

## Contributor
Shuyu Zhou
