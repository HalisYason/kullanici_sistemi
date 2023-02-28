
from veritabani import *
import time

def print_menu():
    print("""
    - MAİN MENU - 
    ----------
    1- giriş
    2- kaydol
    3- hakkında
    4- kapat
    ----------
    """)


def login_menu(user):
    print(f""" 
        -- ACCOUNT MENU -- 
    -------------------------- 
    
   || {user[1]} |  {user[2]} |  {user[3]} ||

    1- bir kullanıcı arama
    2- tüm kullanıcıları yazdır
    3- hesabımı sil
    4- çıkış yap
    --------------------------
    """)


create_table()

while True:
    print_menu()
    secim = input("seçim = ")

    if secim == "1":
        time.sleep(.4)
        username = input("kullanıcı adı: ")
        password = input("şifre: ")
        search = search_username(username)

        if search == None:
            print("--- böyle bir kullanıcı yok ---")
            continue
        
        if password == search[4]:
            while  True:
                login_menu(search)
                secim = input("seçim: ")

                if secim =="1":
                    u = input("kullanıcı adı: ")
                    birisi = search_username(u)
                    if birisi ==None:
                        print("--- kullanıcı bulunamadı--- ")
                        continue
                    print(f"\n--> kullanıcı:  {birisi[1]} {birisi[2]} {birisi[3]}")
                    time.sleep(.5)

                if secim == "2":
                    print_all()
                if secim == "3":
                    print("- hesap silindi - ")
                    delete_account(username)
                if secim == "4":
                    time.sleep(.5)
                    break

    if secim =="2":
        time.sleep(.4)
        name = input("ad: ")
        lastname = input("soyad: ")
        username  = input("kullanıcı adı: ")
        password = input("şifre: ")

        search = search_username(username )
        if search != None:
            print("--- bu kullanıcı adı ile bir hesap var --- ")
            continue
        insert(name,lastname,username,password)
        print("kayıt başarılı :)")


    if secim == "3":
        print("""
        --------------

        -- developer: Halis Göller
        -- e-posta: gollerhls@gmail.com

        --------------
        
        """)
        input("  devam etmek için enter")
        time.sleep(.5)
        continue

    if secim == "4":
        print("çıkış yapılıyor")
        time.sleep(1.1)
        break

