import requests

print("📂 BABY DIRECTORY FINDER 📂")
print("=" * 30)

url = input("Enter website (like https://example.com): ")

# Pretend to be Chrome browser!
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

folders = ["admin", "backup", "hidden", "secret", "test", 
           "images", "css", "js", "uploads", "tmp", "logs",
           "config", "database", "backup", "wordpress", "wp-admin",
           "cgi-bin", "phpmyadmin", "mysql", "old", "new", "temp"]

print(f"\n🔎 Knocking on {len(folders)} doors...\n")

found = []
for folder in folders:
    full_url = f"{url}/{folder}"
    try:
        # Add headers and shorter timeout
        response = requests.get(full_url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            print(f"🚪 OPEN: {full_url}")
            found.append(full_url)
        elif response.status_code == 403:
            print(f"🔒 FORBIDDEN: {full_url} (Secret stuff!)")
            found.append(full_url)
        elif response.status_code == 404:
            print(f"❌ Not found: {full_url}")
        else:
            print(f"🤔 {full_url} - {response.status_code}")
    except requests.exceptions.Timeout:
        print(f"⏰ {full_url} - Too slow, skipping...")
    except requests.exceptions.ConnectionError:
        print(f"💀 {full_url} - Can't connect!")
    except Exception as e:
        print(f"⚠️ {full_url} - Error: {str(e)[:30]}")

print(f"\n🎯 Found {len(found)} interesting doors!")

if found:
    with open("directories.txt", "w") as f:
        for item in found:
            f.write(item + "\n")
    print(f"💾 Saved to directories.txt")
