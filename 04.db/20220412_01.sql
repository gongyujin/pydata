--alter session set "_ORACLE_SCRIPT"=true; ������ �ٲ���
--
--create user ora_user identified by 1234; ���� ora_user�� 1234�� ��й�ȣ�� ���� ������ ����(����ڻ���)
--
--grant connect,resource,dba to ora_user; connect�� ������������ ora_user�� ������ �� ����(���Ѻο�)
--
--
--<����Ŭ ����>
---���̺����-
--* varchart2�� �����̱� ������ ������ ������ ũ�� ������������, �ѱ�(3byte)�� 10���� ���� �ʹٸ� �⺻ 30byte�� �����;���
--* char�� �����̱� ������ ������ ���Ƶ� ��������� ���ܵ�
--* number: ���ڿ� ���� (�Ǽ�, ���� ��� �ش���)
--
--insert into member(id,pw,name,phone) values(
--'aaa','1111','ȫ�浿','010-1111-1111'); // ���������� ������� ���� ���� ==> �ܺ�(cmdâ)���� �����ϸ� ��Ÿ��������
--
--commit; // DB�� Ȯ���� ��������� (Ŀ���� ���������� ���� ������)
--==> commit�ϸ� db�� �����ϴ¼��� �޸𸮸� ����������
--
--rollback; // ����� �޸𸮸� ������, commit������ ������
--
--** primary key�� �ߺ��ؼ� �ְ� �Ǹ� ���Ἲ ���� ���ǿ� �����
--** null�� ������� �ǹ��ϴ°� �ƴ�
--
--** �ش絥���͸� Ŭ���ؼ� ���������� ���캸�� primary key�� �������� �˼� ����


select * from employees;

select * from departments;

select job_id, job_title, min_salary, max_salary, create_date, update_date  from jobs;

create table member(
id varchar2(20) primary key,
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

desc member; --�����Ͱ� � ���·� ����ִ��� ������

select * from tab;
select * from member;

commit;
rollback;

select * from member;

-- insert ���1: ��� �÷��� �� �ִ� ��
insert into member(id,pw,name,phone) values(
'aaa','1111','ȫ�浿','010-1111-1111');

-- insert ���2: �÷��� ��������
insert into member values(
'ccc','1111','�̼���','010-2222-2222');
insert into member values(
'aaa','1234','������','010-3333-3333');

select * from member;
commit;

-- insert ���3: �κ������� �̿밡��
insert into member(id,pw) values(
'ddd','�豸');

insert into member values(
'eee','1111','������','010-3333-3333');

select * from member;
rollback;

insert into member(id,pw,name) values(
'fff','1111','������');


select name, phone from member;

select * from employees;

select emp_name,job_id from employees;
desc employees; --Ÿ���� ��� �Ǿ��ִ��� �˼� ����--

delete from member; --��� ���̺� ����
select * from member; --���̺��� �� ����
rollback; --�ٽ� ����
select * from member; --���̺� �ٽ� ����

delete from member where id='bbb'; --��ġ�� ã������ �ַ� primary key�� ����ؼ� ������ ����, �ߺ��� �����ϱ� ���ؼ� primary key�� ���

--end ���� ��밡����, where���� ã�� �Ǵµ� �ϳ��� ã������ �ְ� �ε�ȣ�� and�� ����Ͽ� �������� ã�� �� ����
select employee_id, emp_name, salary from employees where employee_id>=150 and salary>4000;

 insert into member values(
 'eee','1111','������','010-5555-5555');
 
 commit;
 rollback;
 
 --�˻�
 select * from employees;
 --����
 delete from member;
 --���뺯��(����)
 update member set phone='010-7777-7777' where id='bbb';

 
 --�Ҽ��� �ڸ� ���ڸ��� �����ؼ� �� 4�ڸ�
create table member2 (
id varchar2(20),
pw number(4),
kor number(4,1)
); 

insert into member2 values(
'aaa',1111,99.9);

commit;

select * from member2;

 --students ���̺� ����
 --stuid,stuname,kor,eng,math,total,avg,rank
 --varchar2(20),number(3),number(4,1)
 --5���� �л��� �Է��غ�����.
 
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
 'aaa','ȫ�浿',100,100,100,100+100+100,(100+100+100)/3);
 
 select * from students;
  insert into students(stuid,stuname,kor,eng,math,total,avg) values(
 'bbb','�̼���',99,99,99,99+99+99,(99+99+99)/3);
  insert into students(stuid,stuname,kor,eng,math,total,avg) values(
 'ccc','������',100,99,98,100+99+98,(100+99+98)/3);
  insert into students(stuid,stuname,kor,eng,math,total,avg) values(
 'ddd','�豸',100,100,100,100+100+100,(100+100+100)/3);
  insert into students(stuid,stuname,kor,eng,math,total,avg) values(
 'eee','������',95,100,100,(95+100+100),(95+100+100)/3);
 
 commit;
 
 select * from students; --DQL
 delete from students; --������� --DML
 drop table member3; --���̺����: ���� �Ұ� --DDL
 
 select * from tab;
 desc employees;
 

 
 
 --table �÷��߰�
 --���̺� ���� �߰��ϰ� ������ date������ create_date�� �߰� (������ �߰�����)
 alter table member add create_date date;
 --table �÷�����
 alter table member drop column create_date;
 --���̺� Ÿ�Ժ���
 alter table member modify pw number(4); --��������� �ٲ��ָ� Ÿ���� �������� �� ����
 update member set pw=''; --��������� �� �ٲ���
 --���̺� �÷��̸�����
 alter table member rename column pw to password;
 --���̺� �̸�����
 alter table member rename to member2; 
 
 select * from tab;
 desc member;
 commit;
 
 
 select * from member;
 --�߰��� ������ ������ ���� ��������
 update member set create_date=sysdate where id='aaa';
 
 create table member(
 id varchar2(20),
 pw varchar2(20),
 name varchar2(20),
 phone varchar2(20)
 );
 
create table member as select * from member2 where 1=2; --����ٿ��ֱ� ���� ���� -- �����ʹ� �������ʰ� Ÿ�Ը� ����Ǵ°�

select *from member;
drop table member;
create table member as select * from member2; --Ÿ�Ե� ����ǰ� �����͵� �����

-- ������ �����ؼ� ���� �߰��ϴ� ��
alter table member add total number(3);
alter table member add avg number(4,1);
desc member;
select * from member;

desc students;
select * from member;
select * from students;

update students set stuid=6,stuname='������' where kor=99;
commit;
desc students;
desc member;
select * from member;

update member set total=100 where name='ȫ�浿';
--for�� �������� ��ӵ����� ��
update member set total=(select total from students where stuname='ȫ�浿') where name='ȫ�浿';

select * from students;
select total from students where stuname='ȫ�浿';

--�ߺ��Ǵ� ���� 1���� ���
select distinct manager_id from employees; --19��
select manager_id from employees; --107��

--�÷����� ��ҹ��ڸ� �������������� ���̺�ȿ� �ִ� �����ʹ� ��ҹ��ڸ� ������
select * from employees;
select emp_name from employees where emp_name='Pat Fay'; --��ҹ��� �����ϱ⶧���� ��Ȯ�ϰ� �������
select emp_name from employees where lower(emp_name)='pat fay';


 select * from departments;
 
 -- �̸�, �޿�, �Ի�����
 -- emp_name, salary, hire_date, employees
 select * from employees;
 select emp_name,salary, hire_date from employees;
 --employees�� ���̺��� �Ȱ��� employees2 �����غ�����.
 create table employees2 as select * from employees;
 delete from employees2;
 drop table employees2;
 
 --employees2 table�� employee_id, emp_name,hire_date,salary�� employees Ÿ�԰� �Ȱ��� ���� 
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
 104,'������','2021/02/01',30000);
 select * from employees2;
 
 --empl table
 --employee_id, emp_name, hire_date�� employees ���̺��� �����ͱ��� �����ؼ�
 --���̺��� ���弼��
 
 create table empl as 
 select employee_id,emp_name,hire_date from employees;
 select * from empl;