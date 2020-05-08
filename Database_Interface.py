from tkinter import *
import os
import sqlite3
from PIL import ImageTk, Image
import pandas as pd
from datetime import date

# KNOW BUGS:
#-> Query and delete have problem when closed and reopened
#-> If multiple windows of the same page are opened at same time, the program breaks

def register():
	global register_screen
	register_screen = Toplevel(main_screen)
	register_screen.title("Register")
	register_screen.geometry("300x250")

	global username
	global password
	global username_entry
	global password_entry
	username = StringVar()
	password = StringVar()

	Label(register_screen, text="Please enter details below", bg="blue").pack()
	Label(register_screen, text="").pack()
	username_lable = Label(register_screen, text="Username * ")
	username_lable.pack()
	username_entry = Entry(register_screen, textvariable=username)
	username_entry.pack()
	password_lable = Label(register_screen, text="Password * ")
	password_lable.pack()
	password_entry = Entry(register_screen, textvariable=password, show='*')
	password_entry.pack()
	Label(register_screen, text="").pack()
	Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()
	Label(register_screen, text="").pack()
	Button(register_screen, text="Exit", bg="red", command = lambda : delete_register_screen()).pack()

def login():
	global login_screen
	login_screen = Toplevel(main_screen)
	login_screen.title("Login")
	login_screen.geometry("300x250")
	Label(login_screen, text="Please enter details below to login").pack()
	Label(login_screen, text="").pack()

	global username_verify
	global password_verify

	username_verify = StringVar()
	password_verify = StringVar()

	global username_login_entry
	global password_login_entry

	Label(login_screen, text="Username * ").pack()
	username_login_entry = Entry(login_screen, textvariable=username_verify)
	username_login_entry.pack()
	Label(login_screen, text="").pack()
	Label(login_screen, text="Password * ").pack()
	password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
	password_login_entry.pack()
	Label(login_screen, text="").pack()
	Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
	Label(login_screen, text=" ").pack()
	Button(login_screen, text="Exit", bg="red", command = lambda : delete_login()).pack()

def register_user():
	username_info = username.get()
	password_info = password.get()

	file = open('Login_Info.txt', "a")
	file.write("\n" + username_info + "," + password_info)
	file.close()

	username_entry.delete(0, END)
	password_entry.delete(0, END)

	Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def login_verify():
	username1 = username_verify.get()
	password1 = password_verify.get()
	username_login_entry.delete(0, END)
	password_login_entry.delete(0, END)

	found = False
	data = pd.read_csv('Login_Info.txt', header=None, delimiter=",")
	for i in range(0, data.shape[0]):
		if(data[0][i] == username1):
			if(data[1][i] == password1):
				login_sucess()
				found = True
			elif(data[1][i] != password1):
				password_not_recognised()
				found = True
	if(found == False):
		user_not_found()

def login_sucess():
	global login_success_screen
	login_success_screen = Toplevel(login_screen)
	login_success_screen.title("Success")
	login_success_screen.geometry("100x100")
	Label(login_success_screen, text="").pack()
	Label(login_success_screen, text="Login Success").pack()
	Button(login_success_screen, text="OK", command=delete_login_success).pack()

def password_not_recognised():
	global password_not_recog_screen
	password_not_recog_screen = Toplevel(login_screen)
	password_not_recog_screen.title("Success")
	password_not_recog_screen.geometry("150x100")
	Label(password_not_recog_screen, text="Invalid Password ").pack()
	Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found():
	global user_not_found_screen
	user_not_found_screen = Toplevel(login_screen)
	user_not_found_screen.title("Success")
	user_not_found_screen.geometry("150x100")
	Label(user_not_found_screen, text="User Not Found").pack()
	Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login_success():
	login_success_screen.destroy()
	open_database()

def delete_login():
	login_screen.destroy()

def insertSighting(flower, person, location, sighting):
	connection = sqlite3.connect('flowers2019.db')
	c = connection.cursor()

	c.execute("INSERT INTO SIGHTINGS VALUES (:name,:person,:location,:date)",
			  {'name': str(flower), 'person': str(person),'location': str(location), 'date': str(sighting)})
	connection.commit()
	connection.close()
	insert_e1.delete(0, END)
	insert_e2.delete(0, END)
	insert_e3.delete(0, END)
	insert_e4.delete(0, END)
	global successfulInsert
	successfulInsert = Toplevel(insertPage)
	successfulInsert.title("")
	successfulInsert.geometry("100x100")
	Label(successfulInsert, text="").pack()
	Label(successfulInsert, text="Successful Insert").pack()
	Button(successfulInsert, text="Okay", command=successfulInsert.destroy).pack()

def Update(condition,genus, species,comname):
	connection = sqlite3.connect('flowers2019.db')
	c = connection.cursor()
	c.execute("UPDATE FLOWERS SET GENUS = :genus, SPECIES = :species, COMNAME = :comname WHERE COMNAME = :condition",
			  {'genus':genus, 'species':species, 'comname':comname, 'condition': condition})
	connection.commit()
	connection.close()
	update_e1.delete(0, END)
	update_e2.delete(0, END)
	update_e3.delete(0, END)
	UpdateSuccess()

def UpdateSuccess():
	global updateSuccess
	updateSuccess=Toplevel(update)
	updateSuccess.geometry("150x100")
	updateSuccess.title("")
	Label(updateSuccess, text="").pack()
	Label(updateSuccess, text="Successful Update").pack()
	Button(updateSuccess, text="Okay", command= lambda : delete_updateSuccess()).pack()

def delete_updateSuccess():
	updateSuccess.destroy()
	flowerUpdate.destroy()
	updateFlowers()

def get():
	userline = mylist.get('active')
	global update
	global update_e1
	global update_e2
	global update_e3

	connection = sqlite3.connect('flowers2019.db')
	c = connection.cursor()

	c.execute("SELECT * FROM FLOWERS WHERE COMNAME=:comname", {'comname':userline})
	flowerInfo=c.fetchall()
	connection.close()

	update = Toplevel(flowerUpdate)
	update.title("Update flower info")
	update.geometry("300x350")
	textString = "Update " + str(userline) + ": "
	Label(update, text=textString, bg="green").grid(row=0)
	Label(update, text=" ").grid(row=1)
	Label(update, text='Current Genus:').grid(row=2)
	Label(update, text='Current Species:').grid(row=3)
	Label(update, text='Current Common Name:').grid(row=4)
	genus = StringVar()
	update_e1 = Entry(update, textvariable=genus)
	species = StringVar()
	update_e2 = Entry(update, textvariable=species)
	comname = StringVar()
	update_e3 = Entry(update, textvariable=comname)
	Label(update, text=flowerInfo[0][0]).grid(row=2, column=1)
	Label(update, text=flowerInfo[0][1]).grid(row=3, column=1)
	Label(update, text=flowerInfo[0][2]).grid(row=4, column=1)
	Label(update, text=" ").grid(row=5)
	Label(update, text="Updated Genus").grid(row=6, column=0)
	Label(update, text="Updated Species").grid(row=7, column=0)
	Label(update, text="Updated Common Name").grid(row=8, column=0)
	update_e1.grid(row=6, column=1)
	update_e2.grid(row=7, column=1)
	update_e3.grid(row=8, column=1)
	Label(update, text=" ").grid(row=9)
	Button(update, text="Update",command= lambda:
	Update(userline, genus.get(), species.get(), comname.get())).grid(row=10, column=1)
	Label(update, text=" ").grid(row=11)
	Button(update, text="Exit", bg="red",command= lambda: delete_update()).grid(row=12, column=1)

def updateFlowers():
	global flowerUpdate
	global mylist
	flowerUpdate = Toplevel(database_interface)
	flowerUpdate.title("Update a flower's info: ")
	flowerUpdate.geometry("300x200")
	connection = sqlite3.connect('flowers2019.db')
	c = connection.cursor()
	c.execute('SELECT COMNAME FROM FLOWERS')
	flowers = c.fetchall()
	connection.close()

	scrollbar = Scrollbar(flowerUpdate)
	scrollbar.pack(side=RIGHT, fill=Y)
	mylist = Listbox(flowerUpdate, yscrollcommand=scrollbar.set)
	for row in flowers:
		mylist.insert(END, row[0])
	mylist.pack(side=LEFT, fill=BOTH)
	scrollbar.config(command=mylist.yview)
	Button(flowerUpdate, text="Select", command=lambda: get()).pack()
	Button(flowerUpdate, text="Exit", bg="red", command=lambda: delete_flowerUpdate()).pack()


def delete_password_not_recognised():
	password_not_recog_screen.destroy()


def delete_user_not_found_screen():
	user_not_found_screen.destroy()

def delete_insert_page():
	insertPage.destroy()

def delete_update():
	update.destroy()

def delete_flowerUpdate():
	flowerUpdate.destroy()

def delete_database_interface():
	database_interface.destroy()

def delete_main_screen():
	main_screen.destroy()

def delete_register_screen():
	register_screen.destroy()

def delete_querySelection():
	querySelection_.destroy()

def delete_flowerQuery():
	flower_Query.destroy()

def delete_sightingDeletion():
	sightingDeletion_.destroy()

def delete_deleteSighting():
	deleteSuccess.destroy()
	deleteSightingFrame.destroy()
	sightingDeletion_.destroy()
	sightingDeletion()

def delete_deleteSightingFrame():
	deleteSightingFrame.destroy()

def delete_logSelection():
	logSelection.destroy()

def insert():
	global insertPage
	insertPage = Toplevel(database_interface)
	insertPage.title("Enter information to insert: ")
	insertPage.geometry("300x250")

	global insert_e1
	global insert_e2
	global insert_e3
	global insert_e4

	Label(insertPage, text="Insert a new sighting: ", bg="green", font=("Roboto", 12)).grid(row=0)
	Label(insertPage, text=" ").grid(row=1)
	Label(insertPage, text='Flower Common Name').grid(row=2)
	Label(insertPage, text='Person').grid(row=3)
	Label(insertPage, text='Location').grid(row=4)
	Label(insertPage, text='Date Sighted').grid(row=5)
	Label(insertPage, text=" ").grid(row=6)
	flower = StringVar()
	insert_e1 = Entry(insertPage, textvariable=flower)
	person = StringVar()
	insert_e2 = Entry(insertPage, textvariable=person)
	location = StringVar()
	insert_e3 = Entry(insertPage, textvariable=location)
	date = StringVar()
	insert_e4 = Entry(insertPage, textvariable=date)
	insert_e1.grid(row=2, column=1)
	insert_e2.grid(row=3, column=1)
	insert_e3.grid(row=4, column=1)
	insert_e4.grid(row=5, column=1)
	Button(insertPage, text="Insert", command=lambda:
	insertSighting(flower.get(), person.get(), location.get(), date.get())).grid(row=7, column=1)
	Label(insertPage, text=" ").grid(row=8)
	Button(insertPage, text="Exit", bg="red", command=lambda: delete_insert_page()).grid(row=9, column=1)

def flowerQuery():
	searchFlower = flowerList.get('active')
	global flower_Query
	flower_Query = Toplevel(querySelection_)
	flower_Query.geometry("550x450")
	flower_Query.title("Flower Sightings Query")
	connection = sqlite3.connect('flowers2019.db')
	c = connection.cursor()
	c.execute("SELECT * FROM SIGHTINGS WHERE NAME=:flower ORDER BY SIGHTED DESC",{'flower':searchFlower})
	sightings = c.fetchmany(10)
	connection.commit()
	connection.close()
	Label(flower_Query, text="Flower Common Name    ").grid(row=0, column=0)
	Label(flower_Query, text="    Person    ").grid(row=0, column=1)
	Label(flower_Query, text="    Location    ").grid(row=0, column=2)
	Label(flower_Query, text="    Date").grid(row=0, column=3)
	Label(flower_Query, text="").grid(row=1)
	i = 2
	for rows in sightings:
		i = i + 1
		for index in range(len(rows)):
			Label(flower_Query, text=rows[index]).grid(row=i, column=index)
	imagePath = os.getcwd() +"/SSWC_Flower_Pics/" + searchFlower + ".jpg"
	Label(flower_Query, text="").grid(row=i)
	i = i + 1

	Label(flower_Query, text="").grid(row=i, column=index)
	i = i+1
	test = Image.open(imagePath)
	test = test.resize((150,150), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(test)
	panel = Label(flower_Query, image=img)
	panel.image=img
	panel.grid(row=i, column=index)
	Button(flower_Query, text="Exit", bg="red", command=lambda: delete_flowerQuery()).grid(row=i, column=0)

def querySelection():
	global flowerList
	global querySelection_
	querySelection_ = Toplevel(database_interface)
	querySelection_.title("Select a flower to see its sightings: ")
	querySelection_.geometry("200x200")
	connection = sqlite3.connect('flowers2019.db')
	c = connection.cursor()
	c.execute('SELECT DISTINCT NAME FROM SIGHTINGS')
	flowers = c.fetchall()
	connection.close()

	scrollbar = Scrollbar(querySelection_)
	scrollbar.pack(side=RIGHT, fill=Y)
	flowerList = Listbox(querySelection_, yscrollcommand=scrollbar.set)
	for row in flowers:
		flowerList.insert(END, row[0])
	flowerList.pack(side=LEFT, fill=BOTH)
	scrollbar.config(command=flowerList.yview)
	Button(querySelection_, text="Select", command=lambda:flowerQuery()).pack()
	Button(querySelection_, text="Exit", bg="red", command=lambda: delete_querySelection()).pack()

def delete():
	to_deletePerson = deleteList.get('active')
	to_deleteFlower = sightingList.get('active')

	connection = sqlite3.connect('flowers2019.db')
	c = connection.cursor()
	script = """
	BEGIN TRANSACTION;
	DELETE from SIGHTINGS
	WHERE PERSON = "{}" AND NAME = "{}";
	COMMIT;
	""".format(to_deletePerson, to_deleteFlower)
	c.executescript(script)
	connection.commit()
	connection.close()
	global deleteSuccess
	deleteSuccess = Toplevel(deleteSightingFrame)
	deleteSuccess.title("")
	deleteSuccess.geometry("100x100")
	Label(deleteSuccess, text="").pack()
	Label(deleteSuccess ,text="Successful Deletion").pack()
	Button(deleteSuccess, text="Okay", command = lambda : delete_deleteSighting()).pack()

def deleteSighting():
	global deleteSightingFrame
	global deleteList
	deleteSightingFrame = Toplevel(sightingDeletion_)
	flowerDelete = sightingList.get('active')
	connection = sqlite3.connect('flowers2019.db')
	c = connection.cursor()
	c.execute('SELECT PERSON FROM SIGHTINGS WHERE NAME=:name',{'name':flowerDelete})
	deletes = c.fetchall()
	connection.close()

	scrollbar = Scrollbar(deleteSightingFrame)
	scrollbar.pack(side=RIGHT, fill=BOTH)
	deleteList = Listbox(deleteSightingFrame, yscrollcommand=scrollbar.set)
	for row in deletes:
		deleteList.insert(END, str(row[0]))
	deleteList.pack(side=LEFT, fill=BOTH)
	scrollbar.config(command=deleteList.yview)
	Button(deleteSightingFrame, text="Select", command=lambda: delete()).pack()
	Button(deleteSightingFrame, text="Exit", bg="red", command=lambda: delete_deleteSightingFrame()).pack()
	deleteSightingFrame.mainloop()

def sightingDeletion():
	global sightingDeletion_
	sightingDeletion_ = Toplevel(database_interface)
	sightingDeletion_.title("Delete Sighting")
	sightingDeletion_.geometry("250x200")
	connection = sqlite3.connect('flowers2019.db')
	c = connection.cursor()
	c.execute('SELECT DISTINCT NAME FROM SIGHTINGS')
	sightings = c.fetchall()
	connection.close()
	global sightingList
	scrollbar = Scrollbar(sightingDeletion_)
	scrollbar.pack(side=RIGHT, fill=BOTH)
	sightingList = Listbox(sightingDeletion_, yscrollcommand=scrollbar.set)
	for row in sightings:
		sightingList.insert(END, row[0])
	sightingList.pack(side=LEFT, fill=BOTH)
	scrollbar.config(command=sightingList.yview)
	Button(sightingDeletion_, text="Select", command=lambda: deleteSighting()).pack()
	Label(sightingDeletion_, text=" ").pack()
	Button(sightingDeletion_, text="Exit", bg="red", command=lambda: delete_sightingDeletion()).pack()

def export(tableName):
	sqlString = tableName+"_LOG"
	sqlString2 = "SELECT * FROM {}".format(sqlString)
	connection = sqlite3.connect('flowers2019.db')
	c = connection.cursor()
	c.execute(sqlString2)
	logInfo = c.fetchall()
	connection.close()
	fileName = os.getcwd()+"/Table Logs/"+tableName+"_Log_"+str(date.today())+".txt"
	file = open(fileName, "w")
	for row in logInfo:
		for index in range(len(row)):
			file.write(str(row[index]))
			if (index != len(row)-1):
				file.write(',')
		file.write("\n")
	global successfulExport
	successfulExport = Toplevel(logSelection)
	successfulExport.title("")
	successfulExport.geometry("100x100")
	Label(successfulExport, text="").pack()
	Button(successfulExport, text="Okay", command=successfulExport.destroy).pack()

def exportLogsSelection():
	global logSelection
	logSelection = Toplevel(database_interface)
	logSelection.title("")
	logSelection.geometry("300x375")
	Label(logSelection, text="").pack()
	Button(logSelection, text="Export FLOWERS Table Logs", height="2", width="30", command= lambda : export("FLOWERS")).pack()
	Label(logSelection, text="").pack()
	Button(logSelection, text="Export SIGHTINGS Table Logs", height="2", width="30", command=lambda: export("SIGHTINGS")).pack()
	Label(logSelection, text="").pack()
	Button(logSelection, text="Export FEATURES Table Logs", height="2", width="30", command=lambda: export("FEATURES")).pack()
	Label(logSelection, text="").pack()
	Button(logSelection, text="Export MEMBERS Table Logs", height="2", width="30", command=lambda: export("MEMBERS")).pack()
	Label(logSelection, text="").pack()
	Button(logSelection, text="Exit", bg="red", command=lambda: delete_logSelection()).pack()

def open_database():
	global database_interface
	database_interface = Toplevel(login_screen)
	database_interface.title("Database Interface")
	database_interface.geometry("300x375")
	Label(database_interface, text=" ").pack()
	Button(database_interface, text="Insert Sighting", height="2", width="30", command=lambda: insert()).pack()
	Label(database_interface, text=" ").pack()
	Button(database_interface, text="Update Flowers", height="2", width="30", command=lambda: updateFlowers()).pack()
	Label(database_interface, text=" ").pack()
	Button(database_interface, text="Search for Flower Sightings", height="2", width="30",
		   command=lambda : querySelection()).pack()
	Label(database_interface, text=" ").pack()
	Button(database_interface, text="Delete Sighting", height="2", width="30", command= lambda: sightingDeletion()).pack()
	Label(database_interface, text="").pack()
	Button(database_interface, text="Export Table Changes Logs", height="2", width="30", command= lambda: exportLogsSelection()).pack()
	Label(database_interface, text=" ").pack()
	Button(database_interface, text="Exit", bg="red", command=lambda: delete_database_interface()).pack()
	database_interface.mainloop()

def loginScreen():
	global main_screen
	main_screen = Tk()
	main_screen.geometry("250x250")
	main_screen.title("Account Login")
	Label(text="Login or Register", bg="blue", width="225", height="1", font=("Roboto", 15)).pack()
	Label(text="").pack()
	Button(text="Login", height="2", width="30", command=login).pack()
	Label(text="").pack()
	Button(text="Register", height="2", width="30", command=register).pack()
	Label(main_screen, text=" ").pack()
	Button(main_screen, text="Exit", bg="red",command =lambda : delete_main_screen()).pack()
	main_screen.mainloop()

loginScreen()