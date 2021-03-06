# HTTP 기본

Hyper Text Transfer Protocol

## 모든 것이 HTTP

- HTTP 메시지에 모든 것을 전송
  - HTML, TEXT
  - IMAGE, 음성, 영상, 파일
  - JSON, XML(API)
  - 거의 모든 형태의 데이터 전송 가능
  - 서버 간에 데이터를 주고 받을 때도 대부분 HTTP 사용
  - 지금은 HTTP 시대!
- HTTP 역사
  - HTTP/1.1 이 가장 중요
    - 가장 많이 사용
    - 우리에게 가장 중요한 버전
    - 이후 버전은 성능 개선 위주
- 기반 프로토콜
  - TCP : HTTP/1.1 , HTTP/2
  - UDP: HTTP/3
  - 현재 HTTP/1.1 주로 사용
    - /2, /3 점점 증가
  - 우리는 1.1의 스펙을 잘 알면 된다
- 특징
  - 클라이언트 서버 구조
  - 무상태 프로토콜(스테이스리스), 비연결성
  - HTTP 메시지
  - 단순함, 확장 가능

## 클라이언트 서버 구조

- Request Response 구조
- 클라이언트는 서버에 요청을 보내고 응답을 대기
- 서버가 요청에 대한 결과를 만들어서 응답
  - 요청
  - 응답 (클라이언트, 서버 분리하는 것이 중요)
    - 비지니스 로직이랑 데이터는 서버에 몰아넣기
    - 클라이언트는 UI, 사용성에 집중
    - 클라이언트와 서버가 독립적으로 발전 가능

## Stateful, Stateless

- 상태 유지 - Stateful, 점원이 중간에 바뀌면?
  - 무엇을? 노트북 상태 유지
  - 몇개를? 노트북 2개 상태 유지
  - 어떻게? 노트북 2개 신용카드 상태 유지
  - 다른 점원으로 바뀌면 원하는 데이터가 사라짐
- 무상태 - Stateless
  - 노트북
  - 노트북 2개
  - 노트북 2개를 신용카드로
  - 점원은 마지막 대화만 가지고도 요청을 처리할 수 있음
  - 점원이 중간에 바뀌어도 쌉가능

- 서버가 클라이언트의 상태를 보존 X

- 장점 : 서버 확장성 높음 (스케일 아웃)

- 단점 : 클라이언트가 추가 데이터 전송

- 상태 유지

  - 중간에 다른 점원으로 바뀌면 안된다..
  - 항상 같은 서버가 유지되어야 한다.
  - 중간에 서버가 장애나면 ..

- 무상태

  - 중간에 다른 점원으로 바뀌어도 된다.

  - 갑자기 고객이 증가해도 점원을 대거 투입

  - 갑자기 클라이언트 요청이 증가해도 서버를 대거 투입할 수 있다.

  - 무상태는 응답 서버를 쉽게 바꿀 수 있다. -> 무한한 서버증설 가능

  - 아무 서버나 호출해도 된다.

  - 중간에 서버가 장애나도 다른 서버로 전달

  - 실무 한계

    - 모든 것을 무상태로 설계 할 수 있는 경우도 있고 없는 경우도 있다.
    - 무상태
      - 로그인이 필요 없는 단순한 서비스 소개 화면

    - 상태유지
      - 로그인
    - 로그인한 사용자의 경우 로그인 했다는 상태를 서버에 유지
    - 일반적으로 브라우저 쿠키와 서버 세션등을 사용해서 상태 유지
    - 상태 유지는 최소한만 사용
    - 최대한 무상태로 설계한다.

## 비 연결성(connectionless)

- 연결 유지하는 모델
  - 요청 응답을 하는 동안 TCP / IP 연결 유지
  - 서버는 연결을 계속 유지, 서버 자원 소모
- 연결 유지하지 않는 모델
  - 요청 응답 끝나면 TCP / IP 연결 종료
  - 최소한의 자원 유지
- HTTP는 기본이 연결을 유지하지 않는 모델
- 일반적으로 초 단위의 이하의 빠른 속도로 응답
- 1시간 동안 수천명이 서비를 사용해도 실제 서버에서 동시에 처리하는 요청은 수십개 이하로 매우 작음
  - ex) 웹 브라우저에서 계속 연속해서 검색 버튼을 누르지는 않는다.
- 서버 자원을 매우 효율적으로 사용할 수 있음
- 한계와 극복
  - TCP / IP 연결을 새로 맺어야 함 - 3 way handshake 시간 추가
  - 웹 브라우저로 사이틀 요청하면 HTML 뿐만 아니라 자바스크립트, css, 추가 이미지 등등 수많은 자원이 함께 다운로드
  - 지금은 HTTP 지속 연결(persistent connections)로 문제 해결
    - 원래는 HTML, 자바스크립트, 이미지 응답 모두 따로 연결, 종료했지만
    - 지속연결을 통해 연결시작후 모든 요청이 끝나면 종료
  - HTTP/2, HTTP/3에서 더 많은 최적화
  - 초기에는 연결, 종료 낭비
  - 지속 연결로 최적화
- 스테이리스를 기억하자
  - 서버 개발자들이 어려워하는 업무
  - 정말 같은 시간에 딱 맞추어 발생하는 대용량 트래픽
  - ex) 선착순 이벤트, 명절 KTX 예약, 학과 수업 등록
  - 수만명 동시 요청

## HTTP 메시지

- 구조
  - 시작 라인
  - 헤더
  - 공백 라인(CRLF)
  - 메시지 바디

- 시작 라인 (요청 메시지)

  - request-line / status-line
  - requset-line = 매서드,  패스, HTTP 버전

  - HTTP 메서드
    - 종류 : GET, POST, PUT, DELETE
    - 서버가 수행해야 할 동작 지정
      - GET : 리소스 조회
      - POST : 요청 내역처리
    - 매우매우 중요
  - 요청 대상
    - 절대경로[?쿼리] (/로 시작하는 경로)
  - HTTP 버전

- 시작 라인 (응답 메시지)

  - request-line / status-line
  - status-line = HTTP 버전 상태코드 이유문구
  - HTTP 상태 코드 : 요청 성공, 실패를 나타냄
    - 200 : 성공
    - 400 : 클라이언트 요청 오류
    - 500 : 서버 내부 오류
  - 이유 문구 : 사람이 이해할 수 있는 짧은 상태 코드 설명 글

- HTTP 헤더

  - 필드 네임: 필드 벨류
  - 필드 네임은 대소문자 구분 없음
  - 용도
    - HTTP 전송에 필요한 모든 부가정보
    - 메시지 바디의 내용, 바디의 크기, 압축, 인증, 요청 클라이언트(브라우저) 정보, 서버 애플리케이션 정보, 캐시 관리 정보
    - 표준 헤더가 너무 많음
    - 필요시 임의의 헤더 추가 가능

- HTTP 메시지 바디

  - 용도
    - 실제 전송할 데이터
    - HTML 문서, 이미지, 영상, JSON 등등 바이트로 표현 가능한 모든 데이터 전송 가능

- 단순함 확장 가능

  - HTTP는 단순하다.
  - 메시지도 매우 단순
  - 크게 성공하는 표준 기술은 단순하지만 확장 가능한 기술

### 