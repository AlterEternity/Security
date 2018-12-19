IF NOT EXISTS (SELECT * FROM Users) {
    CREATE TABLE Users (
        ID int IDENTITY(1,1)
        ,LoginName varchar(255)
        ,FirstName varchar(255)
        ,LastName varchar(255)
        ,Email varchar(255)
        ,PRIMARY KEY (ID)
    );
}
