from re import I
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

# cred = credentials.Certificate("path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
def initialize_firestore():


    # Setup Google Cloud Key - The json file is obtained by going to
    # Project Settings, Service Accounts, Create Service Account, and then
    # Generate New Private Key
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "organizerthing-firebase-adminsdk-9le6c-2ff8841fd7.json"
    # Use the application default credentials. The projectID is obtianed
    # by going to Project Settings and then General.
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
    'projectId': 'organizerthing',
    })
    # Get reference to database
    db = firestore.client()
    return db


def add_show(db):

    nameOfShow = input("Please enter the name of the show: ")
    episodeCount = input("How many episodes have you watched?: ")
    showFinished = input("Have you finished the show (y/n)?: ")
    showScore = input("What would you rate the show on a scale from 1-10?: ")

    addedShowCheck = db.collection("shows").document(nameOfShow).get()
    data = addedShowCheck.to_dict()
    print(data)

    showData = {  "nameOfShow": nameOfShow,
            "episodeCount": episodeCount,
            "showFinished": showFinished,
            "showScore": showScore

    }
    db.collection("shows").document(nameOfShow).set(showData)

def checkShowList(db):
    print("Select Query")
    print("1.) List one show")
    print("2.) List all shows")
    print("3.) List all finished shows")
    print("4.) List all unfinished shows")
    selection = input("> ")
    print()

    if selection == "1":
        selections = db.collection("shows")
        showSelect = selections.to_dict()
        print(showSelect)
    
    elif selection == "2":
        results = db.collection("shows").get()
        for result in results:
            show_result = result.to_dict()
            print(show_result)

    # elif selection == "3"

def main():
    db = initialize_firestore()
    print(db)
    choice = None
    while choice != "0":
        print()
        print("0) Exit")
        print("1) Add New Game")
        print("2) Check Game Info")
        print("3) Delete a game from the database")
        print("4) Edit Game Information (Hours Played, Score)")
        choice = input(f"> ")
        print()
        if choice == "0":
            print("Thank you for using the program! Game on!")
        if choice == "1":
            add_show(db)
        # elif choice == "2":
        #     checkGameList(db)
        # elif choice == "3":
        #     deleteGame(db)
        # elif choice == "4":
        #     editGame(db)                        

if __name__ == "__main__":
    main()