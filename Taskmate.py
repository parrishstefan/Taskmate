# TODO AFTER EVERYTHING IS DONE
# INPUT VALIDATION - FROM->TO TIME MUST BE POSITIVE, HOURS MUST BE > 0, EVENT AND DESCRIPTION CAN'T BE NULL
# CONVERT FROM->TO TIME TO INTEGERS FOR ALGO
# FIGURE OUT A GOOD AMOUNT OF POTENTIAL SCHEDULES
# MAYBE DO A LONG LIST OF SCROLLABLE WITH JUST #S FOR EACH, THEN USER INPUTS A NUMBER?



# NEW STUFF NEEDED FOR TOMORROW
# FIGURE OUT WAY TO CALL FUNCTION WHEN PAGE LOADS INSTEAD OF BUTTON 




import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                             QLabel, QStackedWidget, QLineEdit, QCalendarWidget,
                             QSplashScreen, QMainWindow, QMessageBox, QDateTimeEdit, 
                             QScrollArea, QSpinBox, QComboBox, QTimeEdit)
from PyQt6.QtGui import QIcon, QFont, QFontDatabase, QPixmap, QColor, QPalette
from PyQt6.QtCore import Qt

from itertools import permutations

userInfo = {"Activity": [], "Description": [],"Hours": [], "Day": []}
available_hours = {}
tasks = {}
eventsAdded = 0

class Page1(QWidget):
    def __init__(self):
        super().__init__()

        bg1 = QWidget(self)
        # self.setCentralWidget(bg1)

        # bg1.setStyleSheet("background-color: #F1F6F9;")
        # bg1.setGeometry(0,0, 850, 500)

        taskMateLabel = QLabel("Task Mate", self)
        taskMateLabel.move(400, 20)

        # Font Size
        headerFont = QFont()
        headerFont.setBold(True)
        headerFont.setPointSize(20)

        # Font Color
        taskMateLabel.setFont(headerFont)
        taskMateLabel.setStyleSheet("color: black")

        # Create Event
        eventLabel = QLabel("Event Name", self)
        eventLabel.move(50, 100)
        eventLabel.setStyleSheet("color: black")

        # Textbox for Event Name
        eventTextBox = QLineEdit(self)
        eventTextBox.move(120, 100)
        eventTextBox.setFixedWidth(200)
        eventTextBox.setFixedHeight(20)

        # Hours
        hoursLabel = QLabel("How many hours for this task?", self)
        hoursLabel.move(50, 150)
        hoursBox = QSpinBox(self)
        hoursBox.move(50, 170)

        # Day of the Week
        dayLabel = QLabel("Which day would you like to do the task?", self)
        dayLabel.move(220, 200)
        
        dayComboBox = QComboBox(self)
        dayComboBox.addItems(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
        dayComboBox.move(220, 220)
        dayComboBox.textActivated[str].connect(self.onActivated)

        self.dayText = QLabel('Sunday', self)
        self.dayText.move(-5000,-5000)
        

        # Time Available
        timeLabel = QLabel("Which hours are you available?", self)
        timeLabel.move(50, 200)
        fromTimeEdit = QTimeEdit(self)
        fromTimeEdit.setDisplayFormat("HH:mm")
        fromTimeEdit.move(50, 220)

        toLabel = QLabel("->", self)
        toLabel.move(105, 220)

        toTimeEdit = QTimeEdit(self)
        toTimeEdit.move(120, 220)
        toTimeEdit.setDisplayFormat("HH:mm")

        # Descriptions
        descriptionLabel = QLabel("Notes or Descriptions", self)
        descriptionLabel.move(50, 250)
        descriptionLabel.setStyleSheet("color: black")

        # Textbox for Note and Description
        descriptionTextBox = QLineEdit(self)
        descriptionTextBox.move(50, 270)
        descriptionTextBox.setFixedWidth(300)
        descriptionTextBox.setFixedHeight(150)

        # Add Task
        addTaskButton = QPushButton("Add Task", self)
        addTaskButton.move(50, 440)
        addTaskButton.clicked.connect(lambda: self.addTask(eventTextBox, descriptionTextBox, hoursBox, fromTimeEdit, toTimeEdit, dayLabel, dayComboBox, timeLabel, toLabel))

        # Submit
        submitButton = QPushButton("Submit", self)
        submitButton.move(150, 440)
        submitButton.clicked.connect(lambda: self.goToPage2(dayLabel, dayComboBox, timeLabel, fromTimeEdit, toTimeEdit, toLabel))

        # Set app background
        # self.setStyleSheet("background-image: url('app_bg.jpg');")
        # self.setStyleSheet("background-color: #FEE8B0;")

        # Set developer notes
        btn0 = QPushButton("?", self)
        btn0.clicked.connect(lambda: QMessageBox.information(None, '', 'Version 1.0 (March 7th, 2023)'
                                                                       '\n'
                                                                       '\n- Task creation page developed with limited UI elements'
                                                             '\n- User input validation'
                                                             '\n- Multiple task creation capabilities added'
                                                             '\n- Checkbox integration for days of the week'
                                                             '\n- Console log output for task management for the time being'))
        btn0.move(800, 460)
    
    def onActivated(self, text):
        self.dayText.setText(text)
        self.dayText.adjustSize()

    def addTask(self, eventTextBox, descriptionTextBox, hoursBox, fromTimeEdit, toTimeEdit, dayLabel, dayComboBox, timeLabel, toLabel):
        global eventsAdded

        dayLabel.move(-5000,-5000)
        dayComboBox.move(-5000,-5000)
        timeLabel.move(-5000, -5000)
        fromTimeEdit.move(-5000,-5000)
        toTimeEdit.move(-5000,-5000)
        toLabel.move(-5000,-5000)

        event = eventTextBox.text()
        description = descriptionTextBox.text()
        hours = hoursBox.text()
        day = self.dayText.text()
        fromTime = int(fromTimeEdit.text()[:2])
        toTime = int(toTimeEdit.text()[:2])

        userInfo["Activity"].append(event)
        userInfo["Description"].append(description)
        userInfo["Hours"].append(hours)
        userInfo["Day"].append(day)

        available_hours[day] = (fromTime, toTime)

        tasks[event] = int(hours)

        eventsAdded += 1

        # print(eventsAdded)
        # print(available_hours)
        # print(f"{fromTime} -> {toTime}")
        # print(hours)
        # print(event)
        # print(description)
        # print(day)

    def goToPage2(self, dayLabel, dayComboBox, timeLabel, fromTimeEdit, toTimeEdit, toLabel):
        stacked_widget.setCurrentWidget(page2)

        dayLabel.move(220, 150)
        dayComboBox.move(220, 170)
        timeLabel.move(50, 200)
        fromTimeEdit.move(50, 220)
        toTimeEdit.move(120, 220)
        toLabel.move(105, 220)

        print(userInfo)

# Pop up window


# Page 2
class Page2(QWidget):
    def __init__(self):
        super().__init__()

        label4 = QLabel("Choose Your Schedule", self)
        label4.move(350, 20)

        label0 = QLabel("Need algorithm here", self)
        label0.move(350, 150)

        # Font

        font1 = QFont()
        font1.setBold(True)
        font1.setPointSize(20)

        # Set Font
        label4.setFont(font1)

        button = QPushButton("next", self)
        button.move(50, 400)
        #button.clicked.connect(self.go_to_page3)
        button.clicked.connect(self.generateSchedule)
    
    def deleteThisAfter(self):
        print(tasks)
    
    def generateSchedule(self):
        # generate all possible task orders
        task_orders = permutations(tasks.keys())

        # generate all possible schedules for each day
        schedules = {}
        for day, hours in available_hours.items():
            schedules[day] = []
            for task_order in task_orders:
                schedule = {}
                current_time = hours[0]
                for task in task_order:
                    duration = tasks[task]
                    if current_time + duration > hours[1]:
                        break
                    schedule[task] = (current_time, current_time + duration)
                    current_time += duration
                else:
                    schedules[day].append(schedule)

        # print all possible schedules for each day
        for day, day_schedules in schedules.items():
            print(f"{day}:")
            if len(day_schedules) == 0:
                print("  No valid schedules found.")
            else:
                for i, schedule in enumerate(day_schedules):
                    print(f"  Schedule {i + 1}:")
                    for task, (start_time, end_time) in schedule.items():
                        print(f"    {task}: {start_time}-{end_time}")
                    print()

    def go_to_page3(self):
        stacked_widget.setCurrentWidget(page3)

class Page3(QWidget):
    def __init__(self):
        super().__init__()

        label4 = QLabel("Your Schedule", self)
        label4.move(400,20)

        # Font

        font1 = QFont()
        font1.setBold(True)
        font1.setPointSize(20)

        # Set Font
        label4.setFont(font1)

        # Calendar View
        cal = QCalendarWidget(self)

        cal.setSelectedDate(cal.selectedDate())
        label5 = QLabel()
        label5.setText("Selected Date: " + cal.selectedDate().toString())
        cal.move(250, 150)

        button = QPushButton("Back", self)
        button.move(50, 400)
        button.clicked.connect(self.go_to_page1)



    def go_to_page1(self):
        stacked_widget.setCurrentWidget(page1)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the pages
    page1 = Page1()
    page2 = Page2()
    page3 = Page3()

    # Create the stacked widget and add the pages to it
    stacked_widget = QStackedWidget()
    stacked_widget.addWidget(page1)
    stacked_widget.addWidget(page2)
    stacked_widget.addWidget(page3)
    stacked_widget.setCurrentWidget(page1)

    stacked_widget.setGeometry(300, 300, 850, 500)

    # Show the stacked widget

    stacked_widget.show()

    sys.exit(app.exec())
