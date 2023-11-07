CREATE TABLE EMPLOYEE
(
 EMP_ID INT PRIMARY KEY ,  
LAST_NAME VARCHAR(60), 
JOB_ID INT , 
SALARY DECIMAL(50,4)
); 

INSERT INTO EMPLOYEE(EMP_ID , LAST_NAME , JOB_ID , SALARY )
    VALUES
    (1,'BHOSALE' , 'MANAGER' , 100000),
    (2,'CHOUDHARI','EMP_1', 90000),
    (3,'KOTE' , 'EMP_2', 80000),
    (4,'THAKARE' , 'EMP_3',70000),
    (5,'JADHAV','MANAGER',110000),

-- Q1. Find out all employees having salary less than all managers he should not be manager
SELECT E1.*
    FROM EMPLOYEE E1
    WHERE E1.JOB_ID != 'MANAGER'
    AND E1.SALARY < ALL (
         SELECT SALARY
         FROM EMPLOYEE E2
         WHERE E2.JOB_ID = 'MANAGER'
     );

-- Q2. Find out all employees having salary not equal to any of the managers salary he should not be manager
SELECT E1.*
    FROM EMPLOYEE E1
    WHERE E1.JOB_ID != 'MANAGER'
    AND E1.SALARY <> ALL (
         SELECT DISTINCT SALARY
         FROM EMPLOYEE E2
         WHERE E2.JOB_ID = 'MANAGER'
     );
