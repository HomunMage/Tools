import time
import argparse
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime

def init_webdriver(gecko_driver_path):
    service = Service(gecko_driver_path)
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)
    return driver

def store_tweets(driver, stored_tweets):
    tweets = driver.find_elements(By.XPATH, '//div[@data-testid="tweetText"]')
    new_tweets = []
    for tweet in tweets:
        tweet_text = tweet.text
        if tweet_text not in stored_tweets:
            stored_tweets.add(tweet_text)
            new_tweets.append(tweet_text)
    
    if new_tweets:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{now}.md"
        with open(filename, 'w', encoding='utf-8') as file:
            for tweet in new_tweets:
                file.write(tweet + "\n\n")

def main(twitter_handle, gecko_driver_path):
    url = f"https://twitter.com/{twitter_handle}"
    driver = init_webdriver(gecko_driver_path)
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    # Define a set to keep track of stored tweets to avoid duplicates
    stored_tweets = set()
    scroll_pause_time = 5  # Time to wait before scrolling
    max_scroll_attempts = 5  # Maximum number of scroll attempts

    # Main loop to store tweets every 5 seconds
    scroll_attempts = 0
    while scroll_attempts < max_scroll_attempts:
        store_tweets(driver, stored_tweets)
        time.sleep(5)
        current_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == current_height:
            scroll_attempts += 1
        else:
            scroll_attempts = 0

    # Close the driver
    driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Twitter Crawler')
    parser.add_argument('--id', required=True, help='Twitter handle to crawl')
    parser.add_argument('--gecko_driver', required=True, help='Path to the GeckoDriver executable')
    args = parser.parse_args()
    
    main(args.id, args.gecko_driver)
