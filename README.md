# Scouting-Form-V2
An application that allows students to collect scouting data without any sort of internet connectivity.




------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

                                             HOW TO USE:
              This program is designed to make the collection and storage of scouting data
            easier when there is no access to the internet, whether that is through free wifi
            or cellular data. The program is designed to make the creation and customization
            of the form simple and easy.
            
              Designing a form is simple. In the main file, three things are absolutely needed:
                - The widget class
                - The submit button
                - The createForm function
              
                                    An example form is shown below.
              ----------------------------------------------------------------------------------------
              # Necessary, DO NOT CHANGE
              import Widgets
              
              # This line creates a form. It's a place for all of the widgets that you make
              # to be stored for their creation.
              creator = Widgets.Widget(600, 500, "TEST", "gray", "white", "gray")
              
              # This line creates a text input field.
              creator.createTextInput("TEST_TEXT", 100, 50)
              
              # This line creates a bit of text on screen.
              creator.createLabel("TEST_LABEL", 200, 50)
              
              # This line creates a counter, which can be useful for counting shots made into a goal.
              creator.createCounter("TEST_COUNTER", 1, 300, 400)

              # This line creates a check box
              creator.createBoolean("TEST_BOOLEAN", 400, 50)
              
              # This line creates a dropdown menu
              creator.createDropdown("TEST_DROPDOWN", 100, 100, ["OPTION 1", "OPTION 2", "OPTION 3"])
              
              # This line creates a submit button, which is needed if you want to save data
              # into a .csv file.
              creator.createSubmitButton(300, 250)


              # Finally, this line takes the previously created widgets and places them
              # all onto the form make when creator was instantiated.
              creator.createForm()
              ----------------------------------------------------------------------------------------
              
            
            A more detailed description of the parameters and functions can be found in the file titled:
                                                  
                                                Documentation.pdf (DOES NOT EXIST YET)
                                                
            REMINDER: This program was made for any computer with Python 3.9 installed. Older versions
                      of python may not work, or cause the program to work in unexpected ways.

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
