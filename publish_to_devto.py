import requests
import json
import os
from dotenv import load_dotenv

# Load API Key from .env in parent directory
load_dotenv("../.env")
DEVTO_API_KEY = os.getenv("DEVTO_API_KEY")

def publish_article():
    if not DEVTO_API_KEY:
        print("Error: DEVTO_API_KEY not found in .env")
        return

    # Read the article content
    with open("generated_article.md", "r") as f:
        content = f.read()

    # Split frontmatter and body
    parts = content.split("---", 2)
    if len(parts) < 3:
        print("Error: Invalid article format (missing frontmatter)")
        return
    
    # We'll use the metadata strategy #4 from instructions: metadata in JSON payload
    # For this PoC, we'll parse the title and tags from the frontmatter manually
    import yaml
    frontmatter = yaml.safe_load(parts[1])
    body = parts[2].strip()

    payload = {
        "article": {
            "title": frontmatter.get("title", "Untitled Article"),
            "published": True,
            "body_markdown": body,
            "tags": frontmatter.get("tags", "").split(", "),
            "main_image": frontmatter.get("cover_image", ""),
            "description": frontmatter.get("description", "")
        }
    }

    url = "https://dev.to/api/articles"
    headers = {
        "Content-Type": "application/json",
        "api-key": DEVTO_API_KEY
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 201:
        data = response.json()
        print(f"Successfully published article!")
        print(f"URL: {data['url']}")
    else:
        print(f"Failed to publish article. Status code: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    publish_article()
