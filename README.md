### 三元闭包的大数据验证(Big data verification of ternary closure)
dowland Related Paper:[Empirical Analysis of an evolving social network, Science 2006](https://github.com/JeriYang/Verification-of-Ternary-Closure/blob/master/Empirical%20Analysis%20of%20an%20evolving%20social%20network.pdf)<br>
(1) Converting the qualitative description of the ternary closure into an expression of quantitative investigation;<br>
(2) Find the appropriate social network data verification ternary closure principle, you can use the mail tense data of a European research group, [download address](http://snap.stanford.edu/data/email-Eu-core-temporal.html)<br>
(3) Write an algorithm to achieve the following functions:<br>
a) The time interval of each snapshot is determined according to the data itself. Each pair of snapshots si, si+1, k of the network indicates the number of common friends of two people who are not linked in the snapshot snapshot si, and the calculation becomes in the si+1 snapshot. Friend's probability T(k)<br>
b) Calculate 60 T(k) and find the average probability function of the function T(k)<br>
c) Write the program graph to show the average probability function of T(k)<br>
d) According to the calculation results, whether the ternary closure principle is verified<br>

### Some content of this Ternary Closure:
* [***source data and result***](https://github.com/JeriYang/Verification-of-Ternary-Closure/tree/master/source_data_and_result)
  * [source data](https://github.com/JeriYang/Verification-of-Ternary-Closure/raw/master/source_data_and_result/email-Eu-core-temporal.csv)<br>
  .csv file(u, v, t) : u——sender, v——receiver, t——timestap; Sorting t in ascending order<br>
  * [result]<br>
  .csv file get fifty times probability<br>
  * [result_slove]<br>
  .csv file after get aveage from every column in result.csv<br>
* [***code***](https://github.com/JeriYang/Verification-of-Ternary-Closure/tree/master/code)
  * [main.py]
  * [curve_fit.py]
  * [curve_fit2.py]