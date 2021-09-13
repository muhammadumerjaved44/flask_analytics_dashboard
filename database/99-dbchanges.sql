USE `gigdev`;

 -- DB Changes for Q119-T210 START
USE `gigdev`;

DELIMITER $$

DROP PROCEDURE IF EXISTS addFieldIfNotExists
$$

DROP FUNCTION IF EXISTS isFieldExisting
$$

CREATE FUNCTION isFieldExisting (table_name_IN VARCHAR(100), field_name_IN VARCHAR(100))
RETURNS INT
RETURN (
    SELECT COUNT(COLUMN_NAME)
    FROM INFORMATION_SCHEMA.columns
    WHERE TABLE_SCHEMA = DATABASE()
    AND TABLE_NAME = table_name_IN
    AND COLUMN_NAME = field_name_IN
)
$$

CREATE PROCEDURE addFieldIfNotExists (
    IN table_name_IN VARCHAR(100),
    IN field_name_IN VARCHAR(100),
    IN field_definition_IN VARCHAR(100)
)
BEGIN

    SET @isFieldThere = isFieldExisting(table_name_IN, field_name_IN);
    IF (@isFieldThere = 0) THEN

        SET @ddl = CONCAT('ALTER TABLE ', table_name_IN);
        SET @ddl = CONCAT(@ddl, ' ', 'ADD COLUMN') ;
        SET @ddl = CONCAT(@ddl, ' ', field_name_IN);
        SET @ddl = CONCAT(@ddl, ' ', field_definition_IN);

        PREPARE stmt FROM @ddl;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

    END IF;

END;
$$

DELIMITER ;

 -- DB Changes for Q119-T210 END


 -- DB changes for Q418-T86 START
 -- Updated to use the changes from Q119-T210

-- ALTER TABLE `g1g_change_customer_email` ADD `status` TINYINT(1) NOT NULL DEFAULT '0' AFTER `request_type`;
CALL addFieldIfNotExists ('g1g_change_customer_email', 'status', 'TINYINT(1) NOT NULL DEFAULT 0 AFTER request_type');

CREATE TABLE IF NOT EXISTS `g1g_salePolicyExtensions`
(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hash` varchar(50) NOT NULL,
  `data` text NOT NULL,
  `oldTripEndDate` int(10) NOT NULL,
  `newTripEndDate` int(10) NOT NULL,
  `oldPrice` float NOT NULL,
  `newPrice` float NOT NULL,
  `policyNumber` varchar(255) NOT NULL,
  `purchaserEmail` varchar(255) NOT NULL,
  PRIMARY KEY (id)
)
  ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS `g1g_policyRenewDetails`
 (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hash` varchar(50) NOT NULL,
  `policyNumber` varchar(255) NOT NULL,
  `userEmail` varchar(100) NOT NULL,
  `userName` varchar(100) NOT NULL,
  `user` varchar(100) NOT NULL,
  `isDel` tinyint(1) NOT NULL DEFAULT 0,
  `timestamp` int(11) NOT NULL,
  `extendDate` int(11) NOT NULL,
  `status` int(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- DB changes for Q418-T86 END

-- DB changes for Q418-T98 Start

USE `gigdev`;

CREATE TABLE IF NOT EXISTS `g1g_partialPolicyTravelersInfo`
(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hash` varchar(50) NOT NULL,
  `data` text NOT NULL,
  `policyData` text NOT NULL,
  `actualCost` float NOT NULL,
  `refundCost` float NOT NULL,
  `partialPolicyNos` text NOT NULL,
  `policyTerminationDate` int(10) NOT NULL,
  PRIMARY KEY (id)
  ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- DB changes for Q418-T98 END

-- DB Changes for Q119-T284 Start

USE `gigdev`;

CREATE TABLE IF NOT EXISTS `googleAnalyticsCodes`
(
  `codeID`    int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `pagePath`  varchar(255)     NOT NULL,
  `gaCode`    text             NOT NULL,
  `user`      varchar(255)     NOT NULL,
  `timestamp` int(10) UNSIGNED NOT NULL,
  `isDel`     tinyint(1)       NOT NULL DEFAULT 0,
  PRIMARY KEY (codeID),
  INDEX (pagePath)
) ENGINE = InnoDB
  DEFAULT CHARSET = latin1;

-- DB Changes for Q119-T284 END


-- DB Changes for G-I47 Start

USE `gigdev`;

ALTER TABLE `g1g_products_trip_protection_info` CHANGE `recordID` `recordID` INT(11) NOT NULL AUTO_INCREMENT;

-- DB Changes for G-I47 END

-- DB Changes for G-I62 Start

-- ALTER TABLE `g1g_products_trip_protection_info` ADD `displayName` VARCHAR(255) NOT NULL AFTER `plan_name`;

USE `gigdev`;

CALL addFieldIfNotExists ('g1g_products_trip_protection_info', 'displayName', 'VARCHAR(255) NOT NULL DEFAULT 0 AFTER plan_name');

-- DB Changes for G-I62 End

-- DB Changes for GP-T77 Start

use geodb;
-- ----------------------------
-- Table structure for countries
-- ----------------------------
CREATE TABLE IF NOT EXISTS `countries`
(
    `countryID`            int(10) UNSIGNED                                              NOT NULL AUTO_INCREMENT,
    `country`              varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    `abbr`                 char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci      NOT NULL,
    `abbr3`                char(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci      NOT NULL,
    `country_numeric_code` int(5) UNSIGNED                                               NOT NULL,
    `capital`              varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    `country_demonym`      varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    `total_area`           int(11) UNSIGNED                                              NOT NULL,
    `population`           int(11) UNSIGNED                                              NULL     DEFAULT NULL,
    `idd_code`             int(5) UNSIGNED                                               NOT NULL,
    `currency_code`        char(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci      NULL     DEFAULT NULL,
    `currency_name`        varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL     DEFAULT NULL,
    `lang_code`            char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci      NOT NULL,
    `lang_name`            varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    `cctld`                char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci      NOT NULL,
    `eu`                   tinyint(1)                                                    NOT NULL DEFAULT 0,
    `eea`                  tinyint(1)                                                    NOT NULL DEFAULT 0,
    `schengen`             tinyint(1)                                                    NOT NULL DEFAULT 0,
    `efta`                 tinyint(1)                                                    NOT NULL DEFAULT 0,
    `user`                 varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    `timestamp`            int(10)                                                       NOT NULL,
    PRIMARY KEY (`countryID`) USING BTREE,
    INDEX `countryID` (`countryID`) USING BTREE,
    INDEX `countryName` (`country`) USING BTREE,
    INDEX `abbr` (`abbr`) USING BTREE,
    INDEX `abbr3` (`abbr3`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

use gigdev;

CALL addFieldIfNotExists ('g1g_products_info', 'usProviderNetworkNameNonEU', 'VARCHAR(255) NOT NULL DEFAULT 0 AFTER usProviderNetworkLogoPath');
CALL addFieldIfNotExists ('g1g_products_info', 'usProviderNetworkLinkNonEU', 'VARCHAR(255) NOT NULL DEFAULT 0 AFTER usProviderNetworkNameNonEU');
CALL addFieldIfNotExists ('g1g_products_info', 'usProviderNetworkLogoPathNonEU', 'VARCHAR(255) NOT NULL DEFAULT 0 AFTER usProviderNetworkLinkNonEU');

-- DB Changes for GP-T77 End
