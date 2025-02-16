from django.http import JsonResponse
from django.shortcuts import render
from chatbot.utils import bot_response


# def bot_response(user_input):
#     if ("hello" in user_input.lower() or "hi" in user_input.lower()):
#         return "Hi there! How can I help you?"
#     elif "how are you" in user_input.lower():
#         return "I'm just a bot, but I'm doing great! How about you?"
#     elif "normalisation" in user_input.lower():
#         return 'Which operateur?'
#     else:
#         return "I'm not sure how to respond to that. Can you rephrase?"

# Homepage view


def home(request):
    return render(request, 'chatbot/index.html')

# API view to handle user input


def get_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = bot_response(user_input)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request method'})
