import mysql.connector
from sshtunnel import SSHTunnelForwarder
import pymysql

class MySQLInterface:

    def __init__(self, sshArgumentsDict):

        self.__myServer = SSHTunnelForwarder(
            ssh_address_or_host=(sshArgumentsDict['host'], int(sshArgumentsDict['port'])),
            ssh_username=sshArgumentsDict['username'],
            ssh_password=sshArgumentsDict['password'],
            remote_bind_address=(sshArgumentsDict['remote_bind_host'], int(sshArgumentsDict['remote_bind_port']))
        )

        self.__myServer.start()

    def closeLAMPConnection(self):
        self.__myServer.stop()
        self.__myServer.close()

    def __connect (self, mySQLArgumentsDict):

        myDB = pymysql.connect(
            host=mySQLArgumentsDict['host'],
            user=mySQLArgumentsDict['username'],
            passwd=mySQLArgumentsDict['password'],
            database=mySQLArgumentsDict['database'],
            port=self.__myServer.local_bind_port
        )

        return myDB


    def insert (self, mySQLArgumentsDict, tableName, valuesDict):

        try:

            self.__myServer.start()

            myDB = self.__connect(mySQLArgumentsDict)

            # get cursor which we'll use to perform mysql commands
            myCursor = myDB.cursor()

            # retrieve store column names for this table
            myCursor.execute("SHOW COLUMNS FROM " + tableName)
            columnNames = [column[0] for column in myCursor.fetchall()]

            # get list of values that we want to insert
            valuesList = []
            for columnName in columnNames:
                valuesList.append(valuesDict.get(columnName))

            # generate string of column names separated by comma (,)
            columnNamesString = ','.join(map(str, columnNames))

            # generate string of '%' characters separated by comma (,)
            tempValues = ['%s'] * len(columnNames)
            tempValuesString = ','.join(map(str, tempValues))

            # get and store insert command arguments
            sql = 'INSERT INTO ' + tableName + ' (' + columnNamesString + ') VALUES ' + '(' + tempValuesString + ')'
            val = tuple(valuesList)

            # execute insert statement
            myCursor.execute(sql, val)

            # save changes to the database
            myDB.commit()

            # close connections to server and database
            myDB.close()

        except EOFError as e:
            print(e)


    def select (self, tableName, mySQLArgumentsDict):

        try:

            # connect mysql database
            myDB = self.__connect(mySQLArgumentsDict)

            # get cursor which we'll use to
            myCursor = myDB.cursor()

            # get content of table and print each row
            myCursor.execute('SELECT * FROM ' + tableName)
            tableRows = myCursor.fetchall()

            # close connections to server
            myDB.close()

            # return table comtent
            return  tableRows

        except EOFError as e:
            print(e)

    def selectWhere (self, tableName, whereAttribute, whereValue, mySQLArgumentsDict):

        try:

            # connect to mysql database
            myDB = self.__connect(mySQLArgumentsDict)

            # get cursor which we'll use to
            myCursor = myDB.cursor()

            # build where sql statement
            sql = 'SELECT * FROM ' + tableName + ' WHERE ' + whereAttribute + ' = (%s)'

            # execute and fetch result
            myCursor.execute(sql, whereValue)
            tableRows = myCursor.fetchall()

            # close connections to database
            myDB.close()

            # return result
            return  tableRows

        except EOFError as e:
            print(e)


    def selectLike (self, tableName, likeAttribute, likeValue, mySQLArgumentsDict):

        try:

            # connect to mysql database
            myDB = self.__connect(mySQLArgumentsDict)

            # get cursor which we'll use to
            myCursor = myDB.cursor()

            # build sql select like statement
            sql = 'SELECT * FROM ' + tableName + ' WHERE ' + likeAttribute + ' LIKE (%s)'

            # execute and fetch
            myCursor.execute(sql, likeValue)
            tableRows = myCursor.fetchall()

            # close connections to database
            myDB.close()

            # return result
            return  tableRows

        except EOFError as e:
            print(e)


    def update(self, tableName, attributeToUpdate, updatedValue, whereAttribute, whereValue, mySQLArgumentDict):

        try:

            # connect to mysql database
            myDB = self.__connect(mySQLArgumentDict)

            # get cursor which we'll use to
            myCursor = myDB.cursor()

            # build sql select like statement
            sql = 'UPDATE ' + tableName + ' SET ' + attributeToUpdate + ' = (%s) ' \
                  + ' WHERE ' + whereAttribute + ' = (%s)'
            val = (updatedValue, whereValue)

            # execute and fetch
            myCursor.execute(sql, val)
            tableRows = myCursor.fetchall()

            # save changes
            myDB.commit()

            # close connections to database
            myDB.close()

        except EOFError as e:
            print(e)


    def delete(self, tableName, attribute, value, mySQLArgumentDict):

        try:

            # connect to mysql database
            myDB = self.__connect(mySQLArgumentDict)

            # get cursor which we'll use to
            myCursor = myDB.cursor()

            # build delete statement
            sql = 'DELETE FROM ' + tableName + ' WHERE ' + attribute + ' = (%s)'

            # execute delete statement
            myCursor.execute(sql, value)

            # save changes
            myDB.commit()

            # close connections to database
            myDB.close()


        except EOFError as e:
            print(e)




sshArgDict = dict()
sshArgDict['host'] = '146.141.21.92'
sshArgDict['username'] = 's1748323'
sshArgDict['password'] = 's1748323'
sshArgDict['port'] = '22'
sshArgDict['remote_bind_host'] = 'localhost'
sshArgDict['remote_bind_port'] = '3306'

mysqlArgDict = dict()
mysqlArgDict['host'] = 'localhost'
mysqlArgDict['username'] = 's1748323'
mysqlArgDict['password'] = 's1748323'
mysqlArgDict['database'] = 'd1748323'

test = MySQLInterface(sshArgumentsDict=sshArgDict)

# update test
test.update('PERSONAL_DETAILS', 'F_NAME', 'Awesome dude', 'F_NAME', 'Philip', mysqlArgDict)
res = test.select('PERSONAL_DETAILS', mysqlArgDict)
for x in res:
    print(x)

## delete test
# test.delete('PERSONAL_DETAILS', 'F_NAME', 'Zaeem', mysqlArgDict)
# res = test.select('PERSONAL_DETAILS', mysqlArgDict)
# for x in res:
#     print(x)
#
# test.closeLAMPConnection()

#
# ## select like test
# rows = test.selectLike('PERSONAL_DETAILS', 'PHONE_NUMBER', '%234%', mysqlArgDict)
# for x in rows:
#     print(rows)

# ## select where test
# rows = test.selectWhere('PERSONAL_DETAILS', 'L_NAME', '??', mysqlArgDict)
# for x in rows:
#     print(x)
#
# test.closeLAMPConnection()

## select test
# rows = test.select('PERSONAL_DETAILS', mysqlArgDict)
# for r in rows:
#     print(r)

## insertion test
# f_names = ['Philip', 'Simon', 'Robel', 'Mike', 'Zaeem']
# l_names = ['Phisher', 'Rosen', '?', '??', 'Asvat']
#
# for i in range(5):
#    myDict = dict()
#    myDict['PERSON_ID'] = i + 93838
#    myDict['F_NAME'] = f_names[i]
#    myDict['L_NAME'] = l_names[i]
#    myDict['EMAIL_ADDRESS'] = f_names[i] + l_names[i] + '@gmail.com'
#    myDict['PHONE_NUMBER'] = int(str(i) * 10)
#
#    test.insert(mysqlArgDict, 'PERSONAL_DETAILS', myDict)
#
#    print(5)

test.closeLAMPConnection()
