package db

type DbBase struct {
	ConnectionString string
}

func getConfig() DbBase {
	dbBase := DbBase{}
	dbBase.ConnectionString = "user=postgres password=C0laC0la dbname=DiscountChecker sslmode=disable"
	return dbBase
}
