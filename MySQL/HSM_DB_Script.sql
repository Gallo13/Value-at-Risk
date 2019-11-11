CREATE TABLE IF NOT EXISTS stock_info_tbl (
	id_stock INT AUTO_INCREMENT NOT NULL,
	ticker_1 VARCHAR(6) NOT NULL,
	ticker_2 VARCHAR(6) NOT NULL,
	start_date DATE NOT NULL,
	end_date DATE NOT NULL,
	total_portfolio_value_both_stocks INT NOT NULL,
	PRIMARY KEY (id_stock)
);

CREATE TABLE IF NOT EXISTS ticker_1_return_of_stock_tbl (
	return_of_stock_value_1 INT NOT NULL,
	dates_1 DATE NOT NULL,
	closing_prices_1 INT NOT NULL,
	diff_1 INT NOT NULL,
	div_1 INT NOT NULL,
	PRIMARY KEY (return_of_stock_value_1)
);

SELECT t.*,
       (`closing_prices_1` - (SELECT `closing_prices_1`
                  FROM table t3
                  WHER t3.dates_1 < t.date_1
                  ORDER by t3.date_1 desc
                  LIMIT 1
                 )
       ) AS diff_1
FROM table t;

CREATE TABLE IF NOT EXISTS ticker_2_return_of_stock_tbl (
	return_of_stock_value_2 INT NOT NULL,
	dates_2 DATE NOT NULL,
	closing_prices_2 INT NOT NULL,
	diff_2 INT NOT NULL,
	div_2 INT NOT NULL,
	PRIMARY KEY (return_of_stock_value_2)
);

SELECT t.*,
       (`closing_prices_2` - (SELECT `closing_prices_2`
                  FROM table t3
                  WHERE t3.dates_2 < t.dates_2
                  ORDER by t3.dates_2 desc
                  LIMIT 1
                 )
       ) AS diff_2
FROM table t;

CREATE TABLE IF NOT EXISTS ticker_1_weight_tbl (
	weight_of_stock_value_1 INT NOT NULL,
	number_of_shares_1 INT NOT NULL,
	sum_of_ticker_and_stock_price_1 INT NOT NULL,
	div_mult_and_value_of_stock_1 INT NOT NULL,
	PRIMARY KEY (weight_of_stock_value_1)
);

SELECT COUNT(dates_1)
FROM ticker_1_return_of_stock_tbl

SELECT SUM(closing_prices_1)
FROM ticker_1_return_of_stock_tbl

CREATE TABLE IF NOT EXISTS ticker_2_weight_tbl (
	weight_of_stock_value_2 INT NOT NULL,
	number_of_shares_2 INT NOT NULL,
	sum_of_ticker_and_stock_price_2 INT NOT NULL,
	div_mult_and_value_of_stock_2 INT NOT NULL,
	PRIMARY KEY (weight_of_stock_value_2)
);

SELECT COUNT(dates_2)
FROM ticker_2_return_of_stock_tbl

SELECT SUM(closing_prices_2)
FROM ticker_2_return_of_stock_tbl

CREATE TABLE IF NOT EXISTS ticker_1_portfolio_value_tbl (
	return_of_stock_value_1 NOT NULL,
	weight_of_stock_value_1 INT NOT NULL,
	PRIMARY KEY (weight_of_stock_value_1)
);

CREATE TABLE IF NOT EXISTS ticker_2_portfolio_value_tbl (
	porfolio_values_1 INT NOT NULL,
	portfolio_values_2 INT NOT NULL,
	total_portfolio_value INT NOT NULL,
	PRIMARY KEY (total_portfolio_value)
);