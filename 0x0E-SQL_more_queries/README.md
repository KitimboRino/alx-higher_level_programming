0x0E. SQL - More queries

### 1. How to create a new MySQL user:

To create a new MySQL user, you can use the `CREATE USER` statement. Here's an example:

```sql
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
```

This command creates a new user with the username 'new_user' and sets the password to 'password'. The `@'localhost'` part specifies that the user can only connect from the localhost.

### 2. How to manage privileges for a user to a database or table:

To manage privileges, you use the `GRANT` and `REVOKE` statements. For example, granting read-only access to a specific database:

```sql
GRANT SELECT ON database_name.* TO 'username'@'localhost';
```

Revoking privileges:

```sql
REVOKE SELECT ON database_name.* FROM 'username'@'localhost';
```

### 3. What’s a PRIMARY KEY:

A PRIMARY KEY is a column or a set of columns that uniquely identifies each record in a table. It ensures that the values in the key are unique and cannot be NULL.

Example:

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50)
);
```

### 4. What’s a FOREIGN KEY:

A FOREIGN KEY is a field in a table that is a primary key in another table. It establishes a link between the two tables.

Example:

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

### 5. How to use NOT NULL and UNIQUE constraints:

NOT NULL ensures that a column cannot contain NULL values, while UNIQUE ensures that all values in a column are different.

Example:

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);
```

### 6. How to retrieve data from multiple tables in one request:

You can use the `JOIN` operation to retrieve data from multiple tables based on a related column.

Example:

```sql
SELECT orders.order_id, customers.customer_name
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;
```

### 7. What are subqueries:

A subquery is a query nested inside another query. It can be used to return data that will be used in the main query.

Example:

```sql
SELECT employee_name
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE department_name = 'IT');
```

### 8. What are JOIN and UNION:

- **JOIN:** Combines rows from two or more tables based on a related column between them.

   Example (as mentioned above):

   ```sql
   SELECT orders.order_id, customers.customer_name
   FROM orders
   JOIN customers ON orders.customer_id = customers.customer_id;
   ```

- **UNION:** Combines the result sets of two or more SELECT statements into a single result set.

   Example:

   ```sql
   SELECT employee_id, employee_name FROM employees
   UNION
   SELECT manager_id, manager_name FROM managers;
   ```
