Overview

This project is a multi-agent AI system designed to analyze and route customer support tickets based on sentiment, urgency, and customer metadata. Although designed for integration with OpenAI and Pydantic AI, this version runs completely offline using 'TextBlob' and rule-based logic to simulate intelligent agent behavior.

---

Agent Architecture

1. Sentiment Agent
Input: 'subject' & 'message'
Output: '{sentiment: positive/neutral/negative, urgency: low/medium/high}'
How: Uses 'TextBlob' polarity + rule-based keyword matching for urgency.

2. Routing Agent
Input: 'ticket' + 'sentiment' + 'urgency'
Output: '{route_to': support/product/engineering/escalation, priority: low/medium/high}'
How: Rule-based logic using keywords and metadata.

These agents communicate in sequence: the first classifies tone, the second decides action.

---

Evaluation

A basic evaluator is included in 'result.py' to compare actual routing decisions against expected ones. It reports basic accuracy for test cases.

---

Evaluation Results

A basic evaluator was used to test routing accuracy against expected outcomes:

2/3 routes correctly matched expected teams
1 route was incorrect due to keyword overlap or insufficient context

Offline accuracy: ~66.7% (rule-based; no LLMs used)