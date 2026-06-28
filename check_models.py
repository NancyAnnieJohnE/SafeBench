import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6KMx4EAQPCOCo2280q_m9xZW95NB3SQBAV6qI91wxDy6w")

for m in genai.list_models():
    print(m.name, m.supported_generation_methods)