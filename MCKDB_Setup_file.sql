--CREATE DATABASE MKCDB
----GO

--CREATE TABLE KeycapSet (
--	KeycapSetID NVARCHAR(256) NOT NULL PRIMARY KEY,
--	KeycapName NVARCHAR(256) NOT NULL,
--	Manufacturer NVARCHAR(256) NOT NULL,
--	Material NVARCHAR(256) NOT NULL,
--	PrintingMethod NVARCHAR(256) NOT NULL
--);

--ALTER TABLE KeycapSet
--ADD [Profile] NVARCHAR(256)

--CREATE TABLE GBDates (
--	GBDatesID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
--	KeycapSetID NVARCHAR(256) NOT NULL
--		CONSTRAINT KeycapSet_GBDates_FK FOREIGN KEY (KeycapSetID )
--		REFERENCES KeycapSet (KeycapSetID ),
--	StartDate DATE NOT NULL,
--	FulFillmentDate DATE
--);

--CREATE TABLE Vendor (
--	VendorID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
--	VendorName NVARCHAR(256) NOT NULL,
--	VendorRegion NVARCHAR(256) NOT NULL,
--	VendorWebsite NVARCHAR(256) NOT NULL
--);

--CREATE TABLE KeycapSetVendor (
--	KeycapSetVendorID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
--	VendorID INT NOT NULL
--		CONSTRAINT Vendor_KeycapSetVendor_FK FOREIGN KEY (VendorID)
--		REFERENCES Vendor (VendorID),
--	KeycapSetID NVARCHAR(256)
--		CONSTRAINT KeycapSet_KeycapSetVendor_FK FOREIGN KEY(KeycapSetID)
--		REFERENCES KeycapSet (KeycapSetID),
--);

--CREATE TABLE Kit (
--	KitID NVARCHAR(256) NOT NULL PRIMARY KEY,
--	KeycapSetID NVARCHAR(256)
--		CONSTRAINT KeycapSet_Kit_FK FOREIGN KEY(KeycapSetID)
--		REFERENCES KeycapSet (KeycapSetID),
--	KitName NVARCHAR(256) NOT NULL,
--	LegendChar NVARCHAR(256),
--	SublegendChar NVARCHAR(256),
--	NumberOfKeys INT NOT NULL,
--	TsanganSupport BIT,
--	ISOSupport BIT
--);

--CREATE TABLE Color (
--	ColorID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
--	ColorCode NVARCHAR(256),
--	ColorFamily NVARCHAR(256) NOT NULL
--);

--ALTER TABLE Color
--ADD Shade NVARCHAR(256)


--CREATE TABLE KeycapSetColor (
--	KeycapSetColorID INT NOT NULL IDENTITY(1, 1) PRIMARY KEY,
--	KeycapSetID NVARCHAR(256) NOT NULL
--		CONSTRAINT KeycapSet_KeycapSetColor_FK FOREIGN KEY(KeycapSetID)
--		REFERENCES KeycapSet (KeycapSetID),
--	ColorID INT NOT NULL
--		CONSTRAINT ColorID_FK FOREIGN KEY (ColorID)
--		REFERENCES Color (ColorID)
--);

--ALTER TABLE KeycapSetColor
--ADD KeyTypeName NVARCHAR(256) NOT NULL; --this is like 'alphas/modifiers/accents'





INSERT INTO Vendor (VendorName, VendorRegion, VendorWebsite) VALUES
--('Mykeyboard.eu', 'EU', 'https://myeyboard.eu')
--('Melgeek', 'AS', 'https://melgeek.com'),
--('KBDfans', 'AS', 'https://kbdfans.com'),
--('zFrontier', 'AS', 'https://en.zfrontier.com'),
--('Daily Clack', 'OCE', 'https://www.dailyclack.com'),
--('Deskhero', 'CA', 'https://www.deskhero.ca'),
--('iLumKB', 'SG', 'https://www.ilumkb.com'),
--('proto[Typist]', 'UK', 'https://www.prototypist.net'),
--('Cannon Keys', 'USA', 'https://www.cannonkeys.com'),
--('mekibo', 'USA', 'https://www.mekibo.com'),
--('Omnitype', 'USA', 'https://www.omnitype.com'),
--('Novelkeys_', 'USA', 'https://www.novelkeys.com'),
--('Space Cables', 'USA', 'https://www.spaceholdings.net'),
--('The KeyDot Company', 'USA', 'https://thekey.company'),
--('Kono', 'Global', 'https://www.kono.store'),
--('CandyKeys', 'EU', 'https://www.candykeys.com'),
--('Swag Keys', 'KR', 'https://swagkeys.com'),
--('Fancy Customs', 'SA', 'https://fancycustoms.com')
--('ProjectKeyboard', 'USA', 'https://store.projectkeyboard.com')
--('SwitchKeys', 'OCE', 'https://switchkeys.com.au')
--('Keyspresso', 'CA', 'https://keyspresso.ca'),
--('Base Keys', 'JPN', 'https://basekeys.jp')
--('Originative Co.', 'USA', 'https://originativeco.com')
--('Vala Supply', 'USA', 'https://vala.supply')


INSERT INTO Color (ColorHex, ColorFamily, Shade) VALUES
--('#282a36', 'Grey'),
--('#44475a', 'Grey'),
--('#f8f8f2', 'White')
--('#7a99ac', 'Blue', 'Dark'),
--('#99d6da', 'Blue', 'Light'),
--('#dde5ed', 'Grey', 'Light'),
--('#006a93', 'Blue', 'Balanced'),
--('#f7f2ea', 'White', NULL)
--('#5f6680', 'Blue', 'Dark'),
--('#848ca1', 'Blue', 'Grey'),
--('#dbdbdb', 'Grey', 'Light')
--('#98c9cd', 'Blue', 'Light'),
--('#96c69f', 'Green', 'Light'),
--('#7c5a51', 'Brown', 'Balanced'),
--('#d3cec8', 'White', NULL)
--('#af642b', 'Brown', 'Light'),
--('#f0e1cd', 'White', NULL),
--('#ac2c32', 'Red', 'Balanced')
--('#c22a1d', 'Red', 'Balanced'),
--('#627474', 'Grey', 'Balanced'),
--('#f8f5f6', 'White', NULL)
--('#b8acd6', 'Purple', 'Light'),
--('#f8bed6', 'Pink', 'Light'),
--('#c10016', 'Red', 'Medium Dark'),
--('#f0ebd7', 'Beige', 'Light')
--('#d0c7bb', 'Beige', 'Dark'),
--('#412b27', 'Brown', 'Dark'),
--('#c2a787', 'Brown', 'Light')
--('#393b3b', 'Black', 'Light'),
--('#727474', 'Grey', 'Dark'),
--('#dfd7cc', 'Beige', 'Light'),
--('#4e6c54', 'Green', 'Dark'),
--('#6a3336', 'Red', 'Dark')

SELECT * FROM Color

INSERT INTO KeycapSet (KeycapSetID, KeycapName, Manufacturer, Material, PrintingMethod, [Profile]) VALUES
--('GDRC1AH', 'Dracula', 'GMK', 'ABS', 'Double shot molding')
--('GSKO1AH', 'Shoko', 'GMK', 'ABS', 'Double shot molding')
--('GMSP1AH', 'Masterpiece', 'GMK', 'ABS', 'Double shot molding')
--('MFSH1AH', 'Fishing', 'not public', 'ABS', 'Double shot molding', 'MG')
--('IILR1PS', 'Islander', 'Infinikey', 'PBT', 'Dye submlimation', 'cherry')
--('GHRT1AH', 'Harvest', 'GMK', 'ABS', 'Double shot molding', 'Cherry')
--('GHNW1AH', 'Honeywell', 'GMK', 'ABS', 'Double shot molding', 'Cherry')
--('TSTY1PS', 'Story', 'Tomatocaps', 'PBT', 'Dye submlimation', 'Cherry')
--('ICFE1PS', 'Cafe', 'Infinikey', 'PBT', 'Dye sublimation', 'Cherry')
--('GDST1AH', 'Dualshot', 'GMK', 'ABS', 'Double shot molding', 'Cherry')
--('SDST1AH', 'Dualshot', 'Signature Plastics', 'ABS', 'Double shot molding', 'SA'),
--('GCMP1AH', 'Camping', 'GMK', 'ABS', 'Double shot molding', 'Cherry'),
--('GCMP2AH', 'Camping R2 (Camping in Japan)', 'GMK', 'ABS', 'Double shot molding', 'Cherry')



INSERT INTO KeycapSetColor (KeycapSetID, ColorID, KeyTypeName) VALUES
--('GDRC1AH', 1, 'Modifier'),  
--('GDRC1AH', 2, 'Alpha'),
--('GDRC1AH', 3, 'Legend')
--('GSKO1AH', 4, 'Modifier'),
--('GSKO1AH', 5, 'Accent'),
--('GSKO1AH', 5, 'Legend'),
--('GSKO1AH', 6, 'Alpha'),
--('GMSP1AH', 7, 'Alpha'),
--('GMSP1AH', 7, 'Modifier'),
--('GMSP1AH', 8, 'Legend')
--('MFSH1AH', 9, 'Alpha'),
--('MFSH1AH', 10, 'Modifier'),
--('MFSH1AH', 11, 'Accent'),
--('MFSH1AH', 11, 'Legend')
--('IILR1PS', 12, 'Modifier'),
--('IILR1PS', 13, 'Modifier'),
--('IILR1PS', 14, 'Accent'),
--('IILR1PS', 14, 'Legend'),
--('IILR1PS', 15, 'Alpha')
--('GHRT1AH', 16, 'Modifiers'),
--('GHRT1AH', 17, 'Alpha'),
--('GHRT1AH', 18, 'Accent'),
--('GHRT1AH', 18, 'Legend')
--('GHNW1AH', 19, 'Accent'),
--('GHNW1AH', 20, 'Modifier'),
--('GHNW1AH', 20, 'Legend'),
--('GHNW1AH', 21, 'Alpha')
--('TSTY1PS', 22, 'Modifier'),
--('TSTY1PS', 23, 'Alpha'),
--('TSTY1PS', 24, 'Accent'),
--('TSTY1PS', 24, 'Legend'),
--('TSTY1PS', 25, 'Alternate Alpha')
--('ICFE1PS', 26, 'Alpha'),
--('ICFE1PS', 27, 'Modifier'),
--('ICFE1PS', 27, 'Legend'),
--('ICFE1PS', 28, 'Accent')
--('GCMP1AH', 33, 'Accent'),
--('GCMP1AH', 32, 'Modifier'),
--('GCMP1AH', 32, 'Legend'),
--('GCMP1AH', 31, 'Alpha'),
--('GCMP2AH', 33, 'Accent'),
--('GCMP2AH', 32, 'Modifier'),
--('GCMP2AH', 32, 'Legend'),
--('GCMP2AH', 31, 'Alpha'),
--('GDST1AH', 30, 'Modifier'),
--('GDST1AH', 30, 'Alpha'),
--('GDST1AH', 29, 'Accent'),
--('SDST1AH', 30, 'Modifier'),
--('SDST1AH', 30, 'Alpha'),
--('SDST1AH', 29, 'Accent')


INSERT INTO Kit (KitID, KeycapSetID, KitName, LegendChar, SublegendChar, NumberOfKeys, TsanganSupport, ISOSupport) VALUES
--('DRC-K1', 'GDRC1AH', 'Core module (base)', 'Latin', NULL, 154, 1, 1),
--('DRC-K2', 'GDRC1AH', 'Highlight module', 'Latin', NULL, 21, 0, 1),
--('DRC-K3', 'GDRC1AH', 'Nightmode module', 'Latin', NULL, 43, 1, 1),
--('DRC-K4', 'GDRC1AH', 'Whitespace module(spacebars)', NULL, NULL, 8, 1, 1),
--('DRC-K5', 'GDRC1AH', 'Minify module', 'Latin', NULL, 30, 0, 0),
--('DRC-K6', 'GDRC1AH', 'Localization  module', 'Nordic', NULL, 56, 1, 0),
--('DRC-K7', 'GDRC1AH', 'Command module', 'Latin', NULL, 15, 1, 0),
--('DRC-K8', 'GDRC1AH', 'ERR! module', 'Latin', NULL, 32, 1, 0)
--('SKO-K1', 'GSKO1AH', 'Base', 'Latin', NULL, 167, 1, 1),
--('SKO-K2', 'GSKO1AH', 'Add-on', NULL, NULL, 18, 1, 1),
--('SKO-K3', 'GSKO1AH', 'Spacebar', NULL, NULL, 12, 0, 0)
--('MSP-K1', 'GMSP1AH', 'Value (base)', 'Katakana', NULL, 152, 1, 1),
--('MSP-K2', 'GMSP1AH', 'Clarity', NULL, NULL, 31, 1, 1),
--('MSP-K3', 'GMSP1AH', 'Preserving (spacebars)', NULL, NULL, 16, 0, 0),
--('MSP-K4', 'GMSP1AH', 'West', 'Latin', NULL, 52, 0, 0),
--('FSH-K1', 'MFSH1AH', 'Base', 'Latin', NULL, 140, 1, 0),
--('FSH-K2', 'MFSH1AH', 'Novelties', NULL, NULL, 13, 0, 0),
--('FSH-K3', 'MFSH1AH', 'Alternate (spacebars)', NULL, NULL, 7, 0, 0)
--('ILR-K1', 'IILR1PS', 'Base', 'Latin', NULL, 160, 1, 1),
--('ILR-K2', 'IILR1PS', 'Novelties', NULL, NULL, 47, 0, 0),
--('ILR-K3', 'IILR1PS', 'Expansion', NULL, NULL, 73, 0, 0)
--('HRT-K1', 'GHRT1AH', 'Inari (base)', 'Latin', 'Hiragana', 157, 1, 1),
--('HRT-K3', 'GHRT1AH', 'Wheat Fields (spacebars)', NULL, NULL, 11, 0, 0),
--('HRT-K2', 'GHRT1AH', 'Traveling Merchant', NULL, NULL, 18, 1, 1)
--('HNW-K1', 'GHNW1AH', 'Base', 'Latin', NULL, 155, 1, 1)
--('STY-K1', 'TSTY1PS', 'Hydrangea (base)', 'Latin', 'Hiragana', 174, 1, 1),
--('STY-K2', 'TSTY1PS', 'Namishiro', 'Latin', 'Hiragana', 108, 0, 0),
--('STY-K3', 'TSTY1PS', 'Uniform', 'Kanji', NULL, 63, 1, 1),
--('STY-K4', 'TSTY1PS', 'Ayakoto', 'Kanji', NULL, 55, 1, 0),
--('STY-K5', 'TSTY1PS', 'Koma (spacebars)', NULL, NULL, 14, 0, 0)
--('IFE-K1', 'ICFE1PS', 'Core (base)', 'Latin', NULL, 163, 1, 1),
--('IFE-K2', 'ICFE1PS', 'Add-on', 'Latin', NULL, 73, 1, 0),
--('IFE-K3', 'ICFE1PS', 'Aribica', 'Latin', 'Arabic', 51, 0, 0)
--('CP1-K1', 'GCMP1AH', 'Base', 'Latin', NULL, 168, 1, 1),
--('CP1-K2', 'GCMP1AH', 'Spacebars', NULL, NULL, 12, 0, 0),
--('CP2-K1', 'GCMP2AH', 'Base', 'Latin', 'Hiragana', 145, 1, 1),
--('CP2-K2', 'GCMP2AH', 'Latin', 'Latin', NULL, 56, 0, 0),
--('CP2-K3', 'GCMP2AH', 'Novelties', NULL, NULL, 27, 0, 0),
--('CP2-K4', 'GCMP2AH', 'Communities', NULL, NULL, 9, 0, 0),
--('CP2-K5', 'GCMP2AH', 'Spacebars', NULL, NULL, 14, 0, 0),
--('GDS-K1', 'GDST1AH', 'Standard (base)', 'Latin', NULL, 146, 1, 1),
--('GDS-K2', 'GDST1AH', 'Bars (spacebars)', NULL, NULL, 14, 0, 0),
--('GDS-K3', 'GDST1AH', 'Novelty', 'Latin', NULL, 16, 0, 0)
--('SDS-K1', 'GCMP1AH', 'Standard (base)', 'Latin', NULL, 113, 1, 1),
--('SDS-K2', 'GCMP1AH', 'Bars (spacebars)', NULL, NULL, 6, 0, 0),
--('SDS-K3', 'GCMP1AH', 'Novelty', 'Latin', NULL, 16, 0, 0),
--('SDS-K4', 'GCMP1AH', 'Accent', NULL, NULL, 20, 0, 0),
--('SDS-K5', 'GCMP1AH', 'Numbers', 'Latin', NULL, 24, 0, 0)

SELECT * FROM KeycapSet

INSERT INTO GBDates (KeycapSetID, StartDate, FulFillmentDate) VALUES
--('GDRC1AH', '2019-10-04', '2021-10-04')
--('GSKO1AH', '2018-11-04', '2019-07-04')
--('GMSP1AH', '2020-05-01', NULL)
--('MFSH1AH', '2021-04-01', '2021-12-01')
--('IILR1PS', '2020-05-15', '2020-11-11')
--('GHRT1AH', '2021-08-01', NULL)
--('GHNW1AH', '2017-01-13', '2017-04-21')
--('TSTY1PS', '2021-08-14', NULL)
--('ICFE1PS', '2020-12-01', '2020-12-01')
--('GDST1AH', '2019-12-04', '2020-08-20'),
--('SDST1AH', '2020-10-01', '2021-08-23'),
--('GCMP1AH', '2018-01-07', '2028-09-04'),
--('GCMP2AH', '2019-10-01', '2020-06-20')

INSERT INTO KeycapSetVendor (VendorID, KeycapSetID) VALUES
--(10, 'GDRC1AH'),
--(6, 'GDRC1AH'),
--(18, 'GDRC1AH'),
--(4, 'GDRC1AH')
--(3, 'GSKO1AH'),
--(18, 'GSKO1AH'),
--(14, 'GSKO1AH'),
--(4, 'GSKO1AH')
--(5, 'GMSP1AH'),
--(19, 'GMSP1AH'),
--(18, 'GMSP1AH'),
--(6, 'GMSP1AH'),
--(20, 'GMSP1AH')
--(14, 'MFSH1AH'),
--(15, 'MFSH1AH'),
--(1, 'MFSH1AH')
--(13, 'IILR1PS'),
--(7, 'IILR1PS'),
--(3, 'IILR1PS'),
--(20, 'IILR1PS'),
--(5, 'IILR1PS'),
--(9, 'GHRT1AH'),
--(18, 'GHRT1AH'),
--(3, 'GHRT1AH'),
--(6, 'GHRT1AH'),
--(4, 'GHRT1AH'),
--(21, 'GHRT1AH'),
--(22, 'GHRT1AH')
--(23, 'GHNW1AH')
--(24, 'TSTY1PS'),
--(5, 'TSTY1PS'),
--(7, 'TSTY1PS'),
--(18, 'TSTY1PS'),
--(3, 'TSTY1PS'),
--(22, 'TSTY1PS'),
--(4, 'TSTY1PS')
--(20, 'ICFE1PS'),
--(13, 'ICFE1PS')
--(14, 'GCMP1AH'),
--(18, 'GCMP1AH'),
--(3, 'GCMP1AH'),
--(11, 'GCMP2AH'),
--(18, 'GCMP2AH'),
--(3, 'GCMP2AH'),
--(4, 'GCMP2AH'),
--(10, 'GDST1AH'),
--(18, 'SDST1AH'),
--(4, 'SDST1AH'),
--(6, 'SDST1AH'),
--(10, 'SDST1AH')


--('GDST1AH', '2019-12-04', '2020-08-20'),
--('SDST1AH', '2020-10-01', '2021-08-23'),

SELECT KeycapName, Manufacturer, Material, PrintingMethod, Profile FROM KeycapSet;

SELECT * FROM Color

SELECT * FROM KeycapSet

SELECT * FROM Kit

SELECT * FROM KeycapSetColor

SELECT * FROM Vendor

SELECT * FROM GBDates

SELECT * FROM KeycapSetVendor