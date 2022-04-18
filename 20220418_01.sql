select * from board order by bno desc;

insert into board values(
board_seq.nextval,'aaa' ,'[답글]게시판제목2','게시판2의 답글입니다/', sysdate,1);

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
'[답글][답글]5번째 게시글', --btitle
'[답글 답글입니다. 5번]', --bcontent
sysdate, --bdate
5, --bgroup //답글일때 바뀜
2, --bstep //답글일때 바뀜
2, --bindent //답글일때 바뀜
1, --bhit
'1.jpg' --bimg
);
commit;
select * from tboard order by bgroup desc ,bstep asc;

select employee_id, emp_name, manager_id from employees order by employee_id;

--self join ==> inner join // null값은 해주지 않는다는 문제점이 있음
select e1.employee_id, e1.emp_name, e1.manager_id, e2.emp_name
from employees e1, employees e2 where e1.manager_id=e2.employee_id(+) --부족한거의 반대에 +를 해주면 null값 포함해줌 ==> out join
order by e1.employee_id;

--equi join ==> inner join
select employee_id, emp_name, employees.department_id, department_name
from employees, departments
where employees.department_id=departments.department_id;


select * from departments;
select employee_id, emp_name, department_id from employees;
--equi join
--employees, departments 테이블을 equi join을 해서
--사원번호, 사원이름, 부서번호, 부서이름을 출력하시오
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
--natural join==> employees, departments의 공통컬럼을 찾아서 조인을 자동으로 시켜줌
select employees.emp_name, departments.department_name
from employees natural join departments;

--out join
select employee_id, emp_name, e.department_id, department_name
from employees e , departments d
where e.department_id=d.department_id(+); -- ansi inner join과 같음
--employees테이블의 department_id가 null이더라도 출력을 해주세요.

--ansi out join
select employee_id, emp_name, department_id, department_name
from employees e left outer join departments d --기본 out join과 +의 기준이 반대방향임
using (department_id);