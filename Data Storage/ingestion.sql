-- 1. Create the database if it doesn’t already exist
CREATE DATABASE IF NOT EXISTS stockdb
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;
  
-- Switch to the new database
USE stockdb;

-- 2. Create the stock_prices table
CREATE TABLE IF NOT EXISTS stock_prices (
  id      INT            NOT NULL AUTO_INCREMENT,
  ticker  VARCHAR(10)    NOT NULL,
  date    DATE           NOT NULL,
  open    DECIMAL(12,4)  NULL,
  high    DECIMAL(12,4)  NULL,
  low     DECIMAL(12,4)  NULL,
  close   DECIMAL(12,4)  NULL,
  volume  BIGINT         NULL,
  PRIMARY KEY (id),
  INDEX idx_ticker_date (ticker, date)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;
