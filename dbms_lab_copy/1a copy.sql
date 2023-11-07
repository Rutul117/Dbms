CREATE TABLE Branch (
         branch_name VARCHAR(255) PRIMARY KEY,
         branch_city VARCHAR(255),
         assets DECIMAL(15, 2)
     );

CREATE TABLE Account (
         acc_no INT PRIMARY KEY,
         branch_name VARCHAR(255),
         balance DECIMAL(10, 2),
         FOREIGN KEY (branch_name) REFERENCES Branch(branch_name)
     );


 CREATE TABLE Customer (
         cust_name VARCHAR(255) PRIMARY KEY,
         cust_street VARCHAR(255),
         cust_city VARCHAR(255)
     );


 CREATE TABLE Depositor (
         cust_name VARCHAR(255),
         acc_no INT,
         PRIMARY KEY (cust_name, acc_no),
         FOREIGN KEY (cust_name) REFERENCES Customer(cust_name),
         FOREIGN KEY (acc_no) REFERENCES Account(acc_no)
     );


 CREATE TABLE Loan (
         loan_no INT PRIMARY KEY,
         branch_name VARCHAR(255),
         amount DECIMAL(10, 2),
         FOREIGN KEY (branch_name) REFERENCES Branch(branch_name)
     );


 CREATE TABLE Borrower (
         cust_name VARCHAR(255),
         loan_no INT,
         PRIMARY KEY (cust_name, loan_no),
         FOREIGN KEY (cust_name) REFERENCES Customer(cust_name),
         FOREIGN KEY (loan_no) REFERENCES Loan(loan_no)
    );


INSERT INTO Branch (branch_name, branch_city, assets)
    VALUES
         ('BranchA', 'CityA', 100000.00),
         ('BranchB', 'CityB', 75000.00),
         ('BranchC', 'CityC', 125000.00);


INSERT INTO Customer (cust_name, cust_street, cust_city)
    VALUES
         ('CustomerA', 'StreetA', 'CityA'),
         ('CustomerB', 'StreetB', 'CityB'),
         ('CustomerC', 'StreetC', 'CityC');


 INSERT INTO Account (acc_no, branch_name, balance)
     VALUES
         (101, 'BranchA', 5000.00),
         (102, 'BranchB', 7500.00),
         (103, 'BranchC', 3000.00);


 INSERT INTO Loan (loan_no, branch_name, amount)
     VALUES
         (201, 'BranchA', 10000.00),
         (202, 'BranchB', 8000.00),
         (203, 'BranchC', 12000.00);



 INSERT INTO Depositor (cust_name, acc_no)
     VALUES
         ('CustomerA', 101),
         ('CustomerB', 102),
         ('CustomerC', 103);



 INSERT INTO Borrower (cust_name, loan_no)
     VALUES
         ('CustomerA', 201),
         ('CustomerB', 202),
         ('CustomerC', 203);



-- Q1: Find all customers who have a loan from the bank. Find their names, loan no, and loan amount.
SELECT C.cust_name, L.loan_no, L.amount
FROM Customer C
JOIN Borrower B ON C.cust_name = B.cust_name
JOIN Loan L ON B.loan_no = L.loan_no;

-- Q2: Find all loan numbers for loans made at Akurdi Branch with a loan amount of 12000.
SELECT loan_no
FROM Loan
WHERE branch_name = 'Akurdi' AND amount = 12000;

-- Q3: Find the average account balance at each branch.
SELECT branch_name, AVG(balance) AS avg_balance
FROM Account
GROUP BY branch_name;

-- Q4: Find all customers who have an account or a loan or both at the bank.
SELECT C.cust_name
FROM Customer C
WHERE EXISTS (
    SELECT 1
    FROM Account A
    WHERE C.cust_name IN (SELECT cust_name FROM Depositor WHERE acc_no = A.acc_no)
) OR EXISTS (
    SELECT 1
    FROM Borrower B
    WHERE C.cust_name = B.cust_name
);

-- Q5: Delete all loans with a loan amount between 1300 and 1500.
DELETE FROM Loan
WHERE amount BETWEEN 1300 AND 1500;
