CREATE DATABASE IF NOT EXISTS  sample_db CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
CREATE DATABASE IF NOT EXISTS  test_db CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

CREATE USER IF NOT EXISTS 'mysqluser'@'%' IDENTIFIED WITH mysql_native_password BY 'mysqlpass';
CREATE USER IF NOT EXISTS 'testuser'@'%' IDENTIFIED WITH mysql_native_password BY 'testpass';

GRANT ALL PRIVILEGES ON sample_db.*  TO 'mysqluser'@'%';
GRANT ALL PRIVILEGES ON test_db.* TO 'testuser'@'%';
FLUSH PRIVILEGES;