CREATE TABLE Account (
    Acc_no INT PRIMARY KEY,
    branch_name VARCHAR(50),
    balance DECIMAL(10, 2),
    FOREIGN KEY (branch_name) REFERENCES branch(branch_name)
);

CREATE TABLE branch (
    branch_name VARCHAR(50) PRIMARY KEY,
    branch_city VARCHAR(50),
    assets DECIMAL(12, 2)
);

CREATE TABLE customer (
    cust_name VARCHAR(50) PRIMARY KEY,
    cust_street VARCHAR(50),
    cust_city VARCHAR(50)
);

CREATE TABLE Depositor (
    cust_name VARCHAR(50),
    acc_no INT,
    PRIMARY KEY (cust_name, acc_no),
    FOREIGN KEY (cust_name) REFERENCES customer(cust_name),
    FOREIGN KEY (acc_no) REFERENCES Account(Acc_no)
);

CREATE TABLE Loan (
    loan_no INT PRIMARY KEY,
    branch_name VARCHAR(50),
    amount DECIMAL(10, 2),
    FOREIGN KEY (branch_name) REFERENCES branch(branch_name)
);

CREATE TABLE Borrower (
    cust_name VARCHAR(50),
    loan_no INT,
    PRIMARY KEY (cust_name, loan_no),
    FOREIGN KEY (cust_name) REFERENCES customer(cust_name),
    FOREIGN KEY (loan_no) REFERENCES Loan(loan_no)
);


-- Insert sample data into the "branch" table
INSERT INTO branch (branch_name, branch_city, assets)
VALUES
    ('Akurdi', 'Pune', 200000),
    ('MG Road', 'Bangalore', 250000),
    ('Main Street', 'New York', 300000);

-- Insert sample data into the "customer" table
INSERT INTO customer (cust_name, cust_street, cust_city)
VALUES
    ('Alice', '123 Elm St', 'Pune'),
    ('Bob', '456 Oak Ave', 'Bangalore'),
    ('Charlie', '789 Maple Rd', 'New York');

-- Insert sample data into the "Account" table
INSERT INTO Account (Acc_no, branch_name, balance)
VALUES
    (1, 'Akurdi', 1500),
    (2, 'Akurdi', 2000),
    (3, 'MG Road', 3000),
    (4, 'Main Street', 5000);

-- Insert sample data into the "Depositor" table
INSERT INTO Depositor (cust_name, acc_no)
VALUES
    ('Alice', 1),
    ('Bob', 2),
    ('Charlie', 3),
    ('Alice', 4);

-- Insert sample data into the "Loan" table
INSERT INTO Loan (loan_no, branch_name, amount)
VALUES
    (101, 'Akurdi', 12000),
    (102, 'Akurdi', 1300),
    (103, 'MG Road', 15000),
    (104, 'Main Street', 1400);

-- Insert sample data into the "Borrower" table
INSERT INTO Borrower (cust_name, loan_no)
VALUES
    ('Alice', 101),
    ('Bob', 102),
    ('Charlie', 103),
    ('Alice', 104);


