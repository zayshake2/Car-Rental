from tkinter import *

import sqlite3



root = Tk()

root.title('Car Rental 2019 GUI')

root.geometry("600x350")

#connect to the DB

conn = sqlite3.connect('CarRental2019.db')

print("Connected to DB successfully")

#create a cursor

car_rental_c = conn.cursor()

#These are all the table creation statements we used, data from Pt 2

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
#	ReturnDate date,
#	TotalAmount int,
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

title_label = Label(root, text = 'Car Rental 2019: User Interface!')
title_label.grid(row = 0, column = 1)

### QUERY 1 ###
def req1():
	root = Tk()
	root.title('Requirement 1')
	root.geometry("500x400")

	def insert_cust():
		submit_conn = sqlite3.connect('CarRental2019.db')
		submit_cur = submit_conn.cursor()

		submit_cur.execute("INSERT INTO Customer VALUES(:CustID, :Name, :Phone)",
			{
				'CustID': CustID.get(), 
				'Name': Name.get(), 
				'Phone': Phone.get()
			})

		submit_conn.commit() #like github
		submit_conn.close()

	query1_label = Label(root, text = 'Insert a New Customer')
	query1_label.grid(row = 1, column = 1)

	CustID = Entry(root, width = 30) 
	CustID.grid(row = 2, column = 1, padx = 20) 

	Name = Entry(root, width = 30)

	Name.grid(row = 3, column = 1) 

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

	def viewCustomers():
		viewCustomers_conn = sqlite3.connect('CarRental2019.db')
		viewCustomers_cur = viewCustomers_conn.cursor()

		viewCustomers_cur.execute("SELECT * FROM Customer")

		cust_Records = viewCustomers_cur.fetchall()


		for x in cust_Records:
			print_custRecords = print(x) #prints in terminal

		list_label = Label(root, text = print_custRecords)
		list_label.grid(row=11, column=1, columnspan=2)  

		viewCustomers_conn.commit()
		viewCustomers_conn.close()
	    

	view_cust_btn = Button (root, text = 'View customer table in terminal', command= viewCustomers)
	view_cust_btn.grid(row= 12, column = 0, columnspan=2, pady=10, padx=10, ipadx=100)

req1btn = Button(root, text = 'Requirement 1: Inserting a New Customer', command = req1)
req1btn.grid(row = 2, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


### QUERY 2 ###
def req2():
	root = Tk()
	root.title('Requirement 2')
	root.geometry("600x400")

	def insert_vehicle():
		submit_conn = sqlite3.connect('CarRental2019.db')
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

	query2_label = Label(root, text = 'Insert a New Vehicle')
	query2_label.grid(row = 2, column = 3)

	VehicleID = Entry(root, width = 30) 

	VehicleID.grid(row = 2, column = 3, padx = 40) 

	Description = Entry(root, width = 30)

	Description.grid(row = 3, column = 3) 

	Year = Entry(root, width = 30)

	Year.grid(row = 4, column = 3)

	Type = Entry(root, width = 30)

	Type.grid(row = 5, column = 3)

	Category = Entry(root, width = 30)

	Category.grid(row = 6, column = 3)

	VehicleID_label = Label(root, text = 'Vehicle ID: ')
	VehicleID_label.grid(row = 2, column = 2)

	Description_label = Label(root, text = 'Vehicle Description: ')
	Description_label.grid(row = 3, column = 2)

	Year_label = Label(root, text = 'Year: ')
	Year_label.grid(row = 4, column = 2)

	Type_label = Label(root, text = 'Type: ')
	Type_label.grid(row = 5, column = 2)

	Category_label = Label(root, text = 'Category: ')
	Category_label.grid(row = 6, column = 2)

	submit_btn2 = Button(root, text = 'Enter Vehicle into System', command = insert_vehicle)
	submit_btn2.grid(row = 15, column = 3, columnspan = 2, pady = 20, padx = 20, ipadx = 100)

	def viewVehicles():
		viewVehicles_conn = sqlite3.connect('CarRental2019.db')
		viewVehicles_cur = viewVehicles_conn.cursor()

		viewVehicles_cur.execute("SELECT * FROM Vehicle")

		vehic_Records = viewVehicles_cur.fetchall()


		for x in vehic_Records:
			print_vehicRecords = print(x) #prints in terminal

		list_label = Label(root, text = print_vehicRecords)
		list_label.grid(row=11, column=1, columnspan=2)  

		viewVehicles_conn.commit()
		viewVehicles_conn.close()
	    

	view_vehicle_btn = Button (root, text = 'View vehicle table in terminal', command= viewVehicles)
	view_vehicle_btn.grid(row= 17, column = 3, columnspan=2, pady=10, padx=10, ipadx=100)

req2btn = Button(root, text = 'Requirement 2: Inserting a New Vehicle', command = req2)
req2btn.grid(row = 4, column = 0, columnspan = 2, pady = 20, padx = 20, ipadx = 100)


### QUERY 3 ###

def req3():
    root = Tk()
    root.title('Requirement 3')
    root.geometry("800x400")

    def listCars():
        listCars_conn = sqlite3.connect('CarRental2019.db')
        listCars_cur = listCars_conn.cursor()
        listCars_cur.execute("SELECT DISTINCT Rental.VehicleID , Description, Year FROM Vehicle, Rental WHERE Vehicle.VehicleID = Rental.VehicleID AND Type = ? AND Category = ? AND ((StartDate < ? AND ReturnDate < ?) OR (StartDate > ? AND ReturnDate > ?)) ", (car_type.get(), car_category.get(), start_date.get(), return_date.get(), start_date.get(), return_date.get(),))
        listRecords = listCars_cur.fetchall()
        print_listRecords = ''
        print_listRecords2 = ''
        print_listRecords3 = ''
        for listing in listRecords:
            print_listRecords += str(listing[0]) + str("\n")
            print_listRecords2 += (listing[1] + "\n")
            print_listRecords3 += str(listing[2]) + str("\n")
            
        list_label = Label(root, text = print_listRecords)
        list_label.grid(row=5, column=1, columnspan=2)  
        list_label = Label(root, text = print_listRecords2)
        list_label.grid(row=5, column=20, columnspan=2)  
        list_label = Label(root, text = print_listRecords3)
        list_label.grid(row=5, column=40, columnspan=2)  
        listCars_conn.commit()
        listCars_conn.close()

    #submit_btn = Button(root, text = 'List Vehicles', command = listCars)
    #submit_btn.grid(row=4, column = 0, columnspan=2, pady=10, padx=10, ipadx=100)
#
    
    def addReservation():
        add_conn = sqlite3.connect('CarRental2019.db')
        add_cur = add_conn.cursor()
        
        rental_type_value = add_cur.execute("SELECT CASE WHEN (JULIANDAY(?)- JULIANDAY(?)) >= 7 THEN 7 ELSE 1 END" , (return_date.get(), start_date.get(),) ).fetchall()
        quantity_value = add_cur.execute("SELECT CASE WHEN (JULIANDAY(?)- JULIANDAY(?)) >= 7 THEN (JULIANDAY(?)- JULIANDAY(?))/7 ELSE (JULIANDAY(?)- JULIANDAY(?)) END", (return_date.get(), start_date.get(),return_date.get(), start_date.get(),return_date.get(), start_date.get(), )).fetchall()

        total_amount_value = add_cur.execute("SELECT CASE WHEN (JULIANDAY(?)- JULIANDAY(?)) >=7 THEN Weekly*((JULIANDAY(?)- JULIANDAY(?))/7)  ELSE Daily*(JULIANDAY(?)- JULIANDAY(?)) END FROM Rate WHERE Type =? AND Category = ?", (return_date.get(), start_date.get(),return_date.get(), start_date.get(),return_date.get(), start_date.get(),car_type.get(), car_category.get(), )).fetchall()

        pyt_date_value = add_cur.execute("SELECT CASE WHEN PaymentDate IS NULL THEN 0 ELSE 1 END FROM Rental").fetchall()

        add_cur.execute("INSERT INTO RENTAL VALUES(:cust_id, :car_id, :start_date, :order_date, :rental_type, :quantity, :return_date, :total_amount, :payment_date, :return_attr)",
            {
                'cust_id': cust_id.get(),
                'car_id': car_id.get(),
                'start_date': start_date.get(),
                'order_date': order_date.get(),
                'rental_type': rental_type_value[0][0],         
                'quantity': quantity_value[0][0],                       
                'return_date': return_date.get(),
                'total_amount': total_amount_value[0][0],
                'payment_date': payment_date.get(),
                'return_attr' : pyt_date_value[0][0]
            })

        add_conn.commit()
        add_conn.close()

    start_date = Entry(root, width=30)
    start_date.grid(row=0, column=1)

    return_date = Entry(root, width=30)
    return_date.grid(row=1, column=1)

    car_type = Entry(root, width=30)
    car_type.grid(row=2, column=1)

    car_category = Entry(root, width=30)
    car_category.grid(row=3, column=1)

    order_date = Entry(root, width = 30)
    order_date.grid(row=6, column=1, padx=20)

    payment_date = Entry(root, width = 30)
    payment_date.grid(row=7, column=1)

    cust_id = Entry(root, width = 30)
    cust_id.grid(row=8, column=1)

    car_id = Entry(root, width=30)
    car_id.grid(row=9, column=1)


    start_date_label = Label(root, text = 'Start Date ')
    start_date_label.grid(row=0, column=0)

    return_date_label = Label(root, text = 'Return Date: ')
    return_date_label.grid(row=1, column=0)

    car_type_label = Label(root, text = 'Car Type (1-Compact, 2-Medium, 3-Large, 4-SUV, & 5-Truck): ')
    car_type_label.grid(row=2, column=0)

    car_category_label = Label(root, text = 'Rental Category (0 -Compact & 1 -Luxury): ')
    car_category_label.grid(row=3, column=0)

    order_date_label = Label(root, text = 'Date Ordered: ')
    order_date_label.grid(row=6, column=0)

    pyt_date_label = Label(root, text = 'Payment Date: ')
    pyt_date_label.grid(row=7, column=0)

    cust_id_label = Label(root, text = 'Customer ID: ')
    cust_id_label.grid(row=8, column=0)

    car_id_label = Label(root, text = 'ENTER VIN OF SELECTED VEHICLE: ')
    car_id_label.grid(row=9, column=0)


    submit_btn = Button(root, text = 'List Vehicle', command=listCars)
    submit_btn.grid(row=4, column = 0, columnspan=2, pady=10, padx=10, ipadx=100)

    add_btn = Button(root, text = 'Reserve', command=addReservation)
    add_btn.grid(row=10, column = 0, columnspan=2, pady=10, padx=10, ipadx=100)

    
    def viewRentals():
        viewRentals_conn = sqlite3.connect('CarRental2019.db')
        viewRentals_cur = viewRentals_conn.cursor()
        viewRentals_cur.execute("SELECT * FROM Rental")
        rental_Records = viewRentals_cur.fetchall()
        
        for x in rental_Records:
            print_rentalRecords = print(x) #prints in terminal
        
        list_label = Label(root, text = print_rentalRecords)
        list_label.grid(row=11, column=1, columnspan=2)  
        viewRentals_conn.commit()
        viewRentals_conn.close()
	    
    view_rentals_btn = Button (root, text = 'View rental table', command= viewRentals)
    view_rentals_btn.grid(row= 12, column = 0, columnspan=2, pady=10, padx=10, ipadx=100)


req3button = Button (root, text = 'Requirement 3: Finding and Reserving a Rental', command= req3)
req3button.grid(row= 6, column = 0, columnspan=2, pady=10, padx=10, ipadx=100)


### QUERY 4 ###

def req4a():
	root = Tk()
	root.title('Requirement 4a')
	root.geometry("600x300")

	def four_select():
		root = Tk()
		root.title('Amount Due')
		root.geometry("100x100")
		iq = sqlite3.connect('CarRental2019.db')
		iq_cur = iq.cursor()

		iq_cur.execute("SELECT TotalAmount FROM Rental, Customer, Vehicle WHERE Rental.CustID = ? AND Name = ? AND Description = ? AND ReturnDate = ? AND Customer.CustID = Rental.CustID AND Vehicle.VehicleID = Vehicle.VehicleID",
			(CustID.get(), Name.get(), Description.get(), ReturnDate.get(),))

		records = iq_cur.fetchall()
		print_records = ''

		for record in records:
			print_records += str(record[0]) + str("\n")

		iq_label = Label(root, text = print_records)
		iq_label.grid(row = 56, column = 2, columnspan = 2)



	CustID = Entry(root, width = 30) #everything structured in pixel size
	CustID.grid(row = 32, column = 1, padx = 20) #specifying where we want it

	Name = Entry(root, width = 30)
	Name.grid(row = 33, column = 1)

	Description = Entry(root, width = 30) #everything structured in pixel size
	Description.grid(row = 34, column = 1, padx = 20) #specifying where we want it

	ReturnDate = Entry(root, width = 30)
	ReturnDate.grid(row = 35, column = 1)



	RCI_label = Label(root, text = 'Customer ID: ')
	RCI_label.grid(row = 32, column = 0)

	Name4_label = Label(root, text = 'Customer Name: ')
	Name4_label.grid(row = 33, column = 0)

	Description4_label = Label(root, text = 'Vehicle Description: ')
	Description4_label.grid(row = 34, column = 0)

	ReturnDate4_label = Label(root, text = 'Date Returned: ')
	ReturnDate4_label.grid(row = 35, column = 0)

	submit_btn7 = Button(root, text = 'Get Total Price Due', command = four_select)

	submit_btn7.grid(row = 38, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 80)

req4aBtn = Button(root, text = 'Requirement 4a: Price of Rental Returned', command = req4a)
req4aBtn.grid(row = 8, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

def req4b():
	root = Tk()
	root.title('Requirement 4b')
	root.geometry("600x300")

	def four_update():
		iq = sqlite3.connect('CarRental2019.db')
		iq_cur = iq.cursor()

		iq_cur.execute("UPDATE Rental SET Returned = 1 WHERE CustID = ? AND VehicleID = ? AND ReturnDate = ? AND TotalAmount = ?",
			(CustID.get(), VehicleID.get(), ReturnDate.get(), TotalAmount.get(),))

		records = iq_cur.fetchall()


		iq.commit()
		iq.close

	CustID = Entry(root, width = 30) #everything structured in pixel size
	CustID.grid(row = 32, column = 3, padx = 20) #specifying where we want it

	VehicleID = Entry(root, width = 30)
	VehicleID.grid(row = 33, column = 3)

	ReturnDate = Entry(root, width = 30)
	ReturnDate.grid(row = 34, column = 3)

	TotalAmount = Entry(root, width = 30)
	TotalAmount.grid(row = 35, column = 3)


	CI_label = Label(root, text = 'Customer ID: ')
	CI_label.grid(row = 32, column = 2)

	VI_label = Label(root, text = 'Vehicle ID: ')
	VI_label.grid(row = 33, column = 2)

	ReturnDate4_label = Label(root, text = 'Date Returned: ')
	ReturnDate4_label.grid(row = 34, column = 2)

	TotalAmount_label = Label(root, text = 'Amount Paid: ')
	TotalAmount_label.grid(row = 35, column = 2)


	submit_btn8 = Button(root, text = 'Update Return', command = four_update)

	submit_btn8.grid(row = 38, column = 2, columnspan = 2, pady = 10, padx = 10, ipadx = 80)

	def viewRentals():
		viewRentals_conn = sqlite3.connect('CarRental2019.db')
		viewRentals_cur = viewRentals_conn.cursor()

		viewRentals_cur.execute("SELECT * FROM Rental")

		rental_Records = viewRentals_cur.fetchall()


		for x in rental_Records:
			print_rentalRecords = print(x) #prints in terminal

		list_label = Label(root, text = print_rentalRecords)
		list_label.grid(row=11, column=1, columnspan=2)  

		viewRentals_conn.commit()
		viewRentals_conn.close()
	    

	view_rentals_btn = Button (root, text = 'View rental table in terminal', command= viewRentals)
	view_rentals_btn.grid(row= 45, column = 2, columnspan=2, pady=10, padx=10, ipadx=100)

req4btn = Button(root, text = 'Requirement 4b: Returning a Rental', command = req4b)
req4btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


### QUERY 5 ###

def req5():
	root = Tk()
	root.title('Requirement 5')
	root.geometry("1200x400")

	def fiveA_search():
		root = Tk()
		root.title('Customer Search Results')
		root.geometry("300x300")

		iq = sqlite3.connect('CarRental2019.db')
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

	query5_label = Label(root, text = 'Selections from vRentalInfo')
	query5_label.grid(row = 20, column = 1)


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
	submit_btn4.grid(row = 28, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 80)


	def fiveA_all():
		root = Tk()
		root.title('Customer View Results')
		root.geometry("300x300")
		iq = sqlite3.connect('CarRental2019.db')
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

	submit_btn3 = Button(root, text = 'Get All "vRentalInfo View" Customer Info', command = fiveA_all)
	submit_btn3.grid(row = 44, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


	def fiveB_search():
		root = Tk()
		root.title('Vehicle Search Results')
		root.geometry("400x400")
		iq = sqlite3.connect('CarRental2019.db')
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

	submit_btn6 = Button(root, text = 'Search "vRentalInfo View" Vehicle Info (enter only one)', command = fiveB_search)

	submit_btn6.grid(row = 28, column = 2, columnspan = 2, pady = 10, padx = 10, ipadx = 80)


	VIN = Entry(root, width = 30) #everything structured in pixel size
	VIN.grid(row = 32, column = 3, padx = 20) #specifying where we want it

	Vehicle = Entry(root, width = 30)
	Vehicle.grid(row = 33, column = 3)

	DailyPrice = Entry(root, width = 30) #everything structured in pixel size
	DailyPrice.grid(row = 34, column = 3, padx = 20) #specifying where we want it



	VIN_label = Label(root, text = 'VIN: ')
	VIN_label.grid(row = 32, column = 2)

	Vehicle_label = Label(root, text = 'Vehicle Type: ')
	Vehicle_label.grid(row = 33, column = 2)

	DailyPrice_label = Label(root, text = 'Daily Price: ')
	DailyPrice_label.grid(row = 34, column = 2)

	or_label = Label(root, text = 'OR')
	or_label.grid(row = 42, column = 2)



	def fiveB_all():
		root = Tk()
		root.title('Vehicle View Results')
		root.geometry("400x400")
		iq = sqlite3.connect('CarRental2019.db')
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


	submit_btn5 = Button(root, text = 'Get All "vRentalInfo View" Vehicle Info', command = fiveB_all)

	submit_btn5.grid(row = 44, column = 2, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

req5button = Button(root, text = 'Requirement 5: Searching the Rental View', command = req5)
req5button.grid(row = 12, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


root.mainloop()
