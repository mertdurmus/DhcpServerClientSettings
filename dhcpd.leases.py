# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:17:03 2020

@author: elifaskvav
"""

import datetime, bisect
import hashlib
import time
import mysql.connector



def parse_timestamp(raw_str):
        tokens = raw_str.split()

        if len(tokens) == 1:
                if tokens[0].lower() == 'never':
                        return 'never';

                else:
                        raise Exception('Parse error in timestamp')

        elif len(tokens) == 3:
                return datetime.datetime.strptime(' '.join(tokens[1:]),
                        '%Y/%m/%d %H:%M:%S')

        else:
                raise Exception('Parse error in timestamp')




def parse_hardware(raw_str):
        tokens = raw_str.split()

        if len(tokens) == 2:
                return tokens[1]

        else:
                raise Exception('Parse error in hardware')


def strip_endquotes(raw_str):
        return raw_str.strip('"')


def identity(raw_str):
        return raw_str


def parse_binding_state(raw_str):
        tokens = raw_str.split()

        if len(tokens) == 2:
                return tokens[1]

        else:
                raise Exception('Parse error in binding state')


def parse_next_binding_state(raw_str):
        tokens = raw_str.split()

        if len(tokens) == 3:
                return tokens[2]

        else:
                raise Exception('Parse error in next binding state')


def parse_rewind_binding_state(raw_str):
        tokens = raw_str.split()

        if len(tokens) == 3:
                return tokens[2]

        else:
                raise Exception('Parse error in next binding state')


def parse_leases_file(leases_file):
        valid_keys = {
                'starts':               parse_timestamp,
                'ends':                 parse_timestamp,
                'tstp':                 parse_timestamp,
                'tsfp':                 parse_timestamp,
                'atsfp':                parse_timestamp,
                'cltt':                 parse_timestamp,
                'hardware':             parse_hardware,
                'binding':              parse_binding_state,
                'next':                 parse_next_binding_state,
                'rewind':               parse_rewind_binding_state,
                'uid':                  strip_endquotes,
                'client-hostname':      strip_endquotes,
                'option':               identity,
                'set':                  identity,
                'on':                   identity,
                'abandoned':            None,
                'bootp':                None,
                'reserved':             None,
                }

        leases_db = {}

        lease_rec = {}
        in_lease = False
        in_failover = False

        for line in leases_file:
                if line.lstrip().startswith('#'):
                        continue

                tokens = line.split()

                if len(tokens) == 0:
                        continue

                key = tokens[0].lower()

                if key == 'lease':
                        if not in_lease:
                                ip_address = tokens[1]

                                lease_rec = {'ip_address' : ip_address}
                                in_lease = True

                        else:
                                raise Exception('Parse error in leases file')

                elif key == 'failover':
                        in_failover = True
                elif key == '}':
                        if in_lease:
                                for k in valid_keys:
                                        if callable(valid_keys[k]):
                                                lease_rec[k] = lease_rec.get(k, '')
                                        else:
                                                lease_rec[k] = False

                                ip_address = lease_rec['ip_address']

                                if ip_address in leases_db:
                                        leases_db[ip_address].insert(0, lease_rec)

                                else:
                                        leases_db[ip_address] = [lease_rec]

                                lease_rec = {}
                                in_lease = False

                        elif in_failover:
                                in_failover = False
                                continue
                        else:
                                raise Exception('Parse error in leases file')

                elif key in valid_keys:
                        if in_lease:
                                value = line[(line.index(key) + len(key)):]
                                value = value.strip().rstrip(';').rstrip()

                                if callable(valid_keys[key]):
                                        lease_rec[key] = valid_keys[key](value)
                                else:
                                        lease_rec[key] = True

                        else:
                                raise Exception('Parse error in leases file')

                else:
                        if in_lease:
                                raise Exception('Parse error in leases file')

        if in_lease:
                raise Exception('Parse error in leases file')

        return leases_db


def ipv4_to_int(ipv4_addr):
        parts = ipv4_addr.split('.')
        return (int(parts[0]) << 24) + (int(parts[1]) << 16) + \
                (int(parts[2]) << 8) + int(parts[3])
                

def returnLeases(leases_db):
        retarray = []
        sortedarray = []

        for ip_address in leases_db:
                lease_rec = leases_db[ip_address][0]
                ip_as_int = ipv4_to_int(ip_address)
                insertpos = bisect.bisect(sortedarray, ip_as_int)
                sortedarray.insert(insertpos, ip_as_int)
                retarray.insert(insertpos, lease_rec)

        return retarray
    
    


##db conneciton
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="toor",
    database="DhcpServer"
)
##conneciton check
print(mydb)



##db existing record control
myfile = open('dhcpd.leases.txt', 'r')
leases = parse_leases_file(myfile)
myfile.close()
report_dataset = returnLeases(leases)
ipList = []
for lease in report_dataset:
    mycursor = mydb.cursor()
    sql = "INSERT INTO dhcpClients (ipAddress, startTime,endTime,Mac) VALUES (%s, %s,%s,%s)"
    val = (format(str(lease['ip_address'])), format(str(lease['starts'])), format(str(lease['ends'])),format(str(lease['hardware'])))
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    ipList.append(lease['ip_address'])



#old file 
hasher1 = hashlib.md5()
afile1 = open('dhcpd.leases.txt', 'rb')
buf1 = afile1.read()
a = hasher1.update(buf1)
md5_a=(str(hasher1.hexdigest()))

#always check in leases file
hasher2 = hashlib.md5()
afile2 = open('dhcpd.leases.txt', 'rb')
buf2 = afile2.read()
b = hasher2.update(buf2)
md5_b=(str(hasher2.hexdigest()))



while True:
    
    hasher2 = hashlib.md5()
    afile2 = open('dhcpd.leases.txt', 'rb')
    buf2 = afile2.read()
    b = hasher2.update(buf2)
    md5_b=(str(hasher2.hexdigest()))
    
    if(md5_a==md5_b):
        time.sleep(300)
    else:
        time.sleep(300)
        hasher1 = hashlib.md5()
        afile1 = open('dhcpd.leases.txt', 'rb')
        buf1 = afile1.read()
        a = hasher1.update(buf1)
        md5_a=(str(hasher1.hexdigest()))
        myfile = open('dhcpd.leases.txt', 'r')
        leases = parse_leases_file(myfile)
        myfile.close()
        report_dataset = returnLeases(leases)

        for lease in report_dataset:
            if lease['ip_address'] in ipList:
                continue
            else:       
                mycursor = mydb.cursor()
                sql = "INSERT INTO dhcpClients (ipAddress, startTime,endTime,Mac) VALUES (%s, %s,%s,%s)"
                val = (format(str(lease['ip_address'])), format(str(lease['starts'])), format(str(lease['ends'])),format(str(lease['hardware'])))
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                ipList.append(lease['ip_address'])
















