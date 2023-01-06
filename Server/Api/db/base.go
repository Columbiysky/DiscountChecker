package db

type DbBase struct {
	ConnectionString string
}

func getConfig() DbBase {
	dbBase := DbBase{}
	dbBase.ConnectionString = "user=postgres password=postgrespw dbname=DiscountChecker sslmode=disable"
	return dbBase
}
