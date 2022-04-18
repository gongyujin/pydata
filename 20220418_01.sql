select * from board order by bno desc;

insert into board values(
board_seq.nextval,'aaa' ,'[���]�Խ�������2','�Խ���2�� ����Դϴ�/', sysdate,1);

commit;
desc membership;

create table tboard (
bno number(4) primary key,
id varchar2(20) not null,
btitle varchar2(200) not null,
bcontent varchar2(3000),
bdate date default sysdate,
bgroup number(4) not null,
bstep number(4),
bindent number(4),
bhit number(4),
bimg varchar2(200),
constraint membership_fk_id foreign key(id) references membership(id)
);

desc tboard;

select * from tboard;
insert into tboard values(
b_seq.nextval, --bno
'aaa', --id
'[���][���]5��° �Խñ�', --btitle
'[��� ����Դϴ�. 5��]', --bcontent
sysdate, --bdate
5, --bgroup //����϶� �ٲ�
2, --bstep //����϶� �ٲ�
2, --bindent //����϶� �ٲ�
1, --bhit
'1.jpg' --bimg
);
commit;
select * from tboard order by bgroup desc ,bstep asc;

select employee_id, emp_name, manager_id from employees order by employee_id;

--self join ==> inner join // null���� ������ �ʴ´ٴ� �������� ����
select e1.employee_id, e1.emp_name, e1.manager_id, e2.emp_name
from employees e1, employees e2 where e1.manager_id=e2.employee_id(+) --�����Ѱ��� �ݴ뿡 +�� ���ָ� null�� �������� ==> out join
order by e1.employee_id;

--equi join ==> inner join
select employee_id, emp_name, employees.department_id, department_name
from employees, departments
where employees.department_id=departments.department_id;


select * from departments;
select employee_id, emp_name, department_id from employees;
--equi join
--employees, departments ���̺��� equi join�� �ؼ�
--�����ȣ, ����̸�, �μ���ȣ, �μ��̸��� ����Ͻÿ�
--employee_id, emp_name, department_id, department_name
select employee_id, emp_name, e.department_id, department_name
from employees e, departments d
where e.department_id=d.department_id(+)
order by employee_id;



--equi join
select emp_name, department_name from employees e, departments d
where e.department_id=d.department_id;
--ansi inner join
select emp_name, department_name
from employees e inner join departments d
on e.department_id = d.department_id;
--ansi using
select e.emp_name, d.department_name
from employees e inner join departments d
using (department_id);
--natural join==> employees, departments�� �����÷��� ã�Ƽ� ������ �ڵ����� ������
select employees.emp_name, departments.department_name
from employees natural join departments;

--out join
select employee_id, emp_name, e.department_id, department_name
from employees e , departments d
where e.department_id=d.department_id(+); -- ansi inner join�� ����
--employees���̺��� department_id�� null�̴��� ����� ���ּ���.

--ansi out join
select employee_id, emp_name, department_id, department_name
from employees e left outer join departments d --�⺻ out join�� +�� ������ �ݴ������
using (department_id);