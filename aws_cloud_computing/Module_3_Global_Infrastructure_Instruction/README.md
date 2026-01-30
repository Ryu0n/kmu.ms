# AWS 글로벌 인프라
* AWS 글로벌 인프라는 우수한 품질의 글로벌 네트워크 성능으로 유연하고, 안정적이며, 확장가능하고, 안전한 클라우드 컴퓨팅 환경을 제공하도록 설계되고 구축되었다.
* https://infrastructure.aws 의 맵에서 현재의 AWS 리전과 곧 제공될 더 많은 리전을 볼 수 있다.

## AWS 리전 (Region)
AWS 리전은 **지리적 영역**을 의미한다.
* 리전 간의 데이터 복제는 고객이 제어해야 한다.
  - 한 리전의 리소스는 다른 리전으로 자동 복제되지 않는다.  
  - 특정 리전에 데이터를 저장하는 경우 데이터는 해당 리전 내에서만 복제된다.
* 리전 간 통신에는 AWS 백본 네트워크 인프라가 사용됨
* 각 AWS 리전은 완전한 이중화 및 네트워크 연결을 제공
* 리전은 일반적으로 2개 이상의 가용 영역으로 구성됨
* 가용영역은 하나 이상의 데이터 센터로 구성됨
* AWS 리전은 내결함성 및 안정성을 위해 서로 격리함

2019년 3월 20일 이전에 도입된 리전은 기본적으로 활성화 되어 있으나 그 이후 도입된
아시아 태평양 홍콩, 중동 바레인 등의 리전은 비활성화되어 있는 상태이기 때문에 사용자가 AWS Management Console을 통해 활성화(혹은 비활성화)해주어야 한다.  

AWS GovCloud 리전은 특정 규제 요건에 따라 미국 정부 기관과 고객이 민감한 워크로드를 클라우드로 이전하도록 설계되었다.

### 리전 선택
서비스, 애플리케이션 및 데이터에 적합한 리전을 결정할 때 고려할 요인
* 데이터 거버넌스, 법적 요구사항
* 고객에 대한 근접성 (지연시간)
  - Cloud ping을 통해 리전간의 지연시간을 테스트할 수 있다.
* 리전 내에서 사용가능한 서비스
* 비용 (리전별로 다르다.)

### 가용영역
<img width="386" alt="image" src="https://user-images.githubusercontent.com/32003817/111061937-34063300-84e9-11eb-981a-8e02a6a109f9.png">

* 각 리전에는 다수의 가용영역이 존재한다.
* 각 가용영역은 AWS 인프라의 완전히 격리된 파티션이다.
* 전세계에는 69개의 가용영역이 있다.
* 가용영역은 다수의 데이터센터로 구성되어 있다. (일반적으로 3)
* 내결함성을 갖도록 설계되어 있다.
* 고속 프라이빗 네트워크를 통해 다른 가용 영역과 상호 연결된다.
* 사용할 가용영역을 고객이 선택한다.
* 복원력을 위해 여러 가용영역에 걸쳐 데이터와 리소스를 복제하는 것이 좋다.
* 모든 가용영역은 100km 이내의 거리에 있다.

### 데이터 센터
* AWS 데이터 센터는 보안을 고려하여 설계되었다.
* 데이터 센터는 데이터가 상주하고 데이터가 처리되는 위치이다.
* 각 데이터 센터는 이중화된 전력, 네트워킹 및 연결을 사용하며 별도의 시설에 구축된다.
* 데이터 센터에는 일반적으로 50,000~80,000 대의 물리적 서버가 있다.

AWS는 여러 ODM(Original Device Manufactures) 사용자 지정 네트워킹 장비를 사용한다. 2차 회사의 사용에 따라 ODM 제품을 설계하고 제조한다. 2차 회사에서는 판매를 위해 제품을 리브랜딩한다.

## PoP (Point of Presence)
* AWS는 187개의 PoP로 구성된 글로벌 네트워크를 제공한다.
* 176개의 엣지 로케이션과 11개의 리전 엣지 캐시로 구성된다.
* Amazon CloudFront와 함께 사용된다.
  - Amazon CloudFront : 짧은 지연 시간으로 최종 사용자에게 콘텐츠를 전송하는 글로벌 CDN (Contents Deliver Network)
* 액세스 빈도가 낮은 콘텐츠에서는 리전 엣지 캐시가 사용된다.
* Amazon Route 53 : DNS (Domain Name System)로 서비스 중 하나에 대한 요청은 지연 시간을 줄이기 위해 자동으로 가장 가까운 엣지 로케이션으로 라우팅된다.

## AWS 인프라 기능
<img width="240" alt="image" src="https://user-images.githubusercontent.com/32003817/111062456-328a3a00-84ec-11eb-8e51-f4f59350b2be.png">

* 탄력성 및 확장성
  - 탄력적 인프라, 동적 용량 조정
  - 확장 가능한 인프라 : 성장을 수용할 수 있도록 조정됨    

* 내결함성
  - 장애 발생 시에도 계속해서 제대로 작동
  - 구성 요소의 내장된 이중화    

* 고가용성
  - 높은 수준의 운영 성능
  - 가동 중단 시간 최소화    
  - 인적 개입 없음

# AWS 서비스 및 서비스 범주 개요
## AWS 기초 서비스
![image](https://user-images.githubusercontent.com/32003817/111489302-5912d400-877d-11eb-9d39-34ed090b061e.png)

AWS 글로벌 인프라는 세 가지 요소로 나눌 수 있다.
1. 리전
2. 가용영역
3. 엣지 로케이션을 포함한 Points of Presence

## AWS 서비스 범주
![image](https://user-images.githubusercontent.com/32003817/111489553-937c7100-877d-11eb-93cb-f101b0b73d58.png)
박스친 서비스들이 주로 클라우드 컴퓨팅 서비스에서 가장 널리 사용되는 것들이다.

### 스토리지 서비스
![image](https://user-images.githubusercontent.com/32003817/111489810-d1799500-877d-11eb-918f-6458c28f36b8.png)
* Amazon S3  
  AWS 스토리지 서비스 범주는 확장성, 데이터 가용성, 보안 및 성능을 제공하는 객체 스토리지 서비스이다.
  
* Amazon EBS  
   높은 처리량이 요구되는 트랜잭션 집약적 워크로드에 Amazon EC2와 함께 사용할 수 있다.

* Amazon EFS  
  AWS 클라우드 서비스 및 온프레미스 리소스 내에서 사용할 수 있는 확장 가능하고 탄력적인 완전관리형 네트워크 파일 시스템 (NFS)를 제공한다.

* Amazon Simple Storage Service Glacier  
  데이터 아카이빙 및 장기백업을 위한 안전하고 내구성이 높으며 비용이 매우 저렴한 AWS S3 클라우드 스토리지 클래스이다. 

### 컴퓨팅 서비스  
![image](https://user-images.githubusercontent.com/32003817/111545684-c7758780-87b9-11eb-8807-6a0bf74d0c28.png)
* Amazon EC2  
  AWS 컴퓨팅 서비스에는 크기 조정이 가능한 컴퓨팅 용량을 클라우드의 가상 머신으로 제공하는 Amazon Elastic Compute Cloud.
* Amazon EC2 Auto Scaling  
  정의한 조건에 따라 EC2 인스턴스를 자동으로 추가하거나 제거할 수 있다. 
* Amazon ECS  
  Docker 컨테이너를 지원하는 확장성이 뛰어난 고성능 컨테이너 오케스트레이션 서비스이다. 
* Amazon Elastic Container Registry Service (ECR)  
  개발자가 Docker 컨테이너 이미지를 손쉽게 저장, 관리 및 배포할 수 있게 해주는 완전관리형 Docker 컨테이너 레지스트리이다.
* AWS Elastic Beanstalk  
  Apache 및 Microsoft Internet Information Service (IIS)와 같은 잘 알려진 서버에 웹 애플리케이션 및 서비스를 배포하고 확장할 때 사용되는 서비스다.
* AWS Lambda  
  서버를 프로비저닝 하거나 관리하지 않고도 코드를 실행할 수 있게 해준다. 
* AWS Elastic Kubernetes Service (EKS)  
  AWS에서 Kubernetes를 사용하는 컨테이너식 애플리케이  션을 손쉽게 배포하고 관리하고 확장할 수 있다.
* AWS Fargate  
  서버 또는 클러스터를 관리할 필요 없이 컨테이너를 실행할 수 있는 Amazon ECS용 컴퓨팅 엔진이다.

### 데이터베이스 서비스
![image](https://user-images.githubusercontent.com/32003817/111547011-e117ce80-87bb-11eb-9507-1a1ef519e76f.png)
* AWS Relational Database Service  
  클라우드에 간편하게 설정할 수 있고 확장가능한 관계형 데이터베이스이다. 크기조정이 가능한 용량을 제공하며 하드웨어 프로비저닝, 데이터베이스 설정, 패치적용, 백업과 같은 시간 소모적인 관리작업을 자동화한다.
* AWS Aurora  
  MySQL과 PostgreSQL과 호환되는 관계형 데이터베이스이다. 속도는 표준 MySQL 데이터베이스보다 최대 5배 빠르고 표준 PostgreSQL보다 최대 3배 빠르다. 
* Amazon Redshift  
  Amazon에 로컬로 저장된 페타바이트 규모의 데이터에 대해 분석 쿼리를 실행할 수 있다. 
* Amazon DynamoDB  
  내장된 보안, 백업 및 복원, 인메모리 캐싱을 통해 모든 규모에서 10ms 미만의 성능을 제공하는 완전관리형 키-값 및 문서 NoSQL 데이터베이스이다.

### 네트워킹 및 콘텐츠 전송 서비스 
![image](https://user-images.githubusercontent.com/32003817/111547829-1bce3680-87bd-11eb-9f58-d42a2a678cee.png)
* Amazon Virtual Private Cloud (VPC)  
  AWS 클라우드의 논리적으로 격리된 섹션을 프로비저닝하여 정의된 가상 네트워크에서 AWS 리소스를 시작할 수 있다.
* Amazon Load Balancing  
  수신되는 애플리케이션 트래픽을 Amazon EC2 인스턴스, 컨테이너, IP주소 및 Lambda 함수와 같은 여러 대상에 자동으로 분산한다. 
* Amazon CloudFront   
  짧은 지연시간과 빠른 전송속도로 데이터, 동영상, 애플리케이션 및 API를 전세계 고객에게 안전하게 전송하는 고속 콘텐츠 전송 네트워크(CDN) 서비스이다.
* Amazon Transit Gateway  
  고객이 Amazon Virtual Private Cloud 와 은프레미스 네트워크를 중앙에서 관리하는 단일 게이트웨이에 연결할 수 있다.
* Amazon Route 53  
  최종 사용자를 인터넷 애플리케이션으로 라우팅하는 안정적인 수단을 제공하도록 설계된 확장형 클라우드 DNS (Domain Name System) 웹서비스이다. 이 서비스는 URL을 컴퓨터의 상호연결에 사용되는 숫자 IP주소로 변환한다.
* AWS Direct Connect  
  데이터센터 또는 사무실에서 AWS로 연결되는 전용 프라이빗 네트워크 연결을 설정하는 기능을 제공하므로 비용을 대폭 줄이고 대역폭 처리량을 늘릴 수 있다. 
* AWS VPN  
  네트워크 또는 디바이스에서 AWS 글로벌 네트워크로 연결되는 보안 브라이빗 터널을 제공한다.

### 보안, 자격 증명 및 규정 준수 서비스 
![image](https://user-images.githubusercontent.com/32003817/111549161-1540be80-87bf-11eb-82e7-4e4e5b1cd909.png)
* AWS IAM  
  AWS 서비스와 리소스에 대한 액세스를 안전하게 관리할 수 있는 서비스이다.
* AWS Organizations  
  계정에서 허용되는 서비스와 작업을 제한할 수 있다.
* AWS Cognito  
  웹 및 모바일 앱에 사용자 인증 및 액세스 제어 기능을 추가할 수 있다.
* AWS Artifact  
  AWS 보안 및 규정 준수 보고서와 일부 온라인 계약에 대한 온디맨드 액세스를 제공한다.
* AWS Key Management Service(KMS)  
  암호화 키를 생성하고 관리할 수 있다.
* AWS KMS  
  애플리케이션에서 다양한 AWS 서비스에 대한 암호화 사용을 제어할 수 있다.
* AWS Shield  
  AWS에서 실행되는 애플리케이션을 보호하는 관리형 DDoS 공격방지 서비스이다.

### AWS 비용 관리 서비스
![image](https://user-images.githubusercontent.com/32003817/111549825-3655df00-87c0-11eb-9cb0-0e882ea238d4.png)
* AWS 비용 및 사용 보고서  
  AWS 서비스 요금 및 예약에 대한 추가 메타데이터를 비롯하여 사용가능한 가장 포괄적인 AWS 비용 및 사용량 데이터 세트를 포함한다.
* AWS 예산  
  AWS 비용 및 사용량이 예산 금액을 초과하거나 초과할 것으로 예상될 때 알려주는 사용자 지정 예산을 설정할 수 있다.
* AWS Cost Explorer  
  사용이 쉬운 인터페이스를 통해 시간 경과에 따른 AWS 비용 및 사용량을 시각화하고 파악하고 관리할 수 있다.

### 관리 및 가버넌스 서비스
![image](https://user-images.githubusercontent.com/32003817/111630072-507dd480-8835-11eb-9811-908909ef7de0.png)
* AWS Management Console  
  AWS 계정에 액세스하기 위한 웹 기반 UI (사용자 인터페이스) 서비스이다.
* AWS Config  
  리소스 인벤토리 및 변경사항을 추적하는데 유용하다.
* AWS Auto Scaling  
  수요에 따라 여러 리소스를 확장할 수 있는 기능을 제공한다.
* AWS CloudWatch  
  리소스와 애플리케이션을 모니터링할 수 있다.
* AWS Command line interface  
  AWS 서비스를 관리하는 통합 도구를 제공한다.
* AWS Trusted Advisor  
  AWS 모범 사례를 바탕으로 성능과 보안을 최적화 하는데 유용한 온라인 도구이다. 
* AWS Well-Architect Tool  
  워크로드를 검토하고 개선하는데 도움이 된다.
* AWS CloudTrail  
  AWS 계정 전체에서 사용자 활동 및 API 사용을 추적한다.
