1251. Average Selling Price
[Problem Link](https://leetcode.com/problems/average-selling-price/submissions/1278676083?envType=study-plan-v2&envId=top-sql-50)

Oracle (sql)
-- This query selects the product ID and calculates the rounded average price for each product.
SELECT 
    p.product_id,
    ROUND(
        -- The average price is calculated by dividing the sum of the product of price and units sold by the total units sold.
        COALESCE(
            SUM(p.price * u.units) / NULLIF(SUM(u.units), 0), -- COALESCE handles division by zero by returning 0.
            0 -- If the total units sold is zero, the average price is set to zero.
        ), 
        2 -- The average price is rounded to two decimal places.
    ) AS average_price
FROM 
    Prices p
LEFT JOIN 
    UnitsSold u
ON 
    p.product_id = u.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY 
    p.product_id -- The results are grouped by product ID.
ORDER BY 
    p.product_id -- The results are ordered by product ID.
    ;
