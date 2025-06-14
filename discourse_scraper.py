import requests
import json
from bs4 import BeautifulSoup

def scrape_discourse():
    base_url = "https://discourse.onlinedegree.iitm.ac.in"
    category_id = 104
    category_url = f"{base_url}/c/courses/tools-in-data-science/{category_id}.json"

    print("Fetching topic list...")
    res = requests.get(category_url)
    if res.status_code != 200:
        print("Failed to fetch topics")
        return

    data = res.json()
    posts = []

    for topic in data['topic_list']['topics']:
        topic_id = topic['id']
        topic_title = topic['title']
        topic_link = f"{base_url}/t/{topic_id}"

        print(f"Fetching topic: {topic_title}")
        topic_page = requests.get(f"{base_url}/t/{topic_id}.json")
        if topic_page.status_code != 200:
            continue

        topic_data = topic_page.json()

        for post in topic_data['post_stream']['posts']:
            post_id = post['id']
            cooked_html = post['cooked']
            text = BeautifulSoup(cooked_html, 'html.parser').get_text()

            posts.append({
                "topic_id": topic_id,
                "post_id": post_id,
                "title": topic_title,
                "url": topic_link,
                "text": text
            })

    with open("data/discourse.json", "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

    print(f"✅ Scraped {len(posts)} posts and saved to data/discourse.json")

if __name__ == "__main__":
    scrape_discourse()
