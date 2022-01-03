## 21.01.03

# java.util 개요 및 utility 클래스
### java.util 패키지 개요

- java.util 개요
  + java.util은 자바 프로그램을 개발할 때 유용한 기능들을 모아놓은 패키지임
  + Object
    * Data, Calendar : 날짜와 시간 표현 및 조작
    * Vector, HashMap : 배열
    * Formatter : 다양한 형태의 출력 포맷
    * Enumeration : 인터페이스
- java.util 사용
  + java.util 패키지를 이용하면 반복적으로 작성해야 하는 복잡한 코드를 간단하게 구현할 수 있음
    * java.util.Arrays 클래스를 이용하여 간단하게 데이터 정렬이 가능함
      * 배열 내 최고, 최저 점수 출력
      * 배열 오름차순으로 정렬 기능
### 날짜 관련 
- Date 클래스
  + Date 클래스는 형식이 있는 날짜와 시간을 출력하는 클래스임
  + JDK의 버전이 향상되면서 Deprecate 매서드들도 많아짐
    * Deprecate 매서드는 호환성이 떨어지고, 이후 버전에서는 지원되지 않을 수 있으니 사용핮 ㅣ않는 것이 좋음
  + 생성자
    * Date() : 현재의 날짜와 시간을 저장한 객체를 생성함
    * Date(long msec) : 1970년 1월 1일 0시 0분 0초부터 msec를 1/1000초 단위로 하여 경과한 날짜와 시간을 저장한 객체를 생성함
  ```java
  Date currentDate = new Date();
  long start = currentDate.getTime(); // 1970년 1월 1일 0시 0분 0초로부터의 시간이 환산되어 리턴 (직접해보니깐 9시부터 시간인듯)
  statement 1;
  currentDate = new Date();
  long end = currentDate.getTime();
  System.out.println("프로그램 수행에 걸린 시간 : " + (end - start) + "(ms)초");  //getTime의 단위가 ms초이기 때문
  ```
- Calendar 클래스
  + Date 클래스처럼 날짜와 시간에 관한 정보를 출력할 때 사용
  + Calendar 클래스는 추상 클래스이므로 직접 객체 생성 불가
    * getInstance() 매서드를 이용하여 객체 생성 가능
    * ``` Calendar cal = Calendar.getInstance(); ```
  ```java
  Calendar cal = Calendar.getInstance();
	int year = cal.get(Calendar.YEAR);
	int mon = cal.get(Calendar.MONTH)+1;
	int day = cal.get(Calendar.DAY_OF_MONTH);
	int hour = cal.get(Calendar.HOUR_OF_DAY);
	int min = cal.get(Calendar.MINUTE);
	int sec = cal.get(Calendar.SECOND);
  ```
### Formatter 클래스
- Formatter 클래스
  + 형식화된 문자열을 출력하기 위해서 C 언어의 printf()와 같은 기능의 Formatter 클래스를 제공함
  + Formatter 클래스는 형식 문자열을 제공하고, 이 문자열에서 지정한대로 데이터가 형식화되어 출력함
  + ```Formatter formatter = new Formatter(Appendable a); ```
    * Formatter에서 형식화된 문자열을 만들었을 때, 결과가 저장되는 곳임
    * Appendable 인터페이스를 구현한 대표적인 클래스인 StringBuffer
  ```java
  StringBuffer sb = new StringBuffer();
  Formatter formatter = new Formatter(sb);
  ```
     * StringBuffer 클래스의 객체에 대해 Formatter를 지정하는 문장
     * Formatter 객체에서 적용한 출력 포맷 결과가 StringBuffer 객체에 저장됨
  + Formatter format(String format, Object... obj)
    * String 타입의 format 문자열은 출력하고자 하는 문자열 형태로 지정하고, 중간에 %로 시작하는 format을 지정함
    * format 문자열 Object 타입의 가변형 매개변수 개수와 동일해야함
    * 몇 개의 데이터를 형식화된 출력으로 지정할 것인지 사전에 확정할 수 없기 때문에 가변적 매개변수를 사용함
  ```java
  //현재의 시간을 24시간 체계의 시, 분, 초 단위로 표현하기 위해 날짜형 형식화 인자를 사용하는 예
  StringBuffer sb = new StringBuffer();
	Formatter formatter = new Formatter(sb);
	Calendar cc = Calendar.getInstance();
	formatter.format("현재 시간은 %tk : %tM : %tS  %n ", c,c,c);
	System.out.println(formatter.toString());
  ```
# 기본 Collection
### Collection 개요
- 배열의 한계
  * 배열은 한 번 선언하면 배열의 길이가 증가되거나 감소될 수 없음
  * 배열의 크기를 벗어나는 인덱스에 접근하면 java.lang.ArrayIndexOutOfBoundsException이 발생함
  * 사전에 배열의 길이를 알 수 없을 때 Vector와 같은 다양한 Collection 클래스를 지원함
- Vector 클래스 개요
  + 자바는 동적인 길이로 다양한 객체들을 저장하기 위해 Vector 클래스를 제공함
  + Vector는 저장되는 객체들에 대한 참조 값을 저장하는 일종의 가변 길이의 배열
    * 가변 배열에는 객체만 저장이 가능함
    * 가변 크기로서 객체의 갯수를 염려할 필요가 없음
    * 한 객체가 삭제되면 컬렉션이 자동으로 자리를 옮겨줌
  + 다양한 객체들이 하나의 Vector에 저장될 수 있고, 길이도 필요에 따라 자동으로 증가됨
    * Vector() : 10개의 데이터를 저장할 수 있는 길이의 객체를 생성하고, 저장 공간이 부족한 경우 10개씩 증가함
    * Vector(int size) : size 개의 데이터를 저장할 수 있는 길이의 객체를 생성하고, 저장 공간이 부족한 경우 size개 씩 증가함
    * Vector(int size, int incr) : size 개의 데이터를 저장할 수 있는 길이의 객체를 생성하고, 저장 공간이 부족한 경우 incr 개씩 증가함
  ```java
  Vector list = new Vector(3); // 벡터 생성
  list.capacity() // 저장능력 | int 타입
  list.size() // 저장 요소 개수 | int 타입
  list.addElement(new Integer(10)); // 벡터에 새로운 요소 추가
  list.contains("자바"); // list에 자바라는 요소가 있는 지 확인 | boolean 타입
  list.indexOf("자바"); // list에 자바라는 요소가 몇 번 인덱스인지 보여줌 | int 타입
  list.elementAt(i); // i번째 있는 요소 | println 등으로 출력함 
- Enumeration 인터페이스 개요
  + 객체들의 집합(Vector)에서 각각의 객체들을 한 순간에 하나씩 처리할 수 있는 매서드를 제공함
  + 인터페이스이므로 직접 new 연산자를 이용하여 객체를 생성할 수 없음
  + 매서드
    * boolean hasMoreElements() : Vector로부터 생성된 Enumeration의 요소가 있으면 true 아니면 false를 반환함
    * Object nextElemnet() : Enumeration 내의 다음 요소를 반환함
  + Enumeration 인터페이스에 선언된 매서드는 그 인터페이스를 사용하는 클래스로 구현해서 사용해야함
    * Vector 클래스의 elements()라는 매서드에 의해 생성
    * Enumeration 객체 내의 메서드들은 모두 Vector 클래스에서 이미 구현하여 제공
  ```java
  //앞에서 미리 Vector list = new Vector(5); 을 통해 list라는 이름을 갖는 벡터 클래스 생성했다고 가정
  //여기에 add.Element()를 통해 3 객체를 집어 넣음
  Enumeration e = list.elements(); // enumeration 객체를 생성하여 Vector의 요소들을 여기에 복사하여 저장함
  while(e.hasMoreElements())
      System.out.println(e.nextElement());  // 생성된 enumeration 객체 내의 요소 값이 존재하면 그 객체들을 출력함
  ```
- Stack 클래스 개용
  + 스택은 사전적으로 더미,쌓아올림 이라는 의미를 가짐
  + 일종의 쌓여있는 접시들을 생각하면 편하다
  + 제일 마지막에 저장한 데이터를 제일 먼저 꺼내는 __후입선출(LIFO-last in first out)__ 형태의 자료구조
  + top
    + 가장 최근에 입력된 데이터로 삽입, 삭제, 읽기 동작이 발생함
    + 데이터의 수에 따라 유동적으로 변함
    + 데이터가 삽입되면 증가하고, 삭제되면 감소함
  + bottom
    * 가장 먼저 입력된 데이터
    * 0으로 값이 고정되어 있음
  + push
    * top 값을 하나 증가시킨 후, 새로운 데이터를 삽입함
  + pop
    * top이 가리키고 있는 자료 삭제 후, top값을 하나 감소하도록 구현함
  + peek
    * top이 가리키는 데이터를 읽는 작업
    * top값에는 변화 없음
  ```java
  import java.util.Stack;
  Stack<Integer> stack = new Stack<Integer>();
  stack.push(1);
  ```
- Queue 인터페이스 개요
  + 큐는 줄이라는 의미를 가지고 있음
  + 가장 먼저 삽입된 데이터가 가장 먼저 제거되는 __선입선출(FIFO-First In First Out) 형태의 자료구조
  + front : 가장 먼저 입력된 데이터
  + rear : 가장 최근 입력된 데이터
  + front 값이 rear를 추월하게 되면 더 이상 제거할 데이터가 없는 상태, 자료가 하나도 없는 빈 큐임을 의미함
  + 큐에서 front가 가리키는 데이터를 읽는 작업을 peek라고 하며, 데이터를 제거하지 않고 읽는 작업만 수행하므로 front 값을 변경시키지 않음
  ```java
  import java.util.Queue;
  import java.util.LinkedList;
  Queue<String> queue = new LinkedList<String>();
  queue.add("zzz");
  queue.peek();
  queue.poll(); //  출력 메세지 띄우고 싶으면 sysout 필수...!
  ```
### Generics
- Generics를 이용한 Collection API 사용
  - 자바에서 제공하는 다양한 컬렉션들은 다른 타입의 Object들을 저장하고 관리하는 기능을 제공함
  - 하지만 실제 프로그램을 개발할 때는 다른 타입의 데이터를 저장할 일이 거의 없음
  - 오히려 다른 타입의 데이터들을 컬렉션에 저장함으로써 문제가 발생되는 경우도 있음
  - 자바에서 제공하는 컬렉션 객체가 특정 타입의 데이터만 저장하고 사용할 수 있도록 지원함
    + 컬렉션에 저장할 객체의 타입을 제한해서 사용하도록함
      * 타입의 안정성을 제공
      * 타입 체크와 형변환 과정 생략
      * 코드의 간결화
    + 제네릭스를 사용하기 위한 문법
      + 컬렉션<데이터 타입> 변수이름 = new 컬렉션 <데이터타입>(); 
  ```java
  Vector<Integer> list = new Vector<Integer>();  // list 벡터는 integer 타입만 저장이 가능함
  ```
- Collection을 사용하는 확장 for문
  + 배열을 포함한 컬렉션을 쉽게 사용할 수 있도록 향상된 for문을 제공함
  + Collection
    * 요소들을 순차적으로 꺼내기 위해서 Collection에 저장된 요소의 개수를 확인하고, 그 길이 만큼 반복함
    * Enumeration을 이용함
  + for문
    * Enumeration을 사용하지 않고도, Collection에서 요소들을 순차적으로 접근할 수 있음
  + for(데이터타입 접근변수명 : 배열이나 컬렉션 참조변수명){ statement;}
  ```java
  int[] scoreList = {50,44,42,70,77}; // int 타입의 값
  int sum = 0;
  for(int score : scoreList){
      sum = sum + score;
  }
  ```




















