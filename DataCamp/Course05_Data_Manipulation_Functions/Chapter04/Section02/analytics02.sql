--Create a new column, showing the cocoa percentage of the chocolate bar that received a lower score, with cocoa coming from the same location (broad_bean_origin is the same).
--Create a new column with the difference between the current bar's cocoa percentage and the percentage of the previous bar.

SELECT 
	broad_bean_origin AS bean_origin,
	rating,
	cocoa_percent,
    -- Retrieve the cocoa % of the bar with the previous rating
	LAG(cocoa_percent) 
		OVER(PARTITION BY broad_bean_origin ORDER BY rating) AS percent_lower_rating
FROM ratings
WHERE company = 'Fruition'
ORDER BY broad_bean_origin, rating ASC;