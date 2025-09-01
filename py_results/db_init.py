import sqlite3

def db_init():
    with sqlite3.connect("results.db") as con:
        con.executescript("""
--
-- File generated with SQLiteStudio v3.4.17 on Mon Sep 1 13:00:56 2025
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: MainCategories
CREATE TABLE IF NOT EXISTS MainCategories (
    MainCategoryID   INTEGER PRIMARY KEY AUTOINCREMENT
                             UNIQUE
                             NOT NULL,
    MainCategoryName TEXT    UNIQUE
                             NOT NULL
);


-- Table: Samples
CREATE TABLE IF NOT EXISTS Samples (
    SampleID       INTEGER PRIMARY KEY AUTOINCREMENT
                           UNIQUE
                           NOT NULL,
    SampleDate     TEXT,
    SampleTime     TEXT,
    SampleValue    REAL    NOT NULL,
    MainCategoryID INTEGER REFERENCES MainCategories (MainCategoryID) 
                           NOT NULL,
    SubCategoryID          REFERENCES SubCategories (SubCategoryID),
    TestTypeID     INTEGER REFERENCES TestTypes (TestTypeID) 
                           NOT NULL
);


-- Table: SubCategories
CREATE TABLE IF NOT EXISTS SubCategories (
    SubCategoryID   INTEGER PRIMARY KEY AUTOINCREMENT
                            UNIQUE
                            NOT NULL,
    SubCategoryName TEXT    NOT NULL
                            UNIQUE,
    MainCategoryID          REFERENCES MainCategories (MainCategoryID) 
                            NOT NULL
);


-- Table: TestTypes
CREATE TABLE IF NOT EXISTS TestTypes (
    TestTypeID   INTEGER PRIMARY KEY AUTOINCREMENT
                         UNIQUE
                         NOT NULL,
    TestTypeName TEXT    UNIQUE,
    TestTypeUnit TEXT
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

    """)
        con.commit()