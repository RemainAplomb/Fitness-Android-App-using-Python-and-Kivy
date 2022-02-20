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

#==========          IMPORTS          ==========#
from kivy.app import App
import os


#========== LOGIN_SIGNUP_SYSTEM CLASS ==========#
"""
 THIS POS CLASS HOLDS ALL THE BACK END METHODS
 AND PROCESSES OF THE LOGIN AND SIGN UP.

 THEE METHODS WITHIN ARE:
   __init__: THE METHOD THAT INITIALIZES THE 
             VARIABLES THAT WOULD BE USED.

   try_login: THE METHOD THAT WILL BE EXECUTED
              ONCE THE USER CLICKS THE LOG IN
              BUTTON.

   try_signup: THE METHOD THAT WILL BE EXECUTED
               ONCE THE USER CLICKS THE SIGN UP
               BUTTON.
"""
class POS:
    def __init__( self ):
        # IN THIS BLOCK OF CODE, THE PROGRAM WILL INITIALIZE THE VARIABLES
        # CRITICAL TO THE POS CLASS.
        self.root_directory = os.getcwd()
        self.accounts_directory = os.path.join( self.root_directory, "accounts" )
        if not os.path.exists( self.accounts_directory ):
            os.makedirs( self.accounts_directory )
        self.accounts_list = os.listdir( self.accounts_directory )

        
    def try_login( self, username, password ):
        app = App.get_running_app()
        self.username = username
        self.password = password

        # IF THE ACCOUNT NAME GIVEN TO THIS METHOD CAN BE FOUND IN THE ACCOUNTS LIST,
        # THEN THE PROGRAM WILL PROCEED TO CHECKING IF THE ACCOUNT'S PASSWORD ALSO
        # MATCHES.
        # OTHERWISE, THE PROGRAM WILL SHOW A PROMPT TO THE USER THAT THE USERNAME
        # INPUTTED IS INVALID.
        if self.username in self.accounts_list:
            # IN THIS BLOCK OF CODE, THE PROGRAM WILL FIND THE ACCOUNT DIRECTORY OF THE
            # GIVEN USERNAME.
            self.account_directory = os.path.join( self.accounts_directory, self.username )
            self.accountInfo = [ line.strip() for line in
                                 open ( os.path.join( self.account_directory
                                                      , "password.txt" )) ]

            # IF THE PASSWORD MATCHES WITH WHAT IS STORED INSIDE THE DATABASE, THEN THE
            # USER WILL BE REDIRECTED TO THE PROGRAM'S MAIN SCREEN.
            # OTHERWISE, IF THE PASSWORD DOESN'T MATCH, THE PROGRAM WILL GIVE OUT AN
            # INVALID PASSWORD PROMPT.
            if self.accountInfo[0] == self.password:
                app.root.ids['login_screen'].ids['login_username'].text = ""
                app.root.ids['login_screen'].ids['login_password'].text = ""
                app.root.ids['login_screen'].ids['login_message'].text = ""
                app.root.ids["report_screen"].ids["username_lbl"].text = self.username

                app.root.current = "main_screen"
                return True
            else:
                app.root.ids['login_screen'].ids['login_message'].text = "INVALID PASSWORD"
                app.root.ids['login_screen'].ids['login_username'].text = ""
                app.root.ids['login_screen'].ids['login_password'].text = ""
        else:
            app.root.ids['login_screen'].ids['login_message'].text = "INVALID USERNAME"
            app.root.ids['login_screen'].ids['login_username'].text = ""
            app.root.ids['login_screen'].ids['login_password'].text = ""

        
    def try_signup( self, username, password ):
        app = App.get_running_app()
        self.username = username
        self.password = password

        # IF THE INPUT GIVEN IS NOT BLANK, THE PROGRAM WILL CHECK IF THE ACCOUNT CAN BE CREATED.
        # OTHERWISE, IT WILL PROMPT THE USER THAT THE INPUT WAS INVALID.
        if self.username != "" and self.password != "":
            # IF THE USERNAME INPUTTED CAN BE FOUND IN THE ACCOUNTS_LIST, THEN THE PROGRAM WILL PROMPT
            # THE USER THAT THE USERNAME HAD ALREADY BEEN TAKEN.
            # OTHERWISE, IT WILL CREATE THE ACCOUNT.
            if self.username in self.accounts_list:
                app.root.ids['signup_screen'].ids['signup_message'].text = "USERNAME ALREADY TAKEN" 
            else:
                self.account_directory = os.path.join( self.accounts_directory, self.username )
                if not os.path.exists( self.account_directory ):
                    os.makedirs( self.account_directory )
                self.passTxt = open( os.path.join( self.account_directory
                                                  , "password.txt" ) , "w" )
                self.passTxt.write( self.password + "\n" )
                self.passTxt.close()
                self.tempTxt = open( os.path.join( self.account_directory
                                                  , "back.txt" ) , "w" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.close()
                self.tempTxt = open( os.path.join( self.account_directory
                                                  , "arms.txt" ) , "w" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.close()
                self.tempTxt = open( os.path.join( self.account_directory
                                                  , "chest.txt" ) , "w" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.close()
                self.tempTxt = open( os.path.join( self.account_directory
                                                  , "abs.txt" ) , "w" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.close()
                self.tempTxt = open( os.path.join( self.account_directory
                                                  , "butt.txt" ) , "w" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.close()
                self.tempTxt = open( os.path.join( self.account_directory
                                                  , "legs.txt" ) , "w" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.close()
                self.tempTxt = open( os.path.join( self.account_directory
                                                  , "total_workouts.txt" ) , "w" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.close()
                self.tempTxt = open( os.path.join( self.account_directory
                                                  , "total_exercises.txt" ) , "w" )
                self.tempTxt.write( "0" + "\n" )
                self.tempTxt.close()
                self.accounts_list = os.listdir( self.accounts_directory )
                app.root.current = "startup_screen"
        else:
            app.root.ids['signup_screen'].ids['signup_message'].text = "INVALID INPUT"
