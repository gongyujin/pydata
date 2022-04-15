select * from member;

--tableŸ��Ȯ��
desc member; 

-- ora_user ������ �ִ� table
select * from tab;

--table�κ� �÷� ���
select id, password from member;

--employees���̺� salary ����
select salary from employees;
--����, �ֱ�, ����
select salary, salary/5, salary*12 from employees; --�����ִ� �״�� ���������� �ްԵ�
--�÷���Ī����
select salary, salary/5 as salary5, salary*12 as salary12 from employees; --�÷����� �������� (as�� ��� ��Ī�̶�� �νİ�����)
--**�÷����� ��ҹ��� �������� ����, �� ""�� ��ҹ��ڱ����ؼ� �÷����� ������ټ� ���� ==> ��ҹ��ڱ����ؼ� �÷����� ������ٸ� select�Ҷ��� �����ؼ� ��ȸ�ؾ���
select salary, salary/5 as "Salary5", salary*12 as salary12 from employees;

desc employees; 

select * from member;
select * from employees;

--order by: ��������, order by desc: �ش��÷� �������� ==> desc�� ���� ���ı��� �޶���
select * from employees order by employee_id desc;
--�ִ밪, �ּҰ� (max, min)
select max(employee_id) from employees;
select min(employee_id) from employees;

select * from member;
--drop table member2;

select * from students;
select max(stuid)+1 from students;

--max+1 ���� insert
insert into students values(
(select max(stuid)+1 from students), 'ȫ����',100,100,100,100+100+100,(100+100+100)/3,0);

--**null�� ���Ѵ밪�̱� ������ ����� ����ص� ������ ���Ѵ밪�̱� ������ null�� �����Ե�, null�� ������� �ƴ�
select id,name,nvl(total,0)+10 from member; --nvl�Լ�: null value�϶� 0���� �����ؼ� ����϶�� �ǹ�


select * from employees;

-- ����, ����, �Ǽ��� ����
select emp_name, 
salary*1230, salary*12*1230 as salary12, commission_pct,
salary*12*1230+(salary*12*1230*nvl(commission_pct,0)) as real_salary 
from employees; --nvl�� ������������ �Ǽ��ɿ������� salary*12*1230�κе� ���󰡼� ��ü���� null�� �����Ե�
-- nvl���� null value�� 0���� �������־ ������ ����� ���� null��, �ܼ��� ����� ������ �����ϱ� ���ؼ� ���� �������ִ� �� 
-- 0�� �ƴϿ��� �ٸ� ���ڵ� ������

-- (�غ�*����)/2

create table triangle(
tno number(5) primary key,
base number(5,1),
height number(5,1),
area number(7,1)
);

--���߰�
insert into triangle values(
1,10,5,10*5*0.5);
select * from triangle;

commit;
-- 3�� 15,4 20,9 35,12
insert into triangle values(
(select max(tno)+1 from triangle),15,4,15*4*0.5);
insert into triangle values(
(select max(tno)+1 from triangle),20,9,20*9*0.5);
insert into triangle values(
(select max(tno)+1 from triangle),35,12,35*12*0.5);

select * from employees;
--���,�̸�,�̸���,��ȭ��ȣ,�Ի��� ��Ī�� ����ؼ� ����Ͻÿ�.
select employee_id "���", emp_name "�̸�", email "�̸���", phone_number "��ȭ��ȣ", hire_date "�Ի���" from employees; --����� Ư������ ���԰���

select * from departments;
select department_id "�μ���ȣ", department_name "�μ���" from departments;

--concatenation (||): (����),�ΰ��� �÷��� �ϳ��� ��ħ
select * from employees;
select emp_name ||'�� ���� : ' || job_id  as jname from employees; --���÷��� �ϳ��� �÷����� ����

--distinct �ߺ�����
select department_id, department_name from departments; --270��
select department_id from employees; --107��
select distinct department_id from employees; --12��
select distinct department_id from employees order by department_id; --�ߺ����� �� ��������

select distinct job_id from employees;
select * from jobs;

select * from students;
select * from employees where employee_id>150; --���ؼ� ����Ҽ� ����
select emp_name,salary from employees where salary>3000 and salary<7000 order by salary;

-- �ҹ��� ��ȯ, �빮�� ��ȯ, ù���� �빮�� ��ȯ
select * from employees where lower(emp_name)='susan mavris' or 
upper(emp_name)='SUSAN MAVRIS' or initcap(emp_name)='Susan Mavris'; 

select * from employees where initcap(emp_name)='Susan Mavris';

-- Ư�����ڰ� ���Ե� �˻�: like
select emp_name from employees
where lower(emp_name) like '%su%'; --su%: ó������, %su%: �߰�, %su: ��

select * from employees where department_id=20;

--�޿��� 4000����, �μ���ȣ�� 30
select employee_id, emp_name,salary from employees where salary<=4000 and department_id=30 order by salary; 

select * from employees;
--���ڿ� ��¥�� ��쿡�� ''�ȿ� ����
select email from employees where email>='PFAY';
select hire_date from employees where hire_date='07/06/21'; --��¥ �˻�
select hire_date from employees where hire_date>='07/06/21'; 
--2000/01/01 ���� �Ի����� ����� ����Ͻÿ�. ��¥ ��������(���ļ���)
select to_char(hire_date,'YYYY/MM/DD') from employees where hire_date>='2000/01/01' order by hire_date;

--not �˻�
select * from employees where not department_id=10;
select * from employees where department_id !=10;
select * from employees where department_id <>10;
select * from employees where department_id ^=10;

--3000�̻� 7000���� �˻����
select salary from employees where salary>=3000 and salary<=7000 order by salary;
select salary from employees where salary between 3000 and 7000 order by salary; --between�� �۰ų� ������ '����'�� ������ ������ (�ش� ���ڸ� ������ ������)

select * from employees;
--commission_pct�� 0.1�̰ų� 0.2�̰ų� 0.3
select commission_pct from employees where commission_pct=0.1 or commission_pct=0.2 or commission_pct=0.3;

-- studata ���̺� ����
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

--���� 90�̻� ���� 90�̻� ���� 90�̻� �л����
select * from studata where kor>=90 and eng>=90 and math>=90;

--���� 90�̻� 100���� �л����
select * from studata where kor>=80 and kor<=90;
select * from studata where kor between 80 and 90;

select * from studata where kor not between 80 and 90;

--�����ȣ 120, 130,140�� ����� ����Ͻÿ�.
select * from employees where employee_id=120 or employee_id=130 or employee_id=140;
--in ������ : ������ �ʵ� �˻� / not in: ������ �˻�� �����ϰ� �˻���
select * from employees where employee_id in(120,130,140,150,160);

--�����ȣ�� 130�̻��̸鼭 salary�� 3000�̻� 5000������ ����� ����Ͻÿ�.
select employee_id, salary from employees where employee_id>=130 and salary between 3000 and 5000 order by employee_id;

select * from employees where not (salary>=3000 and salary<=5000);
select * from employees where not salary between 3000 and 5000;

select * from employees where hire_date between '95/01/01' and '02/12/31' order by hire_date; 

select hire_date,hire_date+10 from employees;
-- ��¥ ������ ��Ģ���� ����, daul �������̺�
select '2020/01/01',to_date('2020/01/01')+100 from Dual;
select sysdate,sysdate+100 from Dual; --sysdate�� ���糯¥�� ��Ÿ��, ȭ������ ������ִ� ���̺�(�ӽ����̺��̶�� �����ϸ� ��)

--total 270,280,290�� �л� ��� studata;
select * from studata where total in (270,280,290);

select * from studata;
--like �˻�: %, _
select * from studata where stuname like '__ll%'; --�����(_)������ ���ؼ� ���° �ڸ��� �����˻�� �˻��ϰ� ������ ���� �� ����
select * from studata where stuname like '%l_'; -- �ڿ��� �ι�° �ڸ��� ��������

--�빮�� S�� ���۵Ǵ� �л��˻�
select * from studata where stuname like 'S%';

--3�ڸ��� l�� �����ϴ� �л��˻�
select * from studata where stuname like '__l%';


--1. employees ���ڸ� n���� ������ ������
select * from employees where emp_name like '%n';
--2. ������ s,S�� ���۵Ǵ� ��� ���
select * from employees where emp_name like '%s%' or emp_name like '%S%'; 

--�ι�° ���ڰ� a�� ���ԵǾ� �ִ� �л��˻�
select * from studata where stuname not like '_a%';

-- null�� ��� �˻� : is null, is not null
select * from employees where commission_pct=null; -- null�� �ε�ȣ�� ���Ҽ��� ����
select * from employees where commission_pct is not null;

update member set total=null where id='aaa';
select * from member;

create table studata2 as select * from studata; --��� �����͸� �����Ͽ� ���̺��� ���� �������

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
--���̺����
--drop table employees2;

--���̺� Ÿ�Ը� �������
create table studata2 as select * from studata where 1=2;

--studata�� ��� �����͸� studata�� ����
insert into studata2 select * from studata;
--delete studata2;
commit;

--rank ä��� ���
--studata�� �÷��� �����ؼ� �����͸� studata2�� ���� (studata�� �Ϻ� �÷������͸� studata2�� ����)
select stuno, stuname,rank() over(order by total desc) rank from studata order by total desc;
insert into studata2(stuno, stuname,kor,eng,math,total, avg) select stuno, stuname,kor,eng,math,total,avg from studata;  --�����ͺ���
insert into studata2(stuno, stuname,kor,eng,math,total, avg, rank) select stuno, stuname,kor,eng,math,total,avg, rank() over (order by total desc) rank from studata;-- �������� rank�� ä���ٰ��γĴ� over()�� ���ؼ� ä���ָ� ��

select * from studata2 order by stuno;

--updata studata
update (select * from studata order by total desc) set rank=1;
select * from studata order by total desc;

-- order by ����, asc��������, desc ��������
select employee_id from employees;
select salary from employees order by salary desc;

--employees2���̺�: employee_id, emp_name, salary, rank
--employees�� ��� �����͸� employees2�� ������, salary�� ������ rank �� ��
create table employees2 as select employee_id, emp_name, salary from employees where 1=2;
select * from employees2;
--delete employees2;
commit;
desc employees2;
alter table employees2 add rank number(4); --rank �÷� �߰�

insert into employees2 select employee_id, emp_name,salary,rank() over(order by salary desc) rank from employees order by salary desc;
select * from employees2 order by employee_id desc;

--�μ���ȣ�� ��������, salary�� �������ķ� ������ ���ּ���.
select * from employees order by department_id, salary desc;

--�����ȣ ��������, �μ������� �Ի���� ��������
select employee_id, department_id, hire_date from employees order by employee_id asc, department_id asc, hire_date desc;

--abs�Լ�: ���밪
select -10, abs(-10) from dual;
--floor: �Ҽ��� ����
select floor(10.3456) from dual;
--round: �ش�Ҽ��� �ݿø�
select round(10.3456,2) from dual;
--���� ù°�ڸ����� �ݿø�
select round(277.4567,-1) from dual;

select * from studata;
--mod������: �й��� Ȧ�� ��ȣ�� ���
select * from studata where mod(stuno,2)=1; --mod: ������

--�����ȣ�� ¦����ȣ�� ����ϼ���.
select * from employees where mod(employee_id,2)=0 order by employee_id;

--
--drop table employees2;

--employees2 table todtjd employee_id, emp_name, salary, rank �����ȣ�� Ȧ�� �ΰ͸�
--�߰��ؼ� ���̺� �����غ�����.
create table employees2 as select employee_id, emp_name, salary from employees where 1=2;
select * from employees2;
alter table employees2 add rank number(4);
insert into employees2 select employee_id, emp_name, salary, rank() over(order by salary desc) rank from employees where mod(employee_id,2)=1 order by employee_id;

commit;

select * from students2;
insert into students values(
(select max(stuid)+1 from students),'������',100,100,100,300,100,0);

--������ �̸� ����
CREATE SEQUENCE TEST_SEQ
    START WITH 1
INCREMENT BY 1
MINVALUE 1
MAXVALUE 99999
CYCLE
CACHE 10;

--nextval: ��������� ������ȣ�� ������, currval: �����ȣ�� ������.
create table students2 as select * from students where 1=2;
insert into students2 values(
board_seq.nextval, '������', 100,100,100,(100+100+100),(100+100+100)/3,0);

select board_seq.currval from dual;

select board_seq.nextval from dual; --�ѹ� nextval�� �ع����� insert�Ҷ� ������ ��ħ, ���Ἲ���� ����ũ�����ʱ⶧���� back�� ��������

--���۰��� 1�̰� 1�� �����ϰ�, �ִ밪�� 100000�� �Ǵ� ������ EMP_SEQ����
CREATE SEQUENCE EMP_SEQ
    START WITH 1
INCREMENT BY 1
minvalue 1
MAXVALUE 10000;

--emp01 ���̺� ����
--empno, employee_id, emp_name,salary
--empno emp_seq �����ؼ� �߰�, ������ �÷� employees�� ������ �Է��Ͻÿ�.
create table emp01 as select employee_id, emp_name, salary from employees where 1=2;
alter table emp01 add empno number(5);
insert into emp01 select employee_id, emp_name, salary, emp_seq.nextval from employees;

select * from emp02;
--emp02 empno, employee_id, emp_name, salary
--emp01���� ������ ����
create table emp02 as select empno, employee_id, emp_name, salary from emp01;