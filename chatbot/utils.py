def bot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "salam": "Hi there! How can I help you?",
        "hello": "Hi there! How can I help you?",
        "hi": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "relais proximite": "<br>".join([
            "Suivi les etapes suivante:",
            "<br><b>Etape 1:</b> ",
            "<b>Etape 2:</b> .",
            "<b>Etape 3:</b> ",
            "<b>Etape 4:</b> "
        ]),
        # "": "",
        # "": "",
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return "I'm not sure how to respond to that. Can you rephrase?"
