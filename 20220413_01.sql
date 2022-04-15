select * from member;

--table타입확인
desc member; 

-- ora_user 가지고 있는 table
select * from tab;

--table부분 컬럼 출력
select id, password from member;

--employees테이블 salary 월급
select salary from employees;
--월급, 주급, 연봉
select salary, salary/5, salary*12 from employees; --써져있는 그대로 변수명으로 받게됨
--컬럼별칭선언
select salary, salary/5 as salary5, salary*12 as salary12 from employees; --컬럼명을 변경해줌 (as가 없어도 별칭이라고 인식가능함)
--**컬럼명은 대소문자 구분하지 않음, 단 ""로 대소문자구분해서 컬럼명을 만들어줄수 있음 ==> 대소문자구분해서 컬럼명을 만들었다면 select할때도 구분해서 조회해야함
select salary, salary/5 as "Salary5", salary*12 as salary12 from employees;

desc employees; 

select * from member;
select * from employees;

--order by: 순차정렬, order by desc: 해당컬럼 역순정렬 ==> desc에 따라서 정렬기준 달라짐
select * from employees order by employee_id desc;
--최대값, 최소값 (max, min)
select max(employee_id) from employees;
select min(employee_id) from employees;

select * from member;
--drop table member2;

select * from students;
select max(stuid)+1 from students;

--max+1 증가 insert
insert into students values(
(select max(stuid)+1 from students), '홍길자',100,100,100,100+100+100,(100+100+100)/3,0);

--**null은 무한대값이기 때문에 어떤값을 계산해도 어차피 무한대값이기 때문에 null이 나오게됨, null은 빈공간이 아님
select id,name,nvl(total,0)+10 from member; --nvl함수: null value일때 0으로 변경해서 계산하라는 의미


select * from employees;

-- 월급, 연봉, 실수령 연봉
select emp_name, 
salary*1230, salary*12*1230 as salary12, commission_pct,
salary*12*1230+(salary*12*1230*nvl(commission_pct,0)) as real_salary 
from employees; --nvl을 해주지않으면 실수령연봉계산시 salary*12*1230부분도 날라가서 전체값이 null이 나오게됨
-- nvl으로 null value을 0으로 변경해주어도 실제로 저장된 값은 null임, 단순히 계산의 오류를 방지하기 위해서 계산시 변경해주는 것 
-- 0이 아니여도 다른 숫자도 가능함

-- (밑변*높이)/2

create table triangle(
tno number(5) primary key,
base number(5,1),
height number(5,1),
area number(7,1)
);

--행추가
insert into triangle values(
1,10,5,10*5*0.5);
select * from triangle;

commit;
-- 3개 15,4 20,9 35,12
insert into triangle values(
(select max(tno)+1 from triangle),15,4,15*4*0.5);
insert into triangle values(
(select max(tno)+1 from triangle),20,9,20*9*0.5);
insert into triangle values(
(select max(tno)+1 from triangle),35,12,35*12*0.5);

select * from employees;
--사번,이름,이메일,전화번호,입사일 별칭을 사용해서 출력하시오.
select employee_id "사번", emp_name "이름", email "이메일", phone_number "전화번호", hire_date "입사일" from employees; --공백과 특수문자 삽입가능

select * from departments;
select department_id "부서번호", department_name "부서명" from departments;

--concatenation (||): (연결),두개의 컬럼을 하나로 합침
select * from employees;
select emp_name ||'의 직급 : ' || job_id  as jname from employees; --두컬럼이 하나의 컬럼으로 나옴

--distinct 중복제거
select department_id, department_name from departments; --270개
select department_id from employees; --107개
select distinct department_id from employees; --12개
select distinct department_id from employees order by department_id; --중복제거 및 순차정렬

select distinct job_id from employees;
select * from jobs;

select * from students;
select * from employees where employee_id>150; --비교해서 출력할수 있음
select emp_name,salary from employees where salary>3000 and salary<7000 order by salary;

-- 소문자 변환, 대문자 변환, 첫글자 대문자 변환
select * from employees where lower(emp_name)='susan mavris' or 
upper(emp_name)='SUSAN MAVRIS' or initcap(emp_name)='Susan Mavris'; 

select * from employees where initcap(emp_name)='Susan Mavris';

-- 특정문자가 포함된 검색: like
select emp_name from employees
where lower(emp_name) like '%su%'; --su%: 처음시작, %su%: 중간, %su: 끝

select * from employees where department_id=20;

--급여가 4000이하, 부서번호가 30
select employee_id, emp_name,salary from employees where salary<=4000 and department_id=30 order by salary; 

select * from employees;
--문자와 날짜인 경우에는 ''안에 넣음
select email from employees where email>='PFAY';
select hire_date from employees where hire_date='07/06/21'; --날짜 검색
select hire_date from employees where hire_date>='07/06/21'; 
--2000/01/01 이후 입사일인 사원을 출력하시오. 날짜 포맷지정(형식수정)
select to_char(hire_date,'YYYY/MM/DD') from employees where hire_date>='2000/01/01' order by hire_date;

--not 검색
select * from employees where not department_id=10;
select * from employees where department_id !=10;
select * from employees where department_id <>10;
select * from employees where department_id ^=10;

--3000이상 7000이하 검색출력
select salary from employees where salary>=3000 and salary<=7000 order by salary;
select salary from employees where salary between 3000 and 7000 order by salary; --between은 작거나 같다의 '같다'를 무조건 포함함 (해당 숫자를 무조건 포함함)

select * from employees;
--commission_pct가 0.1이거나 0.2이거나 0.3
select commission_pct from employees where commission_pct=0.1 or commission_pct=0.2 or commission_pct=0.3;

-- studata 테이블 생성
create table studata (
	stuno number(4),
	stuname VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(5,2),
	avg number(5,2),
	rank number
);
insert into studata (stuno, stuname, kor, eng, math, total, avg, rank) values (1, 'Billingsley', 84, 87, 95, 266, 88.67, 0);

select * from studata;
commit;

--국어 90이상 영어 90이상 수학 90이상 학생출력
select * from studata where kor>=90 and eng>=90 and math>=90;

--국어 90이상 100이하 학생출력
select * from studata where kor>=80 and kor<=90;
select * from studata where kor between 80 and 90;

select * from studata where kor not between 80 and 90;

--사원번호 120, 130,140인 사원을 출력하시오.
select * from employees where employee_id=120 or employee_id=130 or employee_id=140;
--in 연산자 : 동일한 필드 검색 / not in: 지정된 검색어를 제외하고 검색됨
select * from employees where employee_id in(120,130,140,150,160);

--사원번호가 130이상이면서 salary가 3000이상 5000이하인 사원을 출력하시오.
select employee_id, salary from employees where employee_id>=130 and salary between 3000 and 5000 order by employee_id;

select * from employees where not (salary>=3000 and salary<=5000);
select * from employees where not salary between 3000 and 5000;

select * from employees where hire_date between '95/01/01' and '02/12/31' order by hire_date; 

select hire_date,hire_date+10 from employees;
-- 날짜 데이터 사칙연산 가능, daul 가상테이블
select '2020/01/01',to_date('2020/01/01')+100 from Dual;
select sysdate,sysdate+100 from Dual; --sysdate는 현재날짜를 나타냄, 화면으로 출력해주는 테이블(임시테이블이라고 생각하면 됨)

--total 270,280,290인 학생 출력 studata;
select * from studata where total in (270,280,290);

select * from studata;
--like 검색: %, _
select * from studata where stuname like '__ll%'; --언더바(_)개수를 통해서 몇번째 자리의 지정검색어를 검색하고 싶은지 정할 수 있음
select * from studata where stuname like '%l_'; -- 뒤에서 두번째 자리를 지정해줌

--대문자 S로 시작되는 학생검색
select * from studata where stuname like 'S%';

--3자리에 l로 시작하는 학생검색
select * from studata where stuname like '__l%';


--1. employees 끝자리 n으로 끝나는 사원출력
select * from employees where emp_name like '%n';
--2. 시작이 s,S로 시작되는 사원 출력
select * from employees where emp_name like '%s%' or emp_name like '%S%'; 

--두번째 문자가 a가 포함되어 있는 학생검색
select * from studata where stuname not like '_a%';

-- null인 경우 검색 : is null, is not null
select * from employees where commission_pct=null; -- null은 부등호로 비교할수가 없음
select * from employees where commission_pct is not null;

update member set total=null where id='aaa';
select * from member;

create table studata2 as select * from studata; --모든 데이터를 복사하여 테이블을 새로 만들어줌

select * from studata2;
update studata2 set total=0;
update studata2 set avg=0;
commit;

update studata2 set total=kor+eng+math;
update studata2 set avg=total/3;

--delete studata2;
select * from studata2;
commit;
desc studata2;
--테이블삭제
--drop table employees2;

--테이블 타입만 복재생성
create table studata2 as select * from studata where 1=2;

--studata의 모든 테이터를 studata에 복제
insert into studata2 select * from studata;
--delete studata2;
commit;

--rank 채우는 방법
--studata의 컬럼을 선택해서 데이터를 studata2에 복사 (studata의 일부 컬럼데이터를 studata2에 복제)
select stuno, stuname,rank() over(order by total desc) rank from studata order by total desc;
insert into studata2(stuno, stuname,kor,eng,math,total, avg) select stuno, stuname,kor,eng,math,total,avg from studata;  --데이터복사
insert into studata2(stuno, stuname,kor,eng,math,total, avg, rank) select stuno, stuname,kor,eng,math,total,avg, rank() over (order by total desc) rank from studata;-- 무엇으로 rank를 채워줄것인냐는 over()를 통해서 채워주면 됨

select * from studata2 order by stuno;

--updata studata
update (select * from studata order by total desc) set rank=1;
select * from studata order by total desc;

-- order by 정렬, asc순차정렬, desc 역순정렬
select employee_id from employees;
select salary from employees order by salary desc;

--employees2테이블: employee_id, emp_name, salary, rank
--employees의 모든 테이터를 employees2에 넣을것, salary를 가지고 rank 할 것
create table employees2 as select employee_id, emp_name, salary from employees where 1=2;
select * from employees2;
--delete employees2;
commit;
desc employees2;
alter table employees2 add rank number(4); --rank 컬럼 추가

insert into employees2 select employee_id, emp_name,salary,rank() over(order by salary desc) rank from employees order by salary desc;
select * from employees2 order by employee_id desc;

--부서번호는 순차정렬, salary는 역순정렬로 정렬을 해주세요.
select * from employees order by department_id, salary desc;

--사원번호 순차정렬, 부서내에서 입사순서 순차정렬
select employee_id, department_id, hire_date from employees order by employee_id asc, department_id asc, hire_date desc;

--abs함수: 절대값
select -10, abs(-10) from dual;
--floor: 소수점 버림
select floor(10.3456) from dual;
--round: 해당소수점 반올림
select round(10.3456,2) from dual;
--정수 첫째자리에서 반올림
select round(277.4567,-1) from dual;

select * from studata;
--mod나머지: 학번이 홀수 번호만 출력
select * from studata where mod(stuno,2)=1; --mod: 나머지

--사원번호가 짝수번호만 출력하세요.
select * from employees where mod(employee_id,2)=0 order by employee_id;

--
--drop table employees2;

--employees2 table todtjd employee_id, emp_name, salary, rank 사원번호가 홀수 인것만
--추가해서 테이블 생성해보세요.
create table employees2 as select employee_id, emp_name, salary from employees where 1=2;
select * from employees2;
alter table employees2 add rank number(4);
insert into employees2 select employee_id, emp_name, salary, rank() over(order by salary desc) rank from employees where mod(employee_id,2)=1 order by employee_id;

commit;

select * from students2;
insert into students values(
(select max(stuid)+1 from students),'이유신',100,100,100,300,100,0);

--시퀀스 이름 생성
CREATE SEQUENCE TEST_SEQ
    START WITH 1
INCREMENT BY 1
MINVALUE 1
MAXVALUE 99999
CYCLE
CACHE 10;

--nextval: 현재시퀀스 다음번호를 가져옴, currval: 현재번호를 가져옴.
create table students2 as select * from students where 1=2;
insert into students2 values(
board_seq.nextval, '김유신', 100,100,100,(100+100+100),(100+100+100)/3,0);

select board_seq.currval from dual;

select board_seq.nextval from dual; --한번 nextval을 해버리면 insert할때 영향을 미침, 무결성에서 유니크하지않기때문에 back이 되지않음

--시작값이 1이고 1씩 증가하고, 최대값이 100000이 되는 시퀀스 EMP_SEQ생성
CREATE SEQUENCE EMP_SEQ
    START WITH 1
INCREMENT BY 1
minvalue 1
MAXVALUE 10000;

--emp01 테이블 생성
--empno, employee_id, emp_name,salary
--empno emp_seq 생성해서 추가, 나머지 컬럼 employees의 내용을 입력하시오.
create table emp01 as select employee_id, emp_name, salary from employees where 1=2;
alter table emp01 add empno number(5);
insert into emp01 select employee_id, emp_name, salary, emp_seq.nextval from employees;

select * from emp02;
--emp02 empno, employee_id, emp_name, salary
--emp01에서 데이터 복사
create table emp02 as select empno, employee_id, emp_name, salary from emp01;