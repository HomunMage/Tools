import time
import os
import sys
import argparse
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def init_driver(geckodriver_path, headless):
    options = Options()
    if headless:
        options.add_argument("--headless")  # Run in headless mode if specified
    service = Service(executable_path=geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)
    return driver

def store_tweet(content):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}.md"
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content + "\n\n")
    print(f"Stored tweet in {filename}")

def crawl_twitter(driver, url):
    driver.get(url)
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        tweets = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")

        for tweet in tweets:
            try:
                content = tweet.text
                store_tweet(content)
            except Exception as e:
                print(f"Error storing tweet: {e}")

        # Scroll down in smaller increments
        driver.execute_script("window.scrollBy(0, 250);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            print("No new tweets found, waiting for 5 seconds...")
            time.sleep(5)
        else:
            last_height = new_height

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Twitter Crawler Script")
    parser.add_argument("--url", required=True, help="The URL of the Twitter page to crawl")
    parser.add_argument("--gecko", required=True, help="The path to the geckodriver executable")
    parser.add_argument("--headless", action="store_true", help="Run the browser in headless mode")

    args = parser.parse_args()
    
    twitter_url = args.url
    geckodriver_path = args.gecko
    headless = args.headless
    
    driver = init_driver(geckodriver_path, headless)
    try:
        crawl_twitter(driver, twitter_url)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
