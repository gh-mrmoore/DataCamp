SELECT 
	first_name,
	last_name,
	email 
FROM voters
-- Look for the "dan" expression in the first_name
WHERE CHARINDEX('dan', first_name) > 0
    -- Look for last_names that do not contain the letter "z"
	AND CHARINDEX('z', last_name) = 0;