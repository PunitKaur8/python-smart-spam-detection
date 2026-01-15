# smart_spam_detection.py
# Context-aware, confidence-based spam detection system

# ---------------- CONFIG ----------------

SPAM_KEYWORDS = [
    "buy now", "free", "discount", "offer", "limited time",
    "win", "click", "urgent"
]

TRANSACTION_KEYWORDS = [
    "balance", "spent", "payment", "due", "available",
    "credited", "debited", "account"
]

TRUSTED_SENDERS = ["CA", "BANK", "PAYTM", "GPAY"]

SPAM_THRESHOLD = 3
TRANSACTION_THRESHOLD = 2


# ---------------- CORE LOGIC ----------------

def clean_text(text):
    return text.lower().strip()


def keyword_score(text, keywords):
    score = 0
    for word in keywords:
        if word in text:
            score += 1
    return score


def analyze_message(sender, message):
    cleaned = clean_text(message)

    spam_score = keyword_score(cleaned, SPAM_KEYWORDS)
    transaction_score = keyword_score(cleaned, TRANSACTION_KEYWORDS)

    sender_type = "UNKNOWN"

    if sender.upper() in TRUSTED_SENDERS:
        sender_type = "TRUSTED"
        spam_score -= 2
        transaction_score += 2

    # ---------------- DECISION ENGINE ----------------

    if spam_score >= SPAM_THRESHOLD:
        decision = "SPAM"
        confidence = min(90, 60 + spam_score * 10)

    elif transaction_score >= TRANSACTION_THRESHOLD:
        decision = "ALLOW (Transactional)"
        confidence = min(95, 70 + transaction_score * 10)

    elif spam_score > 0:
        decision = "FLAG FOR REVIEW"
        confidence = 50 + spam_score * 10

    else:
        decision = "ALLOW"
        confidence = 85

    return {
        "Sender": sender,
        "Sender type": sender_type,
        "Message": message,
        "Spam score": spam_score,
        "Transaction score": transaction_score,
        "Decision": decision,
        "Confidence": f"{confidence}%"
    }


# ---------------- DEMO DATA ----------------

messages = [
    ("CA", "Your balance is 12000 and payment due tomorrow"),
    ("UNKNOWN", "Hi how are you"),
    ("UNKNOWN", "Buy now and get FREE discount"),
    ("UNKNOWN", "Limited time offer just for you"),
    ("CA", "You spent 500 today, available balance 9500"),
    ("UNKNOWN", "Can you help me with something"),
    ("FRIEND", "Let's meet tomorrow")
]


# ---------------- RUN ----------------

for sender, text in messages:
    result = analyze_message(sender, text)
    print(f"Sender: {result['Sender']} ({result['Sender type']})")
    print(f"Message: {result['Message']}")
    print(f"Spam score: {result['Spam score']}")
    print(f"Transaction score: {result['Transaction score']}")
    print(f"Decision: {result['Decision']}")
    print(f"Confidence: {result['Confidence']}")
    print("------")