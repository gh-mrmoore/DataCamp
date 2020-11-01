SELECT
  -- Select the date portion of StartDate
  CONVERT(date, StartDate) as StartDate,
  -- Measure how many records exist for each StartDate
  COUNT(StartDate) as CountOfRows 
FROM CapitalBikeShare 
-- Group by the date portion of StartDate
GROUP BY CONVERT(date, StartDate)
-- Sort the results by the date portion of StartDate
ORDER BY CONVERT(date, StartDate);