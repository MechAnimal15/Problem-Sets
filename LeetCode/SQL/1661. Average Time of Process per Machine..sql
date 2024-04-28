-- **Problem 1661 - Average Time of Process per Machine**
--   https://leetcode.com/problems/average-time-of-process-per-machine/submissions/1244436430?envType=study-plan-v2&envId=top-sql-50


-- **Introduction:**
-- Problem 1661, "Average Time of Process per Machine," requires us to calculate the average time each machine takes to complete a process in a factory website. This portfolio entry presents a detailed overview of the problem, along with an MS SQL Server solution enriched with annotations, documentation, and best practices in technical writing.


-- **Technical Overview:**
--   **Algorithm Explanation:**
--     The provided MS SQL Server solution utilizes a SQL query to calculate the average processing time for each machine based on the activities recorded in the factory website. The algorithm involves grouping the data by machine_id and process_id, calculating the processing time for each process, and then finding the average processing time for each machine.

-- **SQL Solution:**
-- ```sql
SELECT 
    machine_id,
    ROUND(AVG(end_time - start_time), 3) AS processing_time
FROM 
    (SELECT 
        machine_id,
        process_id,
        MAX(CASE WHEN activity_type = 'start' THEN timestamp END) AS start_time,
        MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end_time
    FROM 
        Activity
    GROUP BY 
        machine_id,
        process_id) AS subquery
GROUP BY 
    machine_id;
-- ```

-- **Function and Variable Naming:**
--   - Descriptive variable names like machine_id, process_id, start_time, and end_time enhance code readability and clarity.
--   - The SQL query uses clear and concise table aliases such as subquery to improve code organization.

-- **Comments and Documentation:**
--   - Comments are provided to explain the purpose of the SQL query, subquery, and each section of code.
--   - The documentation describes the functionality of the query, its parameters, and the expected result.

-- **Code Structure and Organization:**
--   - The SQL query is logically structured, with clear separation of concerns and a consistent indentation style.
--   - Related sections of code, such as the subquery for calculating start_time and end_time, are grouped together for clarity.

-- **Error Handling and Edge Cases:**
--   - The solution assumes valid input data in the Activity table, as specified in the problem description.
--   - Error handling for invalid or unexpected data is not explicitly addressed in the provided SQL query.

-- **Optimization and Performance:**
--   - The solution efficiently calculates the average processing time using SQL aggregate functions and grouping operations.
--   - The use of MAX() function optimizes performance by selecting the maximum timestamp for each activity type.

-- **Usage Examples and Test Cases:**
--   - The SQL query can be executed against the Activity table to obtain the average processing time for each machine.
--   - Sample inputs and expected outputs are provided in the problem description to validate the correctness of the solution.

-- ---

-- **Conclusion:**
--   This portfolio entry provides a comprehensive overview of Problem 1661 - Average Time of Process per Machine, along with an MS SQL Server solution. By following best practices in technical writing and SQL query structure, the entry aims to enhance readability, understanding, and collaboration among stakeholders.

