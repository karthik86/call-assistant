from commands.command import Command

class Conversation(Command):

    def execute(self):
        response  = self.aiclient.analyse_conversation(self.meeting_filepath)
        names = self.__find_speakers_and_companies(user_message="Identify the speaker names and their company names. Format it in following format\n speaker: name, company: name", response=response)
        print(self.__format_conversation(names=names, response=response))
    

    def __format_conversation(self, names, response):
        output = []
        speaker_index = 0
        for segment in response["conversation_timestamp_fmt"]:
            start = f"[{segment['start']:.2f}"
            speaker = names[speaker_index]["speaker"]
            company = names[speaker_index]["company"]
            speaker_and_company = f"{speaker} ({company})"
            output.append(f"{start} : {speaker_and_company} : {segment['text']}")
            speaker_index = 1 - speaker_index
        return "\n".join(output)

    
    def __find_speakers_and_companies(self,user_message, response):
        names = []
        response = self.aiclient.chat(user_message=user_message, 
                                     input_text=response["conversation_text_fmt"])
        print(response.choices[0].message)
        content = response.choices[0].message.content
        lines = content.splitlines()
        print(content)
        for line in lines:
             speakers_companies = line.split(",")
             names.append({
                 "speaker": speakers_companies[0].split(":")[1],
                 "company": speakers_companies[1].split(":")[1]
             })
        
        return names