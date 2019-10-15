from ldap3 import Server, Connection, ALL

# Change for your student id and password
studentID = ''
password = ''

server = Server('ss.wits.ac.za', get_info=ALL, use_ssl=True)

print(server)

conn = Connection(server, studentID + '@students.wits.ac.za', password)

print(conn.bind())
print(conn)
print(conn.result)

valid = conn.search('OU=Students,OU=Wits University,DC=ss,DC=WITS,DC=AC,DC=ZA', '(cn='+studentID+')')

print(valid)
print(conn.entries)