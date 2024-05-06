-- 1280. Students and Examinations
-- [Problem Link](https://leetcode.com/problems/students-and-examinations/submissions/1250212731?envType=study-plan-v2&envId=top-sql-50)


-- Overview:
  -- Problem 1280 tasks us with retrieving data regarding the number of exams each student attended for each subject. This SQL query offers a concise solution to this problem, providing insights into student engagement and performance across various subjects.

-- Oracle SQL Solution:

  /*
  Query to find the number of times each student attended each exam.
  This query selects the student ID, student name, subject name, and the number of attended exams.
  */
  
  SELECT 
      s.student_id, -- Selecting the student ID
      s.student_name, -- Selecting the student name
      sub.subject_name, -- Selecting the subject name
      NVL(grouped.attended_exams, 0) AS attended_exams -- Handling NULL values with 0
  FROM 
      Students s -- Alias for the Students table
  CROSS JOIN 
      Subjects sub -- Generating all possible combinations of students and subjects
  LEFT JOIN (
      SELECT 
          student_id, 
          subject_name, 
          COUNT(*) AS attended_exams -- Counting the number of exams each student attended for each subject
      FROM 
          Examinations
      GROUP BY 
          student_id, 
          subject_name
  ) grouped -- Subquery to count the number of exams each student attended for each subject
  ON 
      s.student_id = grouped.student_id -- Matching student IDs
      AND sub.subject_name = grouped.subject_name -- Matching subject names
  ORDER BY 
      s.student_id, 
      sub.subject_name -- Ordering the result by student ID and subject name
  ;
--


-- Algorithm Explanation:
  -- This SQL query efficiently retrieves the desired information by performing a cross join between the "Students" and "Subjects" tables to generate all possible combinations of students and subjects. It then left joins the result with a subquery that counts the number of exams each student attended for each subject. Finally, the data is grouped by student ID and subject name, and the COUNT function is used to calculate the number of attended exams for each group.

-- Comments and Documentation:
  -- Each section of the SQL query is accompanied by inline comments explaining its purpose and logic. Descriptive aliases and column names enhance readability and clarity, making the code easier to understand and maintain.

-- Error Handling and Edge Cases:
  -- The NVL function is used to handle NULL values in the "attended_exams" column, ensuring consistent results. Additionally, the query structure ensures that all combinations of student ID and subject name are retained, even if no exams were attended for a specific combination.

-- Optimization and Performance:
  -- This query achieves optimal performance by efficiently joining tables and aggregating data. The use of appropriate indexing and query optimization techniques can further enhance its performance, especially with large datasets.

-- Usage Examples and Test Cases:
  -- While specific usage examples and test cases are not provided within this portfolio entry, users can execute the query with sample data to verify its correctness and functionality. Additionally, integrating this query into a larger database system or application can provide real-world testing scenarios.


-- Overall, this Oracle SQL solution offers a clear and concise approach to solving Problem 1280, adhering to best practices in coding standards and technical writing.
