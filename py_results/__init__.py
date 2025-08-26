import sqlite3
import xlsxwriter


with sqlite3.connect("db.db") as con:
    cur = con.cursor()
    