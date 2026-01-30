# 행렬연산 (Matrix Operation)
## 행렬 표기법과 관련 용어
```
|3  1|
|1 -2|
|2 -4|
```
다음은 3개의 row(행)과 2개의 column(열)로 이루어진 3 x 2 행렬이다.
각 숫자들은 행렬의 요소(entry)라고 한다.
행렬은 벡터의 리스트로도 볼 수 있다.
  
```
4차원 행 벡터)
|2 1 0 -3|  

2차월 열 벡터)
|1|
|3|
```
행렬은 각 하나의 행(row vector) 혹은 하나의 열(column vector)을 가지고 있는 경우가 있다.

```
|4|
```
1 x 1 행렬은 스칼라이다.

<img width="586" alt="image" src="https://user-images.githubusercontent.com/32003817/111057322-ea5a2000-84c9-11eb-9585-1a7d3cb1ce46.png">

## 벡터 표기법
보통 **소문자 볼드체**로 표기한다.
* 벡터라고 하면 보통 열벡터를 의미한다.
* n-벡터는 n개의 스칼라로 구성된 벡터를 의미한다.

## 전치 행렬 (Transpose Matrix)
m x n 행렬 A에 대한 전치행렬 A^T는 행렬 A의 행을 열로, 열을 행으로 가지는 n x m 행렬이다.
```
    |1 3 5|
A = |     |
    |2 4 6|
    
      |1  2|
A^T = |3  4|
      |5  6|
```

## 영행렬 (Zero Matrix)
행렬의 모든 요소가 0이면 영행렬이라 부르고 O로 표기한다.  
A + O = O + A = A  
영행렬은 **행렬 덧셈연산에 대한 항등원** 역할을 한다.

## 정방행렬 (Square Matrix)
행렬의 행의 갯수와 열의 갯수가 동일한 행렬을 의미한다.
행의 갯수가 n일 경우 n차 정방행렬이라 한다.  
aii(i = 1, 2, ..., n)을 주대각선(main diagonal)이라고 한다.

## 항등행렬 (Identity Matrix)
주대각선의 모든 요소가 1이고 나머지 요소는 0인 n차 정방행렬을 항등행렬이라고 한다.  
항등행렬은 **행렬 곱셈연산에 대한 항등원** 역할을 한다.

## 행렬의 곱
```
     A : m x r            B : r x n           C : m x n
|a11 a12 a13 .. a1r| |b11 b12 b13 .. b1n|   |c11 ... c1n|
| .   .   .  ..  . | | .   .   .  ..  . |   | .  ...  . |
| .   .   .  ..  . | | .   .   .  ..  . | = | .  ...  . |
| .   .   .  ..  . | | .   .   .  ..  . |   | .  ...  . |
|am1  .   .  .. amr| |br1 b12 b13 .. brn|   |cm1 ... cmn|

cij = ai1*b1j + ai2*b2j + ... air*brj
```
행렬 C의 각 요소 cij는 행렬 A의 i번째 행 벡터와 행렬 B의 j번째 열 벡터의 내적(inner product)이다.
행렬의 곱은 **병렬처리로 가속화**할 수 있다.

# 스칼라, 벡터, 행렬, 텐서 계층적 구조 이해하기
## 스칼라 -> 벡터 -> 행렬
스칼라는 숫자 하나로 이루어져 있다.
```
7
```

이 스칼라를 백터로 표현하면 구성요소가 1개인 벡터가 된다.
```
[7]
```

이 스칼라를 행렬로 표현하면 구성요소가 1개인 행렬이 된다.
```
[7]1x1
```

## 벡터 -> 행렬
```
|1|
|2|
|3|
|4|
```
다음과 같은 벡터가 있다고 가정해보자.

```
|1|
|2|
|3|     |1 2|     |1 3|
|4|4x1  |3 4|2x2  |2 4|2x2  |1 2 3 4|1x4  
```
해당 벡터를 행렬로 표현하면 다음과 같이 다양한 모양으로 표현할 수 있다.

## 행렬 -> 벡터
```
|1 2 3|
|4 5 6|2x3

|1|  |1|
|2|  |4|
|3|  |2|
|4|  |5|
|5|  |3|
|6|  |6|
```
위와 같은 2 x 3 행렬을 행 기준으로 혹은 열 기준으로 읽냐에 따라 다음과 같은 벡터로 변환할 수 있다.

## 텐서 (Tensor)
스칼라, 벡터, 행렬을 아우르는 개념이다. 숫자가 **늘어설 수 있는 방향이 k개면 k-텐서**이다.  
* 0-텐서 : 스칼라
* 1-텐서 : 벡터
* 2-텐서 : 행렬

<img width="641" alt="image" src="https://user-images.githubusercontent.com/32003817/111059704-05815b80-84db-11eb-8d77-ea76cd5bd9ed.png">

각 요소가 벡터로써의 형태를 지닐 때, 해당 벡터가 늘어나는 방향을 채널 방향이라고 한다. (R채널, G채널, B채널, Alpha채널)  

<img width="365" alt="image" src="https://user-images.githubusercontent.com/32003817/111060083-c99bc580-84dd-11eb-8560-dd8be235785d.png">  

3-텐서의 대표적인 예는 컬러영상이다. pij가 3-벡터이면 RGB, 4-벡터라면 RGBA 영상이다.  
RGB e.g) p11 = [0, 0, 0]  -->  black  
RGBA e.g) p12 = [255, 255, 255, 80]  -->  white, alpha 80  

4-텐서의 예시로는 동영상이 다. 3-텐서에서 새로운 방향(시간 축)이 추가된 형태이다.

의문) 2-텐서(행렬)를 나열해도 3-텐서를 구성할 수 있는 아닌가?
```
    |m1|
T = |m2|
    |m3|
    
m1~m3는 행렬이라고 전재하면, m1, m2, m3는 R, G, B에 대응할 수 있다.
```

# 분할행렬 (Partitioned Matrix)
<img width="411" alt="image" src="https://user-images.githubusercontent.com/32003817/111060186-61011880-84de-11eb-837d-23cb2558b08e.png">
행렬을 조각단위로 분할하여 생각해도 무방하다. 이런 관점에서 본다면 행렬을 부분행렬(submatrix)로 이루어진 직사각형 구조로 확장해서 생각할 수 있다. 
이렇게 행렬을 구조적인 방법으로 보는 방법을 분할행렬(Partitioned Matrix) 혹은 블록행렬(Block Matrix)라고 한다.

<img width="356" alt="image" src="https://user-images.githubusercontent.com/32003817/111060555-18972a00-84e1-11eb-9538-5144916cedf9.png">  
<img width="727" alt="image" src="https://user-images.githubusercontent.com/32003817/111060594-69a71e00-84e1-11eb-9eca-54aa6fa376e5.png">  
파티션만 잘 나눈다면 이것을 행렬의 곱으로도 확장할 수 있다.  

## 분할행렬로 행렬의 곱 이해하기
### matrix-column vector products
<img width="727" alt="image" src="https://user-images.githubusercontent.com/32003817/111060638-bbe83f00-84e1-11eb-9dc8-27c3fd73505a.png">
행렬 B는 행렬의 곱에서 열을 가져와서 곱해지는 구조이다. 그래서 행렬 B를 행렬이 아닌 컬럼들의 리스트로 해석하면 다음과 같이 표현할 수 있다.  

<img width="520" alt="image" src="https://user-images.githubusercontent.com/32003817/111060679-049ff800-84e2-11eb-8c9f-96fdaca878c6.png">

### row vector-matrix products
<img width="429" alt="image" src="https://user-images.githubusercontent.com/32003817/111060838-2b126300-84e3-11eb-8e38-f6182ea19842.png">
행렬 A는 행렬의 곱에서 행을 가져와서 곱해지는 구조이다. 그래서 행렬 A를 행렬이 아닌 로우들의 리스트로 해석하면 다음과 같이 표현할 수 있다.  

<img width="412" alt="image" src="https://user-images.githubusercontent.com/32003817/111060860-58f7a780-84e3-11eb-81ce-6ef98bd7ee08.png">