import numpy as np
import scipy.stats

w = [10.7, 11.7, 9.8, 11.4, 10.8, 9.9, 10.1, 8.8, 12.2, 11.0, 11.3,
     11.1, 10.3, 10.0, 9.9, 11.1, 11.7, 11.5, 9.1, 10.3, 8.6, 12.1,
     10.0, 13.0, 9.2, 9.8, 9.3, 9.4, 9.6, 9.2]

# 모평균 검정
# 가설에 의한 모평균
mu = 10.5
# 표본평균
xbar = np.mean(w)
# 표본표준편차
sd = np.std(w, ddof=1)
z = (xbar-mu)/(sd/np.sqrt(len(w)))
print('검정통계량 : ', z)

# 유의수준
alpha = 0.05
# 임계값
cri = scipy.stats.norm.ppf(1-alpha/2)
print('임계값 : ', cri)

A = [31, 33, 29, 28, 25, 32, 32, 34, 26,
     30, 29, 29, 32, 26, 27, 27, 25, 26,
     33, 29, 25, 33, 32, 26, 28, 34, 32,
     29, 33, 30, 30, 31, 26, 28, 28, 32]
mu = 29.5
xbar = np.mean(A)
std = np.std(A, ddof=1)
z = (xbar - mu) / (std / np.sqrt(len(A)))
alpha = 0.05
cri = scipy.stats.norm.ppf(1-alpha)
print('z : ', z)
print('cri : ', cri)
print(z >= cri)
