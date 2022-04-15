--시퀀스 생성
create sequence emp_seq
    start with 1
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache;

--시퀀스 수정
alter sequence test_seq
maxvalue 99999
increment by 10;

select test_seq.nextval from dual; --처음시작할때 nextval을 해줘야 currval을 적용할 수 있음

--drop table employees2;
--시퀀스번호, 사원번호, 사원명, 직급, 입사일 employees2테이블 생성
--107명 사원을 입력하시오.
--입사일 기준으로 오름차순으로 정렬하시오.
create table employees2 as select employee_id, emp_name, job_id, hire_date from employees where 1=2;
alter table employees2 add empno number(5);
insert into employees2 select employee_id, emp_name, job_id, hire_date, test_seq.nextval from employees;
select * from employees2 order by hire_date;

--컬럼위치변경(컬럼순서 변경방법)
alter table employees2 modify employee_id invisible; --테이블 컬럼 숨김
alter table employees2 modify emp_name invisible;
alter table employees2 modify job_id invisible;
alter table employees2 modify hire_date invisible;
alter table employees2 modify employee_id visible; --테이블 컬럼 보이기
alter table employees2 modify emp_name visible;
alter table employees2 modify job_id visible;
alter table employees2 modify hire_date visible;

commit;
select * from employees2;


select * from employees;
--문자함수 (upper, lower, inicap)
select upper(emp_name) from employees; --upper: 대문자, lower: 소문자, inicap: 첫글자 대문자
--문자길이 (length)
select emp_name, length(emp_name), lengthb(emp_name) from employees; --lengthb : 몇바이트 차지하는지 보여줌
select stuname, length(stuname), lengthb(stuname) from students;
-- 영어는 한글자당 1바이트, 한글은 한글자당 3바이트

--문자열 추출: substr
select emp_name,substr(emp_name, 0,6) from employees; --0부터 여섯째짜리 자리까지 잘라옴
select emp_name, substr(emp_name,-1) from employees; --뒤에서 한글자만 가져옴

alter table member add juminno char(14);
select * from member;

--컬럼수정
update member set password='        5555     ',juminno='690912-2101111' where id='eee'          ;
alter table member add filname varchar2(20);
update member set filname='asdf.csv' where id='              eee         ';

--컬럼추가
insert into member values(
'hhhh','7777','홍길영   ','010  -8888 -8888',300,100,'22/02/02','010101-4100123','abc    .json');
commit;
desc member;

select name, substr(juminno,0,6) "주민번호앞자리", substr(juminno,8) "주민번호 뒤자리" from member;
select name,juminno,substr(juminno,0,8) ||'******' juminno2, length(substr(juminno,0,8) ||'******') juminlength from member; --함수를 하나가 아니라 겹쳐서 여러개 사용가능

-- .hwp, .xls, .pdf, .csv
--member테이블
--id의 길이, juminno 앞자리, juminno뒤자리, filname 뒤에서 3자리 출력하시오.
select length(id) , substr(juminno, 0,6) "주민번호앞자리", substr(juminno,8) "주민번호 뒤자리", substr(filname,-3) "filename 뒤 3자리" from member;

--특정문자 위치 찾기: instr , 길이가 다를때 주로 사용
select filname, instr(filname,'.'), substr(filname, instr(filname,'.')+1) from member;

--replace 문자 대체
select emp_name from employees;
select replace(emp_name,'a','A') from employees;
--빈공백 없애기
select replace(emp_name,' ','') from employees;
--trim,ltrim,rtrim 공백제거 함수 : 중간의 있는 공백이 아니라면 trim을 사용해서 하면 됨, 그게 아니라면 replace를 사용해야함
select password, length(password), ltrim(password) from member;
select phone, length(phone) from member;
select filname, length(filname),trim(filname),length(trim(filname)) from member;

update member set filname=ltrim(filname);
update member set filname=replace(filname,' ','');
select * from member;


--1. concat 문자열 합치기
select concat(id, concat('-',password)) juminno from member; -- 합쳐서 한컬럼에 보여줌, 이중으로 사용가능
--2. 연결 연산자
select id||'-'||password as juminno from member;

--빈공간 특정문자 채우기 (lpad, rpad)
select rpad(id,10,'*') from member; -- id이후에 *문자로 10자리까지 채워짐

select juminno from member;
select rpad(substr(juminno,0,8),14,'*') juminno from member;

--현재날짜 (어제, 오늘, 내일), 날짜는 더하기, 빼기 가능 단, 곱하기는 안됨
select sysdate-1, sysdate,sysdate+1 from dual;

select * from member;
insert into member(id,password, create_date) values('iii','1111',sysdate);

select to_char(create_date,'YYYY-MM-DD hh:MI:ss') from member; --날짜 형 변환 (MM은 월, MI는 분)

select hire_date from employees;

select trunc(sysdate-to_date('22/03/08')) from dual; --형변환, sysdata-to_date: 지정일로부터 며칠이 지났는지 알려줌

select hire_date, round(hire_date,'month') from employees; --16일을 기준으로 달을 반올림함

select round(create_date,'ddd') from member; --일을 기준으로 함

select emp_name, sysdate, '22/03/08', months_between(sysdate,to_date('22/03/08')) from employees; -- 몇개월 차이가 있는지
select sysdate, add_months(sysdate,6) from dual; -- 개월 추가

select sysdate, next_day(sysdate,'수요일') from dual; -- 오늘날짜에서 다음 수요일의 날짜가 언제인지 알려줌
select sysdate,last_day(sysdate) from dual; --해당 달의 마지막 날짜를 변환 last_day

------------------------------------------------------------
create table membership(
name varchar2(30) not null, --중복이 될 수 있지만 null만 안들어오면 됨
id varchar2(16) primary key, --null이 들어올수 없음, unique(똑같은게 들어오면 안됨)
pw varchar2(20) not null,
email varchar2(50),
send_email number(1), --number(1)로 0,1로 구분할수 있음
zipcode char(50),
adress1 varchar2(50),
adress2 varchar2(50),
phone1 char(11),
tel char(11),
birth date,
newyear number(1),
company number(1),
create_date date,
myip char(15)
);
--drop table membership;
--primary key 추가
alter table membership add primary key(id);
--제약조건 not null 수정
alter table membership modify name not null;
desc membership;

insert into membership values(
'김유신','eee','5555','eee@naver.com',1,'12323','서울 양천구 양천동','101-1','01044444444','0244444444','2000/06/21',0,0,sysdate,'202.202.202.202');

select * from membership;

--미성년자만 출력
select birth, months_between('2022/01/01',birth) from membership where months_between('2022/01/01',birth)<216;


-- board:fk (foregin key 등록)
create table board(
bno number(4) primary key,
id varchar2(100),
title varchar2(100),
content varchar2(3000),
create_date date,
hit number(4) default 0, --default 0은 입력하지않으면 기본0으로 정하겠다는 의미
--선언: idex명 mem_fk_id, 외래키(컬럼) 위치는 membership테이블의 id임 ==> primary key로 등록되어있지 않으면 외래키로 등록할 수 없음
constraint mem_fk_id foreign key(id) references membership(id) --에러가 났을때 어디 index에서 에러가 났는지 알려줌
);
--foregin key 없는 아이디로 등록이 불가능함.
insert into board values(
board_seq.nextval,'bbb','게시판제목2','게시판에 들어가는 내용을 입력합니다.2',sysdate,1); --primary에 없는 id를 입력하는 경우는 오류 (무결성오류) , 부모가 없기 때문에 외래어키를 입력할 수 없는것

commit;
select * from board;
--foregin key 키로 등록되어 있는 경우, 삭제시 에러 발생
delete membership where id='bbb'; --자식 key가 존재하면 부모키를 함부로 지울수가 없음, foreign key로 등록하면 함부로 삭제할수 없다
--ORA-02292: 무결성 제약조건(ORA_USER.MEM_FK_ID)이 위배되었습니다- 자식 레코드가 발견되었습니다 ==> mem_fk_id가 foreign key 오류라는 것을 알려주기위해서 constraint로 선언을 해준것

--문자 ==> 날짜형 변환
select sysdate-to_date('22/03/08') from employees; --날짜형으로 변환을 해주지않으면 계산할 수 없음

select hire_date, to_char(hire_date,'yy/mm/dd hh:mi:ss day') from employees;
select create_date, to_char(create_date,'hh24:mi:ss') from member; --hh24: 24시간형태, am: 오전오후

select * from member;
update member set create_date=sysdate where id='aaa';
commit;

select salary from employees;
select salary, salary*12 "연봉", salary*12*1230 "연봉(원화)" from employees;

--천단위 표시, $: 그냥 추가, L:원화표시 추가, C:KRW 표시 ,0 빈자리는 0으로 채움, 9는 빈자리 생략
select salary, salary*12,to_char(salary*12*1230, 'L999,999,999') from employees; --'999,999,999,999' 단위표시해주고 빈칸이면 공백으로 만듦, 단 '000,000,999,999'로 쓰게되면 빈칸을 0으로 채워줌
select to_char(empno,'000') from employees2;

select '2022-04-14 01:01:01',to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate,'hh') hours, to_char(sysdate,'mi') minutes from dual;

select * from studata;
-- 소수점 표시
select to_char(avg,'99.00') from studata;

--1. 문자를 날짜로 형변환 2. 다시 문자로 형 변환
select to_char(to_date('22/03/08'),'yyyy-mm-dd') from dual;

select hire_date from employees;

--문자로 날짜 검색 가능
select hire_date from employees where hire_date='20080113';
--숫자로 날짜검색 불가능
select hire_date from employees where hire_date=20080113;


--문자=>숫자형 변환
select '20,000'-'19,000' from dual; --오류
-- 문자형을 천단위 타입을 확인해서 숫자로 변환
select to_number('20,000','99,999')-to_number('19,000','99,999') from dual; -- 문자형 타입을 숫자로 변형
-- 숫자를 천단위로 변환
select to_char(2000,'99,999') from dual; -- 숫자를 다음 형태로 문자변환
select to_char('20,000') from dual; -- 타입은 char ==> ,인 문자가 들어가 있어서 to_number로 변형불가능
select to_number('20000') from dual; -- ,이 없기 때문에 숫자형으로 변형가능
-- 천단위표시를 제거후 숫자로 형변환
select to_number(replace('20,000',',','')) from dual;

-- commission_pct중 null은 nvl로 0으로 변환
select salary, salary*12,commission_pct, salary*12+(salary*12*nvl(commission_pct,0)) from employees; 

-----nvl 이용: manager_id null인 경우 999로 표시하시오.------
select * from employees;

select manager_id,nvl(to_char(manager_id),'ceo') manager_id from employees;


select * from students;
------그룹함수 min최소값, max최대값, count 개수
select min(kor) from students;
select emp_name, min(salary), max(salary) from employees; --그룹함수는 일반함수와 함께 사용할 수 없음
select count(*) from employees;
select count(*),count(employee_id),count(manager_id),min(salary) from employees; -- null값은 계산해주지 않음
-- 합계
select sum(salary) from employees where department_id=60; 
-- group by 그룹함수조건 : 조건별로 그룹을 묶음
select department_id, sum(salary) from employees group by department_id order by department_id;

select e.department_id, d.department_name, sum(salary) from employees e, departments d
where e.department_id=d.department_id and e.department_id=60 
group by e.department_id, d.department_name order by e.department_id;
 
-- avg 평균
select round(avg(salary),2) from employees;
-- 평균 월급보다 큰사원 총수
select count(*) from employees where salary<(select round(avg(salary),2) from employees); -- 괄호안을 먼저 계산하기 때문에 그룹함수를 사용해도 단일함수랑 같이 사용할 수 있음

select department_id from employees;
select department_id, department_name from departments; --name은 departments에만 있고 employees에는 없음

select * from employees where mod(employee_id,2)=1 order by employee_id;
select months_between(hire_date,sysdate) from employees;
select months_between(sysdate,hire_date) from employees;

--자기가 태어난 날부터 현재까지 며칠이 되는지 계산
select round(sysdate-to_date('19980114')) from dual;

--drop table emp02;
create table emp02(
id varchar2(20),
content clob
);

--clob: 대용량으로 저장해야함
insert into emp02 values(
'bbb','<p>sdfsfsfsf sfsdffwfwf fwfsfkjwlfkwjf</p><p>fdkjwflwkfjwf</p><p><span style="background-color: rgb(119, 119, 119); color: rgb(255, 0, 0); font-size: 24pt;">많은 글자를 입력하겠어</span></p>');

select * from emp01;
commit;
desc emp01;

alter table emp01 add(job varchar2(9));
alter table emp01 modify(job varchar2(30));

update emp01 set job='manager' where empno>10;

--emp01 job을 number(10)로 바꾸시오
update emp01 set job=1 where job='manager';
alter table emp01 modify(job number(10)); --비어있어야만 데이터 유형을 변경할 수 있음

update emp01 set job='' where job=1;
alter table emp01 modify(job number(10));

--emp01 직급(job)칼럼을 삭제
alter table emp01 drop column job;

select * from studata2;
update studata2 set kor=0, total=0+eng+math,avg=(0+eng+math)/3 where stuno=8;

commit; --cmd창에서 업데이트를 할때 만약 sql에서 업데이트후 commit을 하지않는다면 cmd에서는 대기상태이다