from google import genai

# Initialize the Gemini client with your API key
client = genai.Client(api_key="AIzaSyDN7dJ5IkJDxLJcfbBJt8_TapIDeUFs6-g")

print("AI Bot 🤖: Hello! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AI Bot 🤖: Goodbye!")
        break

    try:
        # Send the user input to Gemini for processing
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # Replace with your desired model
            contents=user_input
        )
        bot_reply = response.text
        print("AI Bot 🤖:", bot_reply)

    except Exception as e:
        print("AI Bot 🤖: Something went wrong:", e)
