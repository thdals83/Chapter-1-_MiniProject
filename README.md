# Business card Wallet
>두꺼워진 지갑을 가볍게 -!
>지갑 없이 스마트폰만 들고 다니는 시대에 걸맞은
>명함 관리 플랫폼
-----------
### 사이트 주소 : http://ujin16.shop/
### Youtube URL : https://www.youtube.com/watch?v=tin3lPlYfI0
<썸네일 이미지>
------------
## 제작기간 및 팀원소개
* 22년 1월 10일 ~ 22년 1월 13일
* 송민혁 : 명함 등록, 수정, 주소 api
* 김동섭 : 즐겨찾기기능, 검색기능, 리스트정렬
* 양승훈 : 회원가입, ash암호화, bscrypt암호화, jwt인증, 주소 api
* 전유진 : 로그인, hash암호화, bscrypt암호화, jwt인증
------------
## 설계 (와이어프레임)

*로그인 페이지

![KakaoTalk_Photo_2022-01-13-14-08-49](https://user-images.githubusercontent.com/94890646/149269565-90385610-4b02-488b-94cc-e293e4539792.jpeg)


  1. 아이디 입력
    a. 아이디는 이메일 주소
    
  2. 비밀번호 입력
  
  6. 로그인 버튼
    a. 아이디
	* 이메일 형식 확인 메시지 노출
	* 아이디 미입력 메시지 노출
   b. 비밀번호
	* 비밀번호 미입력 메시지 노출
  c. 회원이 아닐 경우
	* 회원이 아니라는 메시지와 함께 회원가입 페이지로 이동
    
  7. 회원가입 버튼 
    a. 이메일 중복 결과 확인
    b. 비밀번호 조건 만족 확인
    c. 비밀번호 일치 확인
    d. 나머지 작성내용 다 적었는지 확인



*회원가입 페이지

![KakaoTalk_Photo_2022-01-13-14-08-59](https://user-images.githubusercontent.com/94890646/149269620-2443a3fe-1a45-45fb-8b26-28f2e73d7397.jpeg)


  1. 아이디 입력
    a. 중복확인 버튼
      * 클릭시 db에 중복이메일 확인
    
  2. 비밀번호 입력
    a. 비밀번호 작성제안 ( 해쉬이용 암호화 저장 )
  
  3. 비밀번호 확인
      
  4. 회사 / 직무 입력

  5. 전화번호 입력
  
  6. 회사 주소 입력
    a. 주소찾기
    
  7. 회원가입 버튼 
    a. 이메일 중복 결과 확인
    b. 비밀번호 조건 만족 확인
    c. 비밀번호 일치 확인
    d. 나머지 작성내용 다 적었는지 확인



*리스트 페이지



  1. 즐겨찾기 리스트
    a. 즐겨찾기 목록 노출
    
  2. 명함 리스트
    a. 등록순 목록 노출 (Default)
  
  3. 명함 등록 버튼
    a. 명합등록 페이지로 이동
      
  4. 삭제 버튼
    * 해당명함 삭제
    
  5. 정렬 select box
    a. 등록순(Default)
    b. 이름순(ㄱㄴㄷ)
    c. 직위
    d. 전화번호
    e. 이메일 주소
    
  6. 로그아웃 버튼
    a. 로그아웃
    
  7. 리스트 아이템
    a. 명함이미지, 소속, 이름, 직위, 전화번호, 이메일 주소 노출
    b. 하나의 아이템 클릭 시 ' 명함 상세 페이지' 이동
    
  8. 즐겨찾기 버튼
    a. 클릭 시 즐겨찾기 등록
    b. 명함 리스트에서 즐겨찾기 리스트로 이동
    c. 재클릭시 - 즐겨찾기 리스트에서 명함 리스트로 이동
    
  9. 검색
    a. 검색 조건 선택 후 검색어 입력 (엔터 or 아이콘 클릭시 검색 리스트 노출)




*명함 수정 / 상세정보 페이지



  1. 닫기
  
  3. 수정
    a. 수정 하고 싶은 정보 입력
    b. 명함 주인에게만 수정 버튼 노출
   
   
   
*명함 등록



  1. 사진등록
    a. 이미지 찾기
    b. 사진 등록
    
  2. 이름 입력
    a. 이름 등록
  
  3. 회사명, 직무 입력
    a. 회사명, 직무 등록
      
  4. 전화번호 입력
    a. 전화번호 등록
    
  5. 회사 주소 찾기
    a. 우편번호로 찾기(api 사용)
    
  6. 상세정보
    a. 상세정보 등록
    
  7. 명함 등록

  8. 닫기
      
 -------------
 ## API
 
| 기능 | Method | URL | Request  | Response |
|:----------|:----------:|:----------:|:---------:|:---------:|
| 로그인 | POST |  api/login|id_give: id, password_give: password | 로그인 완료, token
| 회원가입 | POST | api/newMember| email1: email1, email2: email2, name: name, password1: password1, password2: password2,direct: direct, company: company, role: role, position: position, tel: tel, address: address | 회원가입 완료, '/'
| 이메일 중복 확인 | POST | /validate_email |email: email | 사용 가능한 이메일입니다./이미 존재하는 이메일입니다.
| 명함 상세정보 | POST | api/getcard | 'getcard_id': id| cardinfo
| 명함 수정| POST | api/edit | form_data| 
| 명함 삭제  | POST | /api/list/delete | 'card_id_give': cardId|
| 명함 북마크 클릭  | POST | /api/list/bookmark | 'card_id_give': cardId |
| 명함 등록  | POST | api/pluscard | form_data |
| 명함 정렬  | POST | api/sort | action_give: action | result |
| 명함 북마크 정렬  | POST | api/sort/bookmark | action_give: action | result |
| 명함 검색  | POST | api/search | input_give: input, select_give: select | result |
| 명함 북마크 검색  | POST | api/search/bookmark | input_give: input, select_give: select| result |
---------------

## 사용 기술

--------------

## 핵심 기능
      
      
      
