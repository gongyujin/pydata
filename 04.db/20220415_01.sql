select * from tab;

--drop table emp02;
--drop table employees2;
--drop table students2;

rename studata2 to sturank; -- 이름변경

--id가 공통, foregin key로 연결되어 있음
select * from board;
select * from membership;

--만약에 membership에 포함되지않은 id값을 board에 입력해서 삽입하면 무결성제약조건에 위배됨
insert into board values(
board_seq.nextval, 'ccc','이벤트 진행합니다.','이벤트 경품을 진행합니다.',sysdate,1);

create table emp02(
empno number(4) primary key,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2) check(deptno between 10 and 19),
gender char(1) check(gender in ('M','F'))
);

insert into emp02 values(
emp_seq.nextval, '홍길동','manager',10,'M');

insert into emp02 values(
emp_seq.nextval, '홍길자','manager',10,'F'); --check제약조건에 맞춰서 삽입해야함 

insert into emp02 values(
emp_seq.nextval, '홍길순','manager',18,'F'); 

insert into emp02 values(
emp_seq.nextval, '홍길순','manager',18,'D'); 

select * from emp02;
desc emp02;

select emp_seq.currval from dual; --nextval을 이용해서 삽입했을때 잘못된 성립이여도 카운트가 됨


--employees테이블을 참조하여 emp01 테이블 생성
--employee_id는 primary key
--emp_name은 unique
--salary not null
--manager_id
--department_id
--107개의 데이터를 입력하시오.

select * from emp01;

create table emp01(
employee_id number(6) primary key,
emp_name varchar2(80) unique,
salary number(8,2) not null,
manager_id number(6),
department_id number(6)
);

insert into emp01 select employee_id, emp_name, salary, manager_id, department_id from employees;

desc emp01;

--foreign key 등록
--선언: index 명 mem_fk_id, 외래키(컬럼) 위치 membership테이블 id
--constraint mem_fk_id foreign key(id) references membership(id)
alter table emp01
add constraint departments_fk_id foreign key(department_id) 
references departments(department_id);

--primary key 삭제
alter table emp01 drop primary key;
--primary key 생성
alter table emp01 add primary key(employee_id);


select * from students;

select * from studata;

select * from membership;

select * from sturank order by stuno;
update sturank set stuname='eee' where stuno=5;
--1. membership id primary key 등록
alter table membership add primary key(id);
--2. sturank fk 등록
alter table sturank add constraint stu_fk_id foreign key(stuname)
references membership(id);

alter table sturank rename column stuname to id;

desc sturank;

--delete sturank where stuno>5;

select * from employees;

--논리 (decode): if문이랑 같은 개념
select emp_name, department_id, 
decode(department_id,20,'승진대상',
30,'승진보류',
40,'승진보류',
50,'승진보류') "승진확인" from employees;

select * from students;
select stuid, stuname, avg, decode(avg,100,'만점') "상태" from students;

select * from employees;
select job_id from employees;
--sh clerk salary*0.02인상, ad asst 0.05인상, it prog 0.03인상, pu_clerk 0.04인상
select employee_id, emp_name, salary, job_id, decode(job_id, 'SH_CLERK',salary*1.02,
'AD_ASST',salary*1.05,
'IT_PROG',salary*1.03,
'PU_CLERK',salary*1.04) "월급인상현황" from employees;

--조건에 맞게 DECODE함수 이용해서 결과출력
select employee_id, emp_name, job_id, salary,decode(substr(job_id,instr(job_id,'_')+1),'CLERK',salary*1.05,
'MAN',salary*1.07,
'REP',salary*1.04,
'ACCOUNT',salary*1.06) "월급인상현황" from employees;

--조건 CASE함수 사용
select employee_id,emp_name, job_id,salary,
case 
when substr(job_id,4)='CLERK' then salary*0.05
when substr(job_id,4)='MAN' then salary*0.07
when substr(job_id,4)='REP' then salary*0.04
when substr(job_id,4)='ACCOUNT' then salary*0.06
end
as "월급인상현황" from employees;

--studata avg 90점 이상 A, 80점이상 B, 70점이상 C, 60점이상 D ==> "성적결과"
select * from studata;
select stuname, avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
end
as "성적결과" from studata;

select * from employees;
select count(*),count(manager_id), count(commission_pct) from employees; --null값은 count하지 않음
select count(*)-count(commission_pct) as "null count", count(commission_pct) "not null count" from employees;
select count(*) from employees where commission_pct is null;

select emp_name, sum(salary) from employees; --단일그룹은 그룹함수랑 같이 쓸 수 없음
select emp_name, sum(salary) from employees group by emp_name; --name은 공통으로 그룹이 묶일 수 있는 것이기 아니기 때문에 그룹함수의미 없음, 데이터가 그룹으로 묶일수 있는 데이터일때 group by를 사용하는 것이 유용함
select emp_name, salary from employees; --그룹이 없다면 굳이 그룹함수를 쓰는것은 의미가 없음

select department_id, count(*),to_char(avg(salary),999999.99) "평균 salary", sum(salary) from employees group by department_id;
select department_id, department_name from departments;

select department_id, max(salary), min(salary) from employees 
where department_id=50
group by department_id;

select * from employees;
select * from departments;
--60번 부서의 최대로 월급을 많이 받는 사람의 사번,이름,부서,월급을 출력하시오.
select employee_id, emp_name,department_id, salary from employees 
where salary =(select max(salary) from employees where department_id=60) and department_id=60;

--부서별, 전체인원, 커미션을 받는사람, 받지않는사람수
select department_id,count(*), count(commission_pct) "커미션을 받는사람", count(*)-count(commission_pct) "커피션을 받지않는 사람" from employees group by department_id;

--having
select department_id, avg(salary) from employees where department_id>40 
group by department_id having avg(salary)>=4000 order by department_id;  --그룹함수는 where절에 넣을 수 없음==> 일반함수조건식은 where절, 그룹함수조건식은 having절

--부서별 최대월급을 출력하는데, 5000달러 이상인 최대값만 출력하시오.
select department_id, max(salary) maxsalary from employees group by department_id having max(salary)>5000 order by maxsalary;

select department_id from employees;
select department_id, department_name from departments;


create table employees2 as
select department_id, department_name from departments;

select * from employees2;
update employees2 set department_name='기획부'
where department_id=10;
select * from departments; --employees2에서 수정했어도 departments에서 변하지 않음


select * from employees2, departments; --8개 컬럼이 나옴, row는 27*27개 나옴

--equi join : 동일한 컬럼을 가지고 검색
select employee_id, emp_name, e.department_id, department_name,salary, job_id
from employees e, departments d where e.department_id=d.department_id; --(foreign key=primary key로 주로 쓴다)

select * from employees;
select * from jobs;
select * from employees, jobs;
--euqi joint: employees, jobs 테이블
--employee_id, emp_name, job_id, job_title 넣어서 출력하시오.
select employee_id, emp_name, e.job_id, job_title from employees e, jobs j where e.job_id=j.job_id;


select * from board;
select * from membership;
-- bno, name, title, content, create_date, hit
--membership, board 조인해서 출력을 하시오.
select bno, name, title, content, b.create_date, hit 
from membership m, board b where m.id=b.id;

select * from employees;
select * from jobs;
select * from departments;
--테이블: employees,jobs,departments 3개 join
--컬럼: employee_id, job_id, job_title,department_id, department_name 출력하시오.
--조건: employee_id>150이상이면서, 이름이 s,S가 들어가 있는 사람만 출력하시오.
select e.employee_id, e.job_id, j.job_title, d.department_id, d.department_name 
from employees e, jobs j, departments d where e.job_id=j.job_id and e.department_id=d.department_id and e.employee_id>=150 
and lower(e.emp_name) like '%s%';

select e.employee_id, e.job_id, j.job_title, d.department_id, d.department_name 
from employees e, jobs j, departments d where e.job_id=j.job_id and e.department_id=d.department_id(+); --부서 null값이 있기때문에 106개 data나옴
--null값이 있는 곳에 +를 해주면 개수가 맞게 됨 ==> out join

--null값 찾기
select * from employees where department_id is null;


--게시판종류, 글번호, id, content, 날짜, 수정날짜
--이벤트 게시판 제작, 테이블 설계
--1. 이벤트 게시판에 들어갈 내용 검색
--2. 다른 이벤트 게시판에는 어떤 컬럼이 들어가는지 검색
--3. 테이블을 생성해보세요.

create table ebo1(
con number(1), --진행상태(진행중, 종료)
board_type varchar2(50), --게시판
board_num number(5) primary key, --게시물 고유번호
id varchar2(100), --사용자 아이디
title varchar2(100), -- 게시물제목
content clob, --게시물내용
content_date date, --작성날짜
star_date date, --이벤트시작날짜
end_date date, --이벤트종료날짜
hit number(5), --조회수
constraint bo_fk_id foreign key(id) references membership(id)
);


select * from kor_loan_status;
--region 지역별 대출총액을 출력하시오.
select region, sum(loan_jan_amt) "지역별 총액" from kor_loan_status group by region;

--4자리 년도만 가지고 년도별, 지역별 대출총액을 출력하시오.
select substr(period,0,4) newperiod, region, sum(loan_jan_amt) "대출총액" from kor_loan_status group by region, substr(period,0,4) order by sum(loan_jan_amt) desc;

create table salary_grade(
grade number(1),
low_salary number(5),
high_salary number(5)
);

select salary from employees order by salary;
insert into salary_grade values(
5,10001,30000);
commit;

--non-equi join 상관관계가 없는 테이블 서로 조인
select * from salary_grade;
select * from employees;

select employee_id,emp_name,salary, grade
from employees, salary_grade where salary between low_salary and high_salary order by employee_id;

select employee_id, emp_name, salary,
case when salary >=10001 then 5
when salary >=8001 then 4
when salary >=5001 then 3
when salary >=3001 then 2
when salary >=2001 then 1
end
as grade
from employees order by employee_id;


--studata, stu_grade stuno,stuname, grade 출력
--stu_grade (column: grade, low_score, high_score) 100-95:A+, 94-90:A, 89-85:B+, 84-80:B, 79-0:C 
create table stu_grade(
grade char(2),
low_score number(3),
high_score number(3)
);

insert into stu_grade values(
'C',0,79);

select stuno,stuname,avg,grade 
from studata,stu_grade where avg between low_score and high_score order by stuno;

--equi join
select employee_id, emp_name, e.department_id, department_name,salary, job_id
from employees e, departments d where e.department_id=d.department_id;

--self join : 자신 테이블 2개를 가지고 조인하는 것, equi join과 같음
select e1.employee_id, e1.emp_name, e1.manager_id, e2.emp_name
from employees e1, employees e2 
where e1.manager_id=e2.employee_id 
order by e1.employee_id;

--out join
select e1.employee_id, e1.emp_name, e1.manager_id, e2.emp_name
from employees e1, employees e2 
where e1.manager_id=e2.employee_id(+);
