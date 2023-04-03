# Mongo-Queries

About the CRUD Python Module:
The AACoutcomes.py Python Module displays examples of ways to create, read, update, and delete data from a Mongo Database. There methods allow for simple database queries and information inserts.
Motivation:
The Motivation for creating the CRUD Python Module was to allow myself and whoever wishes to use it to perform database queries without the use of a terminal. This expedites the process of logging into a mongo terminal each time you want to use it.

Getting Started:
1.	To get started, download the csv file containing the AAC outcomes and both python scripts called “AACoutcomes.py” and “CRUDExamples.py”. 
2.	Afterwards, the csv file needs to be imported to the Mongo Database as a collection called animals. 
3.	Since the process of logging into MongoDB is automated in the script, all that’s left is to change the data variable to the query you wish to make in the database.

Installation:
“aac_shelter_outcomes.csv”
“AACoutcomes.py”
“CRUDExamples.py”
Usage
Code Example:
The code lets you query specific items in the AAC database. An example of this would be checking whether a query of {"age_upon_outcome": "1.7 years", "animal_type": "Cat"} is found in the database. Another example would be an insert the above query into the database.

The process for these queries is simple. They take a data input (your query) and instantiates an instance of the AACoutcomes class. The results from the query are then posted as either “True” or the displayed data in a dictionary form. The “True” result is posted if you are trying to insert an item into the database. The data in a dictionary form is shown for each item in the read query that satisfies the search results.

Tests And Screenshot:
The screenshot below displays a create and read query for the {"age_upon_outcome": "2.5 years", "animal_type": "Dog"}. Basically, the script takes creates a query then displays the information retrieved from the database.

Create and Read Queries:

![python queries](https://user-images.githubusercontent.com/96409603/229402202-8e20c8b9-bd40-49dc-b130-968d469ad6cf.png)

Update and Delete Queries:

![update](https://user-images.githubusercontent.com/96409603/229402290-e763a21c-abe4-4898-96c4-8ef2a5bfb65d.png)
![delete](https://user-images.githubusercontent.com/96409603/229402296-4a7aac0b-bf1b-42e2-b088-cd052920b498.png)

AACoutcomes.py code:

![cru](https://user-images.githubusercontent.com/96409603/229402412-fef04bee-dd41-4105-bd0e-ea559b490460.png)
![d methods](https://user-images.githubusercontent.com/96409603/229402419-0ba6589e-3110-4415-8534-663cc6fa76f9.png)

Data Import:

![aac csv](https://user-images.githubusercontent.com/96409603/229402434-dcd3bd66-061f-46a6-8e00-c55c02e36533.png)

Admin and User Account Creation And Use:

![aacuser](https://user-images.githubusercontent.com/96409603/229402436-843d2903-55a7-4bd4-970d-780634bf518d.png)
![admin auth](https://user-images.githubusercontent.com/96409603/229402441-036bf6dd-ef8d-48c4-aec6-8331fdb8db45.png)
![both dbs display](https://user-images.githubusercontent.com/96409603/229402445-1762be9e-c0eb-4e83-8353-bae839181eb7.png)

 
 
 

