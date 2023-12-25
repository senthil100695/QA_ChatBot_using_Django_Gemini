import os
from django.shortcuts import render
from django.views.generic import CreateView
from .models import GeminiBot
import google.generativeai as genai
from dotenv import load_dotenv
from IPython.display import Markdown
from IPython.display import display
import textwrap
load_dotenv()


# Create your views here.

def home(request):
    user_input = None

    if request.method == 'POST':
        user_input = request.POST['user_input']
        GeminiBot.objects.create(question=user_input)
        response = gemini_response(question=user_input)
        GeminiBot.objects.create(response=response)


    return render(request, 'home.html', {'response': response})

def gemini_response(question):
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    model = genai.GenerativeModel(model_name='gemini-pro')
    response =model.generate_content(question)
    
    return (to_markdown(response.text)).data

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '<', predicate=lambda _: True))

class AskGemini(CreateView):
    model = GeminiBot
    template_name = 'ask_llm.html'
    fields = ['question']
