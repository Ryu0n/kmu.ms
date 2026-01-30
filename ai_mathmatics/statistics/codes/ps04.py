from scipy import stats

# 랜덤박스에서 3개의 공을 뽑았을 때 꽝이 아닐 확률은 0.2
# 최소 한번은 성공할 확률은?
p = stats.binom.cdf(0, n=3, p=0.2)
print(1-p)
mean_binom, var_binom = stats.binom.stats(n=3, p=0.2)
print(f'mean : {mean_binom}')
print(f'var : {var_binom}')

# X~N(4, 3^2), P[X<=4]
p = stats.norm.cdf(4, loc=4, scale=3)  # (Z 정규화) X = 4, 평균 = 4, 표준편차 = 3
print(p)

# X~N(4, 3^2), P[4<=X<=7]
p = stats.norm.cdf(7, loc=4, scale=3) - stats.norm.cdf(4, loc=4, scale=3)
print(p)

# Poisson distribution
p = stats.poisson.cdf(2, mu=3)  # x=2, mean=3
print(p)

# exponential distribution
lam = 3
p = stats.expon.cdf(0.5, scale=1/lam)  # x=0.5, scale=표준편차(1/lambda)

lam = 60
p = stats.expon.cdf(2/lam, scale=1/lam)
print('expon : ', p)

# import numpy as np
# r = np.random.rand(3)
# print(r*10, type(r))
