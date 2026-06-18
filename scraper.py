import requests
from bs4 import BeautifulSoup

print("🌐 BABY WEB SCRAPER 🌐")
print("=" * 40)

# Get website from user
url = input("Enter website URL (like https://example.com): ")

# Pretend to be a real browser (so websites don't block us!)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

print("\n📡 Connecting to website...")

# Ask the website nicely
response = requests.get(url, headers=headers, timeout=10)
soup = BeautifulSoup(response.text, 'html.parser')

print("✅ Connected!\n")
print("=" * 40)

# 1. Get the page title
print(f"📄 PAGE TITLE: {soup.title.text}")
print("=" * 40)

# 2. Find all headings (h1, h2, h3)
headings = soup.find_all(['h1', 'h2', 'h3'])
print(f"\n📝 HEADINGS FOUND: {len(headings)}")
for h in headings[:5]:  # Show first 5
    print(f"  - {h.text.strip()}")

# 3. Find all links
links = soup.find_all('a')
print(f"\n🔗 LINKS FOUND: {len(links)}")
print("  First 5 links:")
for link in links[:5]:
    href = link.get('href', 'No link')
    text = link.text.strip()[:30]  # Show first 30 characters
    print(f"  - {text} → {href}")

# 4. Find all paragraphs
paras = soup.find_all('p')
print(f"\n📖 PARAGRAPHS FOUND: {len(paras)}")
print("  First 3 paragraphs (first 100 chars):")
for p in paras[:3]:
    text = p.text.strip()[:100]
    print(f"  {text}...")

# 5. Find all images
images = soup.find_all('img')
print(f"\n🖼️ IMAGES FOUND: {len(images)}")
print("  First 3 images:")
for img in images[:3]:
    src = img.get('src', 'No src')
    alt = img.get('alt', 'No alt text')
    print(f"  - {src} ({alt})")

# Save everything to a file
with open("scraped_data.txt", "w") as f:
    f.write(f"Website: {url}\n")
    f.write(f"Title: {soup.title.text}\n")
    f.write(f"Headings found: {len(headings)}\n")
    f.write(f"Links found: {len(links)}\n")
    f.write(f"Paragraphs found: {len(paras)}\n")
    f.write(f"Images found: {len(images)}\n")

print("\n💾 Saved to scraped_data.txt")
print("\n🎉 DONE! You're a web scraper now!")
# Save all links to a file
with open("all_links.txt", "w") as f:
    for link in links:
        href = link.get('href', '')
        if href and not href.startswith('#'):  # Skip empty links
            f.write(href + "\n")
print("💾 Saved all links to all_links.txt")
