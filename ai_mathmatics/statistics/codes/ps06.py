import numpy as np

# sample mean
samples = [9, 4, 0, 8, 1]
print(np.mean(samples))

# sample mean, standard deviation
w = [10.7, 11.7, 9.8, 11.4, 10.8, 9.9, 10.1, 8.8, 12.2, 11.0, 11.3,
     11.1, 10.3, 10.0, 9.9, 11.1, 11.7, 11.5, 9.1, 10.3, 8.6, 12.1,
     10.0, 13.0, 9.2, 9.8, 9.3, 9.4, 9.6, 9.2]

xbar = np.mean(w)
sd = np.std(w, ddof=1)
print('평균 %.2f, 표준편차 %.2f' %(xbar, sd))

# 신뢰구간 추정
import scipy.stats
alpha = 0.05
zalpha = scipy.stats.norm.ppf(1-alpha/2)
print('zalpha : ', zalpha)
print('min : ', xbar - zalpha*sd/np.sqrt(len(w)), 'max : ', xbar + zalpha*sd/np.sqrt(len(w)))

A = [31, 33, 29, 28, 25, 32, 32, 34, 26,
     30, 29, 29, 32, 26, 27, 27, 25, 26,
     33, 29, 25, 33, 32, 26, 28, 34, 32,
     29, 33, 30, 30, 31, 26, 28, 28, 32]
n = len(A)
xbar = np.mean(A)
std = np.std(w, ddof=1)
alpha = 0.05
zalpha = scipy.stats.norm.ppf(1-alpha/2)
diff = zalpha * std / np.sqrt(n)
section = (xbar - diff, xbar + diff)
print('section : ', section)

# 모비율 추정
x = 48
n = 150
phat = x / n
alpha = 0.05
zalpha = scipy.stats.norm.ppf(1-alpha/2)
sd = np.sqrt((phat * (1-phat))/n)
ci = [phat - zalpha*sd, phat + zalpha*sd]
print('phat %.3f, zalpha %.3f, sd %.3f' %(phat, zalpha, sd))
print(ci)

