import requests
import time

print(" BABY SUBDOMAIN FINDER ")
print("=" * 30)

domain = input("Enter domain (like example.com): ")

# Bigger wordlist!
subs = ["www", "mail", "ftp", "admin", "test", "dev", "backup", 
        "api", "blog", "shop", "secure", "support", "webmail",
        "ns1", "ns2", "smtp", "pop", "imap", "vpn", "remote",
        "cloud", "apps", "internal", "staging", "demo", "sandbox"]

print(f"\n Looking for {len(subs)} secret doors...\n")

found = []
for sub in subs:
    # Try HTTPS first, then HTTP
    for protocol in ["https", "http"]:
        url = f"{protocol}://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code < 400:
                print(f" FOUND: {url} (Status: {response.status_code})")
                found.append(url)
                break  # Stop trying protocols once found
            elif response.status_code == 403:
                print(f" FORBIDDEN: {url} (Secret stuff!)")
                found.append(url)
                break
        except:
            pass  # Try next protocol or subdomain
    
    time.sleep(0.1)  # Be nice to the server

print(f"\n Found {len(found)} subdomains!")

# Save to file
if found:
    with open("subdomains.txt", "w") as f:
        for sub in found:
            f.write(sub + "\n")
    print(f" Saved to subdomains.txt")
