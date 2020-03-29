#randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key


import random

# The quiz data. Keys are states and values are their capitals

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
  'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.

for quizNum in random(35):
        #TODO: Create the quiz and answer key files.
        quizfile =open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\capitalquiz%s.txt'%(quizNum+1),'w')
        answerKeyFile = open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
        #TODO: Write out the header for the quiz.
        quizfile.write('Namwe:\n\nDate:\n\nPeriod:\n\n')
        quizfile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
        quizfile.write('\n\n')
        # TODO: Shuffle the order of the states.
        states = list(capitals.keys())
        random.shuffle(states)

        # TODO: Loop through all 50 states, making a question for each.

        for questionNum in range(3):
# Get right and wrong answers.
            corretAnswers = capitals[states[questionNum]]
            wronganswer = list(capitals.values())
            del wronganswer[wronganswer.index(corretAnswers)]
            answerOptions = wronganswer + [corretAnswers]
            random.shuffle(answerOptions)

# Write the question and the answer options to the quiz file.
            quizfile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
            for i in range(4):
               quizfile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
               quizfile.write('\n')
# Write the answer key to a file.
            answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
            answerOptions.index(corretAnswers)]))
        quizfile.close()
        answerKeyFile.close()
