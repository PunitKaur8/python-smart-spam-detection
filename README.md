# python-smart-spam-detection
Context-aware spam detection using Python automation with scoring and confidence.
# Smart Spam Detection (Python)

This project implements a context-aware spam detection system using Python.

Unlike naive filters, it does not assume unknown senders are scammers.
Decisions are made using behavior-based scoring and confidence levels.

## Features
- Keyword-based spam scoring
- Transactional message detection
- Trusted sender handling
- Soft decisions (ALLOW, FLAG FOR REVIEW, SPAM)
- Confidence percentage for each decision

## Why this project
Many real-world spam filters incorrectly block legitimate messages.
This project demonstrates how rule-based logic can reduce false positives
before introducing AI models.

## Tech Stack
- Python 3
- Rule-based automation

This repository represents a foundation that can later be extended with AI.





Example:
from smart_spam_detection import analyze_message

messages = [
    ("CA", "Your balance is 12000 and payment due tomorrow"),
    ("UNKNOWN", "Buy now and get FREE discount"),
    ("FRIEND", "Hi, let's meet tomorrow")
]

for sender, message in messages:
    result = analyze_message(sender, message)
    print(result)

Output will be:
Sender: CA (TRUSTED)
Message: Your balance is 12000 and payment due tomorrow
Spam score: -2
Transaction score: 3
Decision: ALLOW (Transactional)
Confidence: 90%
------

Sender: UNKNOWN
Message: Buy now and get FREE discount
Spam score: 3
Transaction score: 0
Decision: SPAM
Confidence: 90%
------

Sender: FRIEND (UNKNOWN)
Message: Hi, let's meet tomorrow
Spam score: 0
Transaction score: 0
Decision: ALLOW
Confidence: 85%