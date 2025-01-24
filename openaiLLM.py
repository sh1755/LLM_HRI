from openai import OpenAI
import subprocess
 
import os
 
base_prompt = """You are to read the following instructions provided by a user and respond based on the content of the message. If the user's message includes directives related to movement or actions, respond with a specific command. If the message contains no relevant directive or is empty, return an empty response.
 
- If the instruction mentions "pick up the block" or "grab the block", respond with: COMMAND_PICK_UP_BLOCK.
- If the instruction is empty or contains none of the above actions, respond with an empty string.
 
Instructions:
"""
 
while True:
    user_input = input("Instruction: ")
    # user_input="grab the block"
    client = OpenAI(api_key="sk-proj-3E15MaD4J92uKDL7xSd0T3BlbkFJgGgZqzqf72ovaM9ZU4ZJ")
 
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": base_prompt + user_input,
            }
        ],
        temperature=0.7,
        max_tokens=64,
        top_p=1,
 
    )
 
    response_text = response.choices[0].message.content
    print(response_text)
 
    if response_text == "COMMAND_PICK_UP_BLOCK":
 
        subprocess.call("C:\\dev\\cpp\\vcpkg\\libfranka-master\\libfranka-master\\out\\build\\x64-Debug\\examples\\grasp_object.exe")
    # elif response_text == "COMMAND_PICK_UP_CUP":
    #     os.system(
    #         "C:\\dev\\cpp\\vcpkg\\libfranka-master\\libfranka-master\\out\\build\\x64-Debug\\examples\\echo_robot_state.exe"
    #     )
    # elif response_text == "COMMAND_PICK_UP_BLOCK":
    #     os.system(
    #         "C:\\dev\\cpp\\vcpkg\\libfranka-master\\libfranka-master\\out\\build\\x64-Debug\\examples\\grasp_object.exe"
    #     )
 
