SELECT *
	-- Avoid being blocked
	FROM transactions WITH (NOLOCK)
WHERE account_id = 1