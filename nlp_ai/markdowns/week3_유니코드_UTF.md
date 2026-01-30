참고  
- http://egloos.zum.com/sweeper/v/165351 : 언어판, 유니코드
- https://brownbears.tistory.com/124 : BOM

# 언어판
- 기본적으로 언어판은 256 * 256 = 65,536개의 코드 정의
- 유니 코드(UCS-2)에서는 17개의 언어판이 존재하며, 이들은 Group 00에 존재
- BMP (Basic Mulitilingual Plane) : 유니 코드의 첫 언어판
- 반면, ISO 표준(UCS-4)에서는 128개의 언어판그룹이 존재 
- UCS-4의 각 언어판 그룹에는 258개의 언어판이 존재


# 유니 코드
## 유니코드 Character Set
* UCS-2 (Universal Character Set 2)
  - 2 byte character set (2 바이트로 표현됨)
  - 1개의 언어판 (BMP)을 정의
    
* UCS-4 (Universal Character Set 4)
  - 4 byte character set (4 바이트로 표현됨)
  - 32,768 (=128 * 256) 언어판 정의

## 유니 코드 Basics
- BMP (Basic Multilingual Plane) : 1번째 언어판
- SMP (Supplementary Multilingual Plane) : 2 ~ 17번째 언어판

### 인코딩 방식
- UTF-8
- UTF-16 (BE : Big Endian, LE : Little Endian)
- UTF-32

### BOM (Byte Order Mark)
- 문서 맨 앞에 보이지 않는 특정 바이트를 삽입하여 어떤 인코딩 방식이 사용되었는지 알아내는 방법
- UTF-8 : <EF, BB, BF>
- BE : <FE, FF>
- LE : <FF, FE>

## 유니 코드 한글
- 한글 11,172자 (가 : 0xAC00 ~ 힣 : 0xD7A3)
  
### 자모 코드 (0x31 영역)
- 자음 30자 (0x3131 ~ 0x314E)
- 모음 21자 (0x314F ~ 0x3163)
- 채움코드 : 0x3164
- 옛글 자모 : 0x3165 ~ 0x318E

### 초성-중성-종성 코드 (0x11 영역)
- 초성 19자 (0x1100 ~ 0x1112)
- 중성 21자 (0x1161 ~ 0x1175)
- 종성 27자 (0x11A8 ~ 0x11C2)

## CJKV 한자 코드
- U+3400 ~ U+9FA5
- 한, 중, 일 공통 한자는 1개의 코드 부여
- 음가가 2개 이상인 한자에 대해 하나의 코드만 부여

## 유니코드에서 초성/중성/종성 인식
* 초성  
  (((코드값 - 0xAC00) / 28) / 21) % 19
* 중성  
  ((코드값 - 0xAC00) / 28) % 21
* 종성  
  (코드값 - 0xAC00) % 28

# UTF 인코딩 (Unicode Transformation Format)
## UTF-8
1 ~ 4 바이트로 구현
* 1 Byte 구현  
  ASCII 코드는 1바이트로 구현한다. (MSB = 0)  
  0XXX XXXX
* 2 Byte 구현  
  110X XXXX  
  10XX XXXX
* 3 Byte 구현  
  1110 XXXX  
  10XX XXXX  
  10XX XXXX  
* 4 Byte 구현  
  SMP 영역 (Z비트 : 17 ~ 21 bits)  
  1111 0ZZZ  
  10ZZ XXXX  
  10XX XXXX  
  10XX XXXX  

## UTF-16
2 or 4 바이트로 구현

## UTF-32
4 바이트로 구현