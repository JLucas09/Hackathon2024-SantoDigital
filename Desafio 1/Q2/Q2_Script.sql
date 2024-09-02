-- Considerando a quantidade do ano todo de 2017

select c.customerkey as ID, c.firstname, count(s.customerkey) as total_order from customers c
join sales s on s.customerkey = c.customerkey
where extract(year from s.orderdate) = 2017
group by c.customerkey, c.firstname 
order by count(s.customerkey) desc
limit 1;