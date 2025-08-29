from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key= "AIzaSyAwxjTXssSQ9gLXB-Q9QlATJYTk78bpE0g")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Qual a capital do Brasil?"
)
print(response.text)
