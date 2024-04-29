# NoSQL

Welcome to the NoSQL project! In this project, you'll delve into the world of NoSQL databases, with a focus on MongoDB. You will gain practical experience by performing common database operations without relying on traditional SQL queries.

## Resources

- [NoSQL Databases Explained](https://www.mongodb.com/nosql-explained)
- [What is NoSQL?](https://www.mongodb.com/nosql-explained/nosql-databases)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://docs.mongodb.com/manual/tutorial/query-documents/)
- [Aggregation](https://docs.mongodb.com/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://docs.mongodb.com/manual/reference/method/js-collection/)
- [The mongo Shell](https://docs.mongodb.com/manual/mongo/)

## Learning Objectives

After completing this project, you should be able to:

- Understand what NoSQL means.
- Differentiate between SQL and NoSQL databases.
- Explain the ACID properties.
- Identify different types of NoSQL databases and their benefits.
- Perform CRUD operations in MongoDB.
- Utilize MongoDB in conjunction with Python.

## Requirements

### MongoDB Command File

- All files will be interpreted on Ubuntu 18.04 LTS using MongoDB version 4.2.
- All files must end with a new line.
- The first line of all your files should be a comment explaining the purpose of the script.

### Python Scripts

- Python scripts will be interpreted on Ubuntu 18.04 LTS using Python 3.7 and PyMongo 3.10.
- Scripts must be executable and adhere to the pycodestyle (PEP 8) version 2.5.x.
- All functions and modules must have documentation strings.

### Installation and Setup

Ensure you have MongoDB installed and running on your system:

```bash
$ sudo apt update
$ sudo apt install -y mongodb-org
$ sudo service mongod start
$ mongo --version
```

Install PyMongo to interact with MongoDB from Python:

```bash
$ pip3 install pymongo
```

## Tasks

0. **List all databases**
   - Write a script that lists all databases in MongoDB.

1. **Create a database**
   - Create or switch to a database named `my_db`.

2. **Insert document**
   - Insert a document with the name "Holberton school" into the `school` collection.

3. **All documents**
   - List all documents in the `school` collection.

4. **All matches**
   - List all documents in the `school` collection where the name is "Holberton school".

5. **Count documents**
   - Display the number of documents in the `school` collection.

6. **Update document**
   - Add an address "972 Mission street" to all documents with the name "Holberton school".

7. **Delete by match**
   - Delete all documents with the name "Holberton school".

8. **List all documents in Python**
   - Write a Python function that lists all documents in a collection.

9. **Insert a document in Python**
   - Write a Python function that inserts a new document based on `kwargs`.

10. **Change school topics**
    - Write a Python function that updates the topics of a school document based on the school name.

11. **Schools by topic**
    - Write a Python function that returns the list of schools that have a specific topic.

12. **Log stats**
    - Write a Python script that provides some stats about Nginx logs stored in MongoDB.
