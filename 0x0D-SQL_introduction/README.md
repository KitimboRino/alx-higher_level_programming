0x0D. SQL - Introduction

1. **What's a database?**
   - A database is a structured collection of data that is organized and stored in a way that allows efficient retrieval and management. It can store various types of information and is designed for easy access and management of data.

2. **What's a relational database?**
   - A relational database is a type of database that organizes data into tables with rows and columns. It establishes relationships between these tables using keys, enabling the representation of complex relationships and supporting efficient data retrieval.

3. **What does SQL stand for?**
   - SQL stands for Structured Query Language. It is a domain-specific language used for managing and manipulating relational databases. SQL allows users to interact with the database by defining and manipulating the data.

4. **What's MySQL?**
   - MySQL is an open-source relational database management system (RDBMS) that uses SQL. It is widely used for web development and other applications, providing a reliable and scalable solution for managing and retrieving data.

5. **How to create a database in MySQL?**
   - To create a database in MySQL, you can use the following SQL command:
     ```sql
     CREATE DATABASE database_name;
     ```

6. **What does DDL and DML stand for?**
   - DDL stands for Data Definition Language, which includes SQL commands used for defining and managing the structure of a database, such as creating or altering tables.
   - DML stands for Data Manipulation Language, which includes SQL commands used for manipulating the data stored in the database, such as inserting, updating, or deleting records.

7. **How to CREATE or ALTER a table?**
   - To create a table:
     ```sql
     CREATE TABLE table_name (
       column1 datatype,
       column2 datatype,
       ...
     );
     ```
   - To alter a table (add a new column, for example):
     ```sql
     ALTER TABLE table_name
     ADD COLUMN new_column datatype;
     ```

8. **How to SELECT data from a table?**
   - To select data from a table:
     ```sql
     SELECT column1, column2
     FROM table_name
     WHERE condition;
     ```

9. **How to INSERT, UPDATE or DELETE data?**
   - To insert data into a table:
     ```sql
     INSERT INTO table_name (column1, column2, ...)
     VALUES (value1, value2, ...);
     ```
   - To update data in a table:
     ```sql
     UPDATE table_name
     SET column1 = value1, column2 = value2, ...
     WHERE condition;
     ```
   - To delete data from a table:
     ```sql
     DELETE FROM table_name
     WHERE condition;
     ```

10. **What are subqueries?**
    - Subqueries are queries embedded within another query. They are used to retrieve data that will be used in the main query for further filtering or comparison.

11. **How to use MySQL functions?**
    - MySQL provides various built-in functions that perform operations on data. For example, to calculate the average of a column:
      ```sql
      SELECT AVG(column_name) FROM table_name;
      ```
      There are functions for string manipulation, mathematical operations, date and time handling, and more in MySQL.
