CREATE TABLE "MRAPS_TRANSFERS" (
	"State" varchar(10) NOT NULL,
	"Station_Name" varchar(100) NOT NULL,
	"NSN" varchar(30) NOT NULL,
	"Item_Name" varchar(100) NOT NULL,
	"Quantity" varchar(10),
	"UI" varchar(30) NOT NULL,
	"Aquisition_Value" varchar(20),
	"DEMIL_Code" varchar(30) NOT NULL,
	"DEMIL_IC" varchar(30) NOT NULL,
	"Ship_Date" varchar(100) NOT NULL,
	"Station_Type" char(20) NOT NULL,
	"federal_supply_class" varchar(30),
	"year" varchar(10)
);
