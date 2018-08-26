import mysql.connector as connector
import time, math

def connect():
    success = False
    try:
        connection = connector.connect(user='galenite', host='kennethmathis.ch', password='pnR(z*j(xp85Sqf(', port=3306, database='passwords')
        #print("Connection established and closed")
        success = True
    except connector.Error as err:
        if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied, wrong credentials?")
        elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
            print("Database not found!")
        else:
            print(err)
        #print("Unable to connect")

    if success:
        cur = connection.cursor()
        loop = True
        num_lines = 0
        failed = 0
        rList = open('rockyou.txt')
        while loop:
            if num_lines >= 2449398:
                loop = False
            try:
                print(str(round((num_lines/2449398)*100, 3)) + "% " + str(num_lines))
                #print(num_lines)
                line = rList.readline(num_lines)
                if line != '\n':
                    #print(line.replace('\n', ''))
                    data_salary = {'theLine': line.replace('\n', '')}
                    cur.execute("INSERT INTO rockyou (pass) VALUES (%(theLine)s)", data_salary)
                    if num_lines % 100 == 0:
                        connection.commit()
                    #time.sleep(0.1)
                    num_lines += 1
            except:
            #    print("fail")
                failed += 1
        print("failed: {0}".format(failed))
        connection.commit()
        rList.close()
        cur.close()
        connection.close()

connect()
        

