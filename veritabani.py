
import sqlite3 as sql
import time
import os


#tablo oluşturma
def create_table():
    dosya = "ders.db"
    y_dosya = os.path.exists(dosya)
    if y_dosya:
        vt = sql.connect("ders.db")
        print("veritabanına bağlandı")
    else:
        vt = sql.connect("ders.db")
        print("veritabanı oluşturuldu...")


    cursor = vt.cursor()

    cursor.execute("""create table if not exists users(
    id intager PRİMARY KEY,
    name text,
    lastname text,
    username text,
    password text

    )""")
    vt.commit()
    vt.close()


# kullanıcı ekleme
def insert(name,lastname,username,password):
    vt = sql.connect("ders.db")
    cursor = vt.cursor()

    add_command = """ insert into users(name,lastname,username,password) values {} """
    data = (name,lastname,username,password)

    cursor.execute(add_command.format(data))

    vt.commit()
    vt.close()


# kullanıcıadı arama
def search_username(username):
    vt = sql.connect("ders.db")
    cursor = vt.cursor()

    src_command = "select * from users where username='{}' "
    cursor.execute(src_command.format(username))

    user = cursor.fetchone()

    vt.close()
    return user


# hepsini yazdırma
def print_all():
    vt = sql.connect("ders.db")
    cursor = vt.cursor()

    cursor.execute("select * from users")
    list_all = cursor.fetchall()
    for i in list_all:
        time.sleep(.6)
        print("\n")

        print(f"-- ad: {i[1]} soyad: {i[2]} kullanıcı adı: {i[3]} şifre: {i[4]} --")
        print("-"*30)


    vt.close()
 


# şifre güncelleme
def update_password(username,new_password):
    vt = sql.connect("ders.db")
    cursor = vt.cursor()

    upd_command = "update users set password '{}' where username='{}'"
    cursor.execute(upd_command.format(new_password,username))

    vt.commit()
    vt.close()



# hesap silme
def delete_account(username):
    vt = sql.connect("ders.db")
    cursor = vt.cursor()

    dlt_command = "delete from users where username='{}'"
    cursor.execute(dlt_command.format(username))

    vt.commit()
    vt.close()



# tablo silme
def delete_table():
    vt = sql.connect("ders.db")
    cursor = vt.cursor()

    cursor.execute("drop table users")

    vt.commit()
    vt.close()

