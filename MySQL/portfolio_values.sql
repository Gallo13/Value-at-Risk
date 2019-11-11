CREATE PROCEDURE `portfolio_values` ()
BEGIN

INSERT INTO portfolio_value_tbl
SELECT return_of_stock_1 FROM ticker_1_return_of_stock_tbl;

INSERT INTO portfolio_value_tbl
SELECT weight_value_1 FROM ticker_1_weight_stock_tbl;

INSERT INTO portfolio_value_tbl
SELECT return_of_stock_2 FROM ticker_2_return_of_stock_tbl;

INSERT INTO portfolio_value_tbl
SELECT weight_value_2 FROM ticker_2_weight_stock_tbl;

SELECT (return_of_stock_1 * weight_value_1) as portfolio_value_1 FROM portfolio_value_tbl;

SELECT (return_of_stock_2 * weight_value_2) as portfolio_value_2 FROM portfolio_value_tbl;

SELECT concat(portfolio_value_1, portfolio_value_2) as total_portfolio FROM portfolio_value_tbl;

INSERT INTO stock_info_tbl
SELECT total_portfolio FROM portfolio_value_tbl;

END