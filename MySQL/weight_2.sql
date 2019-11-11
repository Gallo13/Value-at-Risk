CREATE PROCEDURE `weight_2` ()
BEGIN

INSERT INTO ticker_2_weight_tbl(number_of_shares_2)
SELECT COUNT(dates_2)
FROM ticker_2_return_of_stock_tbl;

INSERT INTO ticker_2_weight_tbl(stock_price_2)
SELECT closing_prices_2 FROM ticker_2_return_of_stock_tbl;

SELECT (number_of_shares_2 * stock_price_2) as mult_value_2 FROM ticker_2_weight_tbl;

SELECT SUM(stock_price_2) as sum_stocks_2 FROM ticker_2_weight_tbl;

SELECT (mult_value_2 / sum_stocks_2) as weight_value_2 FROM ticker_2_weight_tbl;

END