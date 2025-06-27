# scrape_amazon_reviews_all_and_filtered.py

from google_play_scraper import Sort, reviews
import pandas as pd

# App: Amazon Shopping
app_package = 'com.amazon.mShop.android.shopping'
print(f"Fetching up to 1000 reviews for: {app_package}...")

try:
    result, _ = reviews(
        app_package,
        lang='en',
        country='us',
        sort=Sort.NEWEST,
        count=1000,
    )
    print(f"✅ Fetched {len(result)} reviews.")
except Exception as e:
    print(f"❌ Error fetching reviews: {e}")
    exit()

# Save all reviews to CSV
df_all = pd.DataFrame(result)
df_all.to_csv("amazon_all_reviews.csv", index=False)
print("💾 Saved all reviews to 'amazon_all_reviews.csv'.")

# Sustainability-related keywords
keywords = [
    'eco', 'green', 'sustain', 'climate', 'carbon', 'recycl',
    'planet', 'environment', 'nature', 'biodegrad', 'zero waste', 'plastic', 'conscious'
]

# Filter reviews containing any of the sustainability keywords
filtered = [
    r for r in result
    if any(k in r['content'].lower() for k in keywords)
]

print(f"🌱 Found {len(filtered)} sustainability-related reviews.")

# Save filtered reviews
if filtered:
    df_filtered = pd.DataFrame(filtered)
    df_filtered = df_filtered[['userName', 'score', 'content']]
    df_filtered.to_csv("amazon_sustainability_reviews.csv", index=False)
    print("💾 Saved filtered reviews to 'amazon_sustainability_reviews.csv'.")
else:
    print("⚠️ No sustainability-related reviews found in the fetched data.")
