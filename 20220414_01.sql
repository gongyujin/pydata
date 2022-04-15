--������ ����
create sequence emp_seq
    start with 1
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache;

--������ ����
alter sequence test_seq
maxvalue 99999
increment by 10;

select test_seq.nextval from dual; --ó�������Ҷ� nextval�� ����� currval�� ������ �� ����

--drop table employees2;
--��������ȣ, �����ȣ, �����, ����, �Ի��� employees2���̺� ����
--107�� ����� �Է��Ͻÿ�.
--�Ի��� �������� ������������ �����Ͻÿ�.
create table employees2 as select employee_id, emp_name, job_id, hire_date from employees where 1=2;
alter table employees2 add empno number(5);
insert into employees2 select employee_id, emp_name, job_id, hire_date, test_seq.nextval from employees;
select * from employees2 order by hire_date;

--�÷���ġ����(�÷����� ������)
alter table employees2 modify employee_id invisible; --���̺� �÷� ����
alter table employees2 modify emp_name invisible;
alter table employees2 modify job_id invisible;
alter table employees2 modify hire_date invisible;
alter table employees2 modify employee_id visible; --���̺� �÷� ���̱�
alter table employees2 modify emp_name visible;
alter table employees2 modify job_id visible;
alter table employees2 modify hire_date visible;

commit;
select * from employees2;


select * from employees;
--�����Լ� (upper, lower, inicap)
select upper(emp_name) from employees; --upper: �빮��, lower: �ҹ���, inicap: ù���� �빮��
--���ڱ��� (length)
select emp_name, length(emp_name), lengthb(emp_name) from employees; --lengthb : �����Ʈ �����ϴ��� ������
select stuname, length(stuname), lengthb(stuname) from students;
-- ����� �ѱ��ڴ� 1����Ʈ, �ѱ��� �ѱ��ڴ� 3����Ʈ

--���ڿ� ����: substr
select emp_name,substr(emp_name, 0,6) from employees; --0���� ����°¥�� �ڸ����� �߶��
select emp_name, substr(emp_name,-1) from employees; --�ڿ��� �ѱ��ڸ� ������

alter table member add juminno char(14);
select * from member;

--�÷�����
update member set password='        5555     ',juminno='690912-2101111' where id='eee'          ;
alter table member add filname varchar2(20);
update member set filname='asdf.csv' where id='              eee         ';

--�÷��߰�
insert into member values(
'hhhh','7777','ȫ�濵   ','010  -8888 -8888',300,100,'22/02/02','010101-4100123','abc    .json');
commit;
desc member;

select name, substr(juminno,0,6) "�ֹι�ȣ���ڸ�", substr(juminno,8) "�ֹι�ȣ ���ڸ�" from member;
select name,juminno,substr(juminno,0,8) ||'******' juminno2, length(substr(juminno,0,8) ||'******') juminlength from member; --�Լ��� �ϳ��� �ƴ϶� ���ļ� ������ ��밡��

-- .hwp, .xls, .pdf, .csv
--member���̺�
--id�� ����, juminno ���ڸ�, juminno���ڸ�, filname �ڿ��� 3�ڸ� ����Ͻÿ�.
select length(id) , substr(juminno, 0,6) "�ֹι�ȣ���ڸ�", substr(juminno,8) "�ֹι�ȣ ���ڸ�", substr(filname,-3) "filename �� 3�ڸ�" from member;

--Ư������ ��ġ ã��: instr , ���̰� �ٸ��� �ַ� ���
select filname, instr(filname,'.'), substr(filname, instr(filname,'.')+1) from member;

--replace ���� ��ü
select emp_name from employees;
select replace(emp_name,'a','A') from employees;
--����� ���ֱ�
select replace(emp_name,' ','') from employees;
--trim,ltrim,rtrim �������� �Լ� : �߰��� �ִ� ������ �ƴ϶�� trim�� ����ؼ� �ϸ� ��, �װ� �ƴ϶�� replace�� ����ؾ���
select password, length(password), ltrim(password) from member;
select phone, length(phone) from member;
select filname, length(filname),trim(filname),length(trim(filname)) from member;

update member set filname=ltrim(filname);
update member set filname=replace(filname,' ','');
select * from member;


--1. concat ���ڿ� ��ġ��
select concat(id, concat('-',password)) juminno from member; -- ���ļ� ���÷��� ������, �������� ��밡��
--2. ���� ������
select id||'-'||password as juminno from member;

--����� Ư������ ä��� (lpad, rpad)
select rpad(id,10,'*') from member; -- id���Ŀ� *���ڷ� 10�ڸ����� ä����

select juminno from member;
select rpad(substr(juminno,0,8),14,'*') juminno from member;

--���糯¥ (����, ����, ����), ��¥�� ���ϱ�, ���� ���� ��, ���ϱ�� �ȵ�
select sysdate-1, sysdate,sysdate+1 from dual;

select * from member;
insert into member(id,password, create_date) values('iii','1111',sysdate);

select to_char(create_date,'YYYY-MM-DD hh:MI:ss') from member; --��¥ �� ��ȯ (MM�� ��, MI�� ��)

select hire_date from employees;

select trunc(sysdate-to_date('22/03/08')) from dual; --����ȯ, sysdata-to_date: �����Ϸκ��� ��ĥ�� �������� �˷���

select hire_date, round(hire_date,'month') from employees; --16���� �������� ���� �ݿø���

select round(create_date,'ddd') from member; --���� �������� ��

select emp_name, sysdate, '22/03/08', months_between(sysdate,to_date('22/03/08')) from employees; -- ��� ���̰� �ִ���
select sysdate, add_months(sysdate,6) from dual; -- ���� �߰�

select sysdate, next_day(sysdate,'������') from dual; -- ���ó�¥���� ���� �������� ��¥�� �������� �˷���
select sysdate,last_day(sysdate) from dual; --�ش� ���� ������ ��¥�� ��ȯ last_day

------------------------------------------------------------
create table membership(
name varchar2(30) not null, --�ߺ��� �� �� ������ null�� �ȵ����� ��
id varchar2(16) primary key, --null�� ���ü� ����, unique(�Ȱ����� ������ �ȵ�)
pw varchar2(20) not null,
email varchar2(50),
send_email number(1), --number(1)�� 0,1�� �����Ҽ� ����
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
--primary key �߰�
alter table membership add primary key(id);
--�������� not null ����
alter table membership modify name not null;
desc membership;

insert into membership values(
'������','eee','5555','eee@naver.com',1,'12323','���� ��õ�� ��õ��','101-1','01044444444','0244444444','2000/06/21',0,0,sysdate,'202.202.202.202');

select * from membership;

--�̼����ڸ� ���
select birth, months_between('2022/01/01',birth) from membership where months_between('2022/01/01',birth)<216;


-- board:fk (foregin key ���)
create table board(
bno number(4) primary key,
id varchar2(100),
title varchar2(100),
content varchar2(3000),
create_date date,
hit number(4) default 0, --default 0�� �Է����������� �⺻0���� ���ϰڴٴ� �ǹ�
--����: idex�� mem_fk_id, �ܷ�Ű(�÷�) ��ġ�� membership���̺��� id�� ==> primary key�� ��ϵǾ����� ������ �ܷ�Ű�� ����� �� ����
constraint mem_fk_id foreign key(id) references membership(id) --������ ������ ��� index���� ������ ������ �˷���
);
--foregin key ���� ���̵�� ����� �Ұ�����.
insert into board values(
board_seq.nextval,'bbb','�Խ�������2','�Խ��ǿ� ���� ������ �Է��մϴ�.2',sysdate,1); --primary�� ���� id�� �Է��ϴ� ���� ���� (���Ἲ����) , �θ� ���� ������ �ܷ���Ű�� �Է��� �� ���°�

commit;
select * from board;
--foregin key Ű�� ��ϵǾ� �ִ� ���, ������ ���� �߻�
delete membership where id='bbb'; --�ڽ� key�� �����ϸ� �θ�Ű�� �Ժη� ������� ����, foreign key�� ����ϸ� �Ժη� �����Ҽ� ����
--ORA-02292: ���Ἲ ��������(ORA_USER.MEM_FK_ID)�� ����Ǿ����ϴ�- �ڽ� ���ڵ尡 �߰ߵǾ����ϴ� ==> mem_fk_id�� foreign key ������� ���� �˷��ֱ����ؼ� constraint�� ������ ���ذ�

--���� ==> ��¥�� ��ȯ
select sysdate-to_date('22/03/08') from employees; --��¥������ ��ȯ�� ������������ ����� �� ����

select hire_date, to_char(hire_date,'yy/mm/dd hh:mi:ss day') from employees;
select create_date, to_char(create_date,'hh24:mi:ss') from member; --hh24: 24�ð�����, am: ��������

select * from member;
update member set create_date=sysdate where id='aaa';
commit;

select salary from employees;
select salary, salary*12 "����", salary*12*1230 "����(��ȭ)" from employees;

--õ���� ǥ��, $: �׳� �߰�, L:��ȭǥ�� �߰�, C:KRW ǥ�� ,0 ���ڸ��� 0���� ä��, 9�� ���ڸ� ����
select salary, salary*12,to_char(salary*12*1230, 'L999,999,999') from employees; --'999,999,999,999' ����ǥ�����ְ� ��ĭ�̸� �������� ����, �� '000,000,999,999'�� ���ԵǸ� ��ĭ�� 0���� ä����
select to_char(empno,'000') from employees2;

select '2022-04-14 01:01:01',to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate,'hh') hours, to_char(sysdate,'mi') minutes from dual;

select * from studata;
-- �Ҽ��� ǥ��
select to_char(avg,'99.00') from studata;

--1. ���ڸ� ��¥�� ����ȯ 2. �ٽ� ���ڷ� �� ��ȯ
select to_char(to_date('22/03/08'),'yyyy-mm-dd') from dual;

select hire_date from employees;

--���ڷ� ��¥ �˻� ����
select hire_date from employees where hire_date='20080113';
--���ڷ� ��¥�˻� �Ұ���
select hire_date from employees where hire_date=20080113;


--����=>������ ��ȯ
select '20,000'-'19,000' from dual; --����
-- �������� õ���� Ÿ���� Ȯ���ؼ� ���ڷ� ��ȯ
select to_number('20,000','99,999')-to_number('19,000','99,999') from dual; -- ������ Ÿ���� ���ڷ� ����
-- ���ڸ� õ������ ��ȯ
select to_char(2000,'99,999') from dual; -- ���ڸ� ���� ���·� ���ں�ȯ
select to_char('20,000') from dual; -- Ÿ���� char ==> ,�� ���ڰ� �� �־ to_number�� �����Ұ���
select to_number('20000') from dual; -- ,�� ���� ������ ���������� ��������
-- õ����ǥ�ø� ������ ���ڷ� ����ȯ
select to_number(replace('20,000',',','')) from dual;

-- commission_pct�� null�� nvl�� 0���� ��ȯ
select salary, salary*12,commission_pct, salary*12+(salary*12*nvl(commission_pct,0)) from employees; 

-----nvl �̿�: manager_id null�� ��� 999�� ǥ���Ͻÿ�.------
select * from employees;

select manager_id,nvl(to_char(manager_id),'ceo') manager_id from employees;


select * from students;
------�׷��Լ� min�ּҰ�, max�ִ밪, count ����
select min(kor) from students;
select emp_name, min(salary), max(salary) from employees; --�׷��Լ��� �Ϲ��Լ��� �Բ� ����� �� ����
select count(*) from employees;
select count(*),count(employee_id),count(manager_id),min(salary) from employees; -- null���� ��������� ����
-- �հ�
select sum(salary) from employees where department_id=60; 
-- group by �׷��Լ����� : ���Ǻ��� �׷��� ����
select department_id, sum(salary) from employees group by department_id order by department_id;

select e.department_id, d.department_name, sum(salary) from employees e, departments d
where e.department_id=d.department_id and e.department_id=60 
group by e.department_id, d.department_name order by e.department_id;
 
-- avg ���
select round(avg(salary),2) from employees;
-- ��� ���޺��� ū��� �Ѽ�
select count(*) from employees where salary<(select round(avg(salary),2) from employees); -- ��ȣ���� ���� ����ϱ� ������ �׷��Լ��� ����ص� �����Լ��� ���� ����� �� ����

select department_id from employees;
select department_id, department_name from departments; --name�� departments���� �ְ� employees���� ����

select * from employees where mod(employee_id,2)=1 order by employee_id;
select months_between(hire_date,sysdate) from employees;
select months_between(sysdate,hire_date) from employees;

--�ڱⰡ �¾ ������ ������� ��ĥ�� �Ǵ��� ���
select round(sysdate-to_date('19980114')) from dual;

--drop table emp02;
create table emp02(
id varchar2(20),
content clob
);

--clob: ��뷮���� �����ؾ���
insert into emp02 values(
'bbb','<p>sdfsfsfsf sfsdffwfwf fwfsfkjwlfkwjf</p><p>fdkjwflwkfjwf</p><p><span style="background-color: rgb(119, 119, 119); color: rgb(255, 0, 0); font-size: 24pt;">���� ���ڸ� �Է��ϰھ�</span></p>');

select * from emp01;
commit;
desc emp01;

alter table emp01 add(job varchar2(9));
alter table emp01 modify(job varchar2(30));

update emp01 set job='manager' where empno>10;

--emp01 job�� number(10)�� �ٲٽÿ�
update emp01 set job=1 where job='manager';
alter table emp01 modify(job number(10)); --����־�߸� ������ ������ ������ �� ����

update emp01 set job='' where job=1;
alter table emp01 modify(job number(10));

--emp01 ����(job)Į���� ����
alter table emp01 drop column job;

select * from studata2;
update studata2 set kor=0, total=0+eng+math,avg=(0+eng+math)/3 where stuno=8;

commit; --cmdâ���� ������Ʈ�� �Ҷ� ���� sql���� ������Ʈ�� commit�� �����ʴ´ٸ� cmd������ �������̴�