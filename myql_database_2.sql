DROP DATABASE IF EXISTS gpacalculator;
CREATE DATABASE IF NOT EXISTS gpacalculator;

USE gpacalculator;

DROP TABLE IF EXISTS feedback;
DROP TABLE  IF EXISTS gpa_history;
-- Create the table in the specified schema
CREATE TABLE gpa_history
(   gpa_history_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    scale DECIMAL(4, 2) NOT NULL,
    gpa DECIMAL(4, 2) NOT NULL,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT ck_gpa_scale CHECK(gpa <= scale),
    -- Specify more columns here
    a_plus DECIMAL(4, 2) NOT NULL,
    a DECIMAL(4, 2) NOT NULL,
    a_minus DECIMAL(4, 2) NOT NULL,
    b_plus DECIMAL(4, 2) NOT NULL,
    b DECIMAL(4, 2) NOT NULL,
    b_minus DECIMAL(4, 2) NOT NULL,
    c_plus DECIMAL(4, 2) NOT NULL,
    c DECIMAL(4, 2) NOT NULL,
    c_minus DECIMAL(4, 2) NOT NULL,
    d_plus DECIMAL(4, 2) NOT NULL,
    d DECIMAL(4, 2) NOT NULL,
    d_minus DECIMAL(4, 2) NOT NULL,
    f DECIMAL(4, 2) NOT NULL
);


-- Create the table in the specified schema
CREATE TABLE feedback
(
    feedback_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    gpa DECIMAL(4, 2) NOT NULL,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    query_1 VARCHAR(50) NOT NULL,
    query_2 VARCHAR(50) NOT NULL,
    query_3 VARCHAR(50) NOT NULL,
    -- Specify more columns here

    a_plus DECIMAL(4, 2) NOT NULL,
    a DECIMAL(4, 2) NOT NULL,
    a_minus DECIMAL(4, 2) NOT NULL,
    b_plus DECIMAL(4, 2) NOT NULL,
    b DECIMAL(4, 2) NOT NULL,
    b_minus DECIMAL(4, 2) NOT NULL,
    c_plus DECIMAL(4, 2) NOT NULL,
    c DECIMAL(4, 2) NOT NULL,
    c_minus DECIMAL(4, 2) NOT NULL,
    d_plus DECIMAL(4, 2) NOT NULL,
    d DECIMAL(4, 2) NOT NULL,
    d_minus DECIMAL(4, 2) NOT NULL,
    f DECIMAL(4, 2) NOT NULL
);



