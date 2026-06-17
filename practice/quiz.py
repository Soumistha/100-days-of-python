question_data = [
{"text": "A slug's blood is green.", "ans": "True"},
{"text": "The loudest animal is the African Elephant.", "ans": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "ans": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "ans": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "ans": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "ans": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "ans": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "ans": "False"},
{"text": "Google was originally called 'Backrub'.", "ans": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "ans": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "ans": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "ans": "True"}
]


class Question:
    def __init__(self,q,a):
        self.text = q
        self.ans = a
        

#new_q = Question("am i smart?","True")
#print(new_q.text)
#print(new_q.ans)



class noquiz:
    def __init__(self,q_list):
        self.number = 0
        self.quest_list = q_list
        self.score = 0;
        
    def next_q(self):
        current = self.quest_list[self.number]
        self.number += 1
        user_ans = input(f"Q:{self.number}: {current.text} (True/False) ")
        if(user_ans != "True" and user_ans != "False"):
            print("invalid ans")
            self.number -=1
        else:
            if(self.is_correct(user_ans, current.ans)):
                self.score+=1
                print(f"the score is {self.score}")
            else:
                print(f"the score is {self.score}")
        
    def still_q(self):
        return (len(self.quest_list)>self.number)

    def is_correct(self,a,c_ans):
        return (a == c_ans)
            
quiz_list = []

for q in question_data:
    text = q["text"]
    ans = q["ans"]
    new = Question(text,ans)
    quiz_list.append(new)



quiz = noquiz(quiz_list)

while(quiz.still_q()):
    quiz.next_q()