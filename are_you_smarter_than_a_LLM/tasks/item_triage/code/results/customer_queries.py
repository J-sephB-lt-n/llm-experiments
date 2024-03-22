import random

simulated_customer_queries: list[str] = [
    "Hi, I've recently noticed several unauthorized transactions on my account. Could you help me investigate?",
    "I'm unable to recognize a recurring monthly payment on my account. Can you assist with this?",
    "Hey, there's a large payment made to a vendor I've never done business with. What's going on?",
    "I spotted a suspicious foreign transaction on my account. Could you check it out, please?",
    "Hello, I observed multiple small payments to the same recipient. Is this a fraudulent activity?",
    "I have received an alert for a cash transfer I did not authorize. Can you help me cancel this transaction?",
    "Help! My account shows a payment that exceeds my set transfer limit, but I did not authorize it.",
    "I am noticing an unexpected increase in payments to my utility service provider. Can you help?",
    "Hey, there's a transaction made when I was travelling, and I know I didn't make it. Would you mind checking?",
    "I've seen several payments to an online retailer whom I've never shopped from. Can you please assist me in addressing this issue?",
    "How do I link my saving and checking accounts on your web application?",
    "Can you guide me through setting up automatic bill payments on your website?",
    "I am unable to locate the 'transfer funds' option on your online banking platform.",
    "Could you explain the steps for updating my contact details in your banking application?",
    "I can't seem to find where to check my account balance. Could you help?",
    "How do I create a new payee when making online transactions on your website?",
    "I am having trouble finding the option to set up mobile alerts. Could you assist?",
    "Can you guide me through ordering a new checkbook via your web application?",
    "I cannot locate my credit card statement in your online banking platform. Need assistance.",
    "How do I reset my pin using your banking website? I can't find the option.",
    "Can you please explain why money has been deducted from my account without my knowledge? I remember authorizing a 'debit order' but I didn't know what it was.",
    "I authorized a debit order but I don't really understand what that means. Can you please explain and tell me why my money was taken out?",
    "I saw a transaction on my account that I don't recognize. Turns out I'd authorized a debit order. Can you explain what this debit order is?",
    "Can you clarify how a debit order works? I authorized it and money has been taken out of my account unexpectedly.",
    "Money deducted under 'debit order' and I don't understand what that means - could you kindly explain?",
    "I authorized a debit order but didn't expect my funds to go out. Can customer support assist me in understanding this?",
    "I don't understand the concept of a debit order and I'm seeing deductions on my account. Could you please explain this to me?",
    "I authorized a debit order, but wasn't expecting funds to be deducted from my account. Can you explain why this happened?",
    "Help needed! Money came out of my account labeled as 'debit order.' Can you explain what this is?",
    "I noticed a debit order on my account that I don't understand. What happens when you authorize a debit order?",
    "Can you please clarify the steps followed to report potential fraud in my account?",
    "I received an email asking for my account details. Is this a typical case of email fraud?",
    "I'd like to ensure that I have fraud protection on my account. Can you assist?",
    "I think I'm a victim of fraud. Can you help me secure my account?",
    "What measures does the bank take to warn customers about potential fraud risks?",
    "If someone tried to commit fraud involving my account, how would I be notified?",
    "How do I set up fraud alerts to my phone and email?",
    "What course of action should I take if I suspect fraud on my account?",
    "Can you please explain how your institution handles fraud detection and prevention?",
    "Do you have any educational resources about fraud prevention that I can review?",
]

random.Random(1978).shuffle(simulated_customer_queries)

if __name__ == "__main__":
    # print markdown table for README.md #
    print("| Query ID | Query ")
    print("|----------|-------")
    for idx, query in enumerate(simulated_customer_queries):
        print(f"| {idx:<9}| {query}")
