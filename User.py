from  Question import Question



class User:

    def __init__(self,name,id):
        self.name = name
        self.id = id


class Examiner(User,Question):

    def __init__(self,name,e_id):
        self.name = name
        self.e_id = e_id
        super().__init__(self.name,self.e_id)
        Question.__init__(self)

    def __repr__(self):
        return self.name + " " + str(self.e_id)
    
    def addQuestion(self,topic_name,level_of_ques):
        Question.addQuestion(self,topic_name,level_of_ques)
    
    def displayAllQuestion(self):
        Question.displayAllQuestion(self)


class Testtaker(User):

    def __init__(self,name,s_id):
        self.name = name
        self.s_id = s_id
        super().__init__(name,s_id)

    def __repr__(self):
        return self.name + " " + str(self.s_id)
    
    def viewTopics(self):
        Question.viewTopics(self)

    def run_test(self):
        Question.run_test()

