import mysql.connector
from cryptography.fernet import Fernet


mydb = mysql.connector.connect(
  host="localhost",
  user="fathur",
  password="fathur123",
  database="data_alat"
)


# key = #Fernet.generate_key()

# with open('Andi.key','wb') as kuncinya:
#     kuncinya.write(key)


with open('Andi.key','rb') as kunci_nya:
    key = kunci_nya.read()

print(key)


# Enkripsi data
f = Fernet(key)

with open('Andi.csv','rb') as file_asli:
    asli = file_asli.read()

enkripsi = f.encrypt(asli)

with open('en_Andi.csv','wb') as file_enkripsi:
    file_enkripsi.write(enkripsi)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Andi", enkripsi)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Data Telah ditambah")


# Dekript data
# f= Fernet(key)

with open('en_Andi.csv','rb') as file_terenkripsi:
    terenkripsi = file_terenkripsi.read()

terdekripsi = f.decrypt(terenkripsi)

with open('dec_Andi.csv','wb') as file_terdekripsi:
    file_terdekripsi.write(terdekripsi)