from commands.command import Command

class Summary(Command):
    
    def execute(self):
        response = self.aiclient.analyse_conversation(file_path=self.meeting_filepath)
        summary_response = self.aiclient.chat(user_message="summarize the key points in call conversation", 
                                     input_text=response["conversation_text_fmt"])
        print(summary_response.choices[0].message.content)