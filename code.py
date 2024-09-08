import os
from dotenv import load_dotenv
from chatgpt import *
import datetime
import pytz
load_dotenv()

def main():
    logdir = os.getenv('CODE_LOG_DIR')
    gpt = ChatGPT()
    # create log file to store chat history
    f = open(logdir + "code_log.txt", "a")
    timezone = pytz.timezone("America/Chicago")

    while True:
        user_input = input("You: ")
        if user_input == "exit":
            f.close()
            break

        f.write(str(datetime.datetime.now(timezone)) + "\n")
        f.write("You: " + user_input + "\n")

        response = gpt.get_response("You are a helpful assistant that is going to be asked coding questions", user_input)
        f.write(str(datetime.datetime.now(timezone)) + "\n")
        f.write("ChatGPT: " + response + "\n")
        print("ChatGPT: " + response)
main()
