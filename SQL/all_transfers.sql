DROP TABLE IF EXISTS all_transfers;

CREATE TABLE all_transfers (
	city varchar(100) NOT NULL,
	state varchar(5) NOT NULL,
	station_name varchar(100) NOT NULL PRIMARY KEY,
	item_name varchar(100) NOT NULL,
	quantity varchar(10),
	ui varchar(30) NOT NULL,
	aquisition_value varchar(30) NOT NULL,
	ship_date varchar(100) NOT NULL
);

SELECT * FROM all_transfers;