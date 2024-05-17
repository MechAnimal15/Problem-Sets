620. Not Boring Movies
[Problem Link](https://leetcode.com/problems/not-boring-movies/submissions/1260708281?envType=study-plan-v2&envId=top-sql-50)

Oracle SQL Solution

/* Write your PL/SQL query statement below */
SELECT id, movie, description, rating
FROM Cinema
WHERE MOD(id, 2) = 1
  AND description <> 'boring'
ORDER BY rating DESC;


'''
  Runtime: 1041 ms
'''
