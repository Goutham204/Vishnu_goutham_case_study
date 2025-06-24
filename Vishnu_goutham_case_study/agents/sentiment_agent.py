from textblob import TextBlob

def run_sentiment_agent(subject, message):
    blob = TextBlob(subject + " " + message)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        sentiment = "positive"
    elif polarity < -0.2:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    message_lower = message.lower()
    if any(word in message_lower for word in ["urgent", "broken", "security", "vulnerability"]):
        urgency = "high"
    elif any(word in message_lower for word in ["not working", "issue", "bug"]):
        urgency = "medium"
    else:
        urgency = "low"

    return {
        "sentiment": sentiment,
        "urgency": urgency
    }
