import mysql.connector
from tabulate import tabulate
x=input("Enter Your MySQL password : ")
con=mysql.connector.connect(host='localhost',user='root',password=x)
if con.is_connected():
    print('Connection successful')
#creating database
cur=con.cursor()
cur.execute('use project')
flag=True
flag1=True
flag2=True
print("                                                  _______________________________________________________________ ")
print("                                                 |                                                               |")
print("                                                 |                   *       * *       *  ******                 |")
print("                                                 |                    *     *  **     ** *                       |")
print("                                                 |                     *   *   * *   * *  ******                 |")
print("                                                 |                      * *    *  * *  *        *                |")
print("                                                 |                       *     *   *   *  ******                 |") 
print("                                                 |                    (Vaccine Management System)                |")
print("                                                 |_______________________________________________________________|")
while flag:
    accorlog=input("Enter (1) to Signup\nEnter (2) to Login\nEnter (3) to Exit:")
    print("\n")
    if accorlog =="1":
        username=input("Enter accounts Username to add: ")
        
        pwd=input("Enter account password to add: ")
        name = input("Enter your name: ")
        number = input("Enter your mobile number: ")
        dob = input("Enter your DOB (YYYY-MM-DD Format): ")
        Gender = input("Enter your Gender (M/F): ")
        while True:
            query1="Select * from accounts where Username='{}'".format(username)
            cur.execute(query1)
            if cur.fetchone()==None:
                query="INSERT INTO accounts(Username,Name,Number,DOB,Gender,password)values('{}','{}',{},'{}','{}','{}')".format(username,name,number,dob,Gender,pwd)
                cur.execute(query)
                query2="INSERT INTO slots(Username)values('{}')".format(username)
                cur.execute(query2)
                con.commit()
                print("Signed Up Successfully")
                break
            else:
                print("Username Already Exists")
                break
        
        

    elif accorlog =="2":
        choice=input("1-> To Login as User\n2-> To Login as Admin:\n")
        #User
        if choice=="1":
            cur.execute('use project')
            username=input("Enter Username: ")
            pwd=input("Enter Password: ")
            query1="Select * from accounts where Username='{}' and password='{}'".format(username,pwd)
            cur.execute(query1)
            if cur.fetchone()==None:
                print("Invalid Credentials")
            else:
                query1="Select username from accounts where Username='{}'".format(username)
                cur.execute(query1)
                x=cur.fetchone()
                print("Welcome back",x[0],"!")
                while True:
                    print("***********************************")
                    print("*       VACCINE MANAGEMENT        *")
                    print("*       ------------------        *")
                    print("*        1.Covid Test             *")
                    print("*        2.Vaccine Allotment      *")
                    print("*        3.Doctor Appointment     *")
                    print("*        4.View Your Schedule     *")
                    print("*        5.Logout                 *")
                    print("***********************************")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        cur.execute('use project')
                        sql_select_Query = "select * from covid"
                        cur.execute(sql_select_Query)
                        print (tabulate (cur.fetchall(), headers=['SNO', 'Test_Name', 'Centre_Name', 'Location','Days','Time','Price'], tablefmt="fancy_grid"))
                        while True:
                            slot=input("Enter the option you want to use\nPress E to exit:")
                            query1="Select * from covid where SNO='{}'".format(slot)
                            cur.execute(query1)
                            if cur.fetchone()==None:
                                print("Enter Correct Value")
                            else:                
                                query1="update slots set Covidtest_slot={} where username='{}'".format(slot,username)
                                cur.execute(query1)
                                con.commit()
                                print("Slot Updated")
                                break
                             
                                    
                        print("--------------------------------------------------------------------------")
                        print("--------------------------------------------------------------------------")
                        print("\n\n\n\n\n")

                    elif choice == 2:
                        cur.execute('use project')
                        sql_select_Query = "select * from vaccine"
                        cur.execute(sql_select_Query)
                        print (tabulate (cur.fetchall(), headers=['SNO', 'Vaccine_Name', 'Centre_Name', 'Location','Date_of_availablity','Time_of_slot','Price'], tablefmt="fancy_grid"))
                        while True:
                            slot=input("Enter the option you want to use\nPress E to exit:")
                            query1="Select * from vaccine where SNO='{}'".format(slot)
                            cur.execute(query1)
                            if cur.fetchone()==None:
                                print("Enter Correct Value")
                            else:
                                
                                query1="update slots set Vaccine_slot={} where username='{}'".format(slot,username)
                                cur.execute(query1)
                                con.commit()
                                print("Slot Updated")
                                break
                            print("-----------------------------------------------------------------------------------------------")
                            print("-----------------------------------------------------------------------------------------------")
                            print("\n\n\n\n\n")
                
                            break
                       


                    elif choice == 3:
                        cur.execute('use project')
                        sql_select_Query = "select * from doctor"
                        cur.execute(sql_select_Query)
                        print (tabulate (cur.fetchall(), headers=['SNO', 'Doctors_Name', 'Clinic_Name', 'Location','Contact_Number','Email_id'], tablefmt="fancy_grid"))
                        while True:
                            slot=input("Enter the option you want to use\nPress E to exit: ")
                            query1="Select * from doctor where SNO='{}'".format(slot)
                            cur.execute(query1)
                            if cur.fetchone()==None:
                                print("Enter Correct Value")
                            else:
                                query1="update slots set doctor_appointment={} where username='{}'".format(slot,username)
                                cur.execute(query1)
                                con.commit()
                                print("Slot Updated")
                                break
                            print("-----------------------------------------------------------------------------------------------")
                            print("-----------------------------------------------------------------------------------------------")
                            print("\n\n\n\n\n")
                
                            break

                    elif choice == 4:
                        query="Select * from slots where Username='{}'".format(username)
                        cur.execute(query)
                        print("Users Schedule :")
                        print (tabulate (cur.fetchall(), headers=['Username','Covidtest_Slot','Vaccine_slot','Doctor_appointment'], tablefmt="fancy_grid"))
                        
                        
                    elif choice ==5:
                        break
                    else:
                        print("Wrong Choice")



             
        #Admin       
        elif choice=="2":
            cur.execute('use project')
            admcode=input("Enter Your unique Admin Code: ")
            query1="Select * from admacc where Admin_Code='{}'".format(admcode)
            cur.execute(query1)
            if cur.fetchone()==None:
                print("Invalid Admin Code")
            else:
                query1="Select Name from admacc where Admin_Code='{}'".format(admcode)
                cur.execute(query1)
                x=cur.fetchone()
                print("Hello",x[0]) 
                while True:
                    cur.execute('use project')
                    print("***********************************")
                    print("*        VACCINE MANAGEMENT       *")
                    print("*        ------------------       *")
                    print("*         1.View Data             *")
                    print("*         2.Update Data           *")
                    print("*         3.Delete Data           *")
                    print("*         4.Add Data              *")
                    print("*         5.Logout                *")
                    print("***********************************")
                    choice = int(input("Enter your choice: "))            
                    if choice == 1:
                        while True:
                            print("Which Table do you want to view?")
                            print("1.Covid Test")
                            print("2.Vaccine Allotment")
                            print("3.Doctor Appointment")
                            print("4.View All Schedule")
                            print("5.Back")
                            choice = int(input("Enter your choice: "))
                            if choice == 1:
                                sql_select_Query = "select * from covid"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Test_Name', 'Centre_Name', 'Location','Days','Time','Price'], tablefmt="fancy_grid"))

                            elif choice == 2:
                                sql_select_Query = "select * from vaccine"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Vaccine_Name', 'Centre_Name', 'Location','Date_of_availablity','Time_of_slot','Price'], tablefmt="fancy_grid"))

                            elif choice == 3:
                                sql_select_Query = "select * from doctor"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Doctors_Name', 'Clinic_Name', 'Location','Contact_Number','Email_id'], tablefmt="fancy_grid"))

                            elif choice == 4:
                                cur.execute('use project')
                                query1="Select * from slots"
                                cur.execute(query1)
                                print("Users Schedule :")
                                print (tabulate (cur.fetchall(), headers=['Username','Covid Test Slot','Vaccine Slot','Doctor Appointment'], tablefmt="fancy_grid"))
                                
                    
                            elif choice==5:
                                break
                            else:
                                print("Wrong Choice")
                        print("-----------------------------------------------------------------------------------------------")
                        print("-----------------------------------------------------------------------------------------------")
                        print("\n\n\n\n\n")

                    elif choice == 2:
                        while True:
                            print("In which table you want to update values")
                            print("1.Covid Test")
                            print("2.Vaccine Allotment")
                            print("3.Doctor Appointment")
                            print("4.Back")                            
                            choice = int(input("Enter your choice: "))

                            if choice == 1:
                                sql_select_Query = "select * from covid"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Test_Name', 'Centre_Name', 'Location','Days','Time','Price'], tablefmt="fancy_grid"))
                                print("Which SNO's Price do you want to update? ")
                                SNO = int(input("Enter the SNO value: "))
                                Price = int(input("Enter the price value: "))

                                sqlUpdate = "UPDATE covid SET Price ={} WHERE SNO ={}".format(Price,SNO)
         
                                    # Execute query and commit changes.
                                cur.execute(sqlUpdate)
                                con.commit()
                                    # Confirm successful updating of person information.
                                print("Information updated successfully.")
                                sql_select_Query = "select * from covid"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Test_Name', 'Centre_Name', 'Location','Days','Time','Price'], tablefmt="fancy_grid"))



                            elif choice == 2:
                                sql_select_Query = "select * from vaccine"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Vaccine_Name', 'Centre_Name', 'Location','Date_of_availablity','Time_of_slot','Price'], tablefmt="fancy_grid"))
                                print("Which SNO's Price do you want to update? ")
                                SNO = int(input("Enter the SNO value: "))
                                Price = int(input("Enter the price value: "))
                                sqlUpdate = "UPDATE vaccine SET Price ={} WHERE SNO ={}".format(Price,SNO)                  
                                    
                                    # Execute query and commit changes.
                                cur.execute(sqlUpdate)
                                con.commit()
                                # Confirm successful updating of person information.
                                print("Information updated successfully.")
                                sql_select_Query = "select * from vaccine"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Vaccine_Name', 'Centre_Name', 'Location','Date_of_availablity','Time_of_slot','Price'], tablefmt="fancy_grid"))


                            elif choice == 3:
                                sql_select_Query = "select * from doctor"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Doctors_Name', 'Clinic_Name', 'Location','Contact_Number','Email_id'], tablefmt="fancy_grid"))
                                SNO = int(input("Enter the SNO whose number you want to update? "))
                                Contact_Number = int(input("Enter the Contact Number: "))
                                sqlUpdate = "UPDATE doctor SET Contact_Number ={} WHERE SNO ={}".format(Contact_Number,SNO)
                                    # Execute query and commit changes.
                                cur.execute(sqlUpdate)
                                con.commit()
                                # Confirm successful updating of person information.
                                print("Information updated successfully.")
                                sql_select_Query = "select * from doctor"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Doctors_Name', 'Clinic_Name', 'Location','Contact_Number','Email_id'], tablefmt="fancy_grid"))                                                        
                            elif choice == 4:
                                break
                            else:
                                print("Wrong Choice")
                            print("-----------------------------------------------------------------------------------------------")
                            print("-----------------------------------------------------------------------------------------------")
                            print("\n\n\n\n\n")


                    elif choice == 3:
                        while True:
                            print("In which table you want to delete values")
                            print("1.Covid Test")
                            print("2.Vaccine Allotment")
                            print("3.Doctor Appointment")
                            print("4.Schedule")
                            print("5.User")
                            print("6.Back")
                            choice = int(input("Enter your choice:"))

                            if choice == 1:
                                sql_select_Query = "select * from covid"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Test_Name', 'Centre_Name', 'Location','Days','Time','Price'], tablefmt="fancy_grid"))
                                SNO=int(input("Enter the SNO you want to delete: "))

                                sql = "DELETE FROM covid WHERE SNO = %s"
                                adr = (SNO,)

                                cur.execute(sql, adr)
                                con.commit()
                            # Confirm successful updating of person information.
                                print("Information updated successfully.")
                                sql_select_Query = "select * from covid"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Test_Name', 'Centre_Name', 'Location','Days','Time','Price'], tablefmt="fancy_grid"))

                            elif choice == 2:
                                sql_select_Query = "select * from vaccine"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Vaccine_Name', 'Centre_Name', 'Location','Date_of_availablity','Time_of_slot','Price'], tablefmt="fancy_grid"))

                                print("Which SNO do you want to delete? ")
                                SNO = int(input("Enter the SNO: "))
                                sql = "DELETE FROM vaccine WHERE SNO = %s"
                                adr = (SNO,)

                                cur.execute(sql, adr)
                                con.commit()
                                # Confirm successful updating of person information.
                                print("Information updated successfully.")
                                sql_select_Query = "select * from vaccine"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Vaccine_Name', 'Centre_Name', 'Location','Date_of_availablity','Time_of_slot','Price'], tablefmt="fancy_grid"))


                            elif choice == 3:
                                sql_select_Query = "select * from doctor"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Doctors_Name', 'Clinic_Name', 'Location','Contact_Number','Email_id'], tablefmt="fancy_grid"))
                                print("Which SNO do you want to delete? ")
                                SNO = int(input("Enter the SNo you want to delete: "))
                                sql = "DELETE FROM doctor WHERE SNO = %s"
                                adr = (SNO,)

                                cur.execute(sql, adr)
                                con.commit()
                                # Confirm successful updating of person information.
                                print("Information updated successfully.")
                                sql_select_Query = "select * from doctor"
                                cur.execute(sql_select_Query)
                                print (tabulate (cur.fetchall(), headers=['SNO', 'Doctors_Name', 'Clinic_Name', 'Location','Contact_Number','Email_id'], tablefmt="fancy_grid"))
                                
                            elif choice==4:                            
                                print("Which user slot would you like to remove")
                                cur.execute('select * from slots')
                                print (tabulate (cur.fetchall(), headers=['Username','Covidtest_Slot','Vaccine_slot','Doctor_appointment'], tablefmt="fancy_grid"))
                                username=input("Enter your username: ")
                                query="select * from slots where Username='{}'".format(username)
                                cur.execute(query)
                                
                                if cur.fetchone() == None:
                                    print("Username Not Found")
                                else:
                                    while True:
                                        print("Which Slot would you like to remove")
                                        print("1.Covid Test")
                                        print("2.Vaccine Allotment")
                                        print("3.Doctor Appointment")
                                        print("4.Back")
                                        choice1=int(input("Enter value: "))
                                        if choice1 == 1:
                                            query1="update slots set Covidtest_slot=Null where username='{}'".format(username)
                                            cur.execute(query1)
                                            con.commit()
                                            cur.execute('select * from slots')
                                            print (tabulate (cur.fetchall(), headers=['Username','Covidtest_Slot','Vaccine_slot','Doctor_appointment'], tablefmt="fancy_grid"))
                                            
                                            print("Slot updated successfully!")
                                        elif choice1 == 2:
                                            query1="update slots set Vaccine_slot=Null where username='{}'".format(username)
                                            cur.execute(query1)
                                            con.commit()
                                            cur.execute('select * from slots')
                                            print (tabulate (cur.fetchall(), headers=['Username','Covidtest_Slot','Vaccine_slot','Doctor_appointment'], tablefmt="fancy_grid"))
                                            print("Slot updated successfully!")
                                        elif choice1 == 3:
                                            query1="update slots set Doctor_appointment=Null where username='{}'".format(username)
                                            cur.execute(query1)
                                            con.commit()
                                            cur.execute('select * from slots')
                                            print (tabulate (cur.fetchall(), headers=['Username','Covidtest_Slot','Vaccine_slot','Doctor_appointment'], tablefmt="fancy_grid"))
                                            print("Slot updated successfully!")
                                        elif choice1 == 4:
                                            break
                                        else:
                                            print("Enter Correct values")
                                        
                        
                                
                            elif choice==5:
                                print("Which user slot would you like to remove")
                                cur.execute('select * from slots')
                                print (tabulate (cur.fetchall(), headers=['Username','Covidtest_Slot','Vaccine_slot','Doctor_appointment'], tablefmt="fancy_grid"))
                                username=input("Enter your username: ")
                                query="select * from slots where Username='{}'".format(username)
                                cur.execute(query)
                                if cur.fetchone() == None:
                                    print("Username Not Found")
                                else:
                                    query="DELETE FROM slots WHERE Username='{}'".format(username)
                                    cur.execute(query)
                                    con.commit()
                                    cur.execute('select * from slots')
                                    print (tabulate (cur.fetchall(), headers=['Username','Covidtest_Slot','Vaccine_slot','Doctor_appointment'], tablefmt="fancy_grid"))
                                    print("User removed successfully!")
                                                                                                                
                            elif choice==6:
                                break
                            else:
                                print("Wrong Choice")
                                        

                    elif choice == 4:
                        while True:
                                print("In which table you want to add slots")
                                print("1.Covid Test ")
                                print("2.Vaccine Allotment ")
                                print("3.Doctor Appointment")
                                print("4.Back")
                                choice1=int(input("Enter your Choice: "))
                                if choice1 == 1:
                                    cur.execute('select * from Covid')
                                    print (tabulate (cur.fetchall(), headers=['SNO', 'Test_Name', 'Centre_Name', 'Location','Days','Time','Price'], tablefmt="fancy_grid"))
                                    sno=int(input("Enter the Sno of new row: "))
                                    query="select * from Covid where SNO= '{}'".format(sno)
                                    cur.execute(query)
                                    if cur.fetchone() == None:
                                        testname=input("Enter Covid Test Name: ")
                                        cntrname=input("Enter Centre Name: ")
                                        location=input("Enter Location: ")
                                        days=input("Enter open days: ")
                                        time=input("Enter time slot: ")
                                        price=input("Enter Test price: ")
                                        query="insert into covid(SNO,Test_Name,Centre_Name,Location,Days,Time,Price)values({},'{}','{}','{}','{}','{}',{})".format(sno,testname,cntrname,location,days,time,price)
                                        cur.execute(query)
                                        con.commit()
                                        print("Slot added successfully!")
                                    else:
                                        print("SNO already exists")
                                elif choice1 == 2:
                                    cur.execute('select * from Vaccine')
                                    print (tabulate (cur.fetchall(), headers=['SNO', 'Vaccine_Name', 'Centre_Name', 'Location','Date_of_availablity','Time_of_slot','Price'], tablefmt="fancy_grid"))
                                    sno=int(input("Enter the Sno of new row: "))
                                    query="select * from vaccine where SNO= '{}'".format(sno)
                                    cur.execute(query)
                                    if cur.fetchone() == None:
                                        vacname=input("Enter Vaccine Test Name: ")
                                        cntrname=input("Enter Centre Name: ")
                                        location=input("Enter Location: ")
                                        days=input("Enter open days: ")
                                        time=input("Enter time slot: ")
                                        price=input("Enter Test price: ")
                                        query="insert into vaccine(SNO,Vaccine_Name,Centre_Name,Location,Date_of_availablity,Time_of_slot,Price)values({},'{}','{}','{}','{}','{}',{})".format(sno,vacname,cntrname,location,days,time,price)
                                        cur.execute(query)
                                        con.commit()
                                        print("Slot added successfully!")
                                    else:
                                        print("SNO already exists")
                                elif choice1 == 3:
                                    cur.execute('select * from Doctor')
                                    print (tabulate (cur.fetchall(), headers=['SNO', 'Doctors_Name', 'Clinic_Name', 'Location','Contact_Number','Email_id'], tablefmt="fancy_grid"))
                                    sno=int(input("Enter the Sno of new row: "))
                                    query="select * from doctor where SNO= '{}'".format(sno)
                                    cur.execute(query)
                                    if cur.fetchone() == None:
                                        docname=input("Enter Doctor Name: ")
                                        cntrname=input("Enter Centre Name: ")
                                        location=input("Enter Location: ")
                                        contact=input("Enter contact number: ")
                                        email=input("Enter Email id: ")
                                        query="insert into doctor(SNO,Doctors_Name,Clinic_Name,Location,Contact_Number,Email_id)values({},'{}','{}','{}','{}','{}')".format(sno,docname,cntrname,location,contact,email)
                                        cur.execute(query)
                                        con.commit()
                                        print("Slot added successfully!")
                                    else:
                                        print("SNO already exists")
                                elif choice1 == 4:
                                    break
                                else:
                                    print("Enter correct values")
                                        
                                        
                        
                    elif choice == 5:
                        break
                    else:
                        print("Wrong Choice")
                        print("-----------------------------------------------------------------------------------------------")
                        print("-----------------------------------------------------------------------------------------------")
                        print("\n\n\n\n\n")

                
        else:
            print("Enter values 1 or 2")
    
    elif accorlog =="3":
        flag=False
        
    else:
        print("Enter values 1 or 2 or 3")


    

