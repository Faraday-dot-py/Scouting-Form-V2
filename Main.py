import Widgets

creator = Widgets.Widget(600, 500, "TEST", "gray", "white", "gray")

creator.createTextInput("TEST_TEXT", 100, 50)

creator.createLabel("TEST_LABEL", 200, 50)

creator.createCounter("TEST_COUNTER", 1, 300, 400)

creator.createBoolean("TEST_BOOLEAN", 400, 50)

creator.createDropdown("TEST_DROPDOWN", 100, 100, ["OPTION 1", "OPTION 2", "OPTION 3"])

creator.createSubmitButton(300, 250)



creator.createForm()