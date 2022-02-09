# URL과 웹 브라우저 요청 흐름

## URL

- Uniform Resource Identifer
- URI? URL? URN?
- "URI는 로케이터(locator), 이름(name) 또는 둘 다 추가로 분류될 수 있다."
- URI(Resource Identifier)
  - URL (리소스의 위치를 지정)
    - 웹 브라우저에 적는 것
  - URN (리소스의 이름을 부여)
    - 이름을 구현
- URI  단어 뜻
  - Uniform : 리소스 식별하는 통일된 방식
  - Resource : 자원, URI로 식별할 수 있는 모든 것(제한 없음)
  - Identifier : 다른 항목과 구분하는 데 필요한 정보
- URL, URN
  - 위치는 변할 수 있지만 이름은 변하지 않는다.
  - URN 이름만으로 실제 리소스를 찾을 수 있는 방법이 보편화 되지 않음
  - URI = URL은 거의 같은 의미로 ...
- URL 문법
  - scheme(스키마) : 프로토콜 정보
  - userinfo, host
  - port
  - path
  - 쿼리 파라미터
- scheme
  - 주로 프로토콜 사용
  - 프로토콜 : 어떤 방식으로 자원에 접근할 것인가 하는 약속 규칙
  - http는 80포트, https는 443 포트를 주로 사용, 포트는 생략 가능
  - https는 http에 보안 추가 (HTTP Secure)

- userinfo
  - URL에 사용자 정보를 포함해서 인증
  - 거의 사용하지 않음
- host
  - 호스트명
  - 도메인 명 또는 IP주소 입력
- PORT
  - 포트
  - 접속 포트
  - 일반적으로 생략
- path
  - 리소스 경로, 계층적 구조
  - ex
    - `/home/file.jpg`

- query
  - key=value 형태
  - ?로 시작, &로 추가 가능 ?keyA=valueA&keyB=valueB
  - 쿼리 파라미터, 쿼리 스트링 등으로 불림, 웹서버에 제공하는 파라미터, 문자 형태
- fragment
  - html 내부 북마크 등에 사용
  - 서버에 전송하는 정보는 아님



## 웹 브라우저 요청 흐름

- 순서
  - DNS 조회
  - HTTPS PORT 생략, 433
  - HTTP 요청 메시지 생성 (웹브라우저가 만드는 전송데이터)
  - 요청 패킷이 구글 서버에 도착하면 패킷을 까서 버리고 HTTP 메시지 꺼내서 해석
  - HTTP 응답 메시지 만듦