-- 620. Not Boring Movies
-- [Problem Link](https://leetcode.com/problems/not-boring-movies/submissions/1260708281?envType=study-plan-v2&envId=top-sql-50)

  
--   Overview
-- Leetcode Problem 620, "Not Boring Movies," requires querying a database to find movies that have odd-numbered IDs and descriptions that are not "boring." The results should be ordered by their ratings in descending order. This problem tests your ability to filter and sort data using SQL.

--   Approach
-- The approach to solving Problem 620 involves constructing an SQL query that filters rows from the `Cinema` table based on specific criteria and orders the results accordingly. We employ the `MOD` function to identify odd-numbered IDs and use the `<>` operator to exclude movies with the description "boring." The final step is to order the filtered results by their ratings in descending order.

--   Oracle SQL Solution
  
--   ```sql
    -- Select the columns that need to be included in the result set: id, movie, description, and rating
    SELECT id, movie, description, rating
    
    -- Specify the table from which to retrieve the data
    FROM Cinema
    
    -- Filter the rows to include only those with odd-numbered IDs
    -- The MOD(id, 2) function returns the remainder when id is divided by 2
    -- If the remainder is 1, it means the id is odd
    WHERE MOD(id, 2) = 1
    
      -- Further filter the rows to exclude movies with the description 'boring'
      -- The '<>' operator is used to check for inequality in SQL
      AND description <> 'boring'
    
    -- Sort the filtered results by the rating column in descending order
    -- This ensures that movies with higher ratings appear first in the result set
    ORDER BY rating DESC;
--   ```
--   Runtimes 823 ms


-- Annotations and Documentation

-- - **SELECT Clause**: Specifies the columns to include in the result set.
-- - **FROM Clause**: Indicates the source table from which the data will be selected.
-- - **WHERE Clause**: Filters rows based on odd-numbered IDs and non-boring descriptions.
-- - **ORDER BY Clause**: Sorts the final result set by rating in descending order.

-- Code Structure and Organization
--   The SQL query is logically organized, with each clause clearly separated and annotated for clarity. The code follows best practices for SQL formatting, indentation, and whitespace usage, enhancing readability.

-- Algorithm Explanation
--   The algorithm efficiently filters and sorts movie data based on specified criteria using SQL functions and operators. By leveraging the power of SQL, the solution achieves the desired outcome without the need for complex procedural logic.

-- Error Handling and Edge Cases
--   The SQL query assumes valid input data and does not explicitly handle error conditions. However, it's important to ensure that the input data conforms to the expected schema to avoid unexpected behavior or errors.

-- Optimization and Performance
--   The SQL query is optimized for performance, leveraging built-in SQL functions and operators to efficiently filter and sort data directly within the database engine. By avoiding unnecessary data processing and leveraging database indexing, the solution achieves optimal performance.

-- Usage Examples and Test Cases
--   To demonstrate the functionality of the SQL query, sample inputs and expected outputs can be provided. These examples illustrate how the query filters and sorts movie data according to the specified criteria, helping users understand the expected behavior and use cases of the solution.


