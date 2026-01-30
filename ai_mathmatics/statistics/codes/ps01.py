import numpy
import scipy
import scipy.stats
import random
import statistics

# 평균
a = [random.randint(0, 100) for i in range(10)]
print(a)
mean_of_a = statistics.mean(a)
print(mean_of_a)

# 중앙값
b = [random.randint(0, 100) for i in range(11)]  # 홀수개
c = [random.randint(0, 100) for i in range(10)]  # 짝수개
# 중앙값은 정렬을 전재로한다.
b = sorted(b)
c = sorted(c)
# 중앙값 추출
print(statistics.median(b))  # 홀수개일 경우 값이 정확히 맞아떨어지기 때문에 정수형태로 나온다.
print(statistics.median(c))  # 반면 짝수개일경우 n/2번째 값과 (n/2)+1번째 값의 평균이기 때문에 소수형태로 나온다.

# 분산
print(statistics.variance(a))  # 표본분산
print(statistics.variance(b))
print(scipy.stats.tvar(a))  # 표본 분산

# 표준편차 / 나누기 N-1
print(statistics.stdev(a))
print(statistics.stdev(b))

# 모분산, 모표준편차 (p=population) / 나누기 N
print(statistics.pvariance(a))
print(statistics.pstdev(a))

# variance, standard deviation in numpy
print(numpy.var(a))  # 모분산
print(numpy.std(a))  # 모표준편차

# ddof = Delta Degrees of Freedom
# N-1의 1에 해당하는 값
print(numpy.var(a, ddof=1))  # 표본분산
print(numpy.std(a, ddof=1))  # 표본표준편차

# 범위
print(max(a) - min(a))
print(numpy.max(a) - numpy.min(a))

# 사분위수
# Quartile은 사분위수라는 뜻이다.
# 그러나 numpy의 qua'n'tile 메소드에는 n% 가 가능하다.
print(numpy.quantile(a, .25))  # 25% (1사분위수), 1/4 위치
print(numpy.quantile(a, .5))  # 50% (중위수), 2/4 위치
print(numpy.quantile(a, .75))  # 75% (3사분위수), 3/4 위
print(numpy.quantile(a, .60))  # 60%에 위치하는 값

# 사분위범위
print(numpy.quantile(a, .75) - numpy.quantile(a, .25))

b = [9, 17, 11, 22, 12, 26, 13, 23, 4, 8, 8, 15]
print('b quantile')
print(numpy.quantile(b, .75) - numpy.quantile(b, .25))

# z-score
print(a)
print(scipy.stats.zscore(a))  # 모집단의 z-score
print(scipy.stats.zscore(a, ddof=1))  # 표본의 z-score
