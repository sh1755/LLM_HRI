



from openai import OpenAI
import speech_recognition as sr
import subprocess
import keyboard  # for listening to keyboard inputs to start/stop recording

base_prompt = """
You are to read the following instructions provide
d by a user and respond based on the content of the message. If the user's message includes directives related to movement or actions, respond with a specific command. If the message contains no relevant directive or is empty, return an empty response.

- If the instruction mentions "pick up the block" or "grab the block", respond with: COMMAND_PICK_UP_BLOCK
- If the instruction mentions "pick up the mug" or "grab the mug", respond with: COMMAND_PICK_UP_MUG
- If the instruction is empty or contains none of the above actions, respond with an empty string.

Instructions:
"""




# Setup the speech recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()    

while True:
    print("Press Enter to start recording and Space to stop:")
    keyboard.wait('enter')
    print("Recording...")

    # Record the audio
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)  # adjust for ambient noise
        audio = recognizer.listen(source, phrase_time_limit=10)  # listen to the first phrase

    print("Processing...")
    try:
        # Convert speech to text
        user_input = recognizer.recognize_google(audio)
        print(f"Instruction: {user_input}")

        # Continue with your existing OpenAI API call setup
        client = OpenAI(api_key="sk-proj-3E15MaD4J92uKDL7xSd0T3BlbkFJgGgZqzqf72ovaM9ZU4ZJ")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": base_prompt + user_input},
            ],
            temperature=0.7,
            max_tokens=64,
            top_p=1,
        )

        response_text = response.choices[0].message.content
        print(response_text)

        # Execute commands based on the response
        if response_text == "COMMAND_PICK_UP_BLOCK":
            subprocess.call("C:\\dev\\cpp\\vcpkg\\libfranka-master\\libfranka-master\\out\\build\\x64-Debug\\examples\\grasp_object.exe")
        elif response_text == "COMMAND_PICK_UP_MUG":
            subprocess.call("C:\\dev\\cpp\\vcpkg\\libfranka-master\\libfranka-master\\out\\build\\x64-Debug\\examples\\grasp_object.exe")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
