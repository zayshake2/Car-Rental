
-- tables from Part 2 I used

CREATE TABLE Vehicle (
    VehicleID varchar(100) NOT NULL,
    Description varchar(100) NOT NULL,
    Year int NOT NULL,
    Type int NOT NULL,
    Category int NOT NULL,
    PRIMARY KEY (VehicleID)
    );

CREATE TABLE Customer (
    CustID int NOT NULL,
    Name varchar(50) NOT NULL,
    Phone varchar(100) NOT NULL,
    PRIMARY KEY (CustID)
    );

CREATE TABLE Rental (
    CustID int NOT NULL,
    VehicleID varchar(100) NOT NULL,
    StartDate date NOT NULL,
    OrderDate date NOT NULL,
    RentalType int NOT NULL,
    Qty int NOT NULL,
    ReturnDate date,
    TotalAmount int,
    PaymentDate date,
    FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID) ON UPDATE cascade,
    FOREIGN KEY (CustID) REFERENCES Customer(CustID) ON UPDATE cascade
    );

CREATE TABLE Rate (
    Type int NOT NULL,
    Category int NOT NULL,
    Weekly int NOT NULL,
    Daily int NOT NULL
    );


-- Query 2 (View)
CREATE VIEW vRentalInfo 
AS SELECT OrderDate, StartDate, ReturnDate, SUM(RentalType*Qty) AS TotalDays, 
Rental.VehicleID AS VIN, Description AS Vehicle, Customer.CustID AS CustomerID, 
Name AS CustomerName, TotalAmount AS OrderAmount,
 CASE WHEN PaymentDate is NULL THEN TotalAmount
     ELSE 0 END AS RentalBalance,
 CASE WHEN Vehicle.Type = 1 THEN 'Compact'
      WHEN Vehicle.Type = 2 THEN 'Medium'
      WHEN Vehicle.Type = 3 THEN 'Large'
      WHEN Vehicle.Type = 4 THEN 'SUV'
      WHEN Vehicle.Type = 5 THEN 'Truck'
      ELSE 'Van' END AS Type,
CASE  WHEN Vehicle.Category = 1 THEN 'Luxury'
      ELSE 'Basic' END AS Category
FROM Customer, Vehicle, Rental, Rate
WHERE Vehicle.VehicleID = Rental.VehicleID AND Customer.CustID = Rental.CustID 
AND Vehicle.Type = Rate.Type AND Vehicle.Category = Rate.Category
GROUP BY Rental.VehicleID, Rental.CustID
ORDER BY StartDate ASC


