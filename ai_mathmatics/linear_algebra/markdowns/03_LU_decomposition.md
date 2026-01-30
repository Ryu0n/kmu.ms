# LU 분해 (LU Decomposition)
## LU 분해의 정의
LU 분해는 **Gauss Elimination 을 행렬이라는 자료구조로 표현한 것**을 의미한다.
숫자는 인수분해가 가능하다. 행렬도 숫자와 마찬가지로 분해가 가능하다. 행렬을 분해하는 방법에는 대표적으로 세 가지가 있다.
* LU Decomposition
* QR Decomposition
* SVD (Singular Value Decomposition) : 특이값 분해  

QR Decomposition과 SVD는 직교분할과 관련이 있다.  

LU 분해는 인수분해를 하듯 **Lower triangular matrix**와 **Upper triangular matrix**의 곱으로 분해하는 것이다.  
```
|* * *| LU Decomposition  |* 0 0| |* * *|
|* * *| ----------------> |* * 0| |0 * *|
|* * *|                   |* * *| |0 0 *|
                             L       U
```
이 과정은 실제로 Gauss Elimination의 Forward Elimination과 밀접한 관련이 있다. 
Upper triangular matrix는 **Forward Elimination의 결과물**에 해당하고, 
Lower triangular matrix는 **Forward Elimination을 수행하는 과정**을 행렬로써 표현한 것이다.  

## LU 분해의 장점
**Ax = b** 형태의 linear system이 있다고 가정해보자. 우리의 궁극적인 목표는 *x를 구하는 것*이다.  

A row vector를 LU Decomposition이 가능하다고 가정하면,
**LUx = b** 과 같은 형태로 표현할 수 있다. 결합법칙을 적용하여 **L(Ux) = b**로 표현할 수 있다. Ux를 하나의 벡터 y로 가정하면
**Ly = b**로 정의할 수 있다.  

```
(b는 상수로 이루어진 벡터)

Ax = b
|* * *| |x1|   |b1|
|* * *| |x2| = |b2|
|* * *| |x3|   |b3|

LUx = b
|* * *| LU Decomposition  |* 0 0| |* * *|
|* * *| ----------------> |* * 0| |0 * *|
|* * *|                   |* * *| |0 0 *|
                             L       U

단, Ux = y
|* * *| |x1|   |y1|
|0 * *| |x2| = |y2|
|0 0 *| |x3|   |y3|
              
L(Ux) = b  -> Ly = b
|* 0 0| |y1|   |b1|
|* * 0| |y2| = |b2|
|* * *| |y3|   |b3|
```
위 행렬을 보면 알 수 있듯이 Ly = b 형태를 이용하면, **전방대치법(Forward-substitution)을 통해 y 벡터**를 구할 수 있다.
그리고, **y 벡터를 Ux = y에 실제값으로써 대입하면 x 벡터**도 쉽게 구할 수 있다.  

## LU 분해의 의미
* L : A row vector를 전방소거하는데 쓰인 **replacement와 scaling에 대한 EROs**를 기록한 행렬
* U : A row vector를 전방소거 한 후 남은 **upper triangular matrix**
* P(Permutation) : A row vector를 전방소거하는데 쓰인 **interchange에 대한 EROs**를 기록한 행렬 (Optional)

## LU 분해의 활용
* 수치적 안정성 : 선형시스템 Ax = b의 해를 A^-1을 통해 직접 구하는 것 보다 PLU분해를 사용하는 것이 수치적으로 안정적이다.
* b가 자주 업데이트되는 경우 : 선형시스템 Ax = b에서 A는 고정되어 있고 b가 업데이트되는 경우가 자주 있다.
이런 경우 행렬 A를 PLU로 미리 분해해놓으면 b가 업데이트될때마다 실시간으로 해 x를 구할 수 있다.  
  (y 구할때 forward-substitution, x 구할때 back-substitution)  