-- **Problem 577. Employee Bonus**
--   [Problem Link](https://leetcode.com/problems/employee-bonus/submissions/1248405061?envType=study-plan-v2&envId=top-sql-50)

-- 577. Employee Bonus

-- Oracle  
-- ```sql
  /* Write your PL/SQL query statement below */
  -- Selecting the name and bonus amount of each employee with a bonus less than 1000.
  SELECT e.name, b.bonus
  
  -- From the Employee table (aliased as 'e') and the Bonus table (aliased as 'b').
  FROM Employee e
  -- Performing a LEFT JOIN operation to combine the Employee and Bonus tables based on the empId column.
  LEFT JOIN Bonus b ON e.empId = b.empId
  
  -- Filtering the results to include only rows where the bonus is either NULL (no bonus entry) or less than 1000.
  -- This WHERE clause ensures that all employees are included, even if they don't have a corresponding bonus entry.
  WHERE b.bonus IS NULL OR b.bonus < 1000;

--   ```
-- Runtime: 1445 ms

-- **Explanation:**
--   - **SELECT Statement**: We begin by selecting the columns we want to retrieve from the database. In this case, we're selecting the name from the Employee table and the bonus from the Bonus table.
  
--   - **FROM Clause**: We specify the tables we're querying from, Employee and Bonus, and provide aliases for them (e and b, respectively). This allows us to refer to columns from these tables more concisely throughout the query.
  
--   - **LEFT JOIN Operation**: We perform a LEFT JOIN between the Employee and Bonus tables, ensuring that all rows from the Employee table are included in the result set, regardless of whether they have a corresponding entry in the Bonus table. This is important because not all employees may have a bonus entry.
  
--   - **ON Clause**: We specify the condition for joining the two tables, which is the equality between the empId columns in both tables. This ensures that we're matching the correct bonus amount to each employee based on their empId.
  
--   - **WHERE Clause**: We apply filtering criteria to the result set. Here, we include only rows where the bonus is either NULL (indicating no bonus entry for the employee) or less than 1000. This ensures that we're only retrieving employees with a bonus less than 1000, handling cases where the bonus may be missing or within the specified range.

-- Overall, this SQL query effectively retrieves the name and bonus amount of each employee meeting the specified criteria, providing a clear and concise solution to problem 577.
