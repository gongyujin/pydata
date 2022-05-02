select * from tab;

--drop table emp02;
--drop table employees2;
--drop table students2;

rename studata2 to sturank; -- �̸�����

--id�� ����, foregin key�� ����Ǿ� ����
select * from board;
select * from membership;

--���࿡ membership�� ���Ե������� id���� board�� �Է��ؼ� �����ϸ� ���Ἲ�������ǿ� �����
insert into board values(
board_seq.nextval, 'ccc','�̺�Ʈ �����մϴ�.','�̺�Ʈ ��ǰ�� �����մϴ�.',sysdate,1);

create table emp02(
empno number(4) primary key,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2) check(deptno between 10 and 19),
gender char(1) check(gender in ('M','F'))
);

insert into emp02 values(
emp_seq.nextval, 'ȫ�浿','manager',10,'M');

insert into emp02 values(
emp_seq.nextval, 'ȫ����','manager',10,'F'); --check�������ǿ� ���缭 �����ؾ��� 

insert into emp02 values(
emp_seq.nextval, 'ȫ���','manager',18,'F'); 

insert into emp02 values(
emp_seq.nextval, 'ȫ���','manager',18,'D'); 

select * from emp02;
desc emp02;

select emp_seq.currval from dual; --nextval�� �̿��ؼ� ���������� �߸��� �����̿��� ī��Ʈ�� ��


--employees���̺��� �����Ͽ� emp01 ���̺� ����
--employee_id�� primary key
--emp_name�� unique
--salary not null
--manager_id
--department_id
--107���� �����͸� �Է��Ͻÿ�.

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

--foreign key ���
--����: index �� mem_fk_id, �ܷ�Ű(�÷�) ��ġ membership���̺� id
--constraint mem_fk_id foreign key(id) references membership(id)
alter table emp01
add constraint departments_fk_id foreign key(department_id) 
references departments(department_id);

--primary key ����
alter table emp01 drop primary key;
--primary key ����
alter table emp01 add primary key(employee_id);


select * from students;

select * from studata;

select * from membership;

select * from sturank order by stuno;
update sturank set stuname='eee' where stuno=5;
--1. membership id primary key ���
alter table membership add primary key(id);
--2. sturank fk ���
alter table sturank add constraint stu_fk_id foreign key(stuname)
references membership(id);

alter table sturank rename column stuname to id;

desc sturank;

--delete sturank where stuno>5;

select * from employees;

--�� (decode): if���̶� ���� ����
select emp_name, department_id, 
decode(department_id,20,'�������',
30,'��������',
40,'��������',
50,'��������') "����Ȯ��" from employees;

select * from students;
select stuid, stuname, avg, decode(avg,100,'����') "����" from students;

select * from employees;
select job_id from employees;
--sh clerk salary*0.02�λ�, ad asst 0.05�λ�, it prog 0.03�λ�, pu_clerk 0.04�λ�
select employee_id, emp_name, salary, job_id, decode(job_id, 'SH_CLERK',salary*1.02,
'AD_ASST',salary*1.05,
'IT_PROG',salary*1.03,
'PU_CLERK',salary*1.04) "�����λ���Ȳ" from employees;

--���ǿ� �°� DECODE�Լ� �̿��ؼ� ������
select employee_id, emp_name, job_id, salary,decode(substr(job_id,instr(job_id,'_')+1),'CLERK',salary*1.05,
'MAN',salary*1.07,
'REP',salary*1.04,
'ACCOUNT',salary*1.06) "�����λ���Ȳ" from employees;

--���� CASE�Լ� ���
select employee_id,emp_name, job_id,salary,
case 
when substr(job_id,4)='CLERK' then salary*0.05
when substr(job_id,4)='MAN' then salary*0.07
when substr(job_id,4)='REP' then salary*0.04
when substr(job_id,4)='ACCOUNT' then salary*0.06
end
as "�����λ���Ȳ" from employees;

--studata avg 90�� �̻� A, 80���̻� B, 70���̻� C, 60���̻� D ==> "�������"
select * from studata;
select stuname, avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
end
as "�������" from studata;

select * from employees;
select count(*),count(manager_id), count(commission_pct) from employees; --null���� count���� ����
select count(*)-count(commission_pct) as "null count", count(commission_pct) "not null count" from employees;
select count(*) from employees where commission_pct is null;

select emp_name, sum(salary) from employees; --���ϱ׷��� �׷��Լ��� ���� �� �� ����
select emp_name, sum(salary) from employees group by emp_name; --name�� �������� �׷��� ���� �� �ִ� ���̱� �ƴϱ� ������ �׷��Լ��ǹ� ����, �����Ͱ� �׷����� ���ϼ� �ִ� �������϶� group by�� ����ϴ� ���� ������
select emp_name, salary from employees; --�׷��� ���ٸ� ���� �׷��Լ��� ���°��� �ǹ̰� ����

select department_id, count(*),to_char(avg(salary),999999.99) "��� salary", sum(salary) from employees group by department_id;
select department_id, department_name from departments;

select department_id, max(salary), min(salary) from employees 
where department_id=50
group by department_id;

select * from employees;
select * from departments;
--60�� �μ��� �ִ�� ������ ���� �޴� ����� ���,�̸�,�μ�,������ ����Ͻÿ�.
select employee_id, emp_name,department_id, salary from employees 
where salary =(select max(salary) from employees where department_id=60) and department_id=60;

--�μ���, ��ü�ο�, Ŀ�̼��� �޴»��, �����ʴ»����
select department_id,count(*), count(commission_pct) "Ŀ�̼��� �޴»��", count(*)-count(commission_pct) "Ŀ�Ǽ��� �����ʴ� ���" from employees group by department_id;

--having
select department_id, avg(salary) from employees where department_id>40 
group by department_id having avg(salary)>=4000 order by department_id;  --�׷��Լ��� where���� ���� �� ����==> �Ϲ��Լ����ǽ��� where��, �׷��Լ����ǽ��� having��

--�μ��� �ִ������ ����ϴµ�, 5000�޷� �̻��� �ִ밪�� ����Ͻÿ�.
select department_id, max(salary) maxsalary from employees group by department_id having max(salary)>5000 order by maxsalary;

select department_id from employees;
select department_id, department_name from departments;


create table employees2 as
select department_id, department_name from departments;

select * from employees2;
update employees2 set department_name='��ȹ��'
where department_id=10;
select * from departments; --employees2���� �����߾ departments���� ������ ����


select * from employees2, departments; --8�� �÷��� ����, row�� 27*27�� ����

--equi join : ������ �÷��� ������ �˻�
select employee_id, emp_name, e.department_id, department_name,salary, job_id
from employees e, departments d where e.department_id=d.department_id; --(foreign key=primary key�� �ַ� ����)

select * from employees;
select * from jobs;
select * from employees, jobs;
--euqi joint: employees, jobs ���̺�
--employee_id, emp_name, job_id, job_title �־ ����Ͻÿ�.
select employee_id, emp_name, e.job_id, job_title from employees e, jobs j where e.job_id=j.job_id;


select * from board;
select * from membership;
-- bno, name, title, content, create_date, hit
--membership, board �����ؼ� ����� �Ͻÿ�.
select bno, name, title, content, b.create_date, hit 
from membership m, board b where m.id=b.id;

select * from employees;
select * from jobs;
select * from departments;
--���̺�: employees,jobs,departments 3�� join
--�÷�: employee_id, job_id, job_title,department_id, department_name ����Ͻÿ�.
--����: employee_id>150�̻��̸鼭, �̸��� s,S�� �� �ִ� ����� ����Ͻÿ�.
select e.employee_id, e.job_id, j.job_title, d.department_id, d.department_name 
from employees e, jobs j, departments d where e.job_id=j.job_id and e.department_id=d.department_id and e.employee_id>=150 
and lower(e.emp_name) like '%s%';

select e.employee_id, e.job_id, j.job_title, d.department_id, d.department_name 
from employees e, jobs j, departments d where e.job_id=j.job_id and e.department_id=d.department_id(+); --�μ� null���� �ֱ⶧���� 106�� data����
--null���� �ִ� ���� +�� ���ָ� ������ �°� �� ==> out join

--null�� ã��
select * from employees where department_id is null;


--�Խ�������, �۹�ȣ, id, content, ��¥, ������¥
--�̺�Ʈ �Խ��� ����, ���̺� ����
--1. �̺�Ʈ �Խ��ǿ� �� ���� �˻�
--2. �ٸ� �̺�Ʈ �Խ��ǿ��� � �÷��� ������ �˻�
--3. ���̺��� �����غ�����.

create table ebo1(
con number(1), --�������(������, ����)
board_type varchar2(50), --�Խ���
board_num number(5) primary key, --�Խù� ������ȣ
id varchar2(100), --����� ���̵�
title varchar2(100), -- �Խù�����
content clob, --�Խù�����
content_date date, --�ۼ���¥
star_date date, --�̺�Ʈ���۳�¥
end_date date, --�̺�Ʈ���ᳯ¥
hit number(5), --��ȸ��
constraint bo_fk_id foreign key(id) references membership(id)
);


select * from kor_loan_status;
--region ������ �����Ѿ��� ����Ͻÿ�.
select region, sum(loan_jan_amt) "������ �Ѿ�" from kor_loan_status group by region;

--4�ڸ� �⵵�� ������ �⵵��, ������ �����Ѿ��� ����Ͻÿ�.
select substr(period,0,4) newperiod, region, sum(loan_jan_amt) "�����Ѿ�" from kor_loan_status group by region, substr(period,0,4) order by sum(loan_jan_amt) desc;

create table salary_grade(
grade number(1),
low_salary number(5),
high_salary number(5)
);

select salary from employees order by salary;
insert into salary_grade values(
5,10001,30000);
commit;

--non-equi join ������谡 ���� ���̺� ���� ����
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


--studata, stu_grade stuno,stuname, grade ���
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

--self join : �ڽ� ���̺� 2���� ������ �����ϴ� ��, equi join�� ����
select e1.employee_id, e1.emp_name, e1.manager_id, e2.emp_name
from employees e1, employees e2 
where e1.manager_id=e2.employee_id 
order by e1.employee_id;

--out join
select e1.employee_id, e1.emp_name, e1.manager_id, e2.emp_name
from employees e1, employees e2 
where e1.manager_id=e2.employee_id(+);
