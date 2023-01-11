package db

import (
	"database/sql"
	"fmt"
	"time"
)

type User struct {
	Id              int
	Username        string
	UserSettingsId  int
	Password        string
	Token           string
	TokenExpiration time.Time
}

func getUserByLoginPass(username string, password string) User {
	var dbConfig = getConfig()
	db, err := sql.Open("postgres", dbConfig.ConnectionString)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	row, err := db.Query("select * from Users where UserName=$1 and Password=$2", username, password)
	return getUserInstanceFromRow(row)
}

func getUserById(id int) User {
	var dbConfig = getConfig()
	db, err := sql.Open("postgres", dbConfig.ConnectionString)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	row, err := db.Query("select * from Users where Id=$1", id)
	return getUserInstanceFromRow(row)
}

func registerNewUser(newUser User) {
	var dbConfig = getConfig()
	db, err := sql.Open("postgres", dbConfig.ConnectionString)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	result, err := db.Exec("insert into Users (UserName, Password, UserSettingsId) values ($1, $2, $3)",
		newUser.Username, newUser.Password, -1)
	if err != nil {
		panic(err)
	}
	fmt.Println(result.LastInsertId()) // не поддерживается
	fmt.Println(result.RowsAffected()) // количество добавленных строк
}

//update example
// result, err := db.Exec("update Products set price = $1 where id = $2", 69000, 1)
//     if err != nil{
//         panic(err)
//     }

// returns True if token expired
func checkTokenExpirationById(id int) bool {
	var dbConfig = getConfig()
	db, err := sql.Open("postgres", dbConfig.ConnectionString)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	row, err := db.Query("select TokenExpiration from Users where Id=$1", id)
	resultTime := time.Now()
	row.Scan(&resultTime)
	today := time.Now()
	difference := today.Sub(resultTime)

	if difference.Hours()*24 >= 7 {
		return true
	}
	return false

}

func getUserInstanceFromRow(row *sql.Rows) User {
	user := User{}
	err := row.Scan(&user.Id, &user.Username, &user.Token, &user.TokenExpiration)
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(user.Id, user.Username, user.Token, user.TokenExpiration)
	return user
}
