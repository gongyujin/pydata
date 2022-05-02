create table studata2 as
select * from studata;

select * from studata2;

update studata2 set rank=1;

commit;

rollback;



select stuname, total, rank() over(order by total desc) as  ranks from studata2;
select rank() over(order by total desc) as ranks from studata2 b;


--업데이트할 테이블이름 a
update studata2 a set rank=(
select ranks from 
--테이블이름 b
(select stuno,rank() over(order by total desc) as ranks from studata2) b
where a.stuno=b.stuno

);