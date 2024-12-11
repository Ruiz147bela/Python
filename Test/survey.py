class AnonymousSurvey():

    def __init__(self,question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self,new_repsonse):
        self.responses.append(new_repsonse)

    def show_results(self):
        print("Survey Results")
        for response in self.responses:
            print(' - ' + response)