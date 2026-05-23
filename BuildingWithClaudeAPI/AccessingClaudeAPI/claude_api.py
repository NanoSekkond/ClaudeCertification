from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-haiku-4-5"

def add_user_message(messages, text):
    messages.append(
        {
            "role" : "user",
            "content" : text
        }
    )

def add_assistant_message(messages, text):
    messages.append(
        {
            "role" : "assistant",
            "content" : text
        }
    )

def chat(messages, new_message, system, temperature):
    add_user_message(messages, new_message)
    response = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        system=system,
        temperature=temperature
    )
    add_assistant_message(messages, response.content[0].text)
    return response.content[0].text

def stream_chat(messages, new_message, system, temperature):
    add_user_message(messages, new_message)
    with client.messages.stream(
        model=model,
        max_tokens=1000,
        messages=messages,
        system=system,
        temperature=temperature
    ) as stream:
        for text in stream.text_stream:
            print(text, end="")
        print("")
    add_assistant_message(messages, stream.get_final_message())
    return stream.get_final_message()

def json_chat(user_input, system, temperature):
    messages = []
    add_user_message(messages, user_input)
    add_assistant_message(messages, "Here is the json you requested for without any comments:\n```json")
    response = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        system=system,
        temperature=temperature,
        stop_sequences=["```"]
    )
    add_assistant_message(messages, response.content[0].text)
    return response.content[0].text
    

def chatbot(system="", temperature=1.0):
    messages = []
    while(True):
        user_input = str(input('> '))
        stream_chat(messages, user_input, system, temperature)

def system_prompt_example(with_prompt):
    # To test this out ask a math question to the chatbot and see the difference with and without a system prompt.
    system_prompt = "You're a math tutor, do not answer questions directly, instead incentivise the student to come up with their own response. If they're still struggling show them the solution and explain it to them."
    chatbot(system=system_prompt if with_prompt else "")

def temperature_example(temperature):
    # To test this out ask a creative question to the chatbot and see the difference with low and high temperature.
    chatbot(temperature=temperature)

def json_example():
    # To test this out ask for a json object of anything you can come up with. The idea is that the output will ONLY have the json to the parse it or do whatever.
    user_input = str(input('> '))
    response = json_chat(user_input, "", 0)
    print(response)

def main():
    json_example()
    

if __name__ == "__main__":
    main()