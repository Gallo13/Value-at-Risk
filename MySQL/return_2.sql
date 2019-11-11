CREATE PROCEDURE `return_2` ()
BEGIN

SELECT ticker_2_return_of_stock_tbl.id_return_2,(ticker_2_return_of_stock_tbl.closing_prices_2-t.closing_prices_2) as diff_2 FROM ticker_2_return_of_stock_tbl
inner join ticker_2_return_of_stock_tbl as t on
ticker_2_return_of_stock_tbl.id_return_2=t.id_return_2+1;

SELECT closing_prices_2 / diff_2 as return_of_stock_2 FROM ticker_2_return_of_stock_tbl;

END