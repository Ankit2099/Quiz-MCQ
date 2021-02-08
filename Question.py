class Question:

    options = []
    answers = []
    level_of_ques = []
    topic_name = []
    prompt = []

    def __init__(self):
        pass

    def addQuestion(self,topic_name,level_of_ques):

        statement = input("Enter question: ")
        Question.prompt.append(statement)
        Question.topic_name.append(topic_name)
        Question.level_of_ques.append(level_of_ques)
        l1 = []
        for i in range(4):
            l1.append(input("Enter option no. "+str((i+1))+": "))
        Question.options.append(l1)

        ans = input("Choose the correct option: (1/2/3/4) ? ")
        Question.answers.append(int(ans))




    def displayAllQuestion(self):
        print("Total number of questions are: ", len(Question.prompt))
        print("\n")
        for i in range(len(Question.prompt)):
            print("Ques. "+str(i+1) + Question.prompt[i])
            for j in range(len(Question.options[i])):
                print(str(j+1)+")"+str(Question.options[i][j]))
            print("\n\n")

    def viewTopics(self):
        a = set(Question.topic_name)
        print(a)
    
    @classmethod
    def run_test(cls):
        score = 0

        for statement in range(len(cls.prompt)):
            print("Topic: "+cls.topic_name[statement])
            print(cls.prompt[statement])

            for i in range(len(cls.options[statement])):
                print(str(i+1)+")"+str(cls.options[statement][i]))

            print("Question Level: ",cls.level_of_ques[statement])
            print("\n")

            answer = int(input("choose option number as answer: "))
            print("\n")

            if answer == cls.answers[statement]:
                score+=1
        print("\n")
        print("you got",str(score),"/",str(len(cls.prompt)),"correct. ")