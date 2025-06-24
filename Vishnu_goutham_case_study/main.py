from agents.sentiment_agent import run_sentiment_agent
from agents.routing_agent import run_routing_agent
import json
from pathlib import Path

with open("tickets.json", "r") as f:
    tickets = json.load(f)

for ticket in tickets:
    print(f"\n Ticket: {ticket['ticket_id']}")
    sentiment = run_sentiment_agent(ticket["subject"], ticket["message"])
    print("Sentiment:", sentiment)

    routing = run_routing_agent(ticket, sentiment["sentiment"], sentiment["urgency"])
    print("Routing:", routing)
    print("=" * 60)
