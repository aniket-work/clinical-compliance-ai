"""
publish_to_devto.py - Automates publication to Dev.to via API.
"""
import requests
import os
import json
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
DEVTO_API_KEY = os.getenv("DEVTO_API_KEY")

def publish_article(article_path):
    if not DEVTO_API_KEY:
        print("Error: DEVTO_API_KEY not found in environment.")
        return

    with open(article_path, 'r') as f:
        content = f.read()

    # Extract title and tags if needed, or send as is
    # For reliability, we send the body WITHOUT frontmatter and set metadata in JSON
    
    payload = {
        "article": {
            "title": "Autonomous Clinical Trial compliance: Solving Protocol Bottlenecks with AI Agents",
            "body_markdown": content,
            "published": True,
            "tags": ["healthcare", "ai", "python", "automation"],
            "main_image": "https://raw.githubusercontent.com/aniket-work/clinical-compliance-ai/main/images/title-animation-v3.gif"
        }
    }

    url = "https://dev.to/api/articles"
    headers = {
        "api-key": DEVTO_API_KEY,
        "Content-Type": "application/json"
    }

    print(f"Publishing {article_path} to Dev.to...")
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 201:
        print("Success! Article published.")
        print(f"URL: {response.json().get('url')}")
    else:
        print(f"Failed to publish. Status: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    publish_article("generated_article.md")
