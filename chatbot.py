from google import genai

client = genai.Client(api_key="AIzaSyBUgs882siQ3lbFpgjZZ7FM1Y5bzshH4Uk")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="tell me computer network"
)
print(response.text)