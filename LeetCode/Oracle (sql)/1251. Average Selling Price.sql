-- 1251. Average Selling Price
-- [Problem Link](https://leetcode.com/problems/average-selling-price/submissions/1278676083?envType=study-plan-v2&envId=top-sql-50)


-- **Overview:**
--     Problem 1251, "Average Selling Price," involves calculating the average selling price for each product based on the price and units sold within specified date ranges. Given two tables, "Prices" and "UnitsSold," containing information about product prices and units sold, the task is to compute the average selling price for each product. The solution requires joining the two tables and aggregating the data to calculate the average price, handling edge cases such as division by zero.

-- **Approach:**
--     The approach involves joining the "Prices" and "UnitsSold" tables on the product ID and filtering data based on purchase dates falling within the price validity periods. Then, the total revenue and total units sold are aggregated for each product. Finally, the average selling price is calculated by dividing the total revenue by the total units sold, handling cases where the total units sold is zero to avoid division errors.

    
-- **Oracle SQL Solution:**
    -- ```sql
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
-- ```
--     Runtime: 900 ms


-- **Annotations:**
--     - The query begins by selecting the product ID and calculating the average price for each product.
--     - The ROUND function is used to round the average price to two decimal places for clarity.
--     - The COALESCE function handles cases where the total units sold is zero, avoiding division by zero errors.
--     - A LEFT JOIN is performed between the "Prices" and "UnitsSold" tables on the product ID, filtering data based on the purchase date falling within the price validity period.
--     - The results are grouped by product ID using the GROUP BY clause to compute the average price for each product.
--     - Finally, the results are ordered by product ID using the ORDER BY clause for readability.

-- **Conclusion:**
--     Problem 1251, "Average Selling Price," requires aggregating data from two tables and calculating the average price for each product. The provided Oracle SQL solution efficiently computes the average selling price, handling edge cases gracefully and producing accurate results. By following best practices in SQL coding and providing comprehensive annotations, the solution offers clarity and enhances understanding for both technical and non-technical audiences.

    
