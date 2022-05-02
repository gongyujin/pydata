--alter session set "_ORACLE_SCRIPT"=true; 세션을 바꿔줌
--
--create user ora_user identified by 1234; 유저 ora_user는 1234로 비밀번호를 가진 유저를 생성(사용자생성)
--
--grant connect,resource,dba to ora_user; connect를 해주지않으면 ora_user로 접속할 수 없음(권한부여)
--
--
--<오라클 시작>
---데이블생성-
--* varchart2는 가상이기 때문에 데이터 공간을 크게 차지하지않음, 한글(3byte)를 10글자 쓰고 싶다면 기본 30byte를 가져와야함
--* char은 고정이기 때문에 공간이 남아도 빈공간으로 남겨둠
--* number: 숫자에 대함 (실수, 정수 모두 해당함)
--
--insert into member(id,pw,name,phone) values(
--'aaa','1111','홍길동','010-1111-1111'); // 아직파일이 저장되지 않은 상태 ==> 외부(cmd창)에서 접근하면 나타나지않음
--
--commit; // DB에 확실히 저장시켜줌 (커밋을 하지않으면 아직 대기상태)
--==> commit하면 db에 저장하는순간 메모리를 싹지워버림
--
--rollback; // 저장된 메모리를 날려줌, commit전까지 지워줌
--
--** primary key를 중복해서 넣게 되면 무결성 제약 조건에 위배됨
--** null은 빈공백을 의미하는게 아님
--
--** 해당데이터를 클릭해서 제약조건을 살펴보면 primary key가 무엇인지 알수 있음


select * from employees;

select * from departments;

select job_id, job_title, min_salary, max_salary, create_date, update_date  from jobs;

create table member(
id varchar2(20) primary key,
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

desc member; --데이터가 어떤 형태로 들어있는지 보여줌

select * from tab;
select * from member;

commit;
rollback;

select * from member;

-- insert 방법1: 모든 컬럼을 다 넣는 것
insert into member(id,pw,name,phone) values(
'aaa','1111','홍길동','010-1111-1111');

-- insert 방법2: 컬럼이 생략가능
insert into member values(
'ccc','1111','이순신','010-2222-2222');
insert into member values(
'aaa','1234','유관순','010-3333-3333');

select * from member;
commit;

-- insert 방법3: 부분적으로 이용가능
insert into member(id,pw) values(
'ddd','김구');

insert into member values(
'eee','1111','강감찬','010-3333-3333');

select * from member;
rollback;

insert into member(id,pw,name) values(
'fff','1111','김유신');


select name, phone from member;

select * from employees;

select emp_name,job_id from employees;
desc employees; --타입이 어떻게 되어있는지 알수 있음--

delete from member; --모든 테이블 삭제
select * from member; --테이블이 다 날라감
rollback; --다시 돌림
select * from member; --테이블 다시 생김

delete from member where id='bbb'; --위치를 찾을때는 주로 primary key를 사용해서 동작을 이행, 중복을 방지하기 위해서 primary key를 사용

--end 조건 사용가능함, where에서 찾게 되는데 하나만 찾을수도 있고 부등호랑 and를 사용하여 여러개를 찾을 수 있음
select employee_id, emp_name, salary from employees where employee_id>=150 and salary>4000;

 insert into member values(
 'eee','1111','강감찬','010-5555-5555');
 
 commit;
 rollback;
 
 --검색
 select * from employees;
 --삭제
 delete from member;
 --내용변경(수정)
 update member set phone='010-7777-7777' where id='bbb';

 
 --소수점 자리 한자리를 포함해서 총 4자리
create table member2 (
id varchar2(20),
pw number(4),
kor number(4,1)
); 

insert into member2 values(
'aaa',1111,99.9);

commit;

select * from member2;

 --students 테이블 생성
 --stuid,stuname,kor,eng,math,total,avg,rank
 --varchar2(20),number(3),number(4,1)
 --5명의 학생을 입력해보세요.
 
 create table students(
 stuid varchar2(20),
 stuname varchar2(20),
 kor number(3),
 eng number(3),
 math number(3),
 total number(3),
 avg number(4,1),
 rank number(3)
 );
 
 insert into students(stuid,stuname,kor,eng,math,total,avg) values(
 'aaa','홍길동',100,100,100,100+100+100,(100+100+100)/3);
 
 select * from students;
  insert into students(stuid,stuname,kor,eng,math,total,avg) values(
 'bbb','이순신',99,99,99,99+99+99,(99+99+99)/3);
  insert into students(stuid,stuname,kor,eng,math,total,avg) values(
 'ccc','유관순',100,99,98,100+99+98,(100+99+98)/3);
  insert into students(stuid,stuname,kor,eng,math,total,avg) values(
 'ddd','김구',100,100,100,100+100+100,(100+100+100)/3);
  insert into students(stuid,stuname,kor,eng,math,total,avg) values(
 'eee','강감찬',95,100,100,(95+100+100),(95+100+100)/3);
 
 commit;
 
 select * from students; --DQL
 delete from students; --내용삭제 --DML
 drop table member3; --테이블삭제: 복구 불가 --DDL
 
 select * from tab;
 desc employees;
 

 
 
 --table 컬럼추가
 --테이블에 행을 추가하고 싶을때 date유형의 create_date를 추가 (유형을 추가해줌)
 alter table member add create_date date;
 --table 컬럼삭제
 alter table member drop column create_date;
 --테이블 타입변경
 alter table member modify pw number(4); --빈공간으로 바꿔주면 타입을 변경해줄 수 있음
 update member set pw=''; --빈공백으로 다 바꿔줌
 --테이블 컬럼이름변경
 alter table member rename column pw to password;
 --테이블 이름변경
 alter table member rename to member2; 
 
 select * from tab;
 desc member;
 commit;
 
 
 select * from member;
 --추가된 유형의 데이터 값을 변경해줌
 update member set create_date=sysdate where id='aaa';
 
 create table member(
 id varchar2(20),
 pw varchar2(20),
 name varchar2(20),
 phone varchar2(20)
 );
 
create table member as select * from member2 where 1=2; --복사붙여넣기 같은 느낌 -- 데이터는 들어오지않고 타입만 복사되는것

select *from member;
drop table member;
create table member as select * from member2; --타입도 복사되고 데이터도 복사됨

-- 형식을 지정해서 행을 추가하는 것
alter table member add total number(3);
alter table member add avg number(4,1);
desc member;
select * from member;

desc students;
select * from member;
select * from students;

update students set stuid=6,stuname='김유신' where kor=99;
commit;
desc students;
desc member;
select * from member;

update member set total=100 where name='홍길동';
--for문 돌리듯이 계속돌리면 됨
update member set total=(select total from students where stuname='홍길동') where name='홍길동';

select * from students;
select total from students where stuname='홍길동';

--중복되는 것은 1번만 출력
select distinct manager_id from employees; --19개
select manager_id from employees; --107개

--컬럼명은 대소문자를 구분하지않지만 테이블안에 있는 데이터는 대소문자를 구분함
select * from employees;
select emp_name from employees where emp_name='Pat Fay'; --대소문자 구분하기때문에 정확하게 써줘야함
select emp_name from employees where lower(emp_name)='pat fay';


 select * from departments;
 
 -- 이름, 급여, 입사일자
 -- emp_name, salary, hire_date, employees
 select * from employees;
 select emp_name,salary, hire_date from employees;
 --employees의 테이블을 똑같이 employees2 생성해보세요.
 create table employees2 as select * from employees;
 delete from employees2;
 drop table employees2;
 
 --employees2 table에 employee_id, emp_name,hire_date,salary를 employees 타입과 똑같이 생성 
desc employees;
delete from employees2;
drop table employees2;
create table employees2(
employee_id number(6),
emp_name varchar2(20),
hire_date date,
salary number(8,2)
);
 insert into employees2 values(
 104,'김유신','2021/02/01',30000);
 select * from employees2;
 
 --empl table
 --employee_id, emp_name, hire_date를 employees 테이블에서 테이터까지 복사해서
 --테이블을 만드세요
 
 create table empl as 
 select employee_id,emp_name,hire_date from employees;
 select * from empl;