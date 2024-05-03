-- **Problem 577. Employee Bonus**
--   [Problem Link](https://leetcode.com/problems/employee-bonus/submissions/1248405061?envType=study-plan-v2&envId=top-sql-50)


-- Problem Overview:
  -- Problem 577 on LeetCode, "Employee Bonus," requires reporting the name and bonus amount of each employee with a bonus less than 1000. The solution involves joining the Employee and Bonus tables, selecting employees with bonuses less than 1000 or no bonus at all.

-- Oracle SQL Solution:
  -- The following SQL query retrieves the name and bonus amount of employees meeting the specified criteria.

  -- Selecting the name and bonus amount of each employee with a bonus less than 1000.
  SELECT e.name, b.bonus
  
  -- From the Employee table (aliased as 'e') and the Bonus table (aliased as 'b').
  FROM Employee e
  -- Performing a LEFT JOIN operation to combine the Employee and Bonus tables based on the empId column.
  LEFT JOIN Bonus b ON e.empId = b.empId
  
  -- Filtering the results to include only rows where the bonus is either NULL (no bonus entry) or less than 1000.
  -- This WHERE clause ensures that all employees are included, even if they don't have a corresponding bonus entry.
  WHERE b.bonus IS NULL OR b.bonus < 1000;
---

-- Annotations and Best Practices:

-- Function and Variable Naming:
  -- - Descriptive names such as 'e' for Employee table and 'b' for Bonus table alias enhance code readability.
  -- - Column names 'name' and 'bonus' reflect their purpose clearly.

-- Comments and Documentation:
  -- - Inline comments provide a clear explanation of each section of the query, guiding readers through its purpose and logic.
  -- - Documentation strings (docstrings) are not applicable in SQL, but comments effectively fulfill the purpose of explaining code segments.

-- Code Structure and Organization:
  -- - The query is logically structured, following the standard sequence of SQL operations (SELECT, FROM, JOIN, WHERE).
  -- - Comments separate each section of the query, improving readability and comprehension.

-- Algorithm Explanation:
  -- - The query uses a LEFT JOIN operation to combine the Employee and Bonus tables based on the empId column.
  -- - It retrieves the name and bonus amount of each employee, ensuring inclusion of all employees even if they have no bonus entry.
  -- - Filtering in the WHERE clause ensures that only employees with a bonus less than 1000 or no bonus are selected.

-- Error Handling and Edge Cases:
  -- - No explicit error handling is required as the query focuses on data retrieval. However, it gracefully handles cases where employees have no bonus entry or a bonus less than 1000.

-- Optimization and Performance:
  -- - The query is optimized for performance by efficiently retrieving the required data with a single SQL statement.
  -- - Use of LEFT JOIN minimizes unnecessary data exclusion, ensuring all employees are considered for bonus reporting.

-- Usage Examples and Test Cases:
  -- - Usage example: Given Employee and Bonus tables, execute the SQL query to obtain the name and bonus amount of eligible employees.
  -- - Test case: Verify the correctness of the query output by comparing it with expected results using sample inputs and bonus thresholds.

-- Overall, this Oracle SQL solution for Problem 577 demonstrates best practices in technical writing and SQL query construction, offering a clear and concise approach to reporting employee bonuses.
