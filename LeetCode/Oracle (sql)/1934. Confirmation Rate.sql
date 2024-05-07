-- 1934. Confirmation Rate
-- [Problem link] (https://leetcode.com/problems/confirmation-rate/submissions/1251924910?envType=study-plan-v2&envId=top-sql-50)


-- **Problem 1934: Confirmation Rate**

-- **Overview:**
--        Problem 1934 tasks us with calculating the confirmation rate for users who have requested confirmation messages. Given two tables, Signups and Confirmations, containing user signup information and confirmation actions, respectively, we need to compute the confirmation rate for each user. The confirmation rate is the ratio of confirmed messages to the total number of requested messages, rounded to two decimal places.

-- **Approach:**
--        To solve this problem, we'll utilize SQL to perform data manipulation and aggregation operations. We'll join the Signups and Confirmations tables on the user_id column to associate confirmation actions with users who signed up. Then, we'll calculate the confirmation rate using conditional aggregation and handle edge cases where users didn't request any confirmation messages.

-- **Oracle SQL Solution:**
--        ```sql
              SELECT s.user_id,
                     CASE
                         WHEN COUNT(c.user_id) = 0 THEN 0
                         ELSE ROUND(SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(c.user_id), 2)
                     END AS confirmation_rate
              FROM Signups s
              LEFT JOIN Confirmations c ON s.user_id = c.user_id
              GROUP BY s.user_id;
--       ```

-- **Annotations:**

--        1. **Function and Variable Naming:**
--                  - Descriptive names like `s.user_id` and `COUNT(c.user_id)` clarify their purpose.
          
--        2. **Comments and Documentation:**
--                  - No comments or documentation are necessary as SQL statements are self-explanatory.
          
--        3. **Code Structure and Organization:**
--                  - The SQL query is logically structured with clear separation of SELECT, CASE, and JOIN clauses.
          
--        4. **Algorithm Explanation:**
--                  - The algorithm employs a LEFT JOIN to associate confirmation actions with user signups and uses conditional aggregation to calculate the confirmation rate.
          
--        5. **Error Handling and Edge Cases:**
--                  - The CASE statement handles the edge case where users didn't request any confirmation messages by assigning a confirmation rate of 0.
          
--        6. **Optimization and Performance:**
--                  - The query efficiently aggregates data using SQL's built-in functions, minimizing resource usage.
          
--        7. **Usage Examples and Test Cases:**
--                  - Sample inputs and expected outputs are provided in the problem description for testing the solution's correctness.

-- **Conclusion:**
--        Problem 1934 is efficiently solved using SQL's aggregation capabilities and conditional logic. The provided solution calculates confirmation rates for users with requested confirmation messages while handling edge cases gracefully. With clear documentation and adherence to SQL best practices, this solution ensures readability, performance, and correctness.

