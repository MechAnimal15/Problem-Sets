-- 1280. Students and Examinations
--   [problemm link](https://leetcode.com/problems/students-and-examinations/submissions/1250212731?envType=study-plan-v2&envId=top-sql-50)


-- **Problem 1280: Students and Examinations**
  -- **Problem Description:**
      -- In this problem, we are given three tables: Students, Subjects, and Examinations. The Students table contains the ID and name of each student, the Subjects table contains the names of all subjects, and the Examinations table records which students attended which exams.
      -- The task is to find the number of times each student attended each exam. This involves joining the Students, Subjects, and Examinations tables and counting the occurrences of each student-subject pair.
  
  -- **Approach:**
    -- To solve this problem, we use a combination of SQL joins, aggregations, and conditional counting. We perform a cross join between the Students and Subjects tables to generate all possible combinations of students and subjects. Then, we left join the Examinations table to include exam information for each student-subject pair. Finally, we group the result by student ID, student name, and subject name, and count the number of attended exams for each pair using the COUNT function.

-- **Oracle SQL Solution:**
  -- ```sql
    /* Write your PL/SQL query statement below */
    
    -- Query to find the number of times each student attended each exam
    SELECT 
        -- Selecting the student ID, student name, subject name, and the number of attended exams
        s.student_id,      -- Student ID
        s.student_name,    -- Student Name
        sub.subject_name,  -- Subject Name
        NVL(COUNT(e.subject_name), 0) AS attended_exams -- Number of attended exams, handling NULL values with 0
    FROM 
        Students s          -- Alias for the Students table
        CROSS JOIN Subjects sub -- Generating all possible combinations of students and subjects
        LEFT JOIN Examinations e -- Joining the Examinations table to include exam information
        ON 
            s.student_id = e.student_id      -- Matching student IDs
            AND sub.subject_name = e.subject_name -- Matching subject names
    GROUP BY 
        -- Grouping by student ID, student name, and subject name
        s.student_id, s.student_name, sub.subject_name
    ORDER BY 
        -- Ordering the result by student ID and subject name
        s.student_id, sub.subject_name;
  -- ```
-- Orcacle solution
--   Runtime: 1734 ms


-- **Annotations and Best Practices:**

--   - **Function and Variable Naming:**
--       - Descriptive names such as `student_id`, `student_name`, `subject_name`, and `attended_exams` enhance readability and clarity.
--   - **Comments and Documentation:**
--       - Inline comments explain each section of the SQL query, guiding readers through the purpose and logic of the code.
--       - Comments are provided to describe the purpose of each table and join operation.
--   - **Code Structure and Organization:**
--       - The code is logically organized, with sections separated by comments for clarity.
--       - Proper indentation and whitespace usage improve code readability.
--   - **Algorithm Explanation:**
--       - An overview of the SQL query's approach is provided, explaining the purpose of each table and join operation.
--   - **Error Handling and Edge Cases:**
--       - The `NVL` function is used to handle NULL values and ensure consistent results.
--   - **Optimization and Performance:**
--       - The query achieves optimal performance by efficiently joining tables and aggregating data.
--   - **Usage Examples and Test Cases:**
--       - Usage examples and test cases are not provided in the solution, but users can execute the query with sample data to verify its correctness.

-- **Overall, this Oracle SQL solution provides a clear and concise approach to finding the number of times each student attended each exam, adhering to best practices in coding standards and technical writing.**

