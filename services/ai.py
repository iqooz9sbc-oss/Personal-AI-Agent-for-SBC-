# =====================================
# PERSONAL AI AGENT SBC
# services/ai.py
# =====================================

def get_ai_response(message):
    """
    Basic AI Response Function
    """

    text = message.lower().strip()

    if text in ["hi", "hello", "হ্যালো", "হাই"]:
        return "Hello! Welcome to PERSONAL AI AGENT SBC."

    elif "name" in text or "নাম" in text:
        return "My name is PERSONAL AI AGENT SBC."

    elif "how are you" in text or "কেমন আছ" in text:
        return "I am doing great. Thank you for asking."

    elif "time" in text or "সময়" in text:
        from datetime import datetime
        return datetime.now().strftime("%I:%M:%S %p")

    elif "date" in text or "তারিখ" in text:
        from datetime import datetime
        return datetime.now().strftime("%d-%m-%Y")

    elif "bye" in text or "বিদায়" in text:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand your message yet."
