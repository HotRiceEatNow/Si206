# Your name: Jason Le    
# Your student id: 4025 2793
# Your email: lejaso@umich.edu
# List of who or what you worked with on this homework:
# If you used Generative AI, say that you used it and also how you used it.

import random

class MagicEightBall:
    def __init__(self, answers):
        # intialize the new ball obj

        self.answers_list = answers # list of possible answers
        self.previous_questions = [] #empty list to keep check of question that aksed
        self.previous_answers = [] # empty list to keep check of answers idex

    def __str__(self):
      
        if not self.previous_questions:
            return "Questions Asked:  Answers Given:" # if no question asked by user
        else:
            # Convert stored answer indices back into answer text.
            answers_given = [self.answers_list[i] for i in self.previous_answers] #return questions and answer accordingly
            return "Questions Asked: " + ", ".join(self.previous_questions) + "\n" + \
                   "Answers Given: " + ", ".join(answers_given)

    def get_fortune(self, question):
      
        
        if question in self.previous_questions: # if question asked before => return previous answer
            return "I’ve already answered this question"
        else:
            answer = random.choice(self.answers_list) # if question not asked before => return random answer
            # Get the index of the selected answer.
            idx = self.answers_list.index(answer)
            self.previous_answers.append(idx)
            return answer

    def play_game(self):
        
        print("Welcome to the Magic Eight Ball game!")
        question = input("Please enter a question: ") # prpompt user for question until "done"
        while question != "done":
            fortune = self.get_fortune(question) #if quesiton not duplicated fortune is called 
            print("Magic Eight Ball says:", fortune) # print answer then recorded the question into the list
            # Only add the question if it hasn't been asked before.
            if fortune != "I’ve already answered this question":
                self.previous_questions.append(question)
            question = input("Please enter the next question: ")
        print("Goodbye")

    def print_answer_frequencies(self):
       # count how many time each answer has been given
        if not self.previous_answers:
            print("I have not told your fortune yet") #if not fortune was given yet => print
            return {}
        freq_dict = {}
        # Count the frequency for each answer index.
        for idx in self.previous_answers: 
            answer_text = self.answers_list[idx]
            freq_dict[answer_text] = freq_dict.get(answer_text, 0) + 1
        # Print the frequency information.
        for answer, count in freq_dict.items():
            print(f"The answer '{answer}' has been given {count} times.")
        return freq_dict #reutrs mapping of its freeequency 


def main():
    # possible answers
    answers = [
        "Definitely",
        "Most Likely",
        "It is certain",
        "Maybe",
        "Ask again later",
        "Very doubtful",
        "Don't count on it",
        "Absolutely not"
    ]

    # create the magic ball

    ball = MagicEightBall(answers)

    # print initial nball with nothin in it]
    print(ball)

    #Initiate the game play.
    ball.play_game()

    #  Call print_answer_frequencies().
    ball.print_answer_frequencies()

    # now print the ball which has answer and equesiton
    print(ball)



if __name__ == "__main__":
    main()
