# import to connect to DB
import mysql.connector
from mysql.connector import Error

# create the connection to the DB as shown in class
def create_connection(hostname, uid, pwd, dbname):
    conn = None
    try:
        conn = mysql.connector.connect(
            host = hostname,
            user = uid,
            password = pwd,
            database = dbname
        )
    except Error as e:
        print("Error is ", e)
    return conn

# create cursor to get DB info as shown in class
myconn = create_connection('db3368.c1o8w68m4pjb.us-east-1.rds.amazonaws.com','admin','1963711!', 'db3368')
mycursor = myconn.cursor(dictionary=True)

# function to add a game into DB
def add_game(mycursor):
    # get user to input info about the game
    gamename = input("Enter game name: ")
    maxplayeres = int(input("Enter maximum number of players: "))
    result = input("Enter result: ")
    gameduration = input("Enter game duration: ")
    maxscore = int(input("Enter max score: "))

    # insert the info into the DB
    mycursor.execute("insert into boardgame (gamename, maxplayers, result, gameduration, maxscore) values (%s, %s, %s, %s, %s)",
                     (gamename, maxplayeres, result, gameduration, maxscore))
    myconn.commit()
    # confirm to user that game was added
    print("Game added")

# function to output all games
def output_all_games(mycursor):
    # use cursor as given in class
    mycursor.execute("select * from boardgame")
    bgamelst = mycursor.fetchall()
    # print list as given in class
    for games in bgamelst:
        print(games)

# main function and menu to be displayed
def main():
    # menu given in question
    while True:
        menu = print("MENU \n a-Add game \n o-Output all games in console \n q-Quit")
        user_choice = input().lower()

        # if else statement to execute user choice
        if user_choice == "a":
            add_game(mycursor)
        elif user_choice == "o":
            output_all_games(mycursor)
        elif user_choice == "q":
            break
        else:
            print("Not a valid selection")

# to run code
if __name__ == "__main__":
    main()

