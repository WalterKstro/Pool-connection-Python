CREATE TABLE `usernames` (
	`Username_ID` INT UNSIGNED NOT NULL,
	`Username_Name` VARCHAR(50) NOT NULL DEFAULT '',
	`Username_Nick` VARCHAR(50) NOT NULL DEFAULT '',
	`Username_Pass` VARCHAR(30) NOT NULL DEFAULT '',
	PRIMARY KEY (`Username_ID`)
)
COLLATE='utf8mb4_general_ci'
;
