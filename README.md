
# wanted-pre-onboarding-backend 사전과제


지원자 : 하승찬


### ERD

![원티드 erd](https://github.com/caretim/wanted-pre-onboarding-backend/assets/108650777/d9c92eb2-fec2-4def-b34c-0aee0561c610)


## 배포서버 주소

http://54.180.144.237:8000/


### 시스템 아키텍쳐 
![파일구조](https://github.com/caretim/wanted-pre-onboarding-backend/assets/108650777/8fa01527-4e4a-4c5b-a73f-bf8e73fb462a)


### 데모 영상



### 기능목록


## accounts
1. 이메일,패스워드로 유저 회원가입 (create) 
2. 이메일은 @가 포함되어 있는 이메일 형식이여야한다.
3. 패스워드는 8자 이상이여야한다. (bcrypt로 암호화)  
4. 이메일은 중복될 수 없다.
5. 올바른 이메일, 패스워드일 떄 로그인 성공 
6. 회원가입,로그인시 jwt토큰 발급


## articles
1. 게시글 생성,수정,삭제,조회,목록조회 기능
2. 모든 유저는 글을 조회(detail,list) 할 수 있다.
3. 게시글 작성자만 수정,삭제 할 수 있다.
4. 목록조회시 페이지네이션을 사용하여 페이지를 구분한다.




## API 명세(request/response 포함)

### 1. 회원가입
HTTP method : POST
URL : "/accounts/signup/"
Request 
```bash
{
	"email": str@str,
	"password": str,
}
```
Response
```bash
성공
{
    'message' : str,
    'refresh' : str,
    'access' : str,
}

실패
{
    "message" : str
}

```
HTTP STATUS
201 : 회원가입 성공
400 : 이메일, 비밀번호 유효성 검사 실패

### 2. 로그인
HTTP method : POST
URL : "/accounts/login/"
Request 
```bash
{
	"email": str@str,
	"password": str,
}
```
Response
```bash
성공
{
    "refresh" : str,
    "access" : str,
}

실패
{
    "message" : str
}

```
HTTP STATUS
200 : 로그인 성공
400 : 이메일, 비밀번호 유효성 검사 실패

### 3. 게시글 목록
HTTP Method : GET
URL : "/articles/{page_id}/
Request 
```bash
{
	"page": int(생략가능, 생략시 default 1페이지),
}
```
Response
```bash
{
    "data" : lists,
}

```
HTTP STATUS
200 : 조회 성공

### 4. 게시글 생성
HTTP Method : POST
URL : "/articles/create/"
Request 
```bash
{
	"title": str,
	"content": str,
}
```
Response
```bash
성공
{
    "data" : title,context,
}

실패
{
    "message" : str
}
```
HTTP STATUS
201 : 게시글 생성 성공
400 : 게시글 생성 실패(게시글 제목, 내용이 없는 경우)
401 : 로그인 안한 유저 접근

### 5. 단일 게시글 조회
HTTP Method : GET
URL : "/articles/detail/{id}/"
Request 
```bash

```
Response
```bash
{
    "data" : dict(article.data),
}

```
HTTP STATUS
200 : 조회 성공

### 6. 게시글 수정
HTTP Method : PUT
URL : "/articles/update/{id}/"
Request 
```bash
{
	"title": str,
	"content": str,
}
```
Response
```bash
성공
{
    "data" : dict(object),
}

실패
{
    "message" : str
}
```
HTTP STATUS
200 : 게시글 수정 성공
400 : 게시글 수정 실패(잘못된 유저 접근, title, content가 비어있는 경우)

### 7. 게시글 삭제
HTTP Method : DELETE
URL : "/articles/delete/{id}/"
Response
```bash
http status 
```
HTTP STATUS
204 : 게시글 삭제 성공
400 : 게시글 삭제 실패(잘못된 유저 접근)
