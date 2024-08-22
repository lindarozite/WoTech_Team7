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
