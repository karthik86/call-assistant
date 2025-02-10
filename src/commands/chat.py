from commands.command import Command

class Chat(Command):

    def execute(self):
        text_fmt = self.aiclient.analyse_conversation(self.meeting_filepath)
        print("Starting chat session. Type 'exit' to quit.")
        while True:
            user_message = input("question: ")
            if user_message.lower() == 'exit':
                print("Ending chat session.")
                break
            response = self.aiclient.chat(input_text=text_fmt,user_message=user_message)
            print(f"response: {response.choices[0].message.content}")
    




