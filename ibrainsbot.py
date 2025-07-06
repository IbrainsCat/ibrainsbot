from instagrapi import Client
import os
import time

# Get IG credentials securely from environment variables
USERNAME = os.environ.get("IG_USER")
PASSWORD = os.environ.get("IG_PASS")

# Create Instagram client and login
cl = Client()
cl.login(USERNAME, PASSWORD)

print("✅ IbrainsBot logged into Instagram!")

# Hashtag to target
target_hashtag = "cybersecurity"

# Number of users to interact with per run
max_users = 5

while True:
    print(f"🔍 Searching for users in #{target_hashtag}")
    
    try:
        medias = cl.hashtag_medias_recent(target_hashtag, amount=max_users)
        
        for media in medias:
            user = cl.user_info(media.user.pk)
            cl.user_follow(user.pk)
            cl.media_like(media.pk)
            print(f"✅ Followed @{user.username} and liked their post")
        
        print("✅ Done with this batch. Sleeping for 1 hour...")
        time.sleep(3600)  # 1 hour delay

    except Exception as e:
        print(f"❌ Error: {e}")
        print("⏳ Retrying in 10 minutes...")
        time.sleep(600)
