#!/bin/bash

./bin/ycsb load mongodb -P workloads/workloada -p mongodb.url=mongodb://localhost:27017 -p mongodb.database=stockdb
./bin/ycsb run mongodb -P workloads/workloada -p mongodb.url=mongodb://localhost:27017 -p mongodb.database=stockdb -s -t

./bin/ycsb load jdbc -P workloads/workloada -p db.url=jdbc:mysql://localhost:3306/stockdb -p db.username=root -p db.password=12345
./bin/ycsb run jdbc -P workloads/workloada -p db.url=jdbc:mysql://localhost:3306/stockdb -p db.username=root -p db.password=12345 -p db.driver=com.mysql.cj.jdbc.Driver -s -t
