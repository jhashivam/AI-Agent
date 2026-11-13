from openai import OpenAI  # Bring in the tool that lets this program talk to an AI.
from dotenv import load_dotenv  # Bring in the tool that reads settings from a .env file.
import os  # Bring in tools for reading settings from the computer.

# Read the saved settings so the program can use them.
load_dotenv()  # Load settings such as the server address, key, and model name.

# Set up a connection to the AI service.
client = OpenAI(  # Make a client that will send messages to the AI.
    base_url=os.getenv("BASE_URL"),  # Get the AI service address from the settings.
    api_key=os.getenv("API_KEY")  # Get the access key from the settings.
)  # Finish setting up the client.

print("=" * 40)  # Print a line made of 40 equal signs.
print("      Shivam's AI Assistant")  # Show the name of this program.
print("=" * 40)  # Print another line to frame the name.

while True:  # Keep chatting until the user chooses to stop.

    user_input = input("\nYou : ")  # Ask the user to type a message.

    if user_input.lower() == "quit":  # Check if the user typed "quit" in any letter case.
        print("\nAI  : Goodbye! Have a great day.")  # Say goodbye before stopping.
        break  # Leave the loop and end the chat.

    response = client.chat.completions.create(  # Send the user's message to the AI.
        model=os.getenv("MODEL"),  # Choose the AI model named in the settings.
        messages=[  # Start the list of messages for the AI.
            {  # Make one message for what the user just typed.
                "role": "user",  # Tell the AI that this message is from the user.
                "content": user_input  # Put the user's words into the message.
            }  # Finish the user's message.
        ]  # Finish the list of messages.
    )  # Finish sending the request and save the AI's reply.

    print("\nAI :", response.choices[0].message.content)  # Show the AI's answer on the screen.

