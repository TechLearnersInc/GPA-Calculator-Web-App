DROP DATABASE IF EXISTS gpacalculator;
CREATE DATABASE IF NOT EXISTS gpacalculator;

USE gpacalculator;

DROP TABLE IF EXISTS feedback;
DROP TABLE IF EXISTS gpa_history;

-- Create the table in the specified schema
CREATE TABLE gpa_history
(
    gpa_history_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    scale          DECIMAL(4, 2)  NOT NULL,
    gpa            DECIMAL(4, 2)  NOT NULL,
    date_time      DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT ck_gpa_scale CHECK (gpa <= scale),
    -- Specify more columns here
    grade_sheet    VARCHAR(10000) NOT NULL
);

-- Create the table in the specified schema
CREATE TABLE feedback
(
    feedback_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    feed_back   VARCHAR(10000) NOT NULL,
    date_time   DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)