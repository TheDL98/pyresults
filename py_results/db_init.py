import sqlite3

def db_init():
    with sqlite3.connect("results.db") as con:
        con.executescript("""
    --
    -- File generated with SQLiteStudio v3.4.17 on Wed Aug 27 11:46:30 2025
    --
    -- Text encoding used: System
    --
    PRAGMA foreign_keys = off;
    BEGIN TRANSACTION;

    -- Table: sample_locations
    CREATE TABLE IF NOT EXISTS sample_locations (
        location_id    INTEGER PRIMARY KEY AUTOINCREMENT
                            UNIQUE
                            NOT NULL,
        location_name  TEXT    NOT NULL
                            UNIQUE,
        sample_type_id INTEGER REFERENCES sample_types (sample_type_id) 
    );


    -- Table: sample_types
    CREATE TABLE IF NOT EXISTS sample_types (
        sample_type_id   INTEGER PRIMARY KEY AUTOINCREMENT
                                UNIQUE
                                NOT NULL,
        sample_type_name TEXT    UNIQUE
    );


    -- Table: samples
    CREATE TABLE IF NOT EXISTS samples (
        sample_id    INTEGER PRIMARY KEY AUTOINCREMENT
                            UNIQUE
                            NOT NULL,
        sample_date  TEXT,
        sample_time  TEXT,
        sample_value REAL    NOT NULL,
        location_id  INTEGER REFERENCES sample_locations (location_id),
        test_type_id INTEGER REFERENCES test_types (test_type_id) 
    );


    -- Table: test_types
    CREATE TABLE IF NOT EXISTS test_types (
        test_type_id   INTEGER PRIMARY KEY AUTOINCREMENT
                            UNIQUE
                            NOT NULL,
        test_type_name TEXT    UNIQUE,
        test_type_unit TEXT
    );


    COMMIT TRANSACTION;
    PRAGMA foreign_keys = on;

    """)
        con.commit()