import requests

username = "mahimarawat0707"

def get_data(url):
    users = []
    page = 1
    
    while True:
        response = requests.get(f"{url}?page={page}&per_page=100")
        data = response.json()
        
        if not data:
            break
            
        users.extend([user['login'] for user in data])
        page += 1
    
    return users

followers = get_data(f"https://api.github.com/users/{username}/followers")
following = get_data(f"https://api.github.com/users/{username}/following")

followers_set = set(followers)
following_set = set(following)

print("❌ Not following you back:")
print(following_set - followers_set)
