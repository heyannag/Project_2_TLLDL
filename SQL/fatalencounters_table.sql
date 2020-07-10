DROP TABLE fatal_encounter;

Create Table fatal_encounter(
id VARCHAR(30) PRIMARY KEY,
age VARCHAR(5),
gender VARCHAR(15),
race VARCHAR(50),
city VARCHAR(100),
state VARCHAR(5),
lat VARCHAR(30),
long VARCHAR(30),
cause_of_death VARCHAR(100),
mental_illness VARCHAR (30),
year varchar(5)
);

Select * from fatal_encounter;