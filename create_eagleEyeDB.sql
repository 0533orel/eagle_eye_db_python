
CREATE DATABASE IF NOT EXISTS eagleEyeDB;
USE eagleEyeDB;

CREATE TABLE IF NOT EXISTS agents (
   id INT PRIMARY KEY AUTO_INCREMENT,
    code_name VARCHAR(20) UNIQUE NOT NULL,
    real_name VARCHAR(30) NOT NULL,
    location VARCHAR(50),
    status ENUM
        (
            "active",
            "injured",
            "missing",
            "retired"
        ) DEFAULT "active",
        missions_completed INT DEFAULT 0
);
