from tkinter import *

import sqlite3

#create tkinter window

root = Tk()

root.title('Rental Database')

root.geometry("1000x1000")

#connect to the DB

conn = sqlite3.connect('car_rental.db')

print("Connected to DB successfully")

#create a cursor

car_rental_c = conn.cursor()

#These are all the table creation statements we used, data

#car_rental_c.execute('''CREATE TABLE Vehicle (
#							VehicleID varchar(100) NOT NULL,
#							Description varchar(100) NOT NULL,
#							Year int NOT NULL,
#							Type int NOT NULL,
#							Category int NOT NULL,
#							PRIMARY KEY (VehicleID)
#							)''')

#car_rental_c.execute('''CREATE TABLE Customer (
#						CustID int NOT NULL,
#						Name varchar(50) NOT NULL,
#						Phone varchar(100) NOT NULL,
#						PRIMARY KEY (CustID)
#						)''')

#car_rental_c.execute('''CREATE TABLE Rental (
#	CustID int NOT NULL,
#	VehicleID varchar(100) NOT NULL,
#	StartDate date NOT NULL,
#	OrderDate date NOT NULL,
#	RentalType int NOT NULL,
#	Qty int NOT NULL,
#	ReturnDate date NOT  NULL,
#	TotalAmount int NOT NULL,
#	PaymentDate date,
#	FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID) ON UPDATE cascade,
#	FOREIGN KEY (CustID) REFERENCES Customer(CustID) ON UPDATE cascade
#	)''')

#car_rental_c.execute('''CREATE TABLE Rate (
#	Type int NOT NULL,
#	Category int NOT NULL,
#	Weekly int NOT NULL,
#	Daily int NOT NULL
#	)''')

def insert_cust():
	submit_conn = sqlite3.connect('car_rental.db')
	submit_cur = submit_conn.cursor()

	submit_cur.execute("INSERT INTO Customer VALUES(:CustID, :Name, :Phone)",
		{
			'CustID': CustID.get(), 
			'Name': Name.get(), 
			'Phone': Phone.get()
		})

	submit_conn.commit() #like github
	submit_conn.close()

def insert_vehicle():
	submit_conn = sqlite3.connect('car_rental.db')
	submit_cur = submit_conn.cursor()

	submit_cur.execute("INSERT INTO Vehicle VALUES(:VehicleID, :Description, :Year, :Type, :Category)",
		{
			'VehicleID': VehicleID.get(), 
			'Description': Description.get(), 
			'Year': Year.get(),
			'Type': Type.get(), 
			'Category': Category.get()
		})

	submit_conn.commit() #like github
	submit_conn.close()

def fiveA_search():
	root = Tk()
	root.title('Customer Search Results')
	root.geometry("300x300")

	iq = sqlite3.connect('car_rental.db')
	iq_cur = iq.cursor()

	iq_cur.execute("SELECT CustomerID, CustomerName, PRINTF('$%.2f', RentalBalance) AS RentalBalance FROM vRentalInfo WHERE CustomerID = ? OR CustomerName = ? OR RentalBalance = ? ORDER BY RentalBalance", 
		(CustomerID.get(), CustomerName.get(), RentalBalance.get(),))

	records = iq_cur.fetchall()
	print_records = ''
	print_records3 = ''
	print_records5 = ''

	for record in records:
		print_records += str(record[0]) + str("\n")
		print_records3 += (record[1] + "\n")
		print_records5 += str(record[2]) + str("\n")

	iq_label = Label(root, text = print_records)
	iq_label.grid(row = 20, column = 2, columnspan = 2)
	iq_label2 = Label(root, text = print_records3)
	iq_label2.grid(row = 20, column = 30, columnspan = 2)
	iq_label3 = Label(root, text = print_records5)
	iq_label3.grid(row = 20, column = 40, columnspan = 2)

	iq.commit()
	iq.close


def fiveA_all():
	root = Tk()
	root.title('Customer View Results')
	root.geometry("300x300")
	iq = sqlite3.connect('car_rental.db')
	iq_cur = iq.cursor()

	iq_cur.execute("SELECT CustomerID, CustomerName, PRINTF('$%.2f', RentalBalance) AS RentalBalance FROM vRentalInfo ORDER BY RentalBalance")

	records = iq_cur.fetchall()
	print_records = ''
	print_records3 = ''
	print_records5 = ''

	for record in records:
		print_records += str(record[0]) + str("\n")
		print_records3 += (record[1] + "\n")
		print_records5 += str(record[2]) + str("\n")

	iq_label = Label(root, text = print_records)
	iq_label.grid(row = 16, column = 30, columnspan = 2)
	iq_label2 = Label(root, text = print_records3)
	iq_label2.grid(row = 16, column = 40, columnspan = 2)
	iq_label3 = Label(root, text = print_records5)
	iq_label3.grid(row = 16, column = 50, columnspan = 2)

	iq.commit()
	iq.close

def fiveB_search():
	root = Tk()
	root.title('Vehicle Search Results')
	root.geometry("400x400")
	iq = sqlite3.connect('car_rental.db')
	iq_cur = iq.cursor()

	iq_cur.execute("SELECT VIN, Vehicle, PRINTF('$%.2f', OrderAmount/TotalDays) AS DailyPrice FROM vRentalInfo WHERE VIN = ? OR Vehicle = ? OR DailyPrice = ? ORDER BY DailyPrice", 
		(VIN.get(), Vehicle.get(), DailyPrice.get(),))

	records = iq_cur.fetchall()
	print_records = ''
	print_records3 = ''
	print_records5 = ''

	for record in records:
		print_records += str(record[0]) + str("\n")  #for ints
		print_records3 += (record[1] + "\n")  #for strings
		print_records5 += str(record[2]) + str("\n")

	iq_label = Label(root, text = print_records)
	iq_label.grid(row = 20, column = 2, columnspan = 2)
	iq_label2 = Label(root, text = print_records3)
	iq_label2.grid(row = 20, column = 6, columnspan = 2)
	iq_label3 = Label(root, text = print_records5)
	iq_label3.grid(row = 20, column = 50, columnspan = 2)

	iq.commit()
	iq.close


def fiveB_all():
	root = Tk()
	root.title('Vehicle View Results')
	root.geometry("400x400")
	iq = sqlite3.connect('car_rental.db')
	iq_cur = iq.cursor()

	iq_cur.execute("SELECT VIN, Vehicle, PRINTF('$%.2f', OrderAmount/TotalDays) AS DailyPrice FROM vRentalInfo ORDER BY DailyPrice")

	records = iq_cur.fetchall()
	print_records = ''
	print_records2 = ''
	print_records3 = ''

	for record in records:
		print_records += str(record[0]) + str("\n")
		print_records2 += (record[1] + "\n")
		print_records3 += str(record[2]) + str("\n")

	iq_label = Label(root, text = print_records)
	iq_label.grid(row = 56, column = 2, columnspan = 2)
	iq_label2 = Label(root, text = print_records2)
	iq_label2.grid(row = 56, column = 6, columnspan = 2)
	iq_label3 = Label(root, text = print_records3)
	iq_label3.grid(row = 56, column = 50, columnspan = 2)

	iq.commit()
	iq.close


title_label = Label(root, text = 'Car Rental 2019: User Interface')
title_label.grid(row = 0, column = 1)

query1_label = Label(root, text = 'Option 1: Insert a New Customer')
query1_label.grid(row = 1, column = 1)

CustID = Entry(root, width = 30) #everything structured in pixel size

CustID.grid(row = 2, column = 1, padx = 20) #specifying where we want it

Name = Entry(root, width = 30)

Name.grid(row = 3, column = 1) #don't need to do pad for every entry

Phone = Entry(root, width = 30)

Phone.grid(row = 4, column = 1)

CustID_label = Label(root, text = 'Customer ID: ')
CustID_label.grid(row = 2, column = 0)

Name_label = Label(root, text = 'First Initial and Last Name: ')
Name_label.grid(row = 3, column = 0)

Phone_label = Label(root, text = 'Phone Number: ')
Phone_label.grid(row = 4, column = 0)

submit_btn = Button(root, text = 'Enter Customer into System', command = insert_cust)

submit_btn.grid(row = 8, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

query2_label = Label(root, text = 'Option 2: Insert a New Vehicle')
query2_label.grid(row = 9, column = 1)

VehicleID = Entry(root, width = 30) #everything structured in pixel size

VehicleID.grid(row = 10, column = 1, padx = 40) #specifying where we want it

Description = Entry(root, width = 30)

Description.grid(row = 11, column = 1) #don't need to do pad for every entry

Year = Entry(root, width = 30)

Year.grid(row = 12, column = 1)

Type = Entry(root, width = 30)

Type.grid(row = 13, column = 1)

Category = Entry(root, width = 30)

Category.grid(row = 14, column = 1)

VehicleID_label = Label(root, text = 'Vehicle ID: ')
VehicleID_label.grid(row = 10, column = 0)

Description_label = Label(root, text = 'Vehicle Description: ')
Description_label.grid(row = 11, column = 0)

Year_label = Label(root, text = 'Year: ')
Year_label.grid(row = 12, column = 0)

Type_label = Label(root, text = 'Type: ')
Type_label.grid(row = 13, column = 0)

Category_label = Label(root, text = 'Category: ')
Category_label.grid(row = 14, column = 0)

submit_btn2 = Button(root, text = 'Enter Vehicle into System', command = insert_vehicle)

submit_btn2.grid(row = 15, column = 0, columnspan = 2, pady = 20, padx = 20, ipadx = 100)


query5_label = Label(root, text = 'Option 5: Selections from vRentalInfo')
query5_label.grid(row = 20, column = 1)


submit_btn3 = Button(root, text = 'Get All "vRentalInfo View" Customer Info', command = fiveA_all)

submit_btn3.grid(row = 44, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

CustomerID = Entry(root, width = 30) #everything structured in pixel size
CustomerID.grid(row = 32, column = 1, padx = 20) #specifying where we want it

CustomerName = Entry(root, width = 30)
CustomerName.grid(row = 33, column = 1)

RentalBalance = Entry(root, width = 30) #everything structured in pixel size
RentalBalance.grid(row = 34, column = 1, padx = 20) #specifying where we want it


CustomerID_label = Label(root, text = 'Customer ID: ')
CustomerID_label.grid(row = 32, column = 0)

CustomerName_label = Label(root, text = 'Customer Name: ')
CustomerName_label.grid(row = 33, column = 0)

RentalBalance_label = Label(root, text = 'Remaining Balance: ')
RentalBalance_label.grid(row = 34, column = 0)

or_label = Label(root, text = 'OR')
or_label.grid(row = 42, column = 1)

submit_btn4 = Button(root, text = 'Search "vRentalInfo View" Customer Info (enter only one)', command = fiveA_search)

submit_btn4.grid(row = 28, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

submit_btn6 = Button(root, text = 'Search "vRentalInfo View" Vehicle Info (enter only one)', command = fiveB_search)

submit_btn6.grid(row = 49, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


VIN = Entry(root, width = 30) #everything structured in pixel size
VIN.grid(row = 32, column = 4, padx = 20) #specifying where we want it

Vehicle = Entry(root, width = 30)
Vehicle.grid(row = 33, column = 4)

DailyPrice = Entry(root, width = 30) #everything structured in pixel size
DailyPrice.grid(row = 34, column = 4, padx = 20) #specifying where we want it



VIN_label = Label(root, text = 'VIN: ')
VIN_label.grid(row = 32, column = 3)

Vehicle_label = Label(root, text = 'Vehicle Type: ')
Vehicle_label.grid(row = 33, column = 3)

DailyPrice_label = Label(root, text = 'Daily Price: ')
DailyPrice_label.grid(row = 34, column = 3)

or_label = Label(root, text = 'OR')
or_label.grid(row = 58, column = 1)

submit_btn5 = Button(root, text = 'Get All "vRentalInfo View" Vehicle Info', command = fiveB_all)

submit_btn5.grid(row = 60, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


root.mainloop()
