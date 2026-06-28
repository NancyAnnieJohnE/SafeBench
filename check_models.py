import google.generativeai as genai

genai.configure(api_key="GEMINI-API-KEY") //add your own gemini api key

for m in genai.list_models():
    print(m.name, m.supported_generation_methods)
