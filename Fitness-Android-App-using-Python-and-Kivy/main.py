#===========================================================================================================#
"""
   COURSE-SECTION: BSCPE 2-2
   SUBJECT: SOFTWARE DEVELOPMENT
   GROUP MEMBERS:
           DIBANSA, RAHMANI 
           NAVARRO, KAREN
           PALATTAO, LARRY SIMOUN
           AQUINO, NIKKO LEO
   BRIEF DESCRIPTION OF THE PROGRAM:
           THIS PROGRAM IS A FITNESS APP AIMED TO PROVIDE ITS USERS THE LEISURE AND CONVENIENCE OF FINDING
       SUITABLE EXERCISES. THIS PROGRAM IS MADE USING PYTHON, KIVY, AND ITS DEPENDENCIES TO PROVIDE A
       MULTI-PLATFORM ACCESS TO THE APPLICATION'S USERS.
           THIS FITNESS ANDROID APPLICATION IS A MIDTERM PROJECT FOR THE SOFTWARE DEVELOPMENT SUBJECT. THE
       PROGRAM WILL BE ASSESSED AND GRADED USING THE ESTABLISHED CRITERIA BEFOREHAND.
       
 REPRESENTATION OF THE CONNECTION OF THE PROGRAM'S SCREENS/WINDOWS.
	,->startup_screen <--------------------------------( LOG OUT )--------------------------------------------,
	|			↑						                                  |
	|			'---->login_screen -----> main_screen ------------------------------------------->|
	'-----> SignUpScreen				  ↑	 ↑                                                |
							  |	 '----------------> report_screen --------------->|
							  |			     ↑                            |
							  '----> selected_workout ---'--------------------------->|
							  |  	  |                                               |
							  '-------'----> workout_screen                           |
							  | 		      |                                   |
							  '-------------------'----> congratulation_screen ------>'
"""
#===========================================================================================================#

#========== IMPORTING NECESSARY PYTHON MODULES ==========#
"""
 THE MODULES BELOW ARE BUILT IN PYTHON MODULES.
 THERE'S NO NEED TO INSTALL THESE MODULES.
"""
import random
import sys
import os
from datetime import datetime


#==========  IMPORTING NECESSARY KIVY MODULES  ==========#
"""
 THESE MODULES ARE FROM KIVY. THE MODULES REQUIRED CAN BE
 ACQUIRED BY USING THESE COMMANDS:
       pip install kivy
       pip install --upgrade pip wheel setuptools
       pip install docutils pygments pypiwin32
       pip install kivy.deps.gstreamer
       pip install kivy.deps.angle
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition, CardTransition
from kivy.uix.dropdown import DropDown
from kivy.properties import BooleanProperty
from kivy.graphics import Color, RoundedRectangle
import kivy.utils
from kivy.utils import platform
from kivy.uix.image import Image
from kivy.clock import Clock
from functools import partial
from kivy.uix.button import ButtonBehavior


#==========  IMPORTING NECESSARY PYTHON FILES  ==========#
"""
 THESE PYTHON FILES ARE IMPORTED FROM THE SAME FOLDER.
 THE .py FILE NAMES ARE:
       Login_Signup_System.py
"""
from Login_Signup_System import POS


#==========          GLOBAL VARIABLES          ==========#
"""
 THESE ARE THE GLOBAL VARIABLES THAT WILL BE USED BY THE
 PROGRAM'S CLASSES/OBJECTS.
 THE GLOBAL VARIABLES ARE AS FOLLOWS:
  accounts_list: THIS WILL CONTAIN ALL THE ACCOUNT NAMES.
  sys.path: THIS WILL CONTAIN THE DIRECTORY OF main.py
"""
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
global accounts_list

#===========================================================================================================#


#========== CLASSES FOR THE PROGRAM'S SCREENS/WINDOWS ==========#
"""
 EACH OF THESE CLASSES REPRESENTS A SCREEN THAT CAN BE SEEN IN
 THE ACTUAL ANDROID APPLICATION. THESE OBJECTS ARE REFERENCES
 USED BY THE main.kv AND SOME OF ITS SUBSIDIARY .kv FILES.

 THE SCREENS ARE AS FOLLOWS:
   StartUpScreen: THE VERY FIRST SCREEN THAT WILL WELCOME THE
                  USER WHEN THE APP RUNS.

   LogInScreen: THE SCREEN THAT FACILITATES THE USER'S LOG IN.

   SignUpScreen: THE SCREEN THAT FACILITATES THE USER'S ACCOUNT
                 CREATION.

   MainScreen: THIS SCREEN HOLDS A LIST OF WORKOUT ROUTINES.
               THIS SCREEN CAN ONLY BE ACCESSED AFTER LOGGING IN.

   ReportScreen: THIS SCREEN SHOWS THE USER'S STATS.

   SelectedWorkoutScreen: THIS SCREEN WILL HOLD THE USER'S SELECTED
                          WORKOUT.

   WorkoutScreen: THIS SCREEN SHOWS THE EXERCISES THAT SHOULD BE
                  EXECUTED TO FINISH THE WORKOUT ROUTINE.

   CongratulationScreen: THIS SCREEN WILL POP UP AFTER FINISHING A
                         WORKOUT.

   MenuDropDown: THIS DROP DOWN MENU HOLDS REFERENCE BUTTONS THAT
                 WILL LEAD THE USER TOWARDS ONE OF THESE SCREENS;
                 MainScreen, ReportScreen, StartUpScreen.
"""
class StartUpScreen( Screen ):
    pass


class LogInScreen( Screen ):
    pass


class SignUpScreen( Screen ):
    pass


class MainScreen( Screen ):
    pass

        
class ReportScreen( Screen ):
    pass


class SelectedWorkoutScreen( Screen ):
    global workout_bk

    
class WorkoutScreen( Screen ):
    pass


class CongratulationScreen( Screen ):
    pass


class MenuDropDown( DropDown ):
    state = BooleanProperty( False )


#========== IMAGE BUTTON CLASS ==========#
"""
 THIS CLASS IS INHERITS THE BUTTON BEHAVIOUR AND IMAGE
 MODULE FROM KIVY. THIS ALLOWS OUR PROGRAM TO HAVE A
 NEW FUNCTIONALITY THAT CATERS TO IMAGE BUTTONS.
"""
class ImageButton(ButtonBehavior, Image):
    pass


#==========               THE APP CLASS               ==========#
"""
 THE CLASS 'MainApp' IS THE CORE OF THE ENTIRE PROGRAM.
 THIS CLASS CONTAINS MOST OF THE METHODS NECESSARY TO RUN THIS
 PROGRAM.
 THE METHODS CONTAINED WITHIN THIS CLASS ARE AS FOLLOWS:
   build: THE METHOD THAT BUILDS THE KIVY DEPENDENT PROGRAM.

   initialize_global_vars: THE METHOD THAT INITIALIZE VARIABLES
                           CRITICAL TOWARDS LAUNCHING/STARTING
                           APPLICATION.

   selected_workout: THE METHOD THAT WILL BE EXECUTED AFTER THE
                     USER CLICKS A WORKOUT ROUTINE BUTTON.

   start_workout: THIS METHOD WILL TRIGGER THE START OF A WORKOUT
                  ROUTINE.

   random_workout: THIS METHOD RANDOMLY CHOOSES A WORKOUT FIT FOR
                   THE USER'S WORKOUT ROUTINE.

   update_timer: THIS METHOD UPDATES AT A CERTAIN INTERVAL TO KEEP
                 THE WORKOUT ROUTINE GOING. ITS TASKS ARE: UPDATING
                 THE LOADING BAR, RECORDING FINISHED WORKOUTS AND
                 EXERCISES, RESETTING THE LOADING BAR AFTER AN
                 ACTION IS FINISHED, DETERMINES WETHER THE NEXT
                 ACTION WOULD BE AN EXERCISE OR A REST, AND
                 REDIRECTS THE USER TO THE CONGRATULATION SCREEN
                 AFTER ALL EXERCISES IS FINISHED.

   delay: THE METHOD THAT DETERMINES THE NUMBER OF TIMES THE
          PROGRAM UPDATES WHEN IN WORKOUT PHASE.

   cancel_workout: THIS METHOD STOPS THE WORKOUT MIDWAY AND REDIRECTS
                   THE USER BACK TO THE MAIN SCREEN.

   show_total_stats: THIS METHOD WILL UPDATE THE TOTAL STATS SHOWN IN
                     THE REPORT SCREEN.

   show_bodypart_stats: THIS METHOD WILL SHOW AN UPDATED STAT OF A
                        BODY PART. THE STAT CAN BE SEEN IN THE REPORT
                        SCREEN.

   add_to_specific_workout: THIS METHOD ADDS ONE POINT TO THE USER'S
                            STAT RELATIVE TO TH WORKOUT FINISHED.

   add_to_workout: THIS METHOD ADDS ONE POINT TO THE USER'S TOTAL
                   WORKOUT COUNT.

   add_to_exercise: THIS METHOD ADDS ONE POINT TO THE USER'S TOTAL
                    EXERCISE COUNT
.
   bodypart_selected: THIS METHOD UPDATES THE STAT SHOWN IN THE REPORT
                      SCREEN RELATIVE TO THE BUTTON SELECTED.

   deselect_bodypart: THIS METHOD UPDATES THE STATE OF THE BUTTON
                      PREVIOUSLY SELECTED IN THE REPORT SCREEN.
"""
class MainApp(App):
    # APP VARIABLES
    username = "" 
    password = ""
    
    def build(self):
        self.initialize_global_vars() # INITIALIZE VARIABLES
        self.POS = POS() # REFERENCE THE LOGIN AND SIGN UP SYSTEM
        self.menu_dropdown = MenuDropDown() # REFERENCE THE DROP DOWN MENU
        
        return Builder.load_file("main.kv") # BUILD THE KIVY APP
    
        
    def deselect_bodypart(self):
        # THE PROGRAM WILL TRY TO CHANGE BUTTONS STATE BACK TO ITS NORMAL STATE.
        # THE BUTTON WILL CHANGE FROM YELLOW ---> GREY.
        try:
            self.root.ids["report_screen"].ids[ self.deselect + "_BTN" ].source = "resources/buttons/notclicked_btn.png"
        except:
            pass

        
    def bodypart_selected( self, bodypart):
        # THE PROGRAM WILL UPDATE THE STATE OF THE BUTTON SELECTED IN REPORT SCREEN.
        # FROM GREY -----> YELLOW.
        self.bodypart = bodypart
        self.deselect_bodypart()
        
        self.root.ids["report_screen"].ids[self.bodypart + "_BTN" ].source = "resources/buttons/clicked_btn.png"
        self.deselect = bodypart


    def add_to_exercise( self):
        # IN THIS BLOCK OF CODE, THE PROGRAM WILL FIND AND OPEN THE TXT FILE THAT CONTAINS THE USER'S TOTAL EXERCISE COUNT.
        self.account_directory = os.path.join( self.accounts_directory, self.username )
        self.total_exercises = [ line.strip() for line in open ( os.path.join( self.account_directory, "total_exercises.txt" )) ]

        # IN THIS BLOCK OF CODE, THE PROGRAM WILL ADD ONE TO THE TOTAL EXERCISE COUNT CONTAINED IN THE OPENED TXT FILE.
        self.update_total_exercises = int(self.total_exercises[0]) + 1
        self.tempTxt = open( os.path.join( self.account_directory, "total_exercises.txt" ) , "w" )
        self.tempTxt.write( str( self.update_total_exercises ) + "\n" )
        self.tempTxt.close()


    def add_to_workout( self):
        # IN THIS BLOCK OF CODE, THE PROGRAM WILL FIND AND OPEN THE TXT FILE THAT CONTAINS THE USER'S TOTAL WORKOUT COUNT.
        self.account_directory = os.path.join( self.accounts_directory, self.username )
        self.total_workouts = [ line.strip() for line in open ( os.path.join( self.account_directory, "total_workouts.txt" )) ]

        # IN THIS BLOCK OF CODE, THE PROGRAM WILL ADD ONE TO THE TOTAL WORKOUT COUNT CONTAINED IN THE OPENED TXT FILE.
        self.update_total_workouts = int(self.total_workouts[0]) + 1
        self.tempTxt = open( os.path.join( self.account_directory, "total_workouts.txt" ) , "w" )
        self.tempTxt.write( str( self.update_total_workouts ) + "\n" )
        self.tempTxt.close()


    def add_to_specific_workout( self, bodypart, intensity ):
        # IN THIS BLOCK OF CODE, THE PROGRAM WILL FIND AND OPEN THE TXT FILE THAT CONTAINS A CERTAIN BODYPART'S STAT.
        self.bodypart = bodypart
        self.intensity = intensity
        self.account_directory = os.path.join( self.accounts_directory, self.username )
        self.exercise_stats = [ line.strip() for line in open ( os.path.join( self.account_directory, self.bodypart + ".txt" )) ]

        # IN THIS BLOCK OF CODE, THE PROGRAM WILL ADD ONE TO THE STAT COUNT, AND UPDATE THE TXT FILE OPENED.
        self.beginner_stats = int( self.exercise_stats[0])
        self.intermediate_stats = int( self.exercise_stats[1])
        self.advance_stats = int( self.exercise_stats[2])
        if self.intensity == "beginner":
            self.beginner_stats += 1
        elif self.intensity == "intermediate":
            self.intermediate_stats += 1
        elif self.intensity == "advance":
            self.advance_stats += 1 
        self.tempTxt = open( os.path.join( self.account_directory, self.bodypart + ".txt" ) , "w" )
        self.tempTxt.write( str( self.beginner_stats ) + "\n" )
        self.tempTxt.write( str( self.intermediate_stats ) + "\n" )
        self.tempTxt.write( str( self.advance_stats ) + "\n" )
        self.tempTxt.close()


    def show_bodypart_stats( self, bodypart ):
        # IN THIS BLOCK OF CODE, THE PROGRAM WILL FIND THE DIRECTORY OF THE USER'S ACCOUNT STATS.
        self.bodypart = bodypart
        self.account_directory = os.path.join( self.accounts_directory, self.username )
        self.exercise_stats = [ line.strip() for line in open ( os.path.join( self.account_directory, self.bodypart + ".txt" )) ]

        # IN THIS BLOCK OF CODE, THE PROGRAM WILL UPDATE THE STAT SHOWN IN THE SMALL BOX IN THE LOWER LEFT CORNER OF REPORT SCREEN.
        self.root.ids["report_screen"].ids[ "bodypart_lbl" ].text = bodypart.upper()
        self.root.ids["report_screen"].ids[ "beginner_lbl" ].text = "Beginner: " + str( self.exercise_stats[0] )
        self.root.ids["report_screen"].ids[ "intermediate_lbl" ].text = "Intermediate: " + str( self.exercise_stats[1] )
        self.root.ids["report_screen"].ids[ "advance_lbl" ].text = "Advance: " + str( self.exercise_stats[2] )


    def show_total_stats( self ):
        # IN THIS BLOCK OF CODE, THE PROGRAM WILL FIND THE DIRECTORY OF THE USER'S TOTAL ACCOUNT STATS.
        self.account_directory = os.path.join( self.accounts_directory, self.username )
        self.total_exercises = [ line.strip() for line in open ( os.path.join( self.account_directory, "total_exercises.txt" )) ]
        self.total_workouts = [ line.strip() for line in open ( os.path.join( self.account_directory, "total_workouts.txt" )) ]

        # IN THIS BLOCK OF CODE, THE PROGRAM WILL UPDATE TEXT IN THE LABELS LOCATED AT THE RIGHT SIDE OF THE REPORT SCREEN.
        self.root.ids["report_screen"].ids[ "totalexercises_lbl" ].text = self.total_exercises[0]
        self.root.ids["report_screen"].ids[ "totalworkouts_lbl" ].text = self.total_workouts[0]
        self.root.ids["report_screen"].ids[ "bodypart_lbl" ].text = ""
        self.root.ids["report_screen"].ids[ "beginner_lbl" ].text = ""
        self.root.ids["report_screen"].ids[ "intermediate_lbl" ].text = ""
        self.root.ids["report_screen"].ids[ "advance_lbl" ].text = ""
        

    def cancel_workout( self ):
        # IN THIS BLOCK OF CODDE, THE PROGRAM WILL CANCEL THE WORKOUT IN PROGRESS AND REDIRECT THE USER BACK TO THE MAIN SCREEN.
        self.workout_ongoing.cancel()
        self.root.current = "main_screen"

    def reset(self):
            # IN THIS BLOCK OF CODE, THE PROGRAM WILL RESET THE LOADING BAR.
            self.current_timer = 0
            self.workout_ongoing.cancel()
            for i in range(30):
                self.root.ids["workout_screen"].ids[ "loading" + str(i) ].source = "resources/labels/loading.jpg"

            # IF THE PREVIOUS ACTION IS 'REST', THE PROGRAM WILL UPDATE THE SCREEN AND SHOW AN 'EXERCISE'.
            # OTHERWISE, IF THE PREVIOUS ACTION IS AN 'EXERCISE', THE PROGRAM WILL UPDATE THE SCREEN AND SHOW 'REST'.
            if self.is_Exercise == False:
                self.is_Exercise = True
                
                # IF THE NUMBER OF EXERCISE DONE HAS REACHED THE REQUIRED AMOUNT, THE WORKOUT ROUTINE WILL FINISH
                # AND THE USER WILL BE REDIRECTED TO THE CONGRATULATIONS SCREEN.
                # OTHERWISE, IF THE REQUIRED AMOUNT OF EXERCISE FINISHED IS STILL LACKING, THE PROGRAM WILL SHOW
                # ANOTHER EXERCISE.
                if self.exercises_finished == self.required_exercise :
                    self.exercises_finished = 0
                    self.add_to_workout()
                    self.get_bodypart = self.workout_type.split( "_" )
                    self.add_to_specific_workout( self.get_bodypart[0] , self.intensity )
                    self.root.current = "congratulation_screen"
                else:
                    self.random_workout()
                    self.animation_directory = self.rand_workout_directory
                    self.root.ids["workout_screen"].ids["workout_img"].source = os.path.join( self.rand_workout_directory, "1.jpg" )
                    self.root.ids["workout_screen"].ids["workout_lbl"].source = os.path.join( self.rand_workout_directory, "exercise_lbl.jpg" )
                    self.animation_frame = 1
                    # THIS LINE OF CODE SETS THE SCHEDULED INTERVAL FOR WORKOUT.
                    self.workout_ongoing = Clock.schedule_interval( self.delay, 1)
            else:
                # IN THIS BLOCK OF CODE, THE PROGRAM WILL UPDATE THE GIF, SHOWING THE RESTING GIF.
                # IN ADDITION TO THAT, THE LABEL THAT SHOWS THE TYPE OF ACTION WILL BE UPDATED TO SHOW 'REST'.
                # FURTHERMORE, THE PROGRAM WILL ADD ONE TO THE USER'S EXERCISE COUNT.
                self.animation_directory = os.path.join( self.exercises_directory , "rest" )
                self.root.ids["workout_screen"].ids["workout_img"].source = os.path.join( self.animation_directory, "1.jpg" )
                self.root.ids["workout_screen"].ids["workout_lbl"].source = os.path.join( self.animation_directory, "exercise_lbl.jpg" )
                self.animation_frame = 1
                self.add_to_exercise()
                self.exercises_finished += 1
                self.is_Exercise = False
                # THIS LINE OF CODE SETS THE SCHEDULED INTERVAL FOR WORKOUT.
                self.workout_ongoing = Clock.schedule_interval( self.delay, 1)

                
    def delay(self, dt):
        # DEPENDING ON THE TYPE OF ACTION( EITHER AN EXERCISE OR REST ), THE PROGRAM WILL TRIGGER THE UPDATE A CERTAIN
        # NUMBER OF TIME.
        if self.is_Exercise == False:
            self.update_timer()
            self.update_timer()
            self.update_timer()
        else:
            self.update_timer()
        if  os.path.isfile( os.path.join ( self.animation_directory , str( self.animation_frame ) + ".jpg") ):
            self.root.ids["workout_screen"].ids["workout_img"].source = os.path.join ( self.animation_directory , str( self.animation_frame ) + ".jpg")
            print ( os.path.join ( self.animation_directory , str( self.animation_frame ) + ".jpg") )
            self.animation_frame += 1

        else:
            self.animation_frame = 1
            self.root.ids["workout_screen"].ids["workout_img"].source = os.path.join ( self.animation_directory , str( self.animation_frame ) + ".jpg")
            print ( os.path.join ( self.animation_directory , str( self.animation_frame ) + ".jpg") )
            self.animation_frame += 1
        
        
        # ONCE THE LOADING BAR IS CONSUMED, THE PROGRAM WILL RESET THE LOADING BAR AND UPDATE THE WORKOUT SCREEN.
        if self.current_timer > 29:
            self.reset()


    def update_timer(self):
        # IN THIS BLOCK OF CODE, THE PROGRAM WILL UPDATE THE LOADING BAR AND ADD ONE TO THE VARIABLE CURRENT_TIMER.
        # CURRENT_TIMER IS THE VARIABLE RESPONSIBLE IN HOLDING THE NUMBER OF TIMES THE UPDATE_TIMER HAVE BEEN TRIGGERED.
        self.root.ids["workout_screen"].ids[ "loading" + str( self.current_timer) ].source = "resources/labels/loading_done.jpg"
        self.current_timer += 1


    def random_workout(self):
        # DEPENDING ON THE WORKOUT TYPE, THE PROGRAM WOULD CHOSE AN EXERCISE RANDOMLY.
        # AFTER CHOOSING AN EXERCISE, THE PROGRAM WILL SHOW THE EXERCISE GIF.
        self.rand_workout = random.choice( self.rand_workout_exerList )
        self.rand_workout_directory = os.path.join( self.exercises_directory , self.rand_workout )
        print( self.rand_workout_directory )
        
            
    def start_workout(self):
        # THIS DICTIONARY HAVE THE NUMBER OF REQUIRED EXERCISES FOR EACH LEVEL OF DIFFICULTY.
        self.n_of_exercise = { "beginner" : 5,
                               "intermediate" : 10,
                               "advance" : 15 }

        # IN THIS BLOCK OF CODE, THE PROGRAM WILL GET THE NUMBER OF REQUIRED EXERCISES.
        # AFTER DOING SO, THE PROGRAM WILL PROCEED TO THE START OF THE WORKOUT ROUTINE.
        self.required_exercise = self.n_of_exercise[ self.intensity ]
        self.is_Exercise = False
        self.current_timer = 0
        self.exercises_finished = 0
        for i in range(30):
            self.root.ids["workout_screen"].ids[ "loading" + str(i) ].source = "resources/labels/loading.jpg"

        # THIS LINE OF CODE SETS THE SCHEDULED INTERVAL FOR WORKOUT.
        self.workout_ongoing = Clock.schedule_interval( self.delay, 1)


    def selected_workout(self, workout_type, intensity):
        self.workout_type = workout_type
        self.intensity = intensity
        # IN THIS BLOCK OF CODE, THE PROGRAM WILL UPDATE THE BACKGROUND IMAGE TO FIT THE
        # USER'S SELECTED WORKOUT ROUTINE.
        self.workout_bk = self.bk_sources[ self.workout_type ]
        self.root.ids["selectedworkout_screen"].ids["selectedworkout_bk"].source = self.workout_bk
        self.root.ids["congratulation_screen"].ids["workoutdone_img"].source = self.workout_bk
        self.animation_directory = os.path.join( self.exercises_directory , "rest" )
        self.animation_frame = 1
        self.root.ids["workout_screen"].ids["workout_img"].source = "resources/exercises/rest/1.jpg"
        self.root.ids["workout_screen"].ids["workout_lbl"].source = "resources/exercises/rest/exercise_lbl.jpg"

        # IN THIS BLOCK OF CCODE, THE PROGRAM WOULD CHOOSE THE LIST OF EXERCISES FOR THE SELECTED WORKOUT
        if self.workout_type == "back_beginner":
            self.rand_workout_exerList = self.back_beginner_exerList 
        elif self.workout_type == "back_intermediate":
            self.rand_workout_exerList = self.back_intermediate_exerList
        elif self.workout_type == "back_advance":
            self.rand_workout_exerList = self.back_advance_exerList 
        elif self.workout_type == "arms_beginner":
            self.rand_workout_exerList = self.arms_beginner_exerList 
        elif self.workout_type == "arms_intermediate":
            self.rand_workout_exerList = self.arms_intermediate_exerList 
        elif self.workout_type == "arms_advance":
            self.rand_workout_exerList = self.arms_advance_exerList 
        elif self.workout_type == "chest_beginner":
            self.rand_workout_exerList = self.chest_beginner_exerList 
        elif self.workout_type == "chest_intermediate":
            self.rand_workout_exerList = self.chest_intermediate_exerList 
        elif self.workout_type == "chest_advance":
            self.rand_workout_exerList = self.chest_advance_exerList 
        elif self.workout_type == "abs_beginner":
            self.rand_workout_exerList = self.abs_beginner_exerList 
        elif self.workout_type == "abs_intermediate":
            self.rand_workout_exerList = self.abs_intermediate_exerList 
        elif self.workout_type == "abs_advance":
            self.rand_workout_exerList = self.abs_advance_exerList 
        elif self.workout_type == "butt_beginner":
            self.rand_workout_exerList = self.butt_beginner_exerList 
        elif self.workout_type == "butt_intermediate":
            self.rand_workout_exerList = self.butt_intermediate_exerList 
        elif self.workout_type == "butt_advance":
            self.rand_workout_exerList = self.butt_advance_exerList 
        elif self.workout_type == "legs_beginner":
            self.rand_workout_exerList = self.legs_beginner_exerList 
        elif self.workout_type == "legs_intermediate":
            self.rand_workout_exerList = self.legs_intermediate_exerList 
        elif self.workout_type == "legs_advance":
            self.rand_workout_exerList = self.legs_advance_exerList
        return

        
    def initialize_global_vars(self):
        # THESE VARIABLES WOULD BE REFERENCED AS GLOBAL VARIABLES
        global root_directory
        global accounts_directory
        global accounts_list
        global resources_directory
        global backgrounds_directory
        global buttons_directory

        # IN THIS BLOCK OF CODE, THE PROGRAM WILL TAKEE THE ROOT DIRECTORY,
        # AND IT WILL ALSO MAKE A LIST OF NAMES OF EXISTING ACCOUNTS.
        root_directory = os.getcwd()
        accounts_directory = os.path.join( root_directory, "accounts" )
        if not os.path.exists( accounts_directory ):
            os.makedirs( accounts_directory )
        accounts_list = os.listdir( accounts_directory )
        self.accounts_directory = accounts_directory

        # IN THIS BLOCK OF CODE, THE PROGRAN WILL LOCATE THE DIRECTORIES
        # OF THE RESOURCES, BACKGROUNDS, AND BUTTONS FOLDER.
        resources_directory = os.path.join( root_directory, "resources")
        backgrounds_directory = os.path.join( resources_directory, "backgrounds" )
        buttons_directory = os.path.join( resources_directory, "buttons" )
        self.exercises_directory = os.path.join( resources_directory, "exercises" )
        if not os.path.exists( resources_directory ):
            os.makedirs( resources_directory )
        if not os.path.exists( backgrounds_directory ):
            os.makedirs( backgrounds_directory )
        if not os.path.exists( buttons_directory ):
            os.makedirs( buttons_directory )
        if not os.path.exists( self.exercises_directory ):
            os.makedirs( self.exercises_directory )

        #======== Exercises txt ======#
        # AFTER FINDING THE DIRECTORY OF THE TXT FOLDER, THE PROGRAM WILL INITIALIZE ALL THE TXT FILES INSIDE.
        self.txt_directory = os.path.join( root_directory, "txt" )
        self.back_beginner_exerList = [line.strip() for line in
                                       open( os.path.join( os.path.join(
                                           self.txt_directory , "back" ), "beginner.txt" ))]           
        self.back_intermediate_exerList = [line.strip() for line in open
                                           (os.path.join(os.path.join(self.txt_directory
                                                                      ,"back"),"beginner.txt"))]           
        self.back_advance_exerList = [line.strip() for line in open
                                      ( os.path.join( os.path.join(self.txt_directory
                                                                   , "back" ), "beginner.txt" ))]
        self.arms_beginner_exerList = [line.strip() for line in open
                                       (os.path.join(os.path.join(self.txt_directory
                                                                  ,"arms"),"beginner.txt"))]                  
        self.arms_intermediate_exerList = [line.strip() for line in open
                                           (os.path.join(os.path.join(self.txt_directory
                                                                      ,"arms"),"beginner.txt"))]                       
        self.arms_advance_exerList = [line.strip() for line in open
                                      (os.path.join( os.path.join(self.txt_directory
                                                                  ,"arms"),"beginner.txt"))]
        self.chest_beginner_exerList = [line.strip() for line in open
                                        (os.path.join(os.path.join(self.txt_directory
                                                                   ,"chest"),"beginner.txt"))]             
        self.chest_intermediate_exerList = [line.strip() for line in open
                                           (os.path.join(os.path.join(self.txt_directory
                                                                      ,"chest"),"beginner.txt"))]
        self.chest_advance_exerList = [line.strip() for line in open
                                      (os.path.join(os.path.join(self.txt_directory
                                                                 ,"chest"),"beginner.txt"))]
        self.abs_beginner_exerList = [line.strip() for line in open
                                      ( os.path.join( os.path.join(self.txt_directory
                                                                   ,"abs"),"beginner.txt"))]                         
        self.abs_intermediate_exerList = [line.strip() for line in open
                                          (os.path.join(os.path.join(self.txt_directory
                                                                      ,"abs"),"beginner.txt"))]                                 
        self.abs_advance_exerList = [line.strip() for line in open
                                     (os.path.join(os.path.join(self.txt_directory
                                                                ,"abs"),"beginner.txt"))]
        self.butt_beginner_exerList = [line.strip() for line in open
                                       ( os.path.join( os.path.join(self.txt_directory
                                                                    ,"butt"),"beginner.txt"))]                            
        self.butt_intermediate_exerList = [line.strip() for line in open
                                           (os.path.join(os.path.join(self.txt_directory
                                                                      ,"butt"),"beginner.txt"))]                                 
        self.butt_advance_exerList = [line.strip() for line in open
                                      (os.path.join(os.path.join(self.txt_directory
                                                                 ,"butt" ),"beginner.txt"))]
        self.legs_beginner_exerList = [line.strip() for line in open
                                       (os.path.join(os.path.join(self.txt_directory
                                                                  ,"legs" ),"beginner.txt"))]                                 
        self.legs_intermediate_exerList = [line.strip() for line in open
                                           (os.path.join(os.path.join(self.txt_directory
                                                                      ,"legs"),"beginner.txt"))]         
        self.legs_advance_exerList = [line.strip() for line in open
                                      (os.path.join(os.path.join(self.txt_directory
                                                                 ,"legs"),"beginner.txt" ))]
        
        # THIS DICTIONARY HOLDS THE PATH DIRECTORIES OF THE WORKOUT BACKGROUNDS.
        self.bk_sources = { "back_beginner" : "resources/backgrounds/back_beginner.jpg",
                            "back_intermediate" : "resources/backgrounds/back_intermediate.jpg",
                            "back_advance" : "resources/backgrounds/back_advance.jpg",
                            "arms_beginner" : "resources/backgrounds/arms_beginner.jpg",
                            "arms_intermediate" : "resources/backgrounds/arms_intermediate.jpg",
                            "arms_advance" : "resources/backgrounds/arms_advance.jpg",
                            "chest_beginner" : "resources/backgrounds/chest_beginner.jpg",
                            "chest_intermediate" : "resources/backgrounds/chest_intermediate.jpg",
                            "chest_advance" : "resources/backgrounds/chest_advance.jpg",
                            "abs_beginner" : "resources/backgrounds/abs_beginner.jpg",
                            "abs_intermediate" : "resources/backgrounds/abs_intermediate.jpg",
                            "abs_advance" : "resources/backgrounds/abs_advance.jpg",
                            "butt_beginner" : "resources/backgrounds/butt_beginner.jpg",
                            "butt_intermediate" : "resources/backgrounds/butt_intermediate.jpg",
                            "butt_advance" : "resources/backgrounds/butt_advance.jpg",
                            "legs_beginner" : "resources/backgrounds/legs_beginner.jpg",
                            "legs_intermediate" : "resources/backgrounds/legs_intermediate.jpg",
                            "legs_advance" : "resources/backgrounds/legs_advance.jpg" }
        
#===============================================================#


# THE KIVY APP WILL START/RUN.        
MainApp().run()
