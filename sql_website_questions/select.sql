CREATE TABLE CITY (
    ID INT,
    NAME VARCHAR(50),
    COUNTRYCODE CHAR(3),
    DISTRICT VARCHAR(50),
    POPULATION INT
);

INSERT INTO CITY (ID, NAME, COUNTRYCODE, DISTRICT, POPULATION)
VALUES
(1, 'New York', 'USA', 'New York', 8400000),
(2, 'Los Angeles', 'USA', 'California', 3900000),
(3, 'Chicago', 'USA', 'Illinois', 2700000),
(4, 'Houston', 'USA', 'Texas', 2300000),
(5, 'Miami', 'USA', 'Florida', 90000),
(6, 'Toronto', 'CAN', 'Ontario', 2800000),
(7, 'Boston', 'USA', 'Massachusetts', 675000),
(8, 'Seattle', 'USA', 'Washington', 750000);

-- Question: Display all American cities with populations above 100000

SELECT *
FROM CITY
WHERE COUNTRYCODE = 'USA'
AND POPULATION > 100000;