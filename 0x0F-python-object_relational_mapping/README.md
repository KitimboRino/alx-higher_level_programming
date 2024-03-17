0x0F. Python - Object-relational mapping

Python programming is awesome for several reasons:

1. **Readable and Concise Code**: Python emphasizes readability and simplicity, making it easier to understand and write code quickly.

2. **Versatility**: Python is a multipurpose language suitable for a wide range of tasks, including web development, data analysis, artificial intelligence, automation, and more.

3. **Large Ecosystem**: Python has a vast ecosystem of libraries and frameworks, such as Django, Flask, NumPy, Pandas, TensorFlow, and many others, making it easy to find solutions for various tasks.

4. **Community Support**: Python has a large and active community of developers who contribute to its growth, offer support, and share resources.

To connect to a MySQL database from a Python script, you can use the `mysql-connector-python` library. Here's how you can do it:

```python
import mysql.connector

# Establish connection to MySQL server
conn = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create cursor object to execute queries
cursor = conn.cursor()

# Perform SQL operations
# For example, SELECT operation
cursor.execute("SELECT * FROM your_table")

# Fetch results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
conn.close()
```

To INSERT rows into a MySQL table from a Python script, you can modify the above code as follows:

```python
# Insert operation
sql = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
values = ("value1", "value2")
cursor.execute(sql, values)

# Commit changes
conn.commit()
```

ORM stands for Object-Relational Mapping. It is a programming technique for converting data between incompatible systems using object-oriented programming languages. In the context of Python and databases, an ORM allows you to interact with a database using Python objects, abstracting away the details of SQL queries.

To map a Python class to a MySQL table, you can use an ORM library such as SQLAlchemy. Here's a simple example:

```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class YourTable(Base):
    __tablename__ = 'your_table'

    id = Column(Integer, primary_key=True)
    column1 = Column(String)
    column2 = Column(String)

# Create engine and session
engine = create_engine('mysql://your_username:your_password@your_host/your_database')
Session = sessionmaker(bind=engine)
session = Session()

# Now you can use YourTable class to interact with the database
```

To create a Python virtual environment, you can use the built-in `venv` module. Here's how:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to create the virtual environment.
3. Run the following command:

```bash
python3 -m venv myenv
```

Replace `myenv` with the name you want to give to your virtual environment. This command will create a new directory with the specified name containing the virtual environment.

4. Activate the virtual environment:

- On Windows:

```bash
myenv\Scripts\activate
```

- On macOS and Linux:

```bash
source myenv/bin/activate
```

Once activated, you'll see the virtual environment's name in your command prompt. You can now install packages and run Python scripts within this isolated environment.
