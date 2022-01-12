# GIT

## 초기 설정

- 최초 한 번만 설정

1. 누가 커밋을 남겼는지 확인할 수 있도록 이름과 이메일을 설정

```bash
$ git config --global user.name ~~# git아 나 설정할건데 전역에 사용자이름
$ git config --global user.email ~~# git아 나 설정할건데 전역에 이메일
```

2. 설정된 내용 확인

```bash
$ git config --global --list #or
$ git config --global -l
```



`add` : 현재 상태를 깃으로 관리하겠다.

`commit` : 현재 상태를 버전으로 만들겠다. 

`push` 깃 허브에는 수정 사항과 원본 파일을 집어넣는다 

## git init

- 현재 작업 중인 **디렉토리**를 **깃**으로 관리

```bash
$ git init #초기화 해당디렉토리에...
```

### 주의사항

- 이미 master로 관리중인 폴더 내에서 **절대 절대 절대 git init 금지**

## git status

- working directory와 Staging Area에 있는 파일들의 현재 상태를 확인
- 상태
  - `Untracked` : git이 관리하지 않는 파일 (한번도 staging area에 올라 간 적이 없음) (깃이 수정사항 하나도 모름)
  - `tracked` : git이 관리하는 파일
    - `Unmodified` : 최신상태
    - `modified` : 수정되었지만 commit을 남기기 전
    - `staged` : staging area에 반영된 상태

## git add

```bash
# 특정파일
$ git add file_name.txt
# 특정폴더
$ git add folder/
# 현재 디렉토리에 속한 모든 파일/폴더
$ git add .
```

## git commit

- staging area에 올라온 파일의 변경 사항을 하나의 버전으로 저장하는 명령어
- `커밋 메시지` 는 현재 변경사항을 기록하는 용도로 사용합니다.

```bash
$ git commit -m "커밋 메세지" 
# (root-commit) : 최초 커밋시 메시지 발생
# d3aff7fs : 요상한 문자들은 이 버전의 고유값
# 그 아래 문장들은 커밋 내용들
```



## git log

- 커밋의 내역을 조회할 수 있는 명령어

- 옵션

  - `--oneline` : 한줄로 축약해서 보여줍니다.
  - `--graph` : 브랜치와 머지 내력을 그래프로 보여주는 명령어
  - `--all` : 모든 브랜치의 내역
  - `--reverse` : 커밋 내역의 순서를 반대로 보여주는 명령어

  ```bash
  $ git log
  $ git log --oneline # 커밋 메시지만 간단하게 출력
  ```

  

### 주의사항

수정사항 발생 시 그 파일은 상태가 modified되어 있다.

이것은 add로 다시 staging area에 넣어야하고 그 이후, 커밋만 하면 된다.

































