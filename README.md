Here’s a complete and polished `README.md` for your **Virtual Teaching Assistant Discourse Responder** project:

---

# 🧠 Virtual Teaching Assistant — Discourse Responder for IITM Online BSc (TDS)

This project builds an intelligent **Virtual TA** for the **Tools for Data Science (TDS)** course in IIT Madras’ Online BSc Program. It uses scraped Discourse posts and course material to automatically answer student queries through an API, simulating how a real TA would respond.

---

## 📌 Features

* 🔍 **Question Matching**: Finds the most relevant Discourse posts to a student’s question.
* 💬 **GPT-Powered Answering**: Uses `openai/gpt-3.5-turbo` via OpenRouter to craft a concise and helpful reply.
* 🖼️ **Image Input** (Optional): Accepts base64-encoded screenshots for future OCR integration.
* 🔗 **Source Links**: Provides links to original Discourse posts used in the answer.
* 🌐 **Public API Endpoint**: Ready to be integrated into other platforms or frontends.

---

## 🚀 How It Works

1. Student sends a question (and optionally an image).
2. The app searches the scraped Discourse data for similar posts.
3. It creates a prompt for the language model using the top matching posts.
4. The model returns an answer + supporting links.

---

## 📥 API Usage

### `POST /api/`

#### 🔸 Request (JSON):

```json
{
  "question": "Should I use gpt-4o-mini or gpt-3.5 turbo?",
  "image": "<optional base64 image>"
}
```

#### 🔸 Response (JSON):

```json
{
  "answer": "You should use `gpt-3.5-turbo-0125` even if AI proxy supports `gpt-4o-mini`...",
  "links": [
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/...",
      "text": "Use the model that’s mentioned in the question..."
    }
  ]
}
```

---

## 🧪 Testing

Use cURL or Postman to test locally:

```bash
curl -X POST http://127.0.0.1:5000/api/ \
  -H "Content-Type: application/json" \
  -d '{"question": "What model should I use for GA5 Q8?"}'
```

---

## 🧰 Tech Stack

* Python 🐍
* Flask 🌐
* OpenRouter + GPT (gpt-3.5-turbo) 🤖
* difflib for semantic similarity
* Discourse post scraping (manual/pre-saved)

---

## 📄 MIT License

This project is licensed under the [MIT License](LICENSE). Feel free to use, share, and build upon it.

---

## ✨ Future Improvements

* 🧠 Add OCR from uploaded screenshots using `pytesseract`
* 🔍 Improve semantic search using `SentenceTransformers`
* 📚 Scrape content dynamically using Discourse API
* 🛡️ Rate limiting & abuse prevention

---

## 📎 Related Links

* [IITM Online Degree Portal](https://onlinedegree.iitm.ac.in/)
* [Discourse Forum](https://discourse.onlinedegree.iitm.ac.in/)
* [OpenRouter.ai](https://openrouter.ai/)
* [Project Evaluation Submission](https://exam.sanand.workers.dev/tds-project-virtual-ta)

---

Let me know if you also want a `requirements.txt`, `LICENSE`, or a deployment status badge added!
