-- Create @ReturnCode
DECLARE @ReturnCode int
-- Create @ErrorOut
DECLARE @ErrorOut nvarchar(max)
-- Execute the SP, storing the result in @ReturnCode
EXEC @ReturnCode = dbo.cuspRideSummaryDelete
    -- Specify @DateParm
	@DateParm = '1/32/2018',
    -- Assign @ErrorOut to @Error
	@Error = @ErrorOut OUTPUT
-- Select @ReturnCode and @ErrorOut
SELECT
	@ReturnCode AS ReturnCode,
    @ErrorOut AS ErrorMessage;