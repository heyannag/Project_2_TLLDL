# Group: Thomas Laws Lays Down the Law

## Team
* Thomas Laws
* Kellie Cox
* Alicia Cheasty
* Kevin Eugene
* Anna Givens

## Table of Contents
* [Objective](#Objective)
* [Scope of Work](#Scope of Work)
* [Examples & Inspiration](#Examples & Inspiration)
* [Topic](#Topic)
* [Technologies](#Technologies)
* [Data](#Data)
* [Data Conversion](#Data Conversion)


# Objective 
* Create a visualization must include a Python Flask–powered RESTful API, HTML/CSS, JavaScript, and at least one database (SQL, MongoDB, SQLite, etc.). 

## Project Requirements

* Project should fall into one of the below four tracks: 
    * A custom “creative” D3.js project (i.e., a nonstandard graph or chart)
    * A combination of web scraping and Leaflet or Plotly
    * A dashboard page with multiple charts that update from the same data

* Include at least one JS library that has not been covered in this course.
* Must be powered by a data set with at least 100 records.
* Must include some level of user-driven interaction (e.g., menus, dropdowns, textbxtboxes). Your final visualization should ideally include at least three views. 

 
# Scope of Work
Day 1 (Thursday, June 25):
* Between now and Saturday, you will need to start brainstorming topics with your group and researching potential data sets. Your focus should center around:
	* Selecting a topic 	
	* Finding a data set	
	* Finding inspiration	
	* “Sketching” your ideal visuals
* Creating a 1-page proposal

Day 2 (Tuesday, June 30): 
* You will need to create a 1-page proposal that includes:
	* A brief articulation of your chosen topic and rationale
	* A link to your data set(s) and a screenshot of the metadata if it exists.	
	* 3 or 4 screenshots of relevant, “inspiring” visualizations that frame your creative fodder	
	* A sketch of the final design 	
	* A link to the primary GitHub repository you’ll be housing your work in

Day 3 (Thursday, July 2):
* Project Work

# Examples & Inspiration


# Topic
"1033" Program Transfers Since Ferguson
Analyzing the transfers made by the Defense Logistics Agency to local law enforcement since the protests in Ferguson, Missouri in August 2014. See below for details.

The DLA is a sub-agency of the Department of Defense; it provides equipment to local law enforcement agencies [through its Law Enforcement Support Office](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/PublicInformation/). The program is commonly referred to as the ["1033" program](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/ProgramFAQs.aspx) due to the statute that enabled it in 1997.

# Technologies
* [Python3](#Python)
	* Matplotlib
	* Pandas
* [PostgreSQL](#PostgreSQL)
* [JavaScript](#JavaScript)
    * D3
    * Plotly
* [HTML/CSS](#HTML/CSS)


## Python 

# Data
The data used in this analysis comes from the DLA's [LESO Public Information](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/PublicInformation/) page. The [`data/all_original_data.xlsx`](data/all_original_data.xlsx) file contains all property transferred to participating agencies that was held by them as of March 31, 2020. It is updated quarterly.

# Data Conversion
The convert_data_to_csv.ipynb notebook takes the Excel file the DLA produces, reads each of the 52 sheets, and combines them into a single CSV with all the available data. The resulting CSV file is output to outputs/dla_1033_transfers.csv.

        '''
        xls = pd.read_excel('../data/all_original_data.xlsx', sheet_name = None)
        '''

# Analysis
The [`analyze_transfers.ipynb`](notebooks/analyze_transfers.ipynb) takes the CSV data and analyzes all transfers where the *Ship Date* is after August 25, 2014, which marked the end of the first wave of protests in Ferguson. This notebook contains some of the following analysis:
* Loading the data

        '''
        data = (pd.read_csv(
        "../outputs/dla_1033_transfers.csv", 
        parse_dates = ["Ship Date"])
        '''

* Filtering for transfers post August 25, 2014

        '''
        post_ferguson = data[lambda x: x["Ship Date"] > "2014-08-25"]
        '''

* Totaling the transfers

        '''
        print('''Since Ferguson there have been {:,} total transfers of equipment that are still held by the police agency.
        They total ${:,}'''.format(
            len(post_ferguson),
            post_ferguson["Acquisition Value"].sum()
        ))
        '''
    Since Ferguson there have been 47,429 total transfers of equipment that are still held by the police agency.
    They total $854,104,343.93
    
![image]('outputs/charts_mpl/yearly_totals.png')

* Highlighting categories of items 

# PostgreSQL

        '''
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
        '''
# JavaScript

# HTML/CSS
