# AlexNet
AlexNet은 2012년에 개최된 **ILSVRC(ImageNet Large Scale Visual Recognition Challenge) 대회의 우승을 차지**한 컨볼루션 신경망(CNN) 구조이다. 
CNN의 부흥에 아주 큰 역할을 한 구조라고 말할 수 있다. AlexNet의 original 논문명은 "ImageNet Classification with Deep Convolutional Neural Networks"이다. 
이 논문의 첫번째 저자가 Alex Khrizevsky이기 때문에 그의 이름을 따서 AlexNet이라고 부른다. 

AlexNet의 기본구조의 특징은 **2개의 GPU로 병렬연산**을 수행하기 위해서 병렬적인 구조로 설계되었다는 점이 가장 큰 변화이다.

## Calculate feature map size
![img_1.png](img_1.png)  
S : 보폭  
H : 이미지의 높이, P : Padding size, Fh = 필터의 높이  
W : 이미지의 너비, P : Padding size, Fw = 필터의 너비  
ex) ((55 + 2*1 - 5) / 2) + 1 = (52 / 2) + 1 = 26 + 1 = 27

## Activation function
AlexNet 이전에 사용되던 활성함수들은 하이퍼볼릭 탄젠트나 시그모이드와 같은 saturating nonlinearities가 사용되었는데
Rectified Linear Unit (ReLU)와 같은 non-saturating nonlinearity 활성함수를 사용하자 학습시간이 비약적으로 빨라졌다.

## Local response normalization (LRN)
신경생물학에서는 lateral inhibition 이라는 현상이 있다. 아래의 사진을 보자.  

![img_5.png](img_5.png)
검은 사각형을 보다보면 흰색 라인에 회색 점이 보이는 현상이 생긴다. (사람이라면) 이러한 현상을 말하는데,
이는 강한 신경세포의 신호가 인접한 신경세포들의 신호에도 영향을 주기 때문이다.
그래서 우리는 해당 커널(강한 신경세포에 대응)과 인접한 커널(주변의 약한 신경세포에 대응)들을 **정규화**시켜주어야 한다.  

![img_6.png](img_6.png)  
이 수식은 LRN을 일반화한 것이다.  
* ai(x, y)는 i번째 커널의 (x, y)에 있는 가중치 값을 의미한다.  
* N은 커널의 수를 의미한다.  
* n은 i번째 커널에 인접한 커널의 수를 의미한다.  

여기서 시그마의 역할이 중요한데, (x, y)가 없다고 생각해보자. j는 **i번째의 인접한 n개의 커널의 범위를 의미하게 된다. (자기자신을 포함)**  
즉, **i번째 커널과 주변의 인접한 n-1개의 커널들의 (x, y)값을들 모아 정규화**하겠다는 의미이다.  

![img_7.png](img_7.png)

## Multiple GPUs
여러대의 GPU로 병렬처리를 하여 연산속도를 높였다.

## Overlapping pooling  
![img_8.png](img_8.png)  
기존의 non-overlapping pooling 방식을 사용할 때는 stride를 커널이 겹치지 않도록 설정했다.
반면, AlexNet에서는 Overlapping max pooling을 진행했는데,
이는 특징을 더 세밀하게 보아 에러율이 낮아지는 장점은 있지만
그만큼 연산량이 늘어나는 단점이 있다.

## Dropout
![img_10.png](img_9.png)  
AlextNet은 기존의 fully-connected 방식이 아닌 Dropout (일종의 규제 기술)을 사용하여
완전 연결된 퍼셉트론을 끊어내어 해당 퍼셉트론의 값을 0으로 치환했다. 이는 overfitting을 방지하는데 
효과가 있고, **테스트 시에는 다시 완전 연결상태로 진행한다.**

## Data argumentation
![img_10.png](img_10.png)  
동일한 이미지들을 조금씩 변형시켜가며 학습하면 Overfitting을 방지하는 데 도움이 된다. 
Data Augmentation에는 이미지를 좌우 반전시키는 Mirroring 기법, 
이미지의 특정 부분을 무작위로 자르는 Random Crops 기법, 
RGB채널을 임의로 바꾸는 PCA Color Augmentation 기법 등이 있다. 
AlexNet을 만든 연구원들은 이러한 방법을 사용하여 데이터 양을 2048배로 늘렸다.

## Overall structure
![img.png](img.png)  
위 그림은 AlexNet의 구조도이다. **5개의 컨볼루션 레이어와 3개의 full-connected 레이어**로 구성되어 있다. 
두번째, 네번째, 다섯번째 컨볼루션 레이어들은 전 단계의 같은 채널의 특성맵들과만 연결되어 있는 반면, 
**세번째 컨볼루션 레이어는 전 단계의 두 채널의 특성맵들과 모두 연결되어 있다.**  

local response normalization는 수렴 속도를 높이기 위해 시행된다.

# VGGNet
VGGNet은 옥스포드 대학의 연구팀 VGG에 의해 개발된 모델로써, **2014년 이미지넷 이미지 인식 대회에서 준우승**을 한 모델이다. 
여기서 말하는 VGGNet은 16개 또는 19개의 레이어로 구성된 모델을 의미한다(VGG16, VGG19로 불림). 
AlexNet과 다른점이 있다면 **병렬적 구조로 이뤄지지 않았다.**  

## Depth
![img_2.png](img_2.png)  
위 그림을 보면 알다시피 VGG 네트워크를 기점으로 **레이어의 깊이가 깊어질수록 에러율이 낮게 보이는 것**을 확인할 수 있다. 
이전까지는 8개의 레이어로 구성이 되었지만 VGG 네트워크부터는 16 혹은 19개의 레이어로 구성이 되고, GoogleNet은 22개, RestNet은 152개의 레이어로 구성이 되었다.

![img_11.png](img_11.png)  
위 도표는 여러가지 구조를 토대로 실험한 것이다. A모델을 보면 11개의 레이어로 구성하였고,
A-LRN모델은 A모델에 LRN을 적용한 것이다. 하지만, 그닥 효과가 있지 않아서 레이어의 깊이를 늘려나가기 시작하자
에러율이 감소하였다.

## Number of weight
VGGNet의 구조를 깊이 들여다보기에 앞서 먼저 집고 넘어가야할 것이 있다. 
그것은 바로 3 x 3 필터로 두 차례 컨볼루션을 하는 것과 5 x 5 필터로 한 번 컨볼루션을 하는 것이 결과적으로 동일한 사이즈의 특성맵을 산출한다는 것이다(아래 그림 참고). 
3 x 3 필터로 세 차례 컨볼루션 하는 것은 7 x 7 필터로 한 번 컨볼루션 하는 것과 대응된다.

![img_3.png](img_3.png)  

그러면 3 x 3 필터로 세 차례 컨볼루션을 하는 것이 7 x 7 필터로 한 번 컨볼루션하는 것보다 나은 점은 무엇일까? 
일단 가중치 또는 파라미터의 갯수의 차이다. 3 x 3 필터가 3개면 총 27개의 가중치를 갖는다. 
반면 7 x 7 필터는 49개의 가중치를 갖는다. CNN에서 가중치는 모두 훈련이 필요한 것들이므로, 가중치가 적다는 것은 그만큼 훈련시켜야할 것의 갯수가 작아진다. 따라서 학습의 속도가 빨라진다. 
동시에 층의 갯수가 늘어나면서 특성에 비선형성을 더 증가시키기 때문에 특성이 점점 더 유용해진다.  

-> 가중치의 수는 필터의 원소 수를 의미한다. (필터는 가중치의 집합이기 때문). 고로 3 x 3 필터(가중치 9개)로 3번의 컨볼루션 연산을 수행하면 27개((9개 * 3 = 27)의 가중치가 나온다.
반면, 7 x 7 필터는 한번밖에 사용하지 않았음에도 불구하고 필터의 변의 길이 제곱이므로 가중치의 수가 기하급수적으로 많아진다. 


## Overall structure
![img_4.png](img_4.png)  


# GoogLeNet
GoogLeNet은 인셉션 모델이라고도 불린다.
인셉션 영화를 보면 마치 몽중몽을 꾸듯, GoogLeNet에서도 네트워크 안에 네트워크가 존재하는 **NIN**(Network in network)의 구조 때문이다.

## Background
2014년 당시, 딥러닝 모델은 일종의 한계에 다달았다. 
일반적으로, 네트워크의 성능을 향상시키는 직관적인 방법은 네트워크의 크기를 늘리는 것이었다. 
이 크기는 보통 넓이와 깊이를 의미하며, **넓이란 곧 노드의 갯수를 뜻한다. 즉 패러미터의 갯수**를 가리킨다. 
**깊이는 레이어의 계층 수**를 말한다.  

그러나 무작정 네트워크의 크기를 늘리는 것이 좋은 것은 아니다. 
**overfitting 현상**이 발생하거나 **컴퓨터의 리소스를 과다하게 점유**하거나 **gradient vanishing**과 같은 문제가 발생할 수도 있다.  

이러한 문제를 해결하기 위해 GoogLeNet 개발자는 **네트워크 구조에 대해 손을 보자**는 결론에 도달했다.

## Inception Module
![img_12.png](img_12.png)  
GoogLeNet은 CNN과 다르게 **MLP(Convolution 연산 후 FC Layer 통과)의 개념**을 차용했다.
Convolution 연산 후에 풀링, 그 후에 FC Layer를 거치는 것을 하나의 모듈로 인식한다. 
이것이 하나의 전체적인 네트워크 구성과 유사하여, **Micro Network**라고도 부른다.

GoogLeNet에서는 MLP와 마찬가지로 **하나의 모듈로 완성되는 구조**를 만들고자 했다. 
잘 작동하는 하나의 모듈을 완성하게 되면, 네트워크는 단순히 모듈의 적층으로 구현될 수 있기 때문이다. 
때문에 이 모듈은 단일 구조로서 네트워크 학습을 이상적으로 구현할 수 있어야만 했다.

Serre는 < Robust object recognition with cortex-Like mechanisms >에서 뉴로사이언스의 영감을 받아 **복수 스케일의 Gabor filter**를 이용하여 네트워크를 구성했다. 
Gabor filter는 사물의 윤곽선을 추출하는 필터다. GoogLeNet에서는 **다양한 스케일의 필터를 활용하여 추상적인 정보를 인식**하고자 하는 점을 이용했다.

![img_13.png](img_13.png)  
때문에 인셉션 모듈에서는 세 종류의 크기를 가진 필터가 사용되었다. 
1x1 Convolution filter는 input image의 공간적 정보를 비교적 잘 담아낼 수 있고, 
3x3과 5x5는 더 추상적이고 퍼져있는 정보를 보존한다.  
(커널의 크기가 넓어질수록 특징을 검출하는 범위가 넓어지기 때문)  

Figure 2의 (b)를 보면 3x3, 5x5 convolutions 에도 1x1 convolutions를 적용할 것을 볼 수 있다.
1x1 convolution를 사용하는 주된 이유는 **차원 감소**다. 1x1 커널을 적용하면 이미지의 사이즈는 줄어들지 않지만 커널수를 줄이면 차원이 감소하여 정보를 압축하여 학습량을 줄일 수 있기 때문이다.

## Overall Structure
![img_14.png](img_14.png)  

GoogleNet 의 주요 구성
* Pre-layer  
  Pre-layer 계층은 초기학습을 위해 존재하는 구간이다. 인셉션 모듈은 저층에서의 학습효율이 떨어지기 때문에, 학습의 편의성을 위해 추가되었다. 이 구간에서는 일반적인 CNN 연산을 거친다.
* Inception Layers  
  ![img_15.png](img_15.png)  
* Global Average Pooling  
  위의 표에서 avg pooling의 output size를 보면 1x1x1024 사이즈가 출력으로 나온 것을 확인할 수 있다.
  이는 FC(Fully-Connected) Layer를 통과한 것과 동일한 효과를 얻을 수 있으며 단순히 pooling 연산이기 때문에 **추가로 파라미터가 발생하지 않는다**는 장점이 있다. 
* Auxiliary Classifier  
  Auxiliary Classifier는 깊은 네트워크의 학습에 대한 우려에 의해 추가되었다. 인셉션 모듈이 아무리 잘 작동한다 하더라도, 깊은 네트워크는 항상 Vanishing Gradient의 위험을 안고 있다. 
  때문에 패러미터의 갱신이 잘 되지 않을 가능성이 존재한다. 이를 피하기 위해, GoogLeNet에서는 연산 도중에 있는 image를 불러들여와 분류한다. 총 두번의 Auxiliary classification이 합쳐져 신경망 학습이 이루어다.  
  이 Auxiliary classifier는 어디까지나 학습의 용이를 위해 마련되었으므로, 학습이 완료된 후엔 네트워크에서 삭제된다.
  
# RestNet
![img_16.png](img_16.png)  
이전까지는 신경망의 깊이를 늘리기만 하면 성능이 좋아지는 줄 알았지만, 
위 표(FC layer)를 보면 단순히 깊이를 늘린다 해서 성능이 좋아지는 것은 아님을 깨달았다.
깊이를 늘리기 위해서는 다른 방법을 사용하여 늘려야 한다.

## Residual Block
![img_17.png](img_17.png)  
![img_18.png](img_18.png)  
RestNet의 핵심개념은 **Residual Block**이다. 입력값을 출력값에 더해줄 수 있도록 지름길(shortcut)을 하나 만들어준 것이다.
그리고 이 과정은 입력을 그대로 전해주는 것이므로 Identity mapping이라고 칭한다.  

기존의 신경망은 입력값 x를 타겟값 y로 매핑하는 함수 H(x)를 얻는 것이 목적이었다. 
그러나 ResNet은 F(x) + x를 최소화하는 것을 목적으로 한다. 
x는 현시점에서 변할 수 없는 값이므로 F(x)를 0에 가깝게 만드는 것이 목적이 된다. 
F(x)가 0이 되면 출력과 입력이 모두 x로 같아지게 된다. 
F(x) = H(x) - x이므로 F(x)를 최소로 해준다는 것은 H(x) - x를 최소로 해주는 것과 동일한 의미를 지닌다. 
여기서 H(x) - x를 잔차(residual)라고 한다. 즉, 잔차를 최소로 해주는 것이므로 ResNet이란 이름이 붙게 된다.  

그리고 역전파(back-propagation)관점에서 보자면 기존의 H(x)를 역전파하기 위해서는 ReLU 함수에 대한 편미분을 진행하지만
F(x) + x에 대해 편미분을 진행하면 덧셈 연산에 대한 편미분만 진행하기 때문에 전체 연산량의 증가 또한 미비하다.

![img_19.png](img_19.png)  
그 뿐만 아니라, Identity mapping을 적용하지 않을 경우 (기존의 ConvNet) 곱의 연산에 대해 forward / back-propagation이 일어나지만,
ResNet과 같은 경우 덧셈에 대해 이를 진행하므로 매우 연산량이 줄어든다. 게다가 이 식을 일반화하여 input(xl)이 에러율에 미치는 영향을 파악해보면
input gradient (1 + ~)가 0이 될 가능성이 낮으므로 gradient vanishing 현상도 방지할 수 있다.  

![img_21.png](img_21.png)  
그 결과 깊이가 늘어나도 생기는 문제의 원인들을 해결하자 깊이가 늘어날수록 성능이 향상되는 것을 확인할 수 있다.

## Overall Structure
![img_20.png](img_20.png)
