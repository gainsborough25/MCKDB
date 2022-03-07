ALTER VIEW vwKitCount AS (
							SELECT K.KeycapSetID, COUNT(K.KeycapSetID) AS [NumberOfKits]
							FROM Kit INNER JOIN KeycapSet AS K ON Kit.KeycapSetID = K.KeycapSetID
							GROUP BY K.KeycapSetID
							);


--SELECT * FROM vwKitCount




--ALTER VIEW vwKeycapSetWithKitCount AS(
--							SELECT K.KeycapSetID, K.Manufacturer, K.KeycapName, K.Material, K.PrintingMethod, K.[Profile], KC.[NumberOfKits]
--							FROM KeycapSet AS K
--							INNER JOIN vwKitCount AS KC ON KC.KeycapSetID = K.KeycapSetID
--							);

--SELECT * FROM vwKeycapSetWithKitCount


ALTER VIEW vwColorFamily AS (
								SELECT K.Manufacturer, K.KeycapName, K.KeycapSetID, C.ColorFamily, STRING_AGG(KSC.KeyTypeName, ', ') AS [ClassesMatchingColor]
								FROM KeycapSet AS K
								INNER JOIN KeycapSetColor AS KSC ON K.KeycapSetID = KSC.KeycapSetID
								INNER JOIN Color AS C ON C.ColorID = KSC.ColorID
								--WHERE C.ColorFamily = 'Blue'
								GROUP BY K.Manufacturer, K.KeycapName, C.ColorFamily, K.KeycapSetID
							);

ALTER VIEW vwColorAgg AS (
							SELECT K.KeycapSetID, K.Manufacturer, K.KeycapName, STRING_AGG(C.ColorFamily, ' / ') AS [SetColors]
							FROM KeycapSet AS K
							--INNER JOIN KeycapSetColor AS KSC ON K.KeycapSetID = KSC.KeycapSetID
  							INNER JOIN vwColorFamily AS C ON C.KeycapSetID = K.KeycapSetID
							GROUP BY K.Manufacturer, K.KeycapName, K.KeycapSetID
						  );

CREATE VIEW vwRegionInitial AS (
								SELECT k.KeycapSetID, K.KeycapName, V.VendorName, V.VendorRegion
								FROM KeycapSet AS K
								INNER JOIN KeycapSetVendor AS KV ON KV.KeycapSetID = K.KeycapSetID
								INNER JOIN Vendor AS V On V.VendorID = KV.VendorID
								);

ALTER VIEW vwRegionAgg AS (
							SELECT R.KeycapSetID, R.KeycapName, STRING_AGG(R.VendorRegion, ' / ') AS [VendorAvailabilityByRegion] 
							FROM vwRegionInitial AS R
							GROUP BY R.KeycapSetID, R.KeycapName
						   );
--------------------------------------------------------------------------------------------------------------
-- THIS VIEW TO BE USED TO SEARCH KEYCAPS BY COLOR

ALTER VIEW vwColorSearch AS (
								SELECT KC.*, CF.ColorFamily, CF.[ClassesMatchingColor]
								FROM vwKeycapSetWithKitCount AS KC
								INNER JOIN vwColorFamily AS CF ON KC.KeycapSetID = CF.KeycapSetID
							 );



---------------------------------------------------------------------------------------------------------------

--THIS VIEW TO BE USED TO SEACH KEYCAPS BY MANUFACTURER AND ALSO DISPLAY MAIN RELEVENT INFORMATION

ALTER VIEW vwMain AS (
							  SELECT CA.*, K.Material, K.[Profile], K.PrintingMethod, KC.[NumberOfKits], R.[VendorAvailabilityByRegion] 
							  FROM vwColorAgg AS CA 
							  INNER JOIN vwKitCount AS KC ON KC.KeycapSetID = CA.KeycapSetID
							  INNER JOIN vwRegionAgg AS R ON R.KeycapSetID = CA.KeycapSetID
							  INNER JOIN KeycapSet AS K ON CA.KeycapSetID = K.KeycapSetID
							);


CREATE VIEW vwSearchNameAndKits AS (
									SELECT M.KeycapSetID, M.Manufacturer, M.KeycapName, M.SetColors, K.KitID, K.KitName, K.LegendChar, K.SublegendChar, K.NumberOfKeys, K.TsanganSupport, K.ISOSupport
									FROM vwMain AS M
									INNER JOIN Kit AS K ON K.KeycapSetID = M.KeycapSetID
									);



--TRIGGERS
---------------------------------------------------------------------------------------------------------------

-- THIS TRIGGER INSERTS INFORMATION INTO THE JUNCTION TABLES KeycapSetColor and KeycapSetVendor
-- AND ALSO ADDS A BASE KIT TO THE KIT TABLE

-- THE FUNCTIONALITY OF THIS TRIGGER IS THAT IT ALLOWS THE SET TO SHOW UP IN THE AGGREGATE VIEW OF THE DATABASE

CREATE TRIGGER tr_Set_INSERT
ON KeycapSet
AFTER INSERT
AS
	DECLARE @id NVARCHAR(256)
	SELECT @id = KeycapSetID FROM inserted
	BEGIN
		INSERT INTO KeycapSetColor VALUES
		(@id, 35, '-')

		INSERT INTO KeycapSetVendor VALUES
		(25, @id)

		INSERT INTO Kit VALUES
		('needs update', @id, '-', '-', '-', 0, 0, 0)
	END;

	SELECT * FROM Kit
-- THIS TRIGGER DELETES NECESSARY INFORMATION IN THE JUNCTION TABLES KeycapSetColor and KeycapSetVendor 
-- ALONG WITH KITS PERTAINING TO THE DESIRED DELETED KIT SO THAT THE ENTRY IN KeycapSet CAN BE SUCCESSFULLY DELETED

CREATE TRIGGER tr_Set_DELETE
ON KeycapSet
INSTEAD OF DELETE
AS
	DECLARE @id NVARCHAR(256)
	SELECT @id = KeycapSetID FROM deleted
	BEGIN
		DELETE FROM KeycapSetColor
		WHERE KeycapSetID = @id

		DELETE FROM KeycapSetVendor
		WHERE KeycapSetID = @id

		DELETE FROM Kit
		WHERE KeycapSetID = @id

		DELETE FROM KeycapSet
		WHERE KeycapSetID = @id
	END;


DELETE KeycapSet
WHERE KeycapSetID = 'TEST'



INSERT INTO KeycapSet VALUES
('TEST', 'TEST', 'TEST', 'TEST', 'TEST', 'TEST')

