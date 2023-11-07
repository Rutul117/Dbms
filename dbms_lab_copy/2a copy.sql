- Create the EMP table
CREATE TABLE EMP (
    Emp_no INT PRIMARY KEY,
    Emp_name VARCHAR(255),
    Dept_no INT
);

-- Create the DEPT table
CREATE TABLE DEPT (
    Dept_no INT PRIMARY KEY,
    Dept_name VARCHAR(255)
);

-- Create the Address table
CREATE TABLE Address (
    Dept_name INT PRIMARY KEY,
    Dept_location VARCHAR(255)
);

-- Insert data into the EMP table
INSERT INTO EMP (Emp_no, Emp_name, Dept_no) VALUES
(1, 'John Doe', 101),
(2, 'Jane Smith', 102),
(3, 'Bob Johnson', 101),
(4, 'Alice Brown', 103);

-- Insert data into the DEPT table
INSERT INTO DEPT (Dept_no, Dept_name) VALUES
(101, 'Human Resources'),
(102, 'Marketing'),
(103, 'Finance');

-- Insert data into the Address table
INSERT INTO Address (Dept_no, Dept_location) VALUES
(101, 'HR Building, 5th Avenue'),
(102, 'Marketing Tower, Main Street'),
(103, 'Finance Plaza, Park Avenue');


-- Q1. Display the location of departunent where employee Ram is working.
SELECT A.Dept_location
FROM EMP E
JOIN DEPT D ON E.Dept_no = D.Dept_no
JOIN Address A ON D.Dept_no = A.Dept_name
WHERE E.Emp_name = 'Ram';
-- Q2. Create view to store total no of employees working in each department in
ascending ordeR
CREATE VIEW DepartmentEmployeeCount AS
SELECT D.Dept_name, COUNT(E.Emp_no) AS EmployeeCount
FROM DEPT D
LEFT JOIN EMP E ON D.Dept_no = E.Dept_no
GROUP BY D.Dept_name
ORDER BY EmployeeCount ASC;
 -- 03. Find the name of department in which no employce is working
SELECT D.Dept_name
FROM DEPT D
LEFT JOIN EMP E ON D.Dept_no = E.Dept_no
WHERE E.Emp_no IS NULL;
