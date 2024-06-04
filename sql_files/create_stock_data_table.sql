-- create stock_data_table.sql

CREATE TABLE public.stock_data (
	id SERIAL PRIMARY KEY,
	symbol VARCHAR(10),
	date TIMESTAMP,
	open NUMERIC,
	high NUMERIC,
	low NUMERIC,
	close NUMERIC,
	volume BIGINT
);

