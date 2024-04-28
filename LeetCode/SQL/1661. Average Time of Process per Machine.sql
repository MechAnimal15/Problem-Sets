/*
Problem 1661 - Average Time of Process per Machine
https://leetcode.com/problems/average-time-of-process-per-machine/submissions/1244441749?envType=study-plan-v2&envId=top-sql-50
Related Topics: SQL
Similar Questions: 1126. Active Businesses
*/

/*
Problem Description:
    There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.
    The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.
    The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.
    Return the result table in any order.
*/

/*
SQL Schema:
    Create table If Not Exists Activity (machine_id int, process_id int, activity_type ENUM('start', 'end'), timestamp float);
        Truncate table Activity;
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '0', 'start', '0.712');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '0', 'end', '1.520');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '1', 'start', '3.140');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '1', 'end', '4.120');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '0', 'start', '0.550');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '0', 'end', '1.550');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '1', 'start', '0.430');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '1', 'end', '1.420');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '0', 'start', '4.100');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '0', 'end', '4.512');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '1', 'start', '2.500');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '1', 'end', '5.000');
*/

/*
Approach:
The problem can be solved by joining the 'start' and 'end' timestamps for each process using SQL join operations. We can calculate the processing time for each process by subtracting the 'start' timestamp from the 'end' timestamp. Then, we group the results by machine_id and calculate the average processing time for each machine. Finally, we round the average processing time to 3 decimal places.

SQL Solution:
*/

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

/*
Algorithm Explanation:
1. We use a subquery to group the 'start' and 'end' timestamps for each process using the MAX function.
2. Within the subquery, we calculate the 'start' and 'end' timestamps separately based on the activity_type.
3. We then calculate the processing time for each process by subtracting the 'start' timestamp from the 'end' timestamp.
4. After obtaining the processing times for all processes, we group the results by machine_id and calculate the average processing time for each machine.
5. Finally, we round the average processing time to 3 decimal places using the ROUND function.
*/

/*
Optimization and Performance:
    The SQL query optimizes performance by using efficient join operations and aggregations. However, further optimizations may be possible depending on the database engine and indexing strategies.
    The use of subqueries and aggregation functions ensures that the processing is performed in a single pass through the data, reducing computational overhead.
    Additionally, indexing the relevant columns in the Activity table can improve query performance, especially for large datasets.
    Overall, the SQL solution provides an efficient and scalable approach to calculating the average processing time per machine.
*/

/*
Usage Examples and Test Cases:
    The provided SQL query can be executed on any SQL database supporting the SQL syntax used in the solution. It will produce the average processing time per machine based on the given Activity table.

Example Input:
    Activity table:
        +------------+------------+---------------+-----------+
        | machine_id | process_id | activity_type | timestamp |
        +------------+------------+---------------+-----------+
        | 0          | 0          | start         | 0.712     |
        | 0          | 0          | end           | 1.520     |
        | 0          | 1          | start         | 3.140     |
        | 0          | 1          | end           | 4.120     |
        | 1          | 0          | start         | 0.550     |
        | 1          | 0          | end           | 1.550     |
        | 1          | 1          | start         | 0.430     |
        | 1          | 1          | end           | 1.420     |
        | 2          | 0          | start         | 4.100     |
        | 2          | 0          | end           | 4.512     |
        | 2          | 1          | start         | 2.500     |
        | 2          | 1          | end           | 5.000     |
        +------------+------------+---------------+-----------+

    Expected Output:
        +------------+-----------------+
        | machine_id | processing_time |
        +------------+-----------------+
        | 0          | 0.894           |
        | 1          | 0.995           |
        | 2          | 1.456           |
        +------------+-----------------+
The SQL query should return the average processing time per machine rounded to 3 decimal places, as shown in the expected output.
*/
