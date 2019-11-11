CREATE PROCEDURE `return_1` ()
BEGIN

SELECT ticker_1_return_of_stock_tbl.id_return_1,(ticker_1_return_of_stock_tbl.closing_prices_1-t.closing_prices_1) as diff_1 FROM ticker_1_return_of_stock_tbl
inner join ticker_1_return_of_stock_tbl as t on
ticker_1_return_of_stock_tbl.id_return_1=t.id_return_1+1;

SELECT closing_prices_1 / diff_1 as return_of_stock_1 FROM ticker_1_return_of_stock_tbl;

END