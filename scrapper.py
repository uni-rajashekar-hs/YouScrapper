from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_youtube_search_results(query):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    search_url = f"https://www.youtube.com/results?search_query={query}"
    driver.get(search_url)
    
    # Let the page load
    driver.implicitly_wait(10)
    
    # Extract video details
    video_elements = driver.find_elements(By.ID, 'video-title')
    video_details = []
    
    for video in video_elements[:10]: 
        video_url = video.get_attribute('href')
        video_title = video.get_attribute('title') or video.get_attribute('aria-label')
        video_details.append({'title': video_title, 'url': video_url})
    
    driver.quit()
    return video_details

def main():
    query = "Dwapara Kannada song"
    video_details = get_youtube_search_results(query)
    if video_details:
        for i, video in enumerate(video_details):
            print(f"Video {i+1}:")
            print(f"Title: {video['title']}")
            print(f"URL: {video['url']}")
            print()
    else:
        print("No video details found.")

if __name__ == "__main__":
    main()
