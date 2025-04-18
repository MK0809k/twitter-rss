import requests
import datetime

def get_latest_tweet(username):
    url = f"https://nitter.privacydev.net/{username}/rss"
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception("Failed to fetch from Nitter")

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(resp.text)
    item = tree.find("channel/item")
    title = item.find("title").text
    link = item.find("link").text
    pubDate = item.find("pubDate").text
    desc = item.find("description").text

    return {
        "title": title,
        "link": link,
        "pubDate": pubDate,
        "description": desc
    }

def write_rss(username, name):
    tweet = get_latest_tweet(username)

    rss = f'''<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
<title>{name} - @{username}</title>
<link>https://x.com/{username}</link>
<description>Latest tweets from {name}</description>
<language>en-us</language>
<item>
<title>{tweet['title']}</title>
<link>{tweet['link']}</link>
<description>{tweet['description']}</description>
<pubDate>{tweet['pubDate']}</pubDate>
</item>
</channel>
</rss>'''

    with open(f"{username.lower()}.xml", "w") as f:
        f.write(rss)

# Add profiles here
write_rss("Cobratate", "Andrew Tate")
write_rss("TateTheTalisman", "Tristan Tate")
write_rss("RorSyns", "Rorsyns")
write_rss("AlexTheMarshal", "Alex The Marshal")
