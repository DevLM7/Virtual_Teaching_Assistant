import json
import difflib
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
with open("data/discourse.json", "r", encoding="utf-8") as f:
    discourse_posts = json.load(f)

def find_relevant_posts(question, top_n=2):
    scores = []
    for post in discourse_posts:
        similarity = difflib.SequenceMatcher(None, question.lower(), post["text"].lower()).ratio()
        scores.append((similarity, post))
    scores.sort(reverse=True, key=lambda x: x[0])
    return [item[1] for item in scores[:top_n]]

def build_answer(question):
    top_posts = find_relevant_posts(question)

    context = "\n\n".join([f"Post: {post['text']}" for post in top_posts])

    prompt = f"""
You are a helpful Teaching Assistant for the IITM Online BSc Data Science program.
Answer the student’s question using the relevant discourse posts below.

Question: {question}

Discourse Posts:
{context}

Be short, clear, and include references if needed.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/DevLM7/virtual-ta",
        "X-Title": "Virtual TA for IITM Discourse"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful and precise TA for a Data Science course."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 150
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
        final_answer = data['choices'][0]['message']['content'].strip()
    except Exception as e:
        final_answer = f"Error generating answer: {e}"

    links = [{"url": post["url"], "text": post["text"][:100]} for post in top_posts]

    return {
        "answer": final_answer,
        "links": links
    }

if __name__ == "__main__":
    q = "Should I use gpt-4o-mini or gpt3.5-turbo?"
    result = build_answer(q)
    print(json.dumps(result, indent=2))
