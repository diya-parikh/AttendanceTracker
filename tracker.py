import cv2
import sys
import numpy
import os
import datetime
from cv2 import face

haar_file = r'/Users/diyaparikh/Desktop/CV/haarcascade_frontalface_default.xml'
print("Hello user!!")

# while loop for continuous interaction loop with the user with four different options
# 1. Logging into an existing account   
# 2. Creating a new account.  
# 3. Starting attendance directly with an account name.
# 4. Exiting the program. 
while True:
    print("\nEnter 1 if you want to log into your account.")
    print("Enter 2 if you want to create an account.")
    print("Enter 3 if you want to start the attendance with the account name directly.")
    print("Enter 4 to exit.")

    u_choice = input("Your choice: ")

    if u_choice == '1':
        user_user = input("Please enter your account name: ")
        user_pass = input("Please enter your password: ")

        # Read account data
        with open('U_data.txt', 'r') as f:
            line = f.readline()
            u_data = []
            while line:
                u_data.append(line.split(','))
                line = f.readline()
                
        with open('P_data.txt', 'r') as f:
            line = f.readline()
            p_data = []
            while line:
                p_data.append(line.split(','))
                line = f.readline()

        if u_data and user_user in u_data[0]:
            index = u_data[0].index(user_user)
            if p_data[0][index] == user_pass:
                print(f"SUCCESSFULLY LOGGED IN\nWelcome back to {user_user}")
                while True:
                    print("\nEnter 1 if you want to start attendance.")
                    print("Enter 2 if you want to setup another identity.")
                    print("Enter 3 if you want to log out.")
                    print("Enter 4 if you want to Exit.")
                    ur_input = input("Your choice: ")
                    datasets = '/Users/diyaparikh/Desktop/CV/' + user_user
                    
                    if ur_input == "1":
                        print("Enter 'esc' to exit")
                
                        print("Starting attendance please be in sufficient lights...")
                        ready = input("Press enter when you are ready: ")
                        count = -1
                        prediction_list = []
                        (images, labels, names, id) = ([], [], {}, 0)

                        for (subdirs, dirs, files) in os.walk(datasets):
                            for subdir in dirs:
                                names[id] = subdir
                                subjectpath = os.path.join(datasets, subdir)
                                for filename in os.listdir(subjectpath): 
                                    path = subjectpath + '/' + filename 
                                    label = id
                                    images.append(cv2.imread(path, 0))
                                    labels.append(int(label)) 
                                id += 1
                        (width, height) = (184, 224) 
                        (images, labels) = [numpy.array(lis) for lis in [images, labels]]
                        face_cascade = cv2.CascadeClassifier(haar_file)
                        model = cv2.face.LBPHFaceRecognizer_create() 
                        model.train(images, labels) 
                        webcam = cv2.VideoCapture(0)

                        frame_count = 0  # Frame counter for skipping frames
                        while True:
                            (_, im) = webcam.read() 
                            frame_count += 1
                            
                            # Skip frames to improve performance
                            if frame_count % 5 != 0:
                                continue
                            
                            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
                            
                            # Contrast enhancement using CLAHE
                            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
                            gray = clahe.apply(gray)

                            # Detect faces
                            faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
                            for (x, y, w, h) in faces: 
                                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2) 
                                face = gray[y:y + h, x:x + w] 
                                face_resize = cv2.resize(face, (width, height)) 
                                prediction = model.predict(face_resize)
                                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)

                                def attendance():
                                    if count >= 15:  
                                        for i in range(15, 0, -1):
                                            if prediction_list[i] == prediction_list[i - 1]:
                                                dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                                present = prediction_list[count]
                                                d = dt[0:10]
                                                t = dt[11:19]
                                                space = 25 - len(prediction_list[count])
                                                
                                                with open("Date_data.txt", "r") as f:
                                                    line = f.readline()
                                                    d_data = []
                                                    while line:
                                                        d_data.append(line.split(','))
                                                        line = f.readline()
                                                
                                                with open("Name_data.txt", "r") as f:
                                                    line = f.readline()
                                                    line = str(line)
                                                    n_data = []
                                                    while line:
                                                        n_data.append(line.split(','))
                                                        line = f.readline()
                                                
                                                def upload_print():
                                                    with open('Attendance_data.txt', 'a') as f:
                                                        f.write(prediction_list[count] + ' ' * (space) + d + ' ' * 6 + t + '\n')
                                                    print('Attendance taken:')
                                                    print(prediction_list[count])
                                                    print(dt)
                                                    
                                                    if d_data == []:
                                                        with open('Date_data.txt', 'a') as f:
                                                            f.write(d + ',')
                                                        with open('Name_data.txt', 'a') as f:
                                                            f.write(prediction_list[count] + ',')
                                                    elif d_data[0][-1] == d:
                                                        with open('Date_data.txt', 'a') as f:
                                                            f.write(d + ',')
                                                        with open('Name_data.txt', 'a') as f:
                                                            f.write(prediction_list[count] + ',')
                                                    else:
                                                        with open('Date_data.txt', 'w') as f:
                                                            f.write(d + ',')
                                                        with open('Name_data.txt', 'w') as f:
                                                            f.write(prediction_list[count] + ',')
                                                
                                                if d_data != []:
                                                    number_of_same_dates = d_data[0].count(d)
                                                    if d in d_data[0]:
                                                        index_names = d_data[0].index(d)
                                                        name_check = []
                                                        for i in range(number_of_same_dates):
                                                            names = n_data[0][index_names + i]
                                                            name_check.append(names)
                                                        if prediction_list[count] in name_check:
                                                            cv2.putText(im, "Thank you! Your attendance has already been taken",
                                                                        (x - 60, y - 35), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 225))
                                                        else:
                                                            upload_print()
                                                    else:
                                                        upload_print()
                                                else:
                                                    upload_print()

                                if prediction[1] < 40: 
                                    cv2.putText(im, 'not recognized', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))  
                                else:
                                    count += 1
                                    cv2.putText(im, '% s - %.0f' % (names[prediction[0]], prediction[1]), 
                                                (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
                                    prediction_list.append(names[prediction[0]])
                                    attendance()

                            # Display processed frame
                            cv2.imshow('SmartCam', im)
                            key = cv2.waitKey(10) 
                            if key == 27: 
                                break

                        webcam.release()
                        cv2.destroyAllWindows()

                    elif ur_input == "2":
                        while True:
                            sub_data = input("Enter the name of the person or if you want to change in any existing face identity(Under 25 characters): ")
                            if len(sub_data) <= 25:
                                break

                        print("Please be in sufficient lights...")
                        ready = input("Press enter when you are ready: ")

                        path = os.path.join(datasets, sub_data)
                        if not os.path.isdir(path):
                            os.mkdir(path) 

                        (width, height) = (184, 224)     
                        face_cascade = cv2.CascadeClassifier(haar_file) 
                        webcam = cv2.VideoCapture(0)  
                        count = 1
                        while count < 15:  
                            (_, im) = webcam.read()
                            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
                            faces = face_cascade.detectMultiScale(gray, 1.3, 4) 
                            for (x, y, w, h) in faces: 
                                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2) 
                                face = gray[y:y + h, x:x + w] 
                                face_resize = cv2.resize(face, (width, height)) 
                                cv2.imwrite('%s/%s.png' % (path, count), face_resize) 
                            count += 1
                            cv2.imshow('SmartCam', im)
                            key = cv2.waitKey(100) 
                            if key == 27: 
                               break
                        webcam.release()
                        cv2.destroyAllWindows()

                    elif ur_input == "3":
                        print("Logging out.")
                        break

                    elif ur_input == "4":
                        print("Exiting the program.")
                        sys.exit()

                    else:
                        print("Invalid input!")

            else:
                print("Incorrect password!")
        else:
            print("Account does not exist!")

    elif u_choice == '2':
        print("Please provide the details.")
        user_user = input("Enter your username: ")
        user_pass = input("Enter your password: ")
        
        with open('U_data.txt', 'r') as f:
            line = f.readline()
            u_data = []
            while line:
                u_data.append(line.split(','))
                line = f.readline()

        with open('P_data.txt', 'r') as f:
            line = f.readline()
            p_data = []
            while line:
                p_data.append(line.split(','))
                line = f.readline()

        if u_data == []:
            with open('U_data.txt', 'a') as f:
                f.write(user_user + ',')
            with open('P_data.txt', 'a') as f:
                f.write(user_pass + ',')
            print("Account created successfully.")
        elif user_user in u_data[0]:
            print("Account already exists!")
        else:
            with open('U_data.txt', 'a') as f:
                f.write(user_user + ',')
            with open('P_data.txt', 'a') as f:
                f.write(user_pass + ',')
            print("Account created successfully!")

    elif u_choice == '3':
        print("You chose to start attendance directly.")
        # Enter code for direct attendance here...

    elif u_choice == '4':
        print("Exiting program!")
        sys.exit()

    else:
        print("Invalid input! Try again.")
