import time
import pygame
import pyfiglet
import threading
# Initialize pygame mixer globally
pygame.mixer.init()


def jeopardytheme():
    pygame.mixer.init()
    pygame.mixer.music.load("Jeopardy Theme [ ezmp3.cc ].mp3")
    pygame.mixer.music.play(-1)

jepoardythemeThread = threading.Thread(target=jeopardytheme)
jepoardythemeThread.start()




# Function to play sound effects
def play_sound(sound_type):
    soundfiles = {
        "correct": "Correct answer sound effect.mp3",
        "wrong": "Wrong sound effect.mp3",
        "finishquizhooray": "Hooray! Sound Effect.mp3",
        "failedthequizstupid": "you stupid meme sound effect.mp3"
    }

    sound = pygame.mixer.Sound(soundfiles[sound_type])
    sound.play()
    # Add a small delay to allow the sound to play completely
    time.sleep(1)  # Adjust time based on the length of your sound files


# Display ASCII art for the quiz title
ascii_art = pyfiglet.figlet_format("Quiz Time!", font="block")
print(ascii_art)


# All quiz functions

def runquizhistoryHARD():
    questionshardhis = (
        "Which treaty ended the Thirty Years' War in 1648?",
        "Who was the longest-reigning monarch of the United Kingdom before Queen Elizabeth II?",
        "What empire was ruled by Suleiman the Magnificent in the 16th century?",
        "The Cuban Missile Crisis occurred during the presidency of which U.S. President?",
        "In what year did the French Revolution start?",
        "What was the primary cause of the Opium Wars between China and Britain in the 19th century?",
        "Who was the first emperor of unified China, establishing the Qin dynasty?"
    )

    optionshistoryHARD = (
        ("A. Treaty of Versailles", "B. Treaty of Westphalia", "C. Treaty of Paris", "D. Treaty of Utrecht"),
        ("A. King George III", "B. Queen Victoria", "C. Queen Anne", "D. King Henry VIII"),
        ("A. Byzantine Empire", "B. Ottoman Empire", "C. Persian Empire", "D. Mughal Empire"),
        ("A. Dwight D. Eisenhower", "B. John F. Kennedy", "C. Richard Nixon", "D. Lyndon B. Johnson"),
        ("A. 1789", "B. 1799", "C. 1765", "D. 1812"),
        ("A. Control of Hong Kong", "B. Opium trade", "C. Religious differences", "D. Territorial disputes"),
        ("A. Sun Yat-sen", "B. Kublai Khan", "C. Qin Shi Huang", "D. Confucius")
    )

    answershisHARD = ("B", "B", "B", "B", "A", "B", "C")
    score = 0

    for question_num, question in enumerate(questionshardhis):
        print("------------------------")
        print(question)
        for option in optionshistoryHARD[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        while guess not in ['A', 'B', 'C', 'D']:
            guess = input("Invalid input. Please enter (A, B, C, D): ").upper()

        if guess == answershisHARD[question_num]:
            score += 1
            print("CORRECT!")
            play_sound("correct")
        else:
            print("INCORRECT")
            print(f"{answershisHARD[question_num]} is the correct answer.")
            play_sound("wrong")

    print("-----------------------------------------")
    percentagehardhis = (score / len(questionshardhis)) * 100
    print(f"Your score is {score} out of {len(questionshardhis)} ({percentagehardhis:.2f}%)")

    if percentagehardhis == 100:
        print("You aced the test!")
        play_sound("finishquizhooray")
    elif percentagehardhis < 70:
        print("You failed the test!")
        play_sound("failedthequizstupid")


def run_quizhis():
    questionshis = (
        "Who was the first president of the United States?",
        "Which empire was known as the empire on which the sun never sets?",
        "What year did World War II begin?",
        "Who wrote the Declaration of Independence?",
        "Which civilization built Machu Picchu?",
        "The fall of the Berlin Wall in 1989 marked the end of which major conflict?",
        "Who was the ruler of the Soviet Union during World War II?"
    )
    optionshis = (
        ("A. Thomas Jefferson", "B. Abraham Lincoln", "C. George Washington", "D. John Adams"),
        ("A. Roman Empire", "B. Mongol Empire", "C. Ottoman Empire", "D. British Empire"),
        ("A. 1914", "B. 1939", "C. 1945", "D. 1929"),
        ("A. Benjamin Franklin", "B. Thomas Jefferson", "C. George Washington", "D. Alexander Hamilton"),
        ("A. Aztec", "B. Mayan", "C. Inca", "D. Olmec"),
        ("A. World War II", "B. The Vietnam War", "C. The Cold War", "D. The Korean War"),
        ("A. Vladimir Lenin", "B. Leon Trotsky", "C. Nikita Khrushchev", "D. Joseph Stalin")
    )

    answershis = ("C", "D", "B", "B", "C", "C", "D")
    score = 0

    for question_num, question in enumerate(questionshis):
        print("----------------")
        print(question)
        for option in optionshis[question_num]:
            print(option)
        guessh = input("Enter (A, B, C, D): ").upper()
        while guessh not in ['A', 'B', 'C', 'D']:
            guessh = input("Invalid input. Please enter (A, B, C, D): ").upper()

        if guessh == answershis[question_num]:
            score += 1
            print("CORRECT!")
            play_sound("correct")
        else:
            print("INCORRECT")
            print(f"{answershis[question_num]} is the correct answer.")
            play_sound("wrong")

    print("-----------------------------------------")
    percentagehis = (score / len(questionshis)) * 100
    print(f"Your score is {score} out of {len(questionshis)} ({percentagehis:.2f}%)")

    if percentagehis == 100:
        print("You aced the test!")
        play_sound("finishquizhooray")
    elif percentagehis < 70:
        print("You failed the test!")
        play_sound("failedthequizstupid")


def run_quizhumor():
    questions = (
        "Is Drayden fat?",
        "Is Paulo's pp 8 feet long?",
        "Is Mr. Vasquez the goat?",
        "Is Mr. Vasquez top 3 teachers oat?",
        "Are Mr. Vasquez's jokes funny?",
        "Does Mr. Saing stutter a lot?",
        "Is Mr. Zeller fire?"
    )

    options = (
        ("A. Yes", "B. No", "C. VERY FAT", "D. Absolutely not!"),
        ("A. Yes", "B. No", "C. It's 2 cm", "D. No again"),
        ("A. Yes he is the GOAT", "B. No", "C. No, Mr. Thomas is better", "D. I don't know what to put"),
        ("A. Yes, he is with Mr. White and Mr. Escobar", "B. No, I love Mr. Saing!", "C. Ran out of ideas",
         "D. Ran out of ideas"),
        ("A. Yes, super funny!!", "B. No, his class is so boring", "C. I HATE SCHOOL GRRRRR", "D. I don't know"),
        ("A. YES SO MUCH I HATE HIM AHHH I HATE HIM SO MUCH", "B. No", "C. Sometimes", "D. I don't care"),
        ("A. No", "B. He's okay, the class is boring tho I ain't gon lie", "C. He's awesome", "D. Not really")
    )

    answers = ("C", "A", "A", "A", "A", "A", "B")
    score = 0

    for question_num, question in enumerate(questions):
        print("-----------------")
        print(question)
        for option in options[question_num]:
            print(option)
        guess = input("Enter (A, B, C, D): ").upper()

        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
            play_sound("correct")
        else:
            print("INCORRECT")
            print(f"{answers[question_num]} is the correct answer.")
            play_sound("wrong")

    print("-----------------------------------------")
    percentagesci = (score / len(questions)) * 100
    print(f"Your score is {score} out of {len(questions)} ({percentagesci:.2f}%)")

    if percentagesci == 100:
        print("You aced the test!")
        play_sound("finishquizhooray")
    elif percentagesci < 70:
        print("You failed the test!")
        play_sound("failedthequizstupid")


def runquizscience():
    questionsscience = (
        "What is the chemical symbol for Gold?",
        "What planet is known as the Red Planet?",
        "What is the powerhouse of the cell?",
        "What is H2O commonly known as?",
        "What is the most abundant gas in the Earth's atmosphere?",
        "What is the largest organ in the human body?",
        "What type of bond involves the sharing of electron pairs between atoms?"
    )

    optionsscience = (
        ("A. Au", "B. Ag", "C. Pb", "D. Fe"),
        ("A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"),
        ("A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Endoplasmic Reticulum"),
        ("A. Oxygen", "B. Water", "C. Hydrogen", "D. Carbon Dioxide"),
        ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
        ("A. Skin", "B. Liver", "C. Heart", "D. Brain"),
        ("A. Ionic bond", "B. Covalent bond", "C. Hydrogen bond", "D. Metallic bond")
    )

    answersscience = ("A", "A", "B", "B", "B", "A", "B")
    score = 0

    for question_num, question in enumerate(questionsscience):
        print("----------------")
        print(question)
        for option in optionsscience[question_num]:
            print(option)

        guesssci = input("Enter (A, B, C, D): ").upper()
        while guesssci not in ['A', 'B', 'C', 'D']:
            guesssci = input("Invalid input. Please enter (A, B, C, D): ").upper()

        if guesssci == answersscience[question_num]:
            score += 1
            print("CORRECT!")
            play_sound("correct")
        else:
            print("INCORRECT")
            print(f"{answersscience[question_num]} is the correct answer.")
            play_sound("wrong")

    print("-----------------------------------------")
    percentagesci = (score / len(questionsscience)) * 100
    print(f"Your score is {score} out of {len(questionsscience)} ({percentagesci:.2f}%)")

    if percentagesci == 100:
        print("You aced the test!")
        play_sound("finishquizhooray")
    elif percentagesci < 70:
        print("You failed the test!")
        play_sound("failedthequizstupid")


# Main function to select the quiz




BOLD = "\033[1m"
RESET = "\033[0m"
YELLOW = "\033[93m"


def main():
    while True:
        print("Select a quiz to take:")
        print("1. History (Hard)")
        print("2. History")
        print("3. Humor")
        print("4. Science")
        print("5. Quit")

        choice = input(f"{BOLD}Enter your choice: {RESET} ")

        if choice == '1':
            print("Starting the hard history test!")

            runquizhistoryHARD()
        elif choice == '2':
            print("Starting the history test!")
            run_quizhis()
        elif choice == '3':
            print("Starting the humor quiz!")
            run_quizhumor()
        elif choice == '4':
            print("Starting the science test!")
            runquizscience()
        elif choice == 'Quit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, please try again.")


# Run the main function
if __name__ == "__main__":
    main()
