from tkinter import Image
import customtkinter
import customtkinter as ctk
from PIL import Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pygame
import os
import time
import random





pygame.init()
pygame.mixer.init()



quiz = False



def clearscreen():
    for widget in root.winfo_children():
        widget.destroy()


errorwindow = customtkinter.CTk()
errorwindow.geometry("350x200")
errorwindow.title("Error Screen")
correctsoundpath = "correct answer sound effect.mp3"
incorrectsoundpath = "incorrect sound effect.mp3"
def loadsound(filename):
    if os.path.exists(filename):
        return pygame.mixer.Sound(filename)
    else:
        errorwindow.mainloop()




def playsoundcorrect():
    correctbuzzer.set_volume(0.5)
    correctbuzzer.play()
def playsoundincorrect():
    incorrectbuzzer.set_volume(0.1)
    incorrectbuzzer.play()





def togglefullscreen(event=None):
    isfullscreen = root.attributes("-fullscreen")
    root.attributes("-fullscreen", not isfullscreen)
    if not isfullscreen:
        root.eval('tk::placeWindow . center')




# Load the image
imagePath = "quiz.png"
quizImage = ctk.CTkImage(Image.open(imagePath), size=(600, 400))

imagePath = "gradient.png"

# Initialize the main window
root = customtkinter.CTk()
root.title("Welcome Screen!")

screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()








audiofilemissingtext = customtkinter.CTkLabel(errorwindow, text="You got a rare error, one or more audio files is missing \n in this installation."
                                                         "Please restart the app or refer to the Github. \n \n You are missing one or more audio files.", wraplength=400)
audiofilemissingtext.place(x=0, y=25)

correctbuzzer = loadsound(correctsoundpath)
incorrectbuzzer = loadsound(incorrectsoundpath)



windowwidth = 800
windowheight = 400


xpos = int((screenwidth - windowwidth) / 2)
ypos = int((screenheight - windowheight) / 2)



root.geometry(f"{windowwidth}x{windowheight}+{xpos}+{ypos}")

root.geometry("800x400")
root.bind("<F11>", togglefullscreen)
root.configure(fg_color="#E1E8EB")  # Set background color to light blue




# Questions
history_questions = [
    {"question": "Who was the first President \n of the United States?", "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], "answer": "George Washington"},
    {"question": "In what year did World War II end?", "options": ["1945", "1939", "1918", "1941"], "answer": "1945"},
    {"question": "What empire was ruled by Julius \n Caesar?", "options": ["Mongol Empire", "Roman Empire", "British Empire", "American Revolution"], "answer": "Roman Empire"},
    {"question": "What was the name of the ship that \n carried the Pilgrims to America?", "options": ["Mayflower", "Thousand Sunny", "Santa Maria", "Expedition"], "answer": "Mayflower"}


]

science_questions = [
    {"question": "What is the chemical \n symbol for water?", "options": ["H2O", "O2", "CO2", "NaCl"], "answer": "H2O"},
    {"question": "What planet is known as \n the Red Planet?", "options": ["Jupiter", "Venus", "Mars", "Saturn"], "answer": "Mars"},
    {"question": "What is the chemical symbol\n for gold?", "options": ["Au", "Ag", "Fe", "Pb"], "answer": "Au"},
    {"question": "What is the boiling \n point of water in \n       Celsius?", "options": ["0°C", "50°C", "100°C", "200°C"], "answer": "100°C"},
    {"question": "            What gas do plants \nabsorb from the atmosphere \nfor photosynthesis?", "options": ["Nitrogen", "Oxygen", "Hydrogen", "None of the above"], "answer": "None of the above"}
]




math_questions = [

    {"question": "What is 5 + 3?", "options": ["20", "5.5", "8", "69.420"], "answer": "8"},
    {"question": "What is 9 - 15?", "options": ["-6", "-4", "6", "4"], "answer": "-6"},
    {"question": "Solve for x: 2x + 5 = 13", "options": ["12", "6", "4", "10"], "answer": "4"},
    {"question": "What is the square root of 64?", "options": ["4", "15", "8", "1"], "answer": "8"},
    {"question": "What is the first three digits of PI?", "options": ["6.28", "3.14", "2.17", "6.40"], "answer": "3.14"},








]















incorrectanswertotal = 0
correctanswertotal = 0

# Initialize indexes and quiz selector
questionindex = 0
optionindex = 0
current_quiz = None  # Track the currently selected quiz
def toggle_fullscreen(event=None):
    is_fullscreen = root.attributes("-fullscreen")
    root.attributes("-fullscreen", not is_fullscreen)
root.bind("<F11>", toggle_fullscreen)


root.bind("<Escape>", togglefullscreen)









def startSciquiz():

    global questionindex, optionindex, current_quiz, quiz
    current_quiz = science_questions  # Set the quiz to science
    questionindex = 0  # Reset the index when starting the quiz
    optionindex = 0
    quiz = True
    root.title("Science Quiz")
    root.attributes("-fullscreen", True)
    clearscreen()
    loadquestion(questionindex)


def fade_out(widget, step=0.1):

    alpha = 1.0
    while alpha > 0:
        widget.configure(fg_color=f"rgba(0, 0, 0, {alpha})")
        root.update()
        alpha -= step

def quizselectionmenu():
    global quizSelectionlabel, sciencequizstartlabel, historyquizstartlabel, quiz, mathquizstartlabel
    root.geometry("1100x650")
    root.attributes("-fullscreen", False)
    root.title("Selection Menu")
    if quiz == True:
        resultlabel.destroy()
        takebacklabel.destroy()
        button.destroy()
        correctanswertotal = 0
        incorrectanswertotal = 0

    label.destroy()
    startbutton.destroy()









    quizSelectionlabel = ctk.CTkLabel(root, font=("Arial", 60), text="Select a quiz!")
    quizSelectionlabel.place(x=380, y=50)

    sciencequizstartlabel = ctk.CTkButton(root, font=("Arial", 90), text="Science!", anchor="center", corner_radius=20, command=startSciquiz)
    sciencequizstartlabel.place(x=10, y=400)

    historyquizstartlabel = ctk.CTkButton(root, font=("Arial", 90), text="History!", anchor="center", corner_radius=20, command=startHisquiz)
    historyquizstartlabel.place(x=400, y=400)

    mathquizstartlabel = ctk.CTkButton(root, font=("Arial", 90), text="Math!", anchor="center", corner_radius=20, command=startMathquiz)
    mathquizstartlabel.place(x=750, y=400)

def startquizmenu():
    global label, startbutton, imagePath, quizstartimage
    label = customtkinter.CTkLabel(root, font=("Arial", 60), text="Welcome to the Quiz!", anchor="center")
    label.place(x=120, y=0)

    startbutton = customtkinter.CTkButton(root, font=("Arial", 150), text="START", corner_radius=500, width=650, anchor="center", command=quizselectionmenu)
    startbutton.place(x=70, y=150)

def checkanswer(selectedoption, correctanswer):
    global incorrectanswertotal, resultlabel, correctanswertotal
    if selectedoption == correctanswer:
        playsoundcorrect()
        resulttext = "Correct!"
        resultcolor = "green"
        correctanswertotal += 1

    else:
        playsoundincorrect()
        resulttext = "Incorrect!"
        incorrectanswertotal += 1
        resultcolor = "red"

    # Show result
    resultlabel = customtkinter.CTkLabel(root, font=("Arial", 80), corner_radius=20, text=resulttext, fg_color=resultcolor)
    resultlabel.place(x=750, y=300)

    # Wait a second before showing the next question
    root.after(1000, resultlabel.destroy)
    root.after(1000, loadnextquestion)

def startHisquiz():
    global questionindex, optionindex, current_quiz, quiz
    quiz = True
    current_quiz = history_questions  # Set the quiz to history
    root.title("History Quiz")
    root.geometry("1920x1800")
    root.attributes("-fullscreen", True)
    questionindex = 0  # Reset the index when starting the quiz
    optionindex = 0
    clearscreen()
    loadquestion(questionindex)

def startMathquiz():
    global questionindex, optionindex, current_quiz, quiz, mathquizstartlabel
    current_quiz = math_questions
    questionindex = 0
    optionindex = 0
    quiz = True
    root.title("Math Quiz")
    root.attributes("-fullscreen", True)
    quizSelectionlabel.destroy()
    sciencequizstartlabel.destroy()
    historyquizstartlabel.destroy()
    loadquestion(questionindex)
    mathquizstartlabel.destroy()


def countdowntime(seconds):
    if seconds > 0:
        takebacklabel.configure(
            text=f"Taking you back to quiz selection screen in {seconds} seconds."
        )
        root.after(1000, countdowntime, seconds - 1)  # Call `countdowntime` again after 1 second
    else:
        takebacklabel.configure(text="Returning to quiz selection screen now!")
        clearscreen()
        root.attributes("-fullscreen", False)
        displaypiechart()
def loadnextquestion():
    global questionindex, takebacklabel  # Declare takebacklabel as global
    questionindex += 1
    if questionindex < len(current_quiz):  # Check if there are more questions
        loadquestion(questionindex)
    else:
        # Quiz complete
        clearscreen()
        resulttext = "Quiz Complete! (this took me forever to make)"
        resultcolor = "lightblue"
        resultlabel = customtkinter.CTkLabel(root, font=("Arial", 70), text=resulttext,anchor="center", corner_radius=20, fg_color=resultcolor)
        resultlabel.place(x=150, y=500)

        # Create the countdown label
        takebacklabel = customtkinter.CTkLabel(root, font=("Arial", 50), anchor="center",corner_radius=20, text="", fg_color=resultcolor)
        takebacklabel.place(x=220, y=600)
        countdowntime(5)  # Start the countdown










def gobacktomenu():
    clearscreen()
    quizselectionmenu()













def loadquestion(index):
    global questionlabel, option_buttons, button  # Use global references to modify existing widgets

    # Clear previous question and options if they exist
    if 'questionlabel' in globals():
        questionlabel.destroy()
    if 'option_buttons' in globals():
        for button in option_buttons:
            button.destroy()

    # Get question data
    questiondata = current_quiz[index]  # Use the current quiz
    questiontext = questiondata["question"]
    options = questiondata["options"]
    correctanswer = questiondata["answer"]

    # Display the new question
    questionlabel = customtkinter.CTkLabel(root, font=("Arial", 100), text=questiontext)
    questionlabel.place(x=250, y=50)

    # Display the options
    option_buttons = []  # Store the buttons for later removal
    for i, option in enumerate(options):
        button = customtkinter.CTkButton(root,
                                         font=("Arial", 80),
                                         text=option,
                                         width=800,  # Set the same width for all buttons
                                         height=100,
                                         corner_radius=20,# Set the same height for all buttons
                                         anchor="center",  # Ensure the text is centered
                                         command=lambda opt=option: checkanswer(opt, correctanswer))
        button.place(x=500, y=500 + (i * 150))  # Adjust the y position as needed
        option_buttons.append(button)


def displaypiechart():
    clearscreen()
    labels = ['Correct Answers', 'Incorrect Answers']
    sizes = [correctanswertotal, incorrectanswertotal]
    colors = ['#03fc13', '#fc0303']
    explode = (0.1, 0)

    fig = Figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')


    chartwindow = customtkinter.CTkToplevel(root)
    chartwindow.attributes("-topmost", True, "-fullscreen", True)
    chartwindow.title("Results Screen")
    chartwindow.geometry("700x700")



    canvas = FigureCanvasTkAgg(fig, chartwindow)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
    backbutton = customtkinter.CTkButton(chartwindow, text="Go Back To Menu", command=gobacktomenu)
    backbutton.place(x=550, y=20)


    def onclose():
        chartwindow.destroy()
        quizselectionmenu()

    chartwindow.protocol("WM_DELETE_WINDOW", onclose)


































random.shuffle(math_questions)
random.shuffle(history_questions)



startquizmenu()
root.mainloop()

print(incorrectanswertotal, "INCORRECT")
print(correctanswertotal, "CORRECT")