CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(50) NOT NULL
);

INSERT INTO Categories (CategoryID, CategoryName) VALUES
(1, 'Electronics'),
(2, 'Clothing'),
(3, 'Groceries');

select * from Categories;

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50) NOT NULL,
    CategoryID INT,
    Price DECIMAL(10,2) NOT NULL,
    StockQuantity INT,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

INSERT INTO Products (ProductID, ProductName, CategoryID, Price, StockQuantity) VALUES
(1, 'Laptop', 1, 800.00, 50),
(2, 'Smartphone', 1, 500.00, 100),
(3, 'Jeans', 2, 40.00, 200),
(4, 'T-Shirt', 2, 20.00, 300),
(5, 'Rice', 3, 30.00, 150),
(6, 'Milk', 3, 10.00, 200);

select * from Products;

CREATE TABLE SalesRecords (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    QuantitySold INT NOT NULL,
    SaleDate DATE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);


INSERT INTO SalesRecords (SaleID, ProductID, QuantitySold, SaleDate) VALUES
(1, 1, 5, '2025-11-01'),
(2, 2, 10, '2025-11-02'),
(3, 3, 20, '2025-11-03'),
(4, 4, 15, '2025-11-03'),
(5, 5, 25, '2025-11-04'),
(6, 6, 30, '2025-11-04');

select * from SalesRecords;

SELECT 
    c.CategoryName,
    SUM(p.Price * s.QuantitySold) AS TotalSales
FROM 
    SalesRecords s
JOIN 
    Products p ON s.ProductID = p.ProductID
JOIN 
    Categories c ON p.CategoryID = c.CategoryID
GROUP BY 
    c.CategoryName
ORDER BY
    TotalSales DESC;

