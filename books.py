import sqlite3
import pandas as pd

# David White
# 2023/05/08
# CIS-2532
# Instructor: Mohammad Morovati
# Assignment: Execise 17.1
# Description:
# Perform each of the following tasks on the books database from Section 17.2
#
# a) Select all author's last names form the authors table in descending order.
#
# b) Select all book titles from the titles table in ascending order.
#
# c) Use an INNER JOIN to select all the books for a specific author. Include
# the title, copyright year, and ISBN. Order the information alphabetically
# by title
# 
# d) Insert a new author into the authors table. 
# 
# e) Insert a new title for an author. Remember that the book 
# must have an entry in the author_ISBN table and an entry in the titles table


# load db
db = sqlite3.connect('books.db')

# create cursor
cursor = db.cursor()

# A
print(pd.read_sql("""SELECT last
                     FROM authors 
                     ORDER BY last DESC""", db))

# B
print(pd.read_sql("""SELECT title
                     FROM titles
                     ORDER BY title ASC""", db))

# C 
print(pd.read_sql("""SELECT id, title, copyright 
                     FROM titles
                     INNER JOIN author_ISBN
                        ON titles.isbn = author_ISBN.isbn
                     WHERE id = 1
                     ORDER BY title ASC""", db))

# D

# add author to authors
cursor = cursor.execute("""INSERT INTO authors (first, last)
                           VALUES ('Al','Sweigart')""")

print(pd.read_sql("SELECT id, first, last FROM authors", db, index_col=['id']))

# E
# add book to titles
cursor = cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright)
                           VALUES (1593279922, 'Automate the Boring Stuff', 2, 2019)""")

print(pd.read_sql("SELECT * FROM titles", db))

# add book to author_ISBN
cursor = cursor.execute("""INSERT INTO author_ISBN (id, isbn)
                           VALUES (6, 1593279922)""")

print('\n',pd.read_sql("SELECT * FROM author_ISBN", db).tail())
