SELECT 
	first_name,
	last_name,
   	-- Extract the year of the first vote
	YEAR(first_vote_date)  AS first_vote_year,
    -- Extract the month of the first vote
	MONTH(first_vote_date) AS first_vote_month,
    -- Extract the day of the first vote
	DAY(first_vote_date)   AS first_vote_day
FROM voters
-- The year of the first vote should be greater than 2015
WHERE YEAR(first_vote_date) > 2015;