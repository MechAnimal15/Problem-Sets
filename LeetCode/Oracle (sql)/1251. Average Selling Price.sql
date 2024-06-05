1251. Average Selling Price
[Problem Link](https://leetcode.com/problems/average-selling-price/submissions/1278676083?envType=study-plan-v2&envId=top-sql-50)

Oracle (sql)
  '''solution
  
SELECT 
    p.product_id,
    ROUND(COALESCE(SUM(p.price * u.units) / NULLIF(SUM(u.units), 0), 0), 2) AS average_price
FROM 
    Prices p
LEFT JOIN 
    UnitsSold u
ON 
    p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY 
    p.product_id
ORDER BY 
    p.product_id;


Runtime: 1338 ms
