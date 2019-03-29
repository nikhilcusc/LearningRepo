def hashval(key):
    return key%10

def insert(table,key,val):
    table[hashval(key)].append(val)

table1 = [[] for _ in range(10)]

insert(table1,15,'dog')
insert(table1,125,'cat')
insert(table1,1453,'zebra')
insert(table1,1532,'adavark')

print(table1)