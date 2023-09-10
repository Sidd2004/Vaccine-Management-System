import mysql.connector
x=input("Enter Your MySQL password : ")
con=mysql.connector.connect(host='localhost',user='root',password=x)
if con.is_connected():
    print('Connection successful')

#creating database
cur=con.cursor()
cur.execute('create database project')
cur.execute('use project')
cur.execute("CREATE TABLE admacc (Admin_Code varchar(6) primary key,Name varchar(20) default 'Admin')")
cur.execute("insert into admacc values('980290','')")
con.commit()
cur.execute("insert into admacc values('248540','Shalini Verma')")
con.commit()
cur.execute("insert into admacc values('847240','Sakshi Mam')")
con.commit()
cur.execute("insert into admacc values('200005','Ansh Sharma')")
con.commit()
cur.execute("insert into admacc values('100007','Siddharth Gaur')")
con.commit()
cur.execute("create table accounts (Username varchar(50) primary key,Name varchar(50) NOT NULL,Number varchar(15) NOT NULL,DOB date NOT NULL,Gender varchar(1) default 'M',Password varchar(15) NOT NULL)")
cur.execute("create table slots (Username varchar(50), Covidtest_slot int default Null, Vaccine_slot int default Null, Doctor_appointment int default Null)")

#creating table vaccine
cur.execute("create table vaccine(SNO integer primary key,Vaccine_Name varchar(50) NOT NULL,Centre_Name varchar(20) NOT NULL,Location varchar(20),Date_of_availablity date, Time_of_slot varchar(10) NOT NULL,Price integer)")

#inserting values into vaccine
cur.execute("insert into vaccine values(01,'Vaccine Alpha (dose 1)','centre A','Rohini','2022-03-12','10-11 AM',1200)")
con.commit()
cur.execute("insert into vaccine values(02,'Vaccine Alpha (dose 2)','centre B','Pitampura','2022-03-20','9-10 AM',1000)")
con.commit()
cur.execute("insert into vaccine values(03,'Vaccine Delta (dose 1)','centre A','Rohini','2022-03-15','12-02 PM',1400)")
con.commit()
cur.execute("insert into vaccine values(04,'Vaccine Delta (dose 1)','centre C','Mayapuri','2022-03-21','11-01 PM',00)")
con.commit()
cur.execute("insert into vaccine values(05,'Vaccine Alpha (dose 2)','centre C','Mayapuri','2022-03-13','12-01 PM',00)")
con.commit()
cur.execute("insert into vaccine values(06,'Vaccine Delta (dose 2)','centre B','Pitampura','2022-03-18','9-11 AM',1500)")
con.commit()

#creating table covid
cur.execute("create table covid(SNO integer primary key,Test_Name varchar(10) default 'Rapid',Centre_Name varchar(20) NOT NULL,Location varchar(20),Days varchar(20) NOT NULL, Time varchar(20),Price integer default 00)")

#inserting values into covid
cur.execute("insert into covid values(01,'Rapid','centre A','Rohini','MON-FRI','08-12 PM',1000)")
con.commit()
cur.execute("insert into covid values(02,'RT-PCR','centre A','Rohini','MON-FRI','12-04 PM',1500)")
con.commit()
cur.execute("insert into covid values(03,'Rapid','centre B','Pitampura','MON-SUN','08-10 AM',800)")
con.commit()
cur.execute("insert into covid values(04,'RT-PCR','centre B','Pitampura','MON-SUN','10-12 PM',1200)")
con.commit()
cur.execute("insert into covid values(05,'Rapid','centre C','Mayapuri','SAT-SUN','08-06 PM',00)")
con.commit()
cur.execute("insert into covid values(06,'RT-PCR','centre C','Mayapuri','SAT-SUN','08-06 PM',00)")
con.commit()

#creating table doctor
cur.execute("create table doctor(SNO integer primary key,Doctors_Name varchar(20) NOT NULL,Clinic_Name varchar(20) unique,Location varchar(20),Contact_Number varchar(15) unique,Email_id varchar(40) unique)")

#inserting values into doctor
cur.execute("insert into doctor values(01,'Dr. Arun Kumar','Arun Clinic','Model Town','9912346509','arunkumar@gmail.com')")
con.commit()
cur.execute("insert into doctor values(02,'Dr. Ankita Sharma','Ankita Clinic','Rohini','8910304678','asharma@hotmail.com')")
con.commit()
cur.execute("insert into doctor values(03,'Dr. Vijay Devgun','Vijay Clinic','Dwarka','7679980534','vijay@gmail.com')")
con.commit()
cur.execute("insert into doctor values(04,'Dr. Rajiv Bhatia','Rajiv Clinic','Saket','9099902005','rajivbhatia@yahoo.com')")
con.commit()
cur.execute("insert into doctor values(05,'Dr. Gayatri Verma','Gayatri Clinic','Pitampura','8907604321','g.verma@gmail.com')")
con.commit()
cur.execute("insert into doctor values(06,'Dr. Vikas Gupta','Vikas Clinic','Rajouri Garden','8899685417','vikasgupta1@gmail.com')")
con.commit()
print("\n\n\n")
print("Databases Created")

