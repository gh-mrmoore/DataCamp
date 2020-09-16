-- Create the CTE
WITH BloodPressure(MaxBloodPressure) 
AS
(SELECT MAX(BloodPressure) AS MaxBloodPressure
    FROM Kidney)

SELECT *
FROM Kidney a
-- Join the CTE  
JOIN BloodPressure b
ON a.BloodPressure = b.MaxBloodPressure