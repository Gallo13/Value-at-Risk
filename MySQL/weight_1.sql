CREATE PROCEDURE `weight_1` ()
BEGIN

INSERT INTO ticker_1_weight_tbl(number_of_shares_1)
SELECT COUNT(dates_1)
FROM ticker_1_return_of_stock_tbl;

INSERT INTO ticker_1_weight_tbl(stock_price_1)
SELECT closing_prices_1 FROM ticker_1_return_of_stock_tbl;

SELECT (number_of_shares_1 * stock_price_1) as mult_value_1 FROM ticker_1_weight_tbl;

SELECT SUM(stock_price_1) as sum_stocks_1 FROM ticker_1_weight_tbl;

SELECT (mult_value_1 / sum_stocks_1) as weight_value_1 FROM ticker_1_weight_tbl;

END