# 클라우드 경제성 및 결제
## 주제
### 요금 기본 사항
#### AWS 요금 모델
##### AWS의 3가지 기본적인 비용 발생 요인
1. 컴퓨팅
    * 시간 / 초당(Linux) 청구
    * 인스턴스 유형에 따라 다름

2. 스토리지
    * GB 당 청구

3. 데이터 전송
    * 아웃바운드 요금은 집계하여 청구
    * 인바운드 전송은 무료, 저장도 무료  
      (Amazon EC2에 대한 무료 인바운드 데이터 전송 / 모든 리전내의 AWS 서비스에서 인바운드 전송은 포함안됨)
    * 동일한 리전(지역)간 전송도 무료  
    * 일반적으로 GB당 청구
    
##### 특징
1. 사용한 만큼만 지불
2. 예약 시 더 적은 비용 지불
3. 사용량과 AWS 규모가 증가하면 비용 절감액도 증가  
    3-1. 사용량이 많을수록 비용 절감
    * Amazon Simple Storage Service(S3), Amazon Elastic Block Store(EBS), Amazon Elastic File System(EFS)  
    -> 계층화된 요금제를 사용하는 서비스의 경우 사용량이 늘수록 GB당 지불하는 비용이 줄어든다.  

    3-2. AWS 성장에 따라 더 많은 비용 절감  
    * AWS는 비즈니스 운영 비용을 낮추는 데 중점을 둔다.  
    * 이 방법으로 AWS는 규모의 경제를 통해 절감되는 비용을 고객에게 되돌려준다.

##### AWS 프리티어
AWS 플랫폼, 제품 및 서비스를 무료로 체험할 수 있다. 신규 고객에게는 1년간 무료로 제공된다.  
* Amazon EC2 T2 마이크로 인스턴스를 1년간 무료로 실행 가능
* Amazone VPC
* Elastic Beanstalk**
* Auto Scaling**
* AWS CloudFormation**
* AWS Identity and Access Management (IAM)  

위의 서비스들은 무료로 제공되지만, **이 붙은 서비스들은 프로비저닝한 리소스와 관련된 비용이 발생할 수 있다.
  ex) EC2 인스턴스를 자동으로 조정하는 경우 요금이 부과된다. 다만, Auto Scaling 서비스는 무료이다.

##### Amazon EC2 Reserved Instances
Amazone EC2 예약 인스턴스에 관한 자세한 설명은 아래 링크에서 확인  
https://www.missioncloud.com/blog/optimizing-amazon-ec2-spend-ec2-purchasing-options-programs
* No Upfront payment (NURI)
* Partial Upfront Payment (PURI)
* All Upfront Payment (AURI)

### 총 소유 비용
#### TCO(총 소유 비용)이란?
TCO는 시스템의 직접 및 간접 비용을 확인하는 데 도움이 되는 재정적 추정이다.  

#### TCO를 사용하는 이유
* 온프레미스와 AWS에서 전체 인프라 환경 또는 특정 워크로드를 실행할 때의 비용을 비교하기 위해
* 클라우드로 이전하기 위한 예산을 책정하고 비즈니스 사례를 만들기 위해

#### TCO 고려사항
1번 ~ 3번 공통사항 : 시설비용 (공간, 전력, 냉각)  

1. 서버 비용  
   1-1. 하드웨어  
   서버, PDU(배전 장치), TOR(Top-of-Rack) 스위치  
   1-2. 소프트웨어  
   OS, 가상화 라이선스  
   
   
2. 스토리지 비용  
   2-1. 하드웨어  
   스토리지 디스크, SAN(Storage Area Network), FC(파이버 채널) 스위치  
   2-2. 스토리지 관리 비용  
   
   
3. 네트워크 비용  
   3-1. 네트워크 하드웨어  
   LAN(Local Area Network) 스위치, 로드 밸런서 대역폭 비용  
   3-2. 네트워크 관리 비용  
   
   
4. IT 인건비  
   4-1. 서버 관리 비용  

### AWS 월 사용량 계산기
모든 리전의 모든 서비스에 대한 요금을 합산한다. 월 사용량 계산기는 월별 서비스 비용을 예측하고 비용 절감 기회를 찾고 일반적인 배포 모델의 샘플을 사용하여 서비스 사용량과 관련 파라미터 또는 요금을 비교하는 데 도움이 되는 도구이다.
http://calculator.s3.amazoneaws.com/index.html  

월 사용량 계산기를 사용했을 때 이점
* 월별 비용 추정
* 월별 비용을 줄일 수 있는 기회 파악
* 템플릿을 사용하여 서비스 및 배포 모델 비교


### AWS Organizations
비즈니스 규모에 따라 각 부서 또는 팀에 별도의 AWS 계정을 할당하는 편이 더 쉬울 수 있다. 
각 그룹의 지출과 관련하여 사용 및 비용에 대한 명확하고 정의된 보고서를 확보할 수 있다.
이 경우 개별 계정을 연결하는 서비스가 필요하다. 여러 계정의 통합 결제에 AWS Organizations를 사용한다.  

#### 기능
* 통합 결제 기능
* 조직 보안 관리 기능
   - AWS Identity and Access(IAM)를 사용하여 액세스를 제어
   - IAM 정책을 사용하면 AWS 서비스에 대한 사용자, 그룹 및 역할의 액세스를 허용 및 거부할 수 있다.  
     (사용자, 그룹에 대해서만 제한 / AWS 계정 자체를 제한하지 않음)
   - SCP (Service Control Policy)를 사용하면 AWS 서비스에 대한 OU 내 개인 또는 그 계정의 액세스를 허용 및 거부할 수 있다.
   
* 계정 관리 기능
   - 정책 기반 계정 관리
   - 그룹 기반 계정 관리
   - 계정관리를 자동화하는 API

#### 용어 예시
<img width="490" alt="image" src="https://user-images.githubusercontent.com/32003817/110788691-477b8900-82b2-11eb-95ab-f1ed4a7ea719.png">
OU는 각 조직 단위를 의미하며, 조직의 계정들의 분기점이 된다. 각 계정은 하나의 OU에만 속할 수 있다.

#### 단계별 설정
1. 조직 생성  
   현재 계정을 마스터 계정으로 사용하여 조직을 생성한다. 또한 하나의 AWS 계정을 초대하여 조직에 가입하고 다른 계정을 멤버 계정으로 생성한다.
2. 조직 단위 생성  
   새 조직에 2개의 OU를 생성하고 이러한 OU에 멤버 계정을 배치한다.
3. 서비스 제어 정책 생성  
   멤버 계정의 사용자 및 역할에 위임할 수 있는 작업에 대한 제한을 적용하는 데 사용할 서비스 제어 정책을 생성한다. 서비스 제어 정책은 조직 제어 정책의 한 유형이다.
4. 제한 테스트  
   OU1, OU2와 같은 각 역할에 대한 사용자로 로그인하고 서비스 제어 정책이 계정 액세스에 미치는 영향을 확인한다. 또는 IAM 시뮬레이터를 통해 AWS계정의 IAM사용자, 그룹 또는 역할에 연결된 리소스 기반 정책과 IAM을 테스트하고 문제를 해결할 수 있다.

#### AWS Organizations 액세스
* AWS Management Console
* AWS CLI (Command Line Interface) Tool
* SDK (Software Development Kit)
* HTTPS Query API

### AWS Billing and Cost Management
AWS Billing and Cost Management는 AWS 청구서를 결제하고 사용량을 모니터링하고 비용 예산을 책정하는 데 사용하는 서비스이다.
향후 비용 및 사용량을 예측하고 파악하여 미리 계획을 세울 수 있다. 
사용자가 지정기간을 설정하고 월별 또는 일별 세부 수준에서 데이터를 표시할지 여부를 결정할 수 있다.
필터링 및 그룹화 기능을 사용하면 사용가능한 여러 차원을 사용하여 데이터를 추가로 분석할 수 있다. 
AWS 비용 및 사용 보고서 도구를 사용하면 비용 및 사용량 데이터 추세와 AWS 구현의 사용 현황을 파악하여 최적화 기회를 파악할 수 있다.

<img width="428" alt="image" src="https://user-images.githubusercontent.com/32003817/110793967-8f051380-82b8-11eb-9b20-df487fdbdb73.png">

AWS 결제 대시보드에서는 당월 누계 AWS 비용 상태를 보고 전체 월별 청구서의 대부분을 차지하는 서비스를 식별할 수 있다.
대시보드에 있는 그래프 중 하나는 Spend Summary(비용 요약)이다. Spend Summary에는 지난달의 지출 금액부터 이번 달 현재까지의 AWS 사용에 대한 예상 비용, 이번달의 예상 지출 금액 등이 표시된다.  

또 다른 그래프는 Month-to-Date Spend by Service(서비스별 월-일 사용)로, 가장 많이 사용하는 최상위 서비스와 해당 서비스에 청구되는 비용의 비율을 보여준다.  

#### 도구
결제 대시보드에서 AWS 비용을 추정하고 계획하는 데 사용할 수 있는 다른 여러 비용 관리 도구에 액세스 할 수 있다.
* AWS Bills Page(청구서 페이지)  
<img width="428" alt="image" src="https://user-images.githubusercontent.com/32003817/110794608-439f3500-82b9-11eb-8ed0-7a5c42aff7b5.png">
발생한 비용과 AWS 리전 및 연결 계정별 추가 내역이 나와있다. 이 도구를 사용하면 월 청구서 및 사용하는 AWS 서비스의 세부 내역을 포함하여 비용 및 사용량에 대한 최신 정보에 액세스 할 수 있다.  
  

 * AWS Cost Explorer
<img width="428" alt="image" src="https://user-images.githubusercontent.com/32003817/110795340-0edfad80-82ba-11eb-948d-5ac1dd6d091c.png">
AWS Billing and Cost Management 콘솔에는 AWS 비용 데이터를 그래프로 볼 수 있는 Cost Explorer 페이지가 있다. Cost Explorer를 사용하면 시간 경과에 따른 AWS 비용 및 사용량을 시각화하고 이해하고 관리할 수 있다.  
   

* AWS 예산 (AWS Budget)  
<img width="659" alt="image" src="https://user-images.githubusercontent.com/32003817/110796339-2e2b0a80-82bb-11eb-954e-4de243b19d86.png">
AWS Budget을 사용하여 해당 월의 예산을 초과하는 경우에 대한 알림을 생성할 수 있다. 예산은 월별 분기별 또는 연도별 수준에서 추적할 수 있고 사용자가 시작 및 종료날짜를 지정할 수 있다.
예산 알림은 이메일 또는 Amazon Simple Notification Service(SNS)를 통해 전송될 수 있다.  
  

* AWS 비용 및 사용 보고서 (AWS Reports)  
<img width="473" alt="image" src="https://user-images.githubusercontent.com/32003817/110796122-f3c16d80-82ba-11eb-8dd9-80c2ef3ae4d2.png">
AWS 비용 및 사용보고서는 AWS 비용 및 사용량에 대한 포관적인 정보에 액세스할 수 있는 단일 위치이다. 이 도구는 계정 및 계정 사용자가 시간별 또는 일별 품목에서 사용하는 각 서비스 범주의 사용량과 세금 할당 목적으로 활성화한 모든 세금을 나열한다. 
AWS가 S3 버킷에 결제 보고서를 게시하도록 할 수 있다. 해당 보고서는 하루에 한번만 업데이트 할 수 있다.
  

### AWS 기술 지원 프랜 및 비용 개요
#### AWS Support
* Support Concierge  
계정 지원이 필요한 경우에는 결제 및 계정 전문가인 Support Concierge에게 문의하여 결제 및 계정 문제를 빠르고 효율적으로 분석할 수 있다.  
  
* AWS Trusted Advisor  
AWS 환경에서 모범 사례를 준수하도록 하려면 AWS Trusted Advisor를 사용하면 된다. AWS Trusted Advisor는 맞춤형 클라우드 전문가 같은 역할을 하는 자동화된 서비스이다.  

* TAM (Technical Assistant Manager)  
사전 예방적 지침을 원하는 고객의 경우 AWS Support에서 고객의 기본 담당자로 지정된 기술 지원 관리자 즉, TAM(Technical Assistant Manager)에게 지원을 문의할 수 있다. 
TAM은 지침, 아키텍처 검토 및 지속적 커뮤니케이션을 제공하여 솔루션의 계획, 배포 및 최적화를 위한 정보를 지속적으로 제공하고 필요한 준비를 지원한다. 
기술 지원 관리자는 **Enterprise Support 플랜을 통해서만 이용할 수 있다.**

#### AWS Support Plan
AWS Support는 다음과 같은 4가지 지원 플랜을 제공한다.
* Basic Support  
  Resource Center 액세스, 서비스 상태 대시보드, 제품 FAQ, 토론 포럼 및 상태 확인 지원  
  + Basic 플랜은 무료이며, 계정 및 결제 관련 질문 및 서비스 한도 증가에 대한 지원을 제공한다. 다른 플랜은 장기 계약 없이 월 정액 요금제로 기술 지원 사례를 무제한 제공한다.
  

* Developer Support  
  AWS 기반 초기 개발 지원  
  + Developer Support Plan을 보유한 고객은 모범 사례 지침, 클라이언트 측 진단 도구, 빌딩 블록 아키텍처 지원, AWS 제품, 기능 및 서비스를 유기적으로 활용하는 방법에 대한 지침을 비롯한 추가 기능에 액세스할 수 있다.

  
* Business Support  
  프로덕션 워크로드를 실행하는 고객

  
* Enterprise Support  
  비즈니스 및 미션 크리티컬 워크로드를 실행하는 고객
  
+ Business Support Plan 혹은 Enterprise Support Plan의 경우 AWS Trusted Advisor에 대한 전체 액세스 및 사용 사례 지침을 비롯하여 고급 지원 기능에 액세스할 수 있다. 그리고, 지원 센터 및 Trusted Advisor와 상호 작용할 수 있는 API에 액세스할 수도 있다.
이 API를 사용하면 지원 사례 관리 및 Trusted Advisor 작업을 자동화할 수 있다. Enterprise Support Plan에 한해 기술 계정 관리자, 화이트 글로브 사례 전달, 애플리케이션 아키텍처 지침, 관리 비즈니스 검토, 인프라 이벤트 관리 지원에 액세스할 수 있다.
  
#### 사례 심각도에 따른 Support Plan의 응답시간
<img width="659" alt="image" src="https://user-images.githubusercontent.com/32003817/110860873-ab2ca300-8300-11eb-9b3a-12c0a19a3f39.png">

