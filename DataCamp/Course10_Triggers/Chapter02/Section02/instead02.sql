-- Create a new trigger
CREATE TRIGGER PreventNewDiscounts
ON Discounts
INSTEAD OF INSERT
AS
	RAISERROR ('You are not allowed to add discounts for existing customers.
                Contact the Sales Manager for more details.', 16, 1);