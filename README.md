# Python

## 1. Ch01

- 1-1.파이썬 hello world 실습
    
    ```python
    """
    날짜 : 2023/01/02
    이름 : 서정현
    내용 : 파이썬 hello world 실습
    """
    
    print('Hello World!')
    print('Hello Python!')
    print('안녕하세요. 파이썬!')
    ```
    

## 2. Ch02

- 2-1.파이썬 변수 실습
    
    ```python
    """
    날짜 : 2023/01/02
    이름 : 서정현
    내용 : 파이썬 변수 실습
    """
    
    var1 = 1
    var2 = 2
    var3 = var1 + var2
    print('var3 :', var3)
    
    var1 = 10
    var2 = 20
    var3 = var1 + var2 
    print('var3 :', var3)
    ```
    
- 2-2.파이썬 자료형 실습
    
    ```python
    """
    날짜 : 2023/01/02
    이름 : 서정현
    내용 : 파이썬 자료형 실습
    """
    
    # 정수형
    var1 = 1
    var2 = 2
    var3 = 3
    
    print('var1 :', var1)
    print('var2 :', var2)
    print('var3 :', var3)
    print('var1 type :', type(var1))
    print('var2 type :', type(var2))
    print('var3 type :', type(var3))
    
    # 실수형
    var4 = 0.4
    var5 = 1.123456789
    
    print('var4 :', var4)
    print('var5 :', var5)
    print('var4 type :', type(var4))
    print('var5 type :', type(var5))
    
    # 논리형
    var6 = True
    var7 = False
    
    print('var6 :', var6)
    print('var7 :', var7)
    print('var6 type :', type(var6))
    print('var7 type :', type(var7))
    
    # 문자열
    str1 = 'A'
    str2 = 'Apple'
    str3 = "Apple"
    str4 = "사과"
    
    print('str1 :', str1)
    print('str2 :', str2)
    print('str3 :', str3)
    print('str4 :', str4)
    print('str1 type :', type(str1))
    print('str2 type :', type(str2))
    print('str3 type :', type(str3))
    print('str4 type :', type(str4))
    ```
    
- 2-3.파이썬 연산자 실습
    
    ```python
    """
    날짜 : 2023/01/02
    이름 : 서정현
    내용 : 파이썬 연산자 실습
    """
    
    # 대입 연산자
    a = 1
    b = c = d = 0
    e, f, g = 7, True, 'Apple'
    
    print('a :', a)
    print('b :', b)
    print('c :', c)
    print('d :', d)
    print('e :', e)
    print('f :', f)
    print('g :', g)
    
    # 산술 연산자
    num1 = 1
    num2 = 2
    num3, num4 = 3, 4
    
    r1 = num1 + num2
    r2 = num1 - num2
    r3 = num2 * num3
    r4 = num2 ** num3 # 거듭제곱
    r5 = num4 / num3
    r6 = num4 // num3 # 정수부분만 표시
    r7 = num4 % num3
    
    print('r1 :', r1)
    print('r2 :', r2)
    print('r3 :', r3)
    print('r4 :', r4)
    print('r5 :', r5)
    print('r6 :', r6)
    print('r7 :', r7)
    
    # 복합대입 연산자
    num5, num6, num7, num8 = 5, 6, 7, 8
    
    num5 += 1
    num6 -= 2
    num7 *= 3
    num8 /= 4
    
    print('num5 :', num5)
    print('num6 :', num6)
    print('num7 :', num7)
    print('num8 :', num8)
    
    # 비교 연산자
    var1 = 1
    var2 = 2
    
    rs1 = var1 > var2
    rs2 = var1 < var2
    rs3 = var1 >= var2
    rs4 = var1 <= var2
    rs5 = var1 == var2
    rs6 = var1 != var2
    
    print('rs1 :', rs1)
    print('rs2 :', rs2)
    print('rs3 :', rs3)
    print('rs4 :', rs4)
    print('rs5 :', rs5)
    print('rs6 :', rs6)
    
    # 논리 연산자
    var3 = 3
    var4 = 4
    
    res1 = var3 > 2 and var4 > 3
    res2 = var3 > 2 and var4 > 4
    res3 = var3 > 2 or var4 > 4
    res4 = var3 > 4 or var4 > 5
    res5 = not var3 > var4
    
    print('res1 :', res1)
    print('res2 :', res2)
    print('res3 :', res3)
    print('res4 :', res4)
    print('res5 :', res5)
    ```
    
- 2-4.파이썬 기본 입출력 실습
    
    ```python
    """
    날짜 : 2023/01/23
    이름 : 서정현
    내용 : 파이썬 기본 입출력 실습
    """
    
    # 파이썬 기본 입출력
    num = input('숫자 입력 :')
    print('num :', num)
    print('num type :', type(num))
    
    """
    num : 3
    num type : <class 'str'>
    """
    
    # 파이썬 연속 입력
    a, b = map(int, input().split()) 
    print(a, b)
    
    """
    1 2
    """
    
    # 문자열 변환
    num1 = '1'
    num2 = '2'
    
    num1 = int(num1)
    num2 = int(num2)
    
    print(num1 + num2 )
    
    """
    3
    """
    
    # 기본 출력 옵션
    print('010', '1234', '5678', sep='-')
    print('Hello', end=', ')
    print('World', end=' ')
    print('Python')
    
    """
    010-1234-5678
    Hello, World Python
    """
    
    # 서식문자
    print('%d년 %d월 %d일 %s요일' % (2023, 1, 2, '월'))
    
    """
    2023년 1월 2일 월요일
    """
    
    # 포맷문자
    print('{}년 {}월 {}일 {}요일'.format(2023, 1, 2, '월'))
    
    """
    2023년 1월 2일 월요일
    """
    ```
    
- 2-5.파이썬 문자열 실습하기
    
    ```python
    """
    날짜 : 2023/01/03
    이름 : 서정현
    내용 : 파이썬 문자열 실습하기
    """
    
    # 문자열 더하기
    str1 = 'Hello'
    str2 = 'World'
    str3 =  str1 + str2
    str3
    
    """
    'HelloWorld'
    """
    
    # 문자열 곱하기
    str1 = 'Hello!'
    str2 = str1 * 3
    str2
    
    """
    'Hello!Hello!Hello!'
    """
    
    # 문자열 길이
    text = 'Hello World'
    result = len(text)
    result
    
    # 11
    
    # 문자열 인덱스
    text = 'Hello World'
    print('text 1번째 문자 :', text[0])
    print('text 7번째 문자 :', text[6])
    print('text 뒤에서 1번째 문자 :', text[-1])
    
    """
    text 1번째 문자 : H 
    text 7번째 문자 : W
    text 뒤에서 1번째 문자 : d
    """
    
    # 문자열 자르기
    text = 'Hello World'
    print('text 1-5까지 자르기 :', text[0:5])
    print('text 처음-5까지 자르기 :', text[:5])
    print('text 6-11까지 자르기 :', text[6:11])
    print('text 6-마지막까지 자르기 :', text[6:])
    
    """
    text 1-5까지 자르기 : Hello
    text 처음-5까지 자르기 : Hello
    text 6-11까지 자르기 : World
    text 6-마지막까지 자르기 : World
    """
    
    # 문자열 분리
    cities = '서울^대전^대구^부산^광주'
    c1, c2, c3, c4, c5 = cities.split('^')
    print('c1 :', c1)
    print('c2 :', c2)
    print('c3 :', c3)
    print('c4 :', c4)
    print('c5 :', c5)
    
    # 문자열 이스케이프
    print('서울\n대전\n대구\n부산\n광주')
    print('한국\t미국\t일본\t중국\t호주')
    print('안녕하세요 \'홍길동\'님 반갑습니다.')
    print("안녕하세요 '홍길동'님 반갑습니다.")
    
    """
    c1 : 서울
    c2 : 대전
    c3 : 대구
    c4 : 부산
    c5 : 광주
    서울
    대전
    대구
    부산
    광주
    한국	미국	일본	중국	호주
    안녕하세요 '홍길동'님 반갑습니다.
    안녕하세요 '홍길동'님 반갑습니다.
    """
    ```
    

## 3. Ch03

- 3-1.파이썬 조건문 실습하기
    
    ```python
    """
    날짜 : 2023/01/03
    이름 : 서정현
    내용 : 파이썬 조건문 실습하기
    """
    
    # if
    num1, num2 = 1, 2
    
    if num1 > 0:
        print('num1은 0보다 크다.')
    
    if num1 > num2:
        print('num1은 num2보다 크다.')
    
    if num1 > 0:
        if num2 > 1:
            print('num1은 0보다 크고 num2는 1보다 크다.')
    
    if num1 > 0 and num2 > 1:
            print('num1은 0보다 크고 그리고 num2는 1보다 크다.')
    
    """
    num1은 0보다 크다.
    num1은 0보다 크고 num2는 1보다 크다.
    num1은 0보다 크고 그리고 num2는 1보다 크다.
    """
    
    # if ~ else 
    num3, num4 = 3, 4
    
    if num3 > num4:
        print('num3는 num4보다 크다.')
    else:
        print('num3는 num4보다 작다.')
    
    """
    num3는 num4보다 작다.
    """
    
    # if ~ elif ~ else
    n1, n2, n3, n4 = 1, 2, 3, 4
    
    if n1 > n2:
        print('n1은 n2보다 크다.')
    elif n2 > n3:
        print('n2은 n3보다 크다.')
    elif n3 > n4:
        print('n3은 n4보다 크다.')
    else:
        print('n4가 가장 크다.')
    
    """
    n4가 가장 크다.
    """
    
    # 연습문제
    score = int(input('점수입력 : '))
    
    if score >= 90 and score <= 100:
        print('A입니다.')
    elif 80 <= score < 90:
        print('B입니다.')
    elif 70 <= score < 80:
        print('C입니다.')
    elif 60 <= score < 70:
        print('D입니다.')
    else:
        print('F입니다.')
    
    """
    F입니다.
    """
    ```
    
- 3-2.파이썬 반복문 while 실습하기
    
    ```python
    """
    날짜 : 2023/01/03
    이름 : 서정현
    내용 : 파이썬 반복문 while 실습하기
    """
    
    # while
    i = 1
    
    while i<=5:
        print('i :', i)
        i+=1
    
    """
    i : 1
    i : 2
    i : 3
    i : 4
    i : 5
    """
    
    # 1부터 10까지 합
    total, k = 0, 1
    
    while k<=10:
        total += k
        k += 1
    
    print('1부터 10까지 합 :', total)
    
    """
    1부터 10까지 합 : 55
    """
    
    # 1부터 10까지 짝수 합
    total, k = 0, 1
    
    while k<=10:
        
        if k%2 == 0:
            total += k
    
        k += 1
    
    print('1부터 10까지 짝수 합 :', total)
    
    """
    1부터 10까지 짝수 합 : 30
    """
    
    # break
    num = 1
    
    while True:
    
        if num%5 == 0 and num%7 == 0:
            break
    
        num += 1
    
    print('5와 7의 최소공배수 :', num)
    
    """
    5와 7의 최소공배수 : 35
    """
    
    # continue
    n = 0
    
    while n<=9:
    
        n += 1
    
        if n%2 == 0:
            continue
    
        print(n, end=' ')
    
    """
    1 3 5 7 9
    """
    ```
    
- 3-3.파이썬 반복문 for 실습하기
    
    ```python
    """
    날짜 : 2023/01/03
    이름 : 서정현
    내용 : 파이썬 반복문 for 실습하기
    """
    
    # for
    for i in range(5):
        print('i :', i)
    
    for j in range(10, 20):
        print('j :', j)
    
    for k in range(10, 0, -1):
        print('k :', k)
    
    """
    i : 0
    i : 1
    i : 2
    i : 3
    i : 4
    j : 10
    j : 11
    j : 12
    j : 13
    j : 14
    j : 15
    j : 16
    j : 17
    j : 18
    j : 19
    k : 10
    k : 9
    k : 8
    k : 7
    k : 6
    k : 5
    k : 4
    k : 3
    k : 2
    k : 1
    """
    
    # 1부터 10까지 합
    total = 0
    
    for k in range(11):
        total += k
        
    print('1부터 10까지 합 :', total)
    
    """
    1부터 10까지 합 : 55
    """
    
    # 1부터 10까지 짝수 합
    total = 0
    
    for k in range(11):
        if k%2 == 0:
            total += k
        
    print('1부터 10까지 짝수 합 :', total)
    
    """
    1부터 10까지 짝수 합 : 30
    """
    
    # 중첨 for문
    for a in range(2):
        print('a :', a)
        for b in range(3):
            print('b :', b)
            for c in range(4):
                print('c :', c)
    """
    a : 0
    b : 0
    c : 0
    c : 1
    c : 2
    c : 3
    b : 1
    c : 0
    c : 1
    c : 2
    c : 3
    b : 2
    c : 0
    c : 1
    c : 2
    c : 3
    a : 1
    b : 0
    c : 0
    c : 1
    c : 2
    c : 3
    b : 1
    c : 0
    c : 1
    ...
    c : 0
    c : 1
    c : 2
    c : 3
    
    """
    
    # 구구단 출력
    for i in range(1, 10):
        for k in range(1, 10):
            z = i*k
            print('%d X %d = %d' % (i, k, z))
    """
    1 X 1 = 1
    1 X 2 = 2
    1 X 3 = 3
    1 X 4 = 4
    1 X 5 = 5
    1 X 6 = 6
    1 X 7 = 7
    1 X 8 = 8
    1 X 9 = 9
    2 X 1 = 2
    2 X 2 = 4
    2 X 3 = 6
    2 X 4 = 8
    2 X 5 = 10
    2 X 6 = 12
    2 X 7 = 14
    2 X 8 = 16
    2 X 9 = 18
    3 X 1 = 3
    3 X 2 = 6
    3 X 3 = 9
    3 X 4 = 12
    3 X 5 = 15
    3 X 6 = 18
    3 X 7 = 21
    ...
    9 X 6 = 54
    9 X 7 = 63
    9 X 8 = 72
    9 X 9 = 81
    """
    
    # 별삼각형
    for i in range(1, 11):
        for k in range(i):
            print('*', end='')
        print()
    
    """
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********
    **********
    """
    
    # 별삼각형
    for i in range(1, 11):
        print('*' * i)
    
    """
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********
    **********
    """
    
    ```
    

## 4. Ch04

- 4-1.파이썬 자료구조 List 실습하기
    
    ```python
    """
    날짜 : 2023/01/04
    이름 : 서정현
    내용 : 파이썬 자료구조 List 실습하기
    """
    
    # 리스트
    data = [1, 2, 3, 4, 5]
    print('data type "', type(data))
    print('data[0] :', data[0])
    print('data[1] :', data[1])
    print('data[2] :', data[2])
    print('data[3] :', data[3])
    
    """
    data type " <class 'list'>
    data[0] : 1
    data[1] : 2
    data[2] : 3
    data[3] : 4
    """
    
    # 여러 종류 데이터를 저장하는 리스트
    data = [5, 3.14, True, 'Apple']
    print('data type "', type(data))
    print('data[0] :', data[0])
    print('data[0] type :', type(data[0]))
    print('data[1] :', data[1])
    print('data[1] type :', type(data[1]))
    print('data[2] :', data[2])
    print('data[2] type :', type(data[2]))
    print('data[3] :', data[3])
    print('data[3] type :', type(data[3]))
    
    """
    data type " <class 'list'>
    data[0] : 5
    data[0] type : <class 'int'>
    data[1] : 3.14
    data[1] type : <class 'float'>
    data[2] : True
    data[2] type : <class 'bool'>
    data[3] : Apple
    data[3] type : <class 'str'>
    """
    
    # 다차원 리스트
    data = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    print('date[0][0] :', data[0][0])
    print('date[1][1] :', data[1][1])
    print('date[2][1] :', data[2][1])
    
    """
    date[0][0] : 1
    date[1][1] : 5
    date[2][1] : 8
    """
    
    # 리스트 수정, 추가, 삭제
    data = [1, 2, 3, 4, 5]
    
    data[1] = 7
    print('data :', data)
    
    data[2:4] = [7, 8, 9]
    print('data :', data)
    
    data[3:5] = []
    print('data :', data)
    
    """
    data : [1, 7, 3, 4, 5]
    data : [1, 7, 7, 8, 9, 5]
    data : [1, 7, 7, 5]
    """
    
    # 리스트 반복문
    data = [1, 3, 5, 7, 9]
    for n in data:
        print('n :', n)
    
    cities = ['서울', '대전', '대구', '부산', '광주']
    for city in cities:
        print('city :', city)
    
    for index, value in enumerate(cities):
        print('cities[%d] : %s' % (index, value))
    
    """
    n : 1
    n : 3
    n : 5
    n : 7
    n : 9
    city : 서울
    city : 대전
    city : 대구
    city : 부산
    city : 광주
    cities[0] : 서울
    cities[1] : 대전
    cities[2] : 대구
    cities[3] : 부산
    cities[4] : 광주
    """
    
    # 리스트 comprehension
    data = [1, 2, 3, 4, 5]
    
    rs1 = [num * 2 for num in data]
    rs2 = [num * 3 for num in data if num % 2 == 1]
    
    print(rs1)
    print(rs2)
    
    """
    [2, 4, 6, 8, 10]
    [3, 9, 15]
    """
    ```
    
- 4-2.파이썬 자료구조 Tuple 실습하기
    
    ```python
    """
    날짜 : 2023/01/04
    이름 : 서정현
    내용 : 파이썬 자료구조 Tuple 실습하기
    """
    
    # 튜플
    data = (1, 2, 3, 4, 5)
    print('data type :', type(data))
    print('data[0] :', data[0])
    print('data[2] :', data[2])
    print('data[3] :', data[3])
    
    cities = ('서울', '대전', '대구', '부산', '광주')
    for city in cities:
        print('city :', city)
    
    """
    data type : <class 'tuple'>
    data[0] : 1
    data[2] : 3
    data[3] : 4
    city : 서울
    city : 대전
    city : 대구
    city : 부산
    city : 광주
    """
    
    # 튜플 수정, 추가, 삭제
    data = 1, 2, 3, 4, 5
    print('data type :', type(data))
    print('data :', data)
    data[0] = 7 # 튜플 데이터 수정, 추가, 삭제 안됨
    
    """
    data type : <class 'tuple'>
    data : (1, 2, 3, 4, 5)
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In[11], line 5
          3 print('data type :', type(data))
          4 print('data :', data)
    ----> 5 data[0] = 7
    
    TypeError: 'tuple' object does not support item assignment
    """
    
    ```
    
- 4-3.파이썬 자료구조 Set 실습하기
    
    ```python
    """
    날짜 : 2023/01/04
    이름 : 서정현
    내용 : 파이썬 자료구조 Set 실습하기
    """
    
    # 집합 (중복 허용 X, 순서 X)
    data = {1, 2, 3, 4, 5, 3, 2}
    
    print('data :', data)
    print('data type :', type(data))
    
    """
    data : {1, 2, 3, 4, 5}
    data type : <class 'set'>
    """
    
    # 집합 출력
    data = {1, 2, 3, 4, 5, 3, 2}
    
    for num in data:
        print('num :', num)
    
    """
    num : 1
    num : 2
    num : 3
    num : 4
    num : 5
    """
    
    ```
    
- 4-4.파이썬 자료구조 Dictionary 실습하기
    
    ```python
    """
    날짜 : 2023/01/04
    이름 : 서정현
    내용 : 파이썬 자료구조 Dictionary 실습하기
    """
    
    # 딕션너리 
    data = {'A':'Apple', 'B':'Banana', 'C':'Cherry'}
    
    print('data type :', type(data))
    print('data :', data)
    print('data["A"] :', data['A'])
    print('data["B"] :', data['B'])
    print('data["C"] :', data['C'])
    
    """
    data type : <class 'dict'>
    data : {'A': 'Apple', 'B': 'Banana', 'C': 'Cherry'}
    data["A"] : Apple
    data["B"] : Banana
    data["C"] : Cherry
    """
    
    # 딕션너리 활용
    data = {
        101: [1, 2, 3, 4, 5],
        102: (6, 7, 8, 9, 10),
        103: {'서울', '대전', '대구', '부산', '광주'},
        104: {'n1':'김유신', 'n2':'김춘추', 'n3':'장보고'}
    }
    
    print(data[101][4])
    print(data[102][1])
    print(data[104]['n2'])
    
    """
    5
    7
    김춘추
    """
    
    # 딕션너리 반복문
    data = {1: '서울', 2: '대전', 3: '대구', 4: '부산', 5: '광주'}
    
    for k, v in data.items():
        print(k, v)
    
    """
    1 서울
    2 대전
    3 대구
    4 부산
    5 광주
    """
    ```
    

## 5. Ch05

- 5-1.파이썬 함수 실습하기
    
    ```python
    """
    날짜 : 2023/01/06
    이름 : 서정현
    내용 : 파이썬 함수 실습하기
    """
    
    # 함수
    def f(x):
        y = 2 * x + 3
        return y
    
    y1 = f(1)
    y2 = f(2)
    y3 = f(3)
    
    print('y1 :', y1)
    print('y2 :', y2)
    print('y3 :', y3)
    
    """
    y1 : 5
    y2 : 7
    y3 : 9
    """
    
    # 함수 유형
    def type1(x, y):
        z = x + y
        return z
    
    def type2(dataset):
        tot = 0
        for data in dataset:
            tot += data
        print('dataset 합 :', tot)
    
    def type3():
        dataset = [n for n in range(11)]
    
        tot = 0
    
        for k in dataset:
            tot += k
    
        return tot
    
    rs1 = type1(1, 2)
    type2([1,2, 3, 4, 5])
    type2((2, 4, 6, 8, 10))
    rs2 = type3()
    
    print('rs1 :', rs1)
    print('rs2 :', rs2)
    
    """
    dataset 합 : 15
    dataset 합 : 30
    rs1 : 3
    rs2 : 55
    """
    
    # 디폴트 매개변수
    def hello(name='홍길동', age=20):
        print('이름 :', name)
        print('나이 :', age)
    
    hello()
    hello('김유신')
    hello('김유신', 25)
    
    """
    이름 : 홍길동
    나이 : 20
    이름 : 김유신
    나이 : 20
    이름 : 김유신
    나이 : 25
    """
    
    # 가변 매개변수
    def total(*items):
        tot = 0
    
        for i in items:
            tot += i
    
        return tot
    
    r1 = total(1)
    r2 = total(1, 2)
    r3 = total(1, 2, 3)
    r4 = total(1, 2, 3, 4)
    r5 = total(1, 2, 3, 4, 5)
    r6 = total()
    
    print('r1 :', r1)
    print('r2 :', r2)
    print('r3 :', r3)
    print('r4 :', r4)
    print('r5 :', r5)
    print('r6 :', r6)
    
    """
    r1 : 1
    r2 : 3
    r3 : 6
    r4 : 10
    r5 : 15
    r6 : 0
    """
    
    # 하나 이상의 값을 리턴
    def sumMulti(n1, n2):
        y1 = n1 + n2
        y2 = n1 * n2
        return y1, y2
    
    r1, r2 = sumMulti(1, 2)
    print('r1 :', r1)
    print('r2 :', r2)
    
    """
    r1 : 3
    r2 : 2
    """
    
    # 변수에 저장하는 함수 
    def plus(x, y):
        return x + y
    
    def minus(x, y):
        return x - y
    
    var1 = plus
    var2 = minus
    
    r1 = var1(1, 2)
    r2 = var1(2, 3)
    
    print('r1 :', r1)
    print('r2 :', r2)
    
    """
    r1 : 3
    r2 : 5
    """
    
    # 함수 리스트
    def plus(x, y):
        return x + y
    
    def minus(x, y):
        return x - y
    
    defs = [plus, minus]
    
    r1 = defs[0](1, 2)
    r2 = defs[1](2, 3)
    
    print('r1 :', r1)
    print('r2 :', r2)
    
    """
    r1 : 3
    r2 : -1
    """
    
    # 람다함수
    f1 = lambda x, y: x + y
    f2 = lambda x, y: x - y
    
    r1 = f1(1, 2)
    r2 = f2(1, 2)
    
    print('r1 :', r1)
    print('r2 :', r2)
    
    """
    r1 : 3
    r2 : -1
    
    """
    
    ```
    
- 5-2.파이썬 내장함수 실습하기
    
    ```python
    """
    날짜 : 2023/01/06
    이름 : 서정현
    내용 : 파이썬 내장함수 실습하기
    """
    
    import time
    import math
    import random
    
    # 시간날짜 함수
    t1 = time.time()
    print('t1 :', t1)
    
    t2 = time.ctime()
    print('t2 :', t2)
    
    now = time.localtime(time.time())
    year = time.strftime('%Y', now)
    month = time.strftime('%m', now)
    day = time.strftime('%d', now)
    hour = time.strftime('%H', now)
    min = time.strftime('%M', now)
    sec = time.strftime('%S', now)
    yoil1 = time.strftime('%a', now) # 요일 줄임말 Sun, Mon, … Sat
    yoil2 = time.strftime('%w', now) # 요일을 숫자로 표시, 월~일 0, 1, …, 6
    
    print('now :', now)
    print('{}년 {}월 {}일 {}:{}:{}'.format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)) # 이렇게 사용 X
    print('{}년 {}월 {}일 {}({})요일 {}:{}:{}'.format(year, month, day, yoil1, yoil2,  hour, min, sec))
    
    """
    t1 : 1672988018.7017784
    t2 : Fri Jan  6 15:53:38 2023
    now : time.struct_time(tm_year=2023, tm_mon=1, tm_mday=6, tm_hour=15, tm_min=53, tm_sec=38, tm_wday=4, tm_yday=6, tm_isdst=0)
    2023년 1월 6일 15:53:38
    2023년 01월 06일 Fri(5)요일 15:53:38
    """
    
    # 수학 함수
    r1 = math.ceil(1.2)
    r2 = math.ceil(1.8)
    r3 = math.floor(1.2)
    r4 = math.floor(1.8)
    r5 = round(1.2)
    r6 = round(1.8)
    
    print('r1 :', r1)
    print('r2 :', r2)
    print('r3 :', r3)
    print('r4 :', r4)
    print('r5 :', r5)
    print('r6 :', r6)
    
    """
    r1 : 2
    r2 : 2
    r3 : 1
    r4 : 1
    r5 : 1
    r6 : 2
    """
    
    # 랜덤 함수
    num1 = random.random()
    print('num1 :', num1)
    
    num2 = num1 * 10
    print('num2 :', num2)
    
    num3 = math.ceil(num2)
    print('num3 :', num3)
    
    num4 = random.randint(20, 30) # a <= num4 <= b
    print('num4 :', num4)
    
    """
    num1 : 0.01852069817232682
    num2 : 0.18520698172326822
    num3 : 1
    num4 : 20
    """
    ```
    
- 5-3.파이썬 리스트 함수 실습하기
    
    ```python
    """
    날짜 : 2023/01/06
    이름 : 서정현
    내용 : 파이썬 리스트 함수 실습하기
    """
    import math
    
    # 리스트 내장함수
    dataset = [1, 4, 3]
    
    print('1 -', dataset)
    
    # 추가
    dataset.append(2)
    dataset.append(5)
    
    print('2 -', dataset)
    
    # 정렬
    dataset.sort()
    print('3 -', dataset)
    
    dataset.sort(reverse=True)
    print('4 -', dataset)
    
    dataset.reverse()
    print('5 -', dataset)
    
    # 삽입
    dataset.insert(2, 6)
    print('6 -', dataset)
    
    dataset.insert(1, 7)
    print('7 -', dataset)
    
    # 삭제
    dataset.remove(6)
    print('8 -', dataset)
    
    dataset.pop(1)
    print('9 -', dataset)
    
    """
    1 - [1, 4, 3]
    2 - [1, 4, 3, 2, 5]
    3 - [1, 2, 3, 4, 5]
    4 - [5, 4, 3, 2, 1]
    5 - [1, 2, 3, 4, 5]
    6 - [1, 2, 6, 3, 4, 5]
    7 - [1, 7, 2, 6, 3, 4, 5]
    8 - [1, 7, 2, 3, 4, 5]
    9 - [1, 2, 3, 4, 5]
    """
    
    # map 함수 : 리스트의 원소를 지정된 함수로 일괄 처리해주는 함수
    def plus(n):
        return n + 10
    
    list1 = [1, 2 , 3, 4, 5]
    r1 = map(plus, list1)
    print('r1 :', list(r1))
    
    list2 = [0.1, 1.2, 2.6, 3.4, 4.9]
    r2 = map(math.ceil, list2)
    print('r2 :', list(r2))
    
    list3 = ['1','2','3','4','5']
    r3 = map(int, list3)
    print('r3 :', list(r3))
    
    # filter 함수 : 리스트의 원소를 지정된 함수로 필터링 해주는 함수
    list4 = [1, 2 , 3, 4, 5]
    def minus(n):
        if n%2 == 0:
            return n + 10
    r4 = filter(minus, list4)
    print('r4 :', list(r4))
    
    """
    r1 : [11, 12, 13, 14, 15]
    r2 : [1, 2, 3, 4, 5]
    r3 : [1, 2, 3, 4, 5]
    r4 : [2, 4]
    """
    ```
    

## 6. cH06

- 클래스 모음
    
    ```python
    class Account:
    
        def __init__(self, bank, id, name, balance):
            self._bank = bank
            self._id = id
            self._name = name
            self._balance = balance
            
        def deposite(self, money):
            self._balance += money
        
        def withdraw(self, money):
            self._balance -= money
        
        def show(self):
            print('은행명 :', self._bank)
            print('계좌번호 :', self._id)
            print('입금주 :', self._name)
            print('현재잔액 :', self._balance)
    
    class Car:
    
        # 생성자
        def __init__(self, brand, color, price):
            self.brand = brand
            self.color = color
            self.price = price
        
        # 기능
        def speedUp(self):
            print('%s 속도 올립니다.' % self.brand)
            
    
        def speedDown(self):
            print('%s 속도 내립니다.' % self.brand)
    
        def show(self):
            print('차량명 :', self.brand)
            print('차량색 :', self.color)
            print('차량가격 :', self.price)
            pass
    
    from sub1.Account import Account
    
    class StockAccount(Account) :
        def __init__(self, bank, id, name, balance, stock, amount, price):
            super().__init__(bank, id, name, balance)
    
            self.__stock = stock
            self.__amount = amount
            self.__price = price
    
        def sell(self, amount, price):
            self._balance += amount * price
            self.__amount -= amount
    
        def buy(self, amount, price):
            self._balance -= amount * price
            self.__amount += amount
    
        def show(self):
            super().show()
            print('주식종목 :', self.__stock)
            print('주식수량 :', self.__amount)
            print('주식가격 :', self.__price)
    ```
    
- 6-1.파이썬 클래스 실습하기
    
    ```python
    """
    날짜 : 2023/01/11
    이름 : 서정현
    내용 : 파이썬 클래스 실습하기
    """
    from sub1.Car import Car
    from sub1.Account import Account
    
    sonata = Car("sonata", "red", 1000)
    sonata.speedUp()
    sonata.speedDown()
    sonata.show()
    
    bmw = Car("BMW", "blue", 4000)
    bmw.speedUp()
    bmw.speedDown()
    bmw.show()
    
    kb = Account("국민은행", "101-12-1234", "김유신", 30000)
    kb.deposite(5000)
    kb.withdraw(3000)
    kb.show()
    
    hana = Account("하나은행", "131-22-1234", "김춘추", 20000)
    hana.deposite(5000)
    hana.withdraw(3000)
    hana.show()
    hana._balance -= 1
    print(hana._balance)
    ```
    
- 6-2.파이썬 상속 실습하기
    
    ```python
    """
    날짜 : 2023/01/11
    이름 : 서정현
    내용 : 파이썬 상속 실습하기
    """
    
    from sub1.StockAccount import StockAccount
    
    kb = StockAccount("KB증권", "101-12-1234", "홍길동", 50000, "삼성전자", 10, 60000)
    kb.deposite(500000)
    kb.sell(5, 1000)
    kb.show()
    ```
    
- 6-3.파이썬 모듈 실습하기
    
    ```python
    """
    날짜 : 2023/01/11
    이름 : 서정현
    내용 : 파이썬 모듈 실습하기
    """
    
    from sub2.calc import plus, minus
    import sub2.calc as c
    
    r1 = plus(1, 2)
    r2 = minus(2, 3)
    r3 = c.multi(3, 4)
    r4 = c.div(4, 2)
    
    print("r1 :", r1)
    print("r2 :", r2)
    print("r3 :", r3)
    print("r4 :", r4)
    ```
    
- 6-4.파이썬 외부 패키지 모듈 실습
    
    ```python
    """
    날짜 : 2023/01/12
    이름 : 서정현
    내용 : 파이썬 외부 패키지 모듈 실습
    """
    // pip install openpyxl 실행 외부라이브러리 설치
    from openpyxl import Workbook, load_workbook
    
    # 새로운 엑셀파일 생성
    workbook = Workbook()
    
    # 첫번째 시트 활성화
    sheet = workbook.active
    
    # 데이터 입력
    sheet['A1'] = '파이썬 엑셀 실습'
    sheet.append(['아이디', '이름', '전화번호', '나이', '주소'])
    sheet.append(['a101', '김유신', '010-1234-1001', 25, '김해시'])
    sheet.append(['a102', '김춘추', '010-1234-1002', 22, '경주시'])
    sheet.append(['a103', '장보고', '010-1234-1003', 35, '완도시'])
    sheet.append(['a104', '강감찬', '010-1234-1004', 45, '경기도'])
    sheet.append(['a105', '이순신', '010-1234-1005', 55, '서울시'])
    
    # 저장닫기
    workbook.save('C:/Users/java2/Desktop/Member.xlsx')
    workbook.close()
    
    print('프로그램 종료...')
    
    # 엑셀 파일 읽기
    # data_only=Ture로 해줘야 수식이 아닌 값으로 받아온다.
    load_wb = load_workbook("C:/Users/java2/Desktop/Member.xlsx", data_only=True)
    
    #시트 이름으로 불러오기
    load_ws = load_wb['Sheet']
    
    #셀 주소로 값 출력
    print(load_ws['A1'].value)
    
    get_cells = load_ws['A1':'E7']
    
    for row in get_cells:
            for cell in row:
                if cell.value != None:
                    print('%s ' % cell.value, end='')
            print()
    ```
