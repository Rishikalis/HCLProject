import mysql.connector as driver
import sys
import os
def menu():
    os.system('cls')
    while True:
        print("........MENU.......")
        print("1. ADMIN")
        print("2. EMPLOYEE")
        print("3. EXIT")
        print()
        print()
        choice=int(input("Enter your option (1-3) : "))
        if(choice==1):
            admin_menu()
        elif(choice==2):
            employee_access_menu()
        elif(choice==3):
             sys.exit()
        else:
            print("Wrong Choice.")
            menu()
 
def admin_menu():
    os.system('cls')
    while True:
        print("........ADMIN MENU.......")
        print("1. Database, table creation")
        print("2. DEPARTMENT") 
        print("3. ROLES")
        print("4. EMPLOYEE")
        print("5. LEAVE DETAIL")
        print("6. SALARY")
        print("7. PRINTOUT-VIEW")
        print("8. MODIFICATION - DEPARTMENT")
        print("9. MODIFICATION - ROLES")
        print("10. MODIFICATION - EMPLOYEE")
        print("11. MODIFICATION - SALARY")
        print("12. EXIT")
        print()
        print()
        choice=int(input("Enter your option (1-12) : "))
        if(choice==1):
            db_table_creation_menu()
        elif(choice==2):   
            department_menu()
        elif(choice==3):
            roles_menu()
        elif(choice==4):
            employee_menu()
        elif(choice==5):
            leave_menu()
        elif(choice==6):
            salary_menu()
        elif(choice==7):
            view_menu()
        elif(choice==8):
            mod_department_menu()
        elif(choice==9):
            mod_roles_menu()
        elif(choice==10):
            mod_employee_menu()
        elif(choice==11):
            mod_salary_menu()
        elif(choice==12):    
             sys.exit()
        else:
            print("Invalid option")
            menu()
 

def db_table_creation_menu():
    os.system('cls')
    try:
        con = driver.connect(host='localhost',user='root', passwd='Rocker12#', charset='utf8')
        if con.is_connected():
            cur=con.cursor()
            cur.execute('create database if not exists employee')
            print()
            con.close()
    except driver.Error as err:
        print("Error : ", err)

    try:
        con = driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur = con.cursor()
            cur.execute ('create table if not exists department(deptid integer primary key,deptname varchar(15))')
            print()
            con.close()
    except driver.Error as err:
        print("Error : ", err)

    try:
        con = driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            cur.execute('create table if not exists roles(roleid integer primary key, rolename varchar(15))')
            print()
            con.close()
    except driver.Error as err:
        print("Error : ", err)

    try:
        con = driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            cur.execute('create table if not exists empldetl(empid integer primary key, empname varchar(15), salary float, deptid integer, roleid integer, doj date)')
            print()
            con.close()
    except driver.Error as err:
        print("Error : ", err)

    try:
        con = driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            cur.execute('create table if not exists saldetl(empid integer primary key, salary float, attn integer, lop integer, mon integer, yea integer)')
            print()
            con.close()
    except driver.Error as err:
        print("Error : ", err)

    try:
        con = driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            cur.execute('create table if not exists lvdetl(empid integer, lvaccu float, lvavail float, mon integer, yea integer, lvdate date, lop date)')
            print()
            con.close()
    except driver.Error as err:
        print("Error : ", err)


def department_menu():
    os.system('cls')
    try:
        con = driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            ID=int(input("ENTER DEPARTMENT ID : "))
            NAME=input("ENTER DEPARTMENT NAME : ")
            query1="INSERT INTO department(deptid,deptname) VALUES({},'{}')".format(ID,NAME)
            cur.execute(query1)
            con.commit()
            print('Department Added')
            con.close()
    except driver.Error as err:
        print("Error : ", err)

def roles_menu():
    os.system('cls')
    try:
        con=driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            ID=int(input("ENTER ROLE ID : "))
            NAME=input("ENTER ROLE NAME : ")
            query1="INSERT INTO roles (roleid,rolename) VALUES({},'{}')".format(ID,NAME)
            cur.execute(query1)
            con.commit()
            print('Role Added')
            con.close()
    except driver.Error as err:
        print("Error : ", err)

def employee_menu():
    os.system('cls')
    try:
        con=driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            DID=int(input("ENTER DEPARTMENT CODE : "))
            RID=int(input("ENTER ROLE ID : "))
            ID=int(input("ENTER EMPLOYEE ID : "))
            NAME=input("ENTER EMPLOYEE NAME : ")
            SALARY=float(input("ENTER EMPLOYEE SALARY : "))
            DO=input("ENTER DATE OF JOINING : ")
            query1="INSERT INTO empldetl (empid,empname,salary,deptid,roleid,doj) VALUES({},'{}',{},{},{},'{}')".format(ID,NAME,SALARY,DID,RID,DO)
            cur.execute(query1)
            con.commit()
            print('Employee Added')
            con.close()
    except driver.Error as err:
        print("Error : ", err)

def leave_menu():
    os.system('cls')
    try:
        con=driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            ID=int(input("ENTER EMPLOYEE ID : "))
            MO=int(input("ENTER MONTH : "))
            YE=int(input("ENTER YEAR : "))
            LVAC=int(input("ENTER LEAVE ACCUMULATE "))
            LVAV=int(input("ENTER LEAVE AVAILED "))
            query1="INSERT INTO lvdetl (empid,lvaccu,lvavail,mon,yea) VALUES({},{},{},{},{})".format(ID,LVAC,LVAV,MO,YE)
            cur.execute(query1)
            con.commit()
            print('Leave detail Added')
            con.close()
    except driver.Error as err:
        print("Error : ", err)

def salary_menu():
    os.system('cls')
    try:
        con=driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            ID=int(input("ENTER EMPLOYEE ID : "))
            MO=int(input("ENTER MONTH : "))
            YE=int(input("ENTER YEAR : "))
            ATT=int(input("ENTER ATTENDANCE : "))
            LP=int(input("ENTER LOP(If any) : "))
            if(YE/4 == 0 and MO == 2):
                NOD = 29
            elif(YE/4 > 0 and MO == 2):
                NOD = 28
            elif(MO == 1 or MO == 3 or MO == 5 or MO == 7 or MO == 8 or MO == 10 or MO == 12):
                NOD = 31
            elif(MO == 4 or MO == 6 or MO == 9 or MO == 11):
                 NOD = 30
            query1="INSERT INTO saldetl (empid,attn,lop,mon,yea,nody) VALUES({},{},{},{},{},{})".format(ID,ATT,LP,MO,YE,NOD)
            cur.execute(query1)
            con.commit()
            print('Salary Added')
            con.close()
    except driver.Error as err:
        print("Error : ", err)


def view_menu():
    os.system('cls')
    try:
        con=driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            MO=int(input("ENTER MONTH : "))
            YE=int(input("ENTER YEAR : "))
            if(MO==1):
                mont="January"
            elif(MO==2):
                mont="February"
            elif(MO==3):
                mont="March"
            elif(MO==4):
                mont="April"
            elif(MO==5):
                mont="May"
            elif(MO==6):
                mont="June"
            elif(MO==7):
                mont="July"
            elif(MO==8):
                mont="August"
            elif(MO==9):
                mont="September"
            elif(MO==10):
                mont="October"
            elif(MO==11):
                mont="November"
            elif(MO==12):
                mont="December"
            else:
                mont="Not a valid month"
             
            print("Salary for the month of ",mont,YE)
            cur.execute("select a.empid, b.empname, c.deptname, a.attn, round((b.salary/a.nody)*(a.attn-a.lop))salary from saldetl a, empldetl b, department c where (a.mon='%s' and a.yea='%s')and (a.empid=b.empid and b.deptid=c.deptid)" %(MO,YE))
            rec=cur.fetchall()
            count=cur.rowcount
            print("+-----------------------------------------------------------------+")
            print("+  Emp ID  |   Emp Name   | Department |  Attendance |  Salary    +")
            print("+-----------------------------------------------------------------+")
            for i in rec:
                print('|{0:^9} | {1:12} | {2:10} |{3:10}   | {4:10} |'.format(i[0],i[1],i[2],i[3],i[4])) 
                con.close()
            print("+-----------------------------------------------------------------+")
    except driver.Error as err:
        print("Error : ", err)


def employee_access_menu():
    os.system('cls')
    try:
        con=driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            MO=int(input("ENTER MONTH : "))
            YE=int(input("ENTER YEAR : "))
            EMP=int(input("ENTER EMPLOYEE ID: "))
            if(MO==1):
                mont="January"
            elif(MO==2):
                mont="February"
            elif(MO==3):
                mont="March"
            elif(MO==4):
                mont="April"
            elif(MO==5):
                mont="May"
            elif(MO==6):
                mont="June"
            elif(MO==7):
                mont="July"
            elif(MO==8):
                mont="August"
            elif(MO==9):
                mont="September"
            elif(MO==10):
                mont="October"
            elif(MO==11):
                mont="November"
            elif(MO==12):
                mont="December"
            else:
                mont="Not a valid month"
             
            print("Salary for the month of ",mont,YE)
            cur.execute("select a.empid, b.empname, c.deptname, a.attn, round((b.salary/a.nody)*(a.attn-a.lop))salary from saldetl a, empldetl b, department c where (a.mon='%s' and a.yea='%s')and (a.empid=b.empid and b.deptid=c.deptid) and a.empid=%s" %(MO,YE,EMP))
            rec=cur.fetchall()
            count=cur.rowcount
            print("+-----------------------------------------------------------------+")
            print("+  Emp ID  |   Emp Name   | Department |  Attendance |  Salary    +")
            print("+-----------------------------------------------------------------+")
            for i in rec:
                print('|{0:^9} | {1:12} | {2:10} |{3:10}   | {4:10} |'.format(i[0],i[1],i[2],i[3],i[4])) 
                con.close()
            print("+-----------------------------------------------------------------+")
    except driver.Error as err:
        print("Error : ", err)

def mod_department_menu():
    os.system('cls')
    try:
        con = driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        cur=con.cursor()
        ID=int(input("ENTER DEPARTMENT ID : "))
        NAME=input("ENTER DEPARTMENT NAME : ")
        query1=("update department set deptid=%s, deptname='%s' where deptid=%s") %(ID,NAME,ID)
        cur.execute(query1)
        con.commit()
        print('Department detail updated...')
        con.close()
    except driver.Error as err:
        print("Error : ", err)
    

def mod_roles_menu():
    os.system('cls')
    try:
        con=driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            ID=int(input("ENTER ROLE ID : "))
            NAME=input("ENTER ROLE NAME : ")
            query1=("update roles set roleid=%s, rolename='%s' where roleid=%s") %(ID,NAME,ID)
            cur.execute(query1)
            con.commit()
            print('Role detail updated...')
            con.close()
    except driver.Error as err:
        print("Error : ", err)


def mod_employee_menu():
    os.system('cls')
    try:
        con=driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            DID=int(input("ENTER DEPARTMENT CODE : "))
            RID=int(input("ENTER ROLE ID : "))
            ID=int(input("ENTER EMPLOYEE ID : "))
            NAME=input("ENTER EMPLOYEE NAME : ")
            SALARY=float(input("ENTER EMPLOYEE SALARY : "))
            DO=input("ENTER DATE OF JOINING : ")
            query1=("update empldetl set empid=%s, empname='%s', salary=%s, deptid=%s, roleid=%s, doj='%s' where empid=%s" ) %(ID,NAME,SALARY,DID,RID,DO,ID)
            cur.execute(query1)
            con.commit()
            print('Employee detail updated...')
            con.close()
    except driver.Error as err:
        print("Error : ", err)

        
def mod_leave_menu():
    os.system('cls')
    try:
        con=driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            ID=int(input("ENTER EMPLOYEE ID : "))
            MO=int(input("ENTER MONTH : "))
            YE=int(input("ENTER YEAR : "))
            LVAC=int(input("ENTER LEAVE ACCUMULATE "))
            LVAV=int(input("ENTER LEAVE AVAILED "))
            query1=("update lvdetl set lvaccu=%s, lvavail=%s where (empid=%s and mon=%s and yea=%s)") %(LVAC,LVAV,ID,MO,YE)
            cur.execute(query1)
            con.commit()
            print('Leave detail updated...')
            con.close()
    except driver.Error as err:
        print("Error : ", err)

def mod_salary_menu():
    os.system('cls')
    try:
        con=driver.connect(host='localhost',user='root',passwd='Rocker12#',charset='utf8',database='employee')
        if con.is_connected():
            cur=con.cursor()
            ID=int(input("ENTER EMPLOYEE ID : "))
            MO=int(input("ENTER MONTH : "))
            YE=int(input("ENTER YEAR : "))
            ATT=int(input("ENTER ATTENDANCE : "))
            LP=int(input("ENTER LOP(If any) : "))
            if(YE/4 == 0 and MO == 2):
                NOD = 29
            elif(YE/4 > 0 and MO == 2):
                NOD = 28
            elif(MO == 1 or MO == 3 or MO == 5 or MO == 7 or MO == 8 or MO == 10 or MO == 12):
                NOD = 31
            elif(MO == 4 or MO == 6 or MO == 9 or MO == 11):
                 NOD = 30
            query1=("update saldetl set attn=%s, lop=%s, nody=%s  where (empid=%s and mon=%s and yea=%s)") %(ATT,LP,NOD,ID,MO,YE)
            cur.execute(query1)
            con.commit()
            print('Salary detail updated...')
            con.close()
    except driver.Error as err:
        print("Error : ", err)


menu()
  
     
