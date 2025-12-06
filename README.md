# App Sustainability Review Scraper

A Python tool for scraping and analyzing sustainability-related user reviews from mobile apps on Google Play Store and Apple App Store.

## Overview

This project helps researchers and developers understand how users perceive sustainability features in mobile applications. It fetches reviews from app stores and filters them based on sustainability-related keywords to identify relevant feedback.

## Features

- 🔍 Scrapes reviews from Google Play Store and Apple App Store
- 🌱 Filters reviews using sustainability-related keywords
- 📊 Exports data to CSV format for easy analysis
- 🎯 Configurable review count and sorting options
- 🌍 Multi-language and country support

## Sustainability Keywords

The tool searches for reviews containing the following keywords:
- eco, green, sustain, climate, carbon, recycl
- planet, environment, nature, biodegrad
- zero waste, plastic, conscious

## Requirements

```bash
pip install google-play-scraper
pip install app-store-scraper
pip install pandas
```

## Usage

1. **Install dependencies:**
   ```bash
   pip install google-play-scraper app-store-scraper pandas
   ```

2. **Configure the app:**
   Edit `get_sustainability_reviews.py` to specify your target app's package name:
   ```python
   app_package = 'com.amazon.mShop.android.shopping'  # For Google Play
   ```

3. **Run the scraper:**
   ```bash
   python get_sustainability_reviews.py
   ```

4. **Output files:**
   - `amazon_all_reviews.csv` - All fetched reviews
   - `amazon_sustainability_reviews.csv` - Filtered sustainability-related reviews

## Example Datasets

This repository includes sample datasets from various sustainability-focused apps:
- `aworld_sustainability_reviews.csv` - AWorld app reviews
- `ecosia_sustainability_reviews.csv` - Ecosia browser reviews
- `olio_sustainability_reviews.csv` - OLIO food sharing app reviews
- `App Review Dataset - GreenApes.csv` - GreenApes community app
- `App Review Dataset - Samsung Global.csv` - Samsung Global Goals app

## Output Format

The filtered CSV files contain:
- `userName` - Review author's username
- `score` - Star rating (1-5)
- `content` - Full review text

## Customization

### Change the app:
```python
app_package = 'your.app.package.name'
```

### Adjust review count:
```python
count=1000  # Fetch up to 1000 reviews
```

### Add more keywords:
```python
keywords = [
    'eco', 'green', 'sustain',
    # Add your custom keywords here
]
```

### Change sorting method:
```python
sort=Sort.NEWEST  # Options: NEWEST, RATING, HELPFULNESS
```

## Use Cases

- Academic research on sustainable app design
- Market research for eco-friendly features
- User sentiment analysis on sustainability
- Competitive analysis of green features
- Product development insights

## License

This project is open source and available for educational and research purposes.

## Contributing

Feel free to submit issues or pull requests to improve the scraper or add new features.

## Disclaimer

This tool is for research and educational purposes only. Please respect the terms of service of app stores and use responsibly.