import requests
import re
from bs4 import BeautifulSoup
from email_validator import validate_email, EmailNotValidError
import dns.resolver
import speedtest
import socket

def logo():
    print("""
('-.                                 .-') _        (`\ .-') /`        .-') _    ('-. .-.     .-. .-')                             .-')    
           ( OO ).-.                            ( OO ) )        `.( OO ),'       (  OO) )  ( OO )  /     \  ( OO )                           ( OO ).  
   ,------./ . --. /  ,----.    ,--. ,--.   ,--./ ,--,'      ,--./  .--.  ,-.-') /     '._ ,--. ,--.      ;-----.\  ,--. ,--.     ,----.    (_)---\_) 
('-| _.---'| \-.  \  '  .-./-') |  | |  |   |   \ |  |\      |      |  |  |  |OO)|'--...__)|  | |  |      | .-.  |  |  | |  |    '  .-./-') /    _ |  
(OO|(_\  .-'-'  |  | |  |_( O- )|  | | .-') |    \|  | )     |  |   |  |, |  |  \'--.  .--'|   .|  |      | '-' /_) |  | | .-')  |  |_( O- )\  \:` `.  
/  |  '--.\| |_.'  | |  | .--, \|  |_|( OO )|  .     |/      |  |.'.|  |_)|  |(_/   |  |   |       |      | .-. `.  |  |_|( OO ) |  | .--, \ '..`''.) 
\_)|  .--' |  .-.  |(|  | '. (_/|  | | `-' /|  |\    |       |         | ,|  |_.'   |  |   |  .-.  |      | '--'  /('  '-'(_.-'  |  '--'  | \       / 
  \|  |_)  |  | |  | |  '--'  |('  '-'(_.-' |  | \   |       '--'   '--'  `--'      `--'   `--' `--'      `------'   `-----'      `------'   `-----'  


     \033[1;92mFagun\033[0m 🐞 with \033[1;92mBugs\033[0m
    """)

def website_info():
    site = input("\033[1;92m[*] URL: \033[0m")
    response = requests.get(f"https://myip.ms/{site}")
    content = response.text

    # Use BeautifulSoup for HTML parsing
    soup = BeautifulSoup(content, 'html.parser')
    server_info = soup.find('div', {'class': 'server_info'})

    if server_info:
        print("\033[1;92m[*] Server Information:\033[0m\033[1;77m")
        print(server_info.text.strip())
        print("\033[0m")

    ip_location = re.search(r"IP Location:\s*([^<]+)", content)
    if ip_location:
        print(f"\033[1;92m[*] IP Location:\033[0m\033[1;77m {ip_location.group(1)}\033[0m")

    ip_range = re.search(r"IP Range.*?>([^<]+)", content)
    if ip_range:
        print(f"\033[1;92m[*] IP Range:\033[0m\033[1;77m {ip_range.group(1)}\033[0m")

    ip_reversedns = re.search(r"IP Reverse DNS.*?>\s*([^<]+)", content)
    if ip_reversedns:
        print(f"\033[1;92m[*] IP Reverse DNS:\033[0m\033[1;77m {ip_reversedns.group(1)}\033[0m")

    ipv6 = re.search(r"whois6.*?(\S+)'", content)
    if ipv6:
        print(f"\033[1;92m[*] IPv6:\033[0m\033[1;77m {ipv6.group(1)}\033[0m")

def phone_info():
    phone = input("\033[1;92m[*] Phone (e.g.: 14158586273): \033[0m")
    response = requests.get(f"https://apilayer.net/api/validate?access_key=43fc2577cf1cdb2eb522583eaee6ae8f&number={phone}&country_code=&format=1")
    data = response.json()

    if data.get("valid"):
        print("\033[1;92m[*] Phone Information:\033[0m")
        print(f"\033[1;92m[*] Country:\033[0m\033[1;77m {data.get('country_name')}\033[0m")
        print(f"\033[1;92m[*] Location:\033[0m\033[1;77m {data.get('location')}\033[0m")
        print(f"\033[1;92m[*] Carrier:\033[0m\033[1;77m {data.get('carrier')}\033[0m")
        print(f"\033[1;92m[*] Line Type:\033[0m\033[1;77m {data.get('line_type')}\033[0m")
    else:
        print("\033[1;93m[!] Invalid phone number!\033[0m")

def check_email():
    email = input("\033[1;92m[*] Email Address: \033[0m")
    try:
        mx = validate_email(email)
        print("\033[1;92m[*] Email Account Exists!\033[0m")
        print(f"\033[1;92m[*] Mail Server Information:\033[0m\033[1;77m {mx}\033[0m")
    except EmailNotValidError as e:
        print(f"\033[1;93m[!] Email Account Does Not Exist: {str(e)}\033[0m")


def my_info():
    print("\033[1;92m[*] Additional User Information:\033[0m\033;1m")
    print(f"IP Address: {socket.gethostbyname(socket.gethostname())}")
    print(f"Location: {get_user_location()}")
    print("\033[0m")

def check_dns():
    domain = input("\033[1;92m[*] Domain: \033[0m")
    try:
        record_type = input("\033[1;92m[*] DNS Record Type (A, MX, CNAME, NS, etc.): \033[0m").upper()
        answers = dns.resolver.resolve(domain, record_type)
        for answer in answers:
            print(f"\033[1;92m[*] DNS Record ({record_type}):\033[0m\033[1;77m {answer}\033[0m")
    except dns.resolver.NXDOMAIN:
        print("\033[1;93m[!] Domain not found in DNS.\033[0m")

def check_dns_leak():
    print("\033[1;92m[*] Performing DNS Leak Test...\033[0m")
    # Implement DNS leak test logic here

def internet_speed_test():
    st = speedtest.Speedtest()
    download_speed = st.download()
    upload_speed = st.upload()
    latency = st.results.ping

    print(f"\033[1;92m[*] Download Speed:\033[0m\033[1;77m {download_speed / 1_000_000:.2f} Mbps\033[0m")
    print(f"\033[1;92m[*] Upload Speed:\033[0m\033[1;77m {upload_speed / 1_000_000:.2f} Mbps\033[0m")
    print(f"\033[1;92m[*] Latency:\033[0m\033[1;77m {latency} ms\033[0m")
    print("\033[0m")

def find_ip_behind_cloudflare():
    print("\033[1;92m[*] Finding IP Behind Cloudflare...\033[0m")
    # Implement advanced Cloudflare IP resolution logic here

def get_user_location():
    # Implement a method to get the user's location
    return "Unknown"

def check_whois():
    # Implement the functionality of the check_whois function
    pass  # Placeholder for implementation

def main():
    while True:
        logo()
        print("\n\033[1;91m[*] Choose an option:\033[0m")
        print("\033[1;92m[\033[0m\033[1;77m1\033[0m\033[1;92m]\033[1;93m Website Info\033[0m          \033[1;92m[\033[0m\033[1;77m7\033[0m\033[1;92m]\033[1;93m Check DNS Leak\033[0m")
        print("\033[1;92m[\033[0m\033[1;77m2\033[0m\033[1;92m]\033[1;93m Phone Info\033[0m            \033[1;92m[\033[0m\033[1;77m8\033[0m\033[1;92m]\033[1;93m Internet Speed test\033[0m")
        print("\033[1;92m[\033[0m\033[1;77m3\033[0m\033[1;92m]\033[1;93m Check E-mail\033[0m          \033[1;92m[\033[0m\033[1;77m9\033[0m\033[1;92m]\033[1;93m Find IP behind Cloudflare\033[0m")
        print("\033[1;92m[\033[0m\033[1;77m4\033[0m\033[1;92m]\033[1;93m My Info\033[0m               \033[1;92m[\033[0m\033[1;77m10\033[0m\033[1;92m]\033[1;93m Exit\033[0m")
        print("\033[1;92m[\033[0m\033[1;77m5\033[0m\033[1;92m]\033[1;93m Check Whois\033[0m")
        print("\033[1;92m[\033[0m\033[1;77m6\033[0m\033[1;92m]\033[1;93m Check DNS\033[0m")

        choice = input("\n\033[1;92m[*] Enter your choice:\033[0m ")

        if choice == "1":
            website_info()
        elif choice == "2":
            phone_info()
        elif choice == "3":
            check_email()
        elif choice == "4":
            my_info()
        elif choice == "5":
            check_whois()
        elif choice == "6":
            check_dns()
        elif choice == "7":
            check_dns_leak()
        elif choice == "8":
            internet_speed_test()
        elif choice == "9":
            find_ip_behind_cloudflare()
        elif choice == "10":
            print("\033[1;92m[*] Exiting. Goodbye!\033[0m")
            break
        else:
            print("\033[1;91m[!] Invalid choice. Please choose a valid option.\033[0m")

if __name__ == "__main__":
    main()
