create table studata2 as
select * from studata;

select * from studata2;

update studata2 set rank=1;

commit;

rollback;



select stuname, total, rank() over(order by total desc) as  ranks from studata2;
select rank() over(order by total desc) as ranks from studata2 b;


--������Ʈ�� ���̺��̸� a
update studata2 a set rank=(
select ranks from 
--���̺��̸� b
(select stuno,rank() over(order by total desc) as ranks from studata2) b
where a.stuno=b.stuno

);