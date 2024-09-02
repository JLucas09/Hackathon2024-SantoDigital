-- Considerando os dois últimos anos como 2016/2017 pois são os mais recentes que há na carga de dados.

select p.productkey as id, p.productname, sum(s.orderquantity) as sales_total_quantity from products p
join products_subcategories ps on ps.productsubcategorykey = p.productsubcategorykey
join products_categories pc on pc.productcategorykey = ps.productcategorykey
join sales s on s.productkey = p.productkey 
where pc.categoryname = 'Bikes'
and s.orderdate between '2016-01-01' and '2017-12-31'
group by p.productkey, p.productname
order by sum(s.orderquantity) desc 
limit 10;
