--version 1

--Calculate total Sales by City

SELECT 
    owners.city, 
    SUM(procedures.price) AS totalsales
FROM 
    sales 
JOIN 
    procedures ON sales.procedurecode = procedures.procedurecode
JOIN 
    pets ON sales.petid = pets.petid
JOIN 
    owners ON pets.ownerid = owners.ownerid
GROUP BY 
    owners.city;

--Calculate total Sales by Pet Kind

SELECT 
    pets.kind, 
    SUM(procedures.price) AS totalsales
FROM 
    sales 
JOIN 
    procedures ON sales.procedurecode = procedures.procedurecode
JOIN 
    pets ON sales.petid = pets.petid
GROUP BY 
    pets.kind;
  
--Calculate total Sales by City and Pet Kind

SELECT 
    owners.city, 
    pets.kind, 
    SUM(procedures.price) AS totalsales
FROM 
    sales 
JOIN 
    procedures ON sales.procedurecode = procedures.procedurecode
JOIN 
    pets ON sales.petid = pets.petid
JOIN 
    owners ON pets.ownerid = owners.ownerid
GROUP BY 
    owners.city, 
    pets.kind;
  
--Calculate Average sales by City

SELECT 
    owners.city, 
    SUM(procedures.price) AS totalsales,
    ROUND(AVG(procedures.price),2) AS averagesales
FROM 
    sales 
JOIN 
    procedures ON sales.procedurecode = procedures.procedurecode
JOIN 
    pets ON sales.petid = pets.petid
JOIN 
    owners ON pets.ownerid = owners.ownerid
GROUP BY 
    owners.city;

-- version 2
SELECT Sales.PetID, Pets.OwnerID, Owners.City, count(Sales.PetID) AS SalesPerCity
From Sales
Left Join Pets ON Sales.PetID = Pets.PetID
Left join Owners on Pets.OwnerID = Owners.OwnerID
group by Owners.City;

SELECT Pets.Kind, count(Pets.PetID) as Sales
from Sales
left join Pets on Sales.PetID = Pets.PetID
group by Pets.Kind;

SELECT Pets.Kind, SUM(Procedures.Price) as TotalSum
from Procedures
left join Sales on Sales.ProcedureCode = Procedures.ProcedureCode
Left join Pets on Pets.PetID = Sales.PetID
Group by Pets.Kind;

SELECT Owners.City, 
count(Sales.TransactionID) as Sales, 
SUM(Procedures.Price) AS Sum, 
ROUND(AVG(Procedures.Price),2) AS AverageSales
from Procedures
Left join Sales On Sales.ProcedureCode = Procedures.ProcedureCode
Left join Pets on Pets.PetID = Sales.PetID
Left join Owners on Owners.OwnerID = Pets.OwnerID
Group by Owners.City;
