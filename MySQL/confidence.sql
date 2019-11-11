CREATE PROCEDURE `confidence` ()
BEGIN

INSERT INTO stock_info_tbl
SELECT conf_percent FROM confidence_tbl;

INSERT INTO confidence_tbl
SELECT total_portfolio FROM portfolio_value_tbl;

SELECT total_portfolio FROM confidence_tbl ORDER BY total_portfolio_value, ROLL_NO DESC;

SELECT 1 - (conf_percent / 100) as alpha_percentile FROM confidence_tbl;

SELECT total_portfolio as loss_level FROM confidence_tbl WHERE id = 13;

SELECT loss_level * total_portfolio as value_of_result FROM confidence_tbl;

INSERT INTO stock_id_tbl
SELECT vale_of_result FROM confidence_tbl;

END