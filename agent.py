from transformers import pipeline
from rag import retrieve

# Better QA model
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=256
)

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


def clean_context(docs):
    unique_docs = list(dict.fromkeys(docs))
    context = " ".join(unique_docs)

    return context[:1500]


def answer(query):
    docs = retrieve(query, k=5)
    context = clean_context(docs)

    if len(context.strip()) < 50:
        return "I couldn't find relevant info."

    prompt = f"""
You are a smart assistant.

Answer the question based ONLY on the context below.

Context:
{context}

Question:
{query}

Answer clearly and accurately:
"""

    try:
        result = generator(prompt)
        return result[0]["generated_text"]

    except:
        return context[:300]


def summarize_topic(query):
    docs = retrieve(query, k=5)
    context = clean_context(docs)

    if len(context) < 50:
        return "Not enough content to summarize."

    summary = summarizer(
        context,
        max_length=120,
        min_length=40,
        do_sample=False
    )

    return summary[0]['summary_text']


def generate_quiz(query):
    docs = retrieve(query, k=5)
    context = clean_context(docs)[:800]

    return f"""
Create 3 MCQs from this content:

{context}

Q1:
A)
B)
C)
Answer:

Q2:
A)
B)
C)
Answer:

Q3:
A)
B)
C)
Answer:
"""


def agent(query):
    q = query.lower()

    if "quiz" in q:
        return generate_quiz(query)

    elif "summary" in q or "summarize" in q:
        return summarize_topic(query)

    else:
        return answer(query)