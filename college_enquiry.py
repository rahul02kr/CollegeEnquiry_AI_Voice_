from datetime import datetime
import re
import speech_recognition as sr
import pyttsx3
import sqlite3
import cv2
from complaint import*
# from complaint import*

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Could you repeat?")
        return ""
    except sr.RequestError:
        print("Sorry, I'm unable to access the Google Speech Recognition API.")
        return ""

def handle_inquiry(query):
    if "admissions" in query:
        speak("For admission inquiries, please visit our college website or contact the admissions office.")

########################  HOD INFO ###############################
    elif 'Professor' in query or "Head of departments" in query:
        speak("You can see on screen")
        print('''Professor Miss. yogeshwari haridar
                Department : Computer
                Contact number :7620705249
           
                Professor Mr. Thorat Sir
                Department : Civil
                Contact No:7620705249"
              
                Professor miss. Nisha Shelar
                Department : EX&TC
                Contact No:7620705249")
             
                Professor miss Rupali Gayakvad
                Department : Mechanical
                Contact No:7620705249''')

   #############################################   #####################################################################
    elif "how much departments in this college" in query or "branch" in query:
        speak("there are six departments in this college COMPUTER,MECHANICAL,CIVIL,EX&TC,AI & ML,Data Science'")    
        print('''
                 1.COMPUTER
                 2.MECHANICAL
                 3.CIVIL
                 4.EX&TC
                 5.AI & ML
                 6.Data Science
                                  ''')
    elif "College opening time" in query or  "time of collge" in query:
        speak("opening time of college is : 9.45 AM ")
        print("opening time of college is : 9.45 AM ")
        
    elif "time of college" in query or "college time" in query:
        speak("opening time is : 9.45 AM "
              "Closing time is :5:00 PM")
        print("opening time of college is : 9.45 AM ")
        print("Closing time of college is :5:00 PM ")
    
    elif "where is principal office" in query or "principal cabin" in query:
        speak("left side in college front of enquiry cabin") #ADD
        speak("principal name is  Doctor DD shinde sir") #NAME
        speak("CABIN NUMBER :01")     # CABIN NO
        print("front of enquiry cabin") 
        print("CABIN NUMBER :01")
        print("PRINCIPAL NAME IS : Dr.D.D. shinde")

    elif "where is vice principal office" in query or "vice principal office" in query:
        speak("right side of college principal cabin") #ADD
        speak("vice principal name is  Doctor chavan sir") #NAME
        speak("CABIN NUMBER :02")     # CABIN NO
        print("Right side of principal cabin") 
        print("CABIN NUMBER :02")
        print("VICE PRINCIPAL NAME IS : Dr.CHAVAN SIR")   

    elif "where is computer department" in query or "comp" in query:
        speak("Third floor of the college") # ADD
        speak("H O D name is professor miss yogeshwari hardash mam")   # NAME HOD 
        print("Third floor of the college")  # ADD
        print("HOD:-Professor. Yogeshwari hardash mam")  # NAME OF HOD
        print("CABIN NO : H-318")           
          
    elif "where is mechanical department" in query or "mechanical" in query:
        speak("basement of the college") # ADD
        speak("H O D name is professor miss rupali")   # NAME HOD 
        print("basement of the college")  # ADD
        print("HOD:- Professor.Rupali chavan")  # NAME OF HOD
        print("Cabin NO:B-04")  #Cabin NO

    elif 'where is civil department' in query or "civil" in query:
        speak("basement the of college") # ADD
        speak("H O D is professor thorat sir")   # NAME HOD 
        print("Basement of the college")  # ADD
        print("HOD :-Professor Thorat sir")  # NAME OF HOD
        print("Cabin NO:B-14")  #Cabin NO
        
    elif 'where is EX&TC department' in query or "electronic and telecommunicaton department" in query:
        speak("Second floor of the college") # ADD
        speak("H O D is professor Nisha Shelar")   # NAME HOD 
        print("Second floor of the college")  # ADD
        print("HOD :-Professor Nisha Shelar")  # NAME OF HOD
        print("Cabin NO: H-300")  #Cabin NO

############################################ MEDITAION  ###################################################
               
    elif ' Address Of Dhyanpeeth' in query or "meditation hall" in query:
        speak("new meditation hall is front off G+2 boys hostel")   # for new
        speak("and old meditaion hall is back side of c wing hostel")   # for old
        print("new meditation hall is front off G+2 boys hostel")  # add
        print("and old meditaion hall is back side of c wing hostel")   # add

    elif "courses" in query:
        speak("We offer various undergraduate and graduate courses. You can find detailed information on our college website.")

    elif "Intake" in query:
        speak("1.Computer=100, 2.Mechanical=60, 3.Civil=60, 4.Ex&Tc=60")
        print('''1.Computer=100 
                 2.Mechanical=60
                 3.Civil=60 
                 4.Ex&Tc=60''')
    
    elif "Toppers" in query or "topper of the year " in query:
        speak("These are toppers")
        print('''               #### Toppers ####
              
                 |NAME OF THE STUDENTS  |DEPARTMENTS|  CLASS |  CGPA  |
              ------------------------------------------------------
                 | Sani Desale          | COMPUTER  |    BE  | 9.34   | 
                 | Tanmay Pawar         | COMPUTER  |    TE  | 9.55   | 
                 | Vivek Gadhe          | COMPUTER  |    SE  | 8.95   |
                 | Karan Patil          | EX&TC     |    BE  | 8.96   |
                 | Rituraj Patil        | EX&TC     |    TE  | 9.45   |
                 | Ram Patl             | EX&TC     |    SE  | 8.50   |
                ''')
    
    elif "contact" in query:
        speak("You can contact our college")
        print(" 077200 12139")
    
    elif "how many Students" in query or "Students count" in query or "number of students in college" in query:
        speak("You can contact our college")
        print(" 077200 12139")
    
    elif "location" in query:
        speak("Our college is located at H742+63R, Maharashtra State Highway 79, Mohili, Mohili, Maharashtra 421601")
    
    elif "library" in query or "library time" in query:
        speak("The college library is open from 9:00 AM , Monday to Saturday.")
        
    elif "Where is library" in query:
        speak("third floar of the college")
        print("Third Floar Of The College.")
        
    elif "incharge of lab" in query:
        speak("miss Jyoti is the incharge of computer lab")
        print("miss Jyoti is the incharge of computer lab")
    
    elif "events" in query or "activities" in query:
        speak("We have various events and activities throughout the academic year. Please check our college website  https://www.vishwatmakengg.in/.")
        print("https://www.vishwatmakengg.in/")
    
    elif "fees" in query or "financial aid" in query:
        speak("Tuition fees vary depending on the program. You can find detailed information about fees, scholarships, and financial aid options on our college faculties.")
    
    elif "college website" in query or "webiste" in query:
        speak(" https://www.vishwatmakengg.in")
        print(" https://www.vishwatmakengg.in/")
        
    elif "developer" in query:
        speak("mr. RAHUL RATHOD")
        print("mr. RAHUL RATHOD")
        

    # elif "take complaint" in query or "take my complaint" in query or "complaint" in query:
    #        complaint()


    elif "thank you" in query:
        speak("You're welcome!")
    
    else:
        speak("I'm sorry, I couldn't understand your inquiry.")

def validate_mobile_number(phone):
    pattern = re.compile(r'^\d{10}$')
    return pattern.match(phone) is not None

def get_user_info():
    
    speak("Before we start, can you please provide me with your information?")
    while True:
        fname= input("First Name:")
        fname = fname.upper()
        if fname.isalpha():     
           break
        else:
            speak("Sorry, I didn't catch that. Please tell me your  first name again.")
    while True:
        lname= input("Last Name:")
        lname = lname.upper()
        if lname.isalpha():     
           break
        else:
            speak("Sorry, I didn't catch that. Please tell me your  last name again.")        
    
    speak(f"Hello, {fname}{lname}! Can you please provide me with your address?")
    while True:
        address = input("Enter your Address:")
        if address.isalpha():    
            break
        else:
            speak("Sorry, I didn't catch that. Please tell me your address again.")

    speak("Thank you. Can you please provide me with your phone number?")
    while True:
        phone = input("Enter Your Mobile No:")
        pattern = re.compile(r'^\d{10}$')
        if validate_mobile_number(phone):
               phone = int(phone) 
               break
        else:
            speak("Sorry, I didn't catch that. Please tell me your phone again.")
        
   
    speak("Is there reason of visit college?")
    while True:
        reason =input("Enter Reason of college visit:")
        if reason.isalpha():  
            break
        else:
            speak("Sorry, I didn't catch that. Please tell me reason again.")

  
    return fname,lname, address, phone, reason

def save_to_database(fname,lname, address, phone, reason,image_path):
    conn = sqlite3.connect('user_info.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (FNAME TEXT,LNAME TEXT, ADDRESS TEXT, PHONE INTEGER, REASON TEXT, DATE TEXT, TIME TEXT,image_path)''')
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    c.execute("INSERT INTO users (fname,lname, address, phone, reason, date, time,image_path) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (fname,lname, address, phone, reason, current_date, current_time,image_path))
    conn.commit()
    conn.close()

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    image_path = f"image/captured_image.jpg"
    cv2.imwrite(image_path, frame)
    cap.release()
    return image_path

def college_inquiry():
    fname,lname, address, phone, reason = get_user_info()
    image_path = capture_image()
    save_to_database(fname,lname, address, phone, reason, image_path)
   
    speak("Your information has been saved. Welcome{fname}{lname}in atma malik insitute of technology and research Center. i am Inquiry Assistant. How can I help you?")
    while True:
        command = listen()
        if "hey assistant" in command or "can you help me" in command:
            speak("Yes, I'm here to assist you. What can I do for you?")
        #     while True:
        #         query = listen()
        #         if query == "thank you":
        #             speak("have nice day")
        #             return
        #         else:
        #             handle_inquiry(query)
        # elif command == "thank you!":
        #     speak("have a nice day")
        #     return
        else:
            continue

if __name__ == "__main__":
    college_inquiry()
