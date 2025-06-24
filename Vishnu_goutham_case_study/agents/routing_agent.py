def run_routing_agent(ticket, sentiment, urgency):
    tier = ticket["customer_tier"]
    message = ticket["message"].lower()

    route_to = "support"
    if "feature" in message or "request" in message:
        route_to = "product"
    elif "api" in message or "error" in message:
        route_to = "engineering"
    elif "security" in message or "vulnerability" in message:
        route_to = "escalation"

    if urgency == "high" or tier == "enterprise":
        priority = "high"
    elif urgency == "medium":
        priority = "medium"
    else:
        priority = "low"

    return {
        "route_to": route_to,
        "priority": priority
    }
