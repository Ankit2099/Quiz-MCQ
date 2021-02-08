from User import Examiner, Testtaker


e1 = Examiner("E",234)
print(e1)
e1.addQuestion("General Knowledge","easy")
e1.addQuestion("General Knowledge","medium")
e1.addQuestion("Python","easy")
e1.displayAllQuestion()

t1 = Testtaker("s",2)
print(t1)
t1.viewTopics()
t1.run_test()