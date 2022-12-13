[<< Back to main ReadMe](README.md)

# Manual Testing


Below are the manual test case which was performed on function and to check for validations. All test case ran as expected.

<table>
  <tr>
    <th>What was tested</th>
    <th>How it was tested</th>
    <th>What was expected</th>
    <th>lnput check</th>
    <th>Test output</th>
  </tr>
  <tr>
    <td>Welcome Page</td>
    <td>Initial call of the program</td>
    <td>To load Program title, welcome message, clear screen, enter to continue, then triggers the title page and the display menu function</td>
    <td>Function runs and loads as expcted</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Display Menu</td>
    <td>"g", "0", "", "8", "22"</td>
    <td>Request choice of number input between 1 to 5 to start the program. Every valid inputs triggers the relevant function. An input error displays a message and reloads the Display Menu for another attempt, if input is invalid.</td>
    <td>Function runs and loads as expected, All options triggers relevant function and invalid input repeats the menu choice</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Search word - option 1</td>
    <td>"1", "t", "ghhgt", "f5rd", "8754", " ", "raiin" "t33th"</td>
    <td>Prompt user input word, display word meaning, returns most probable corrected word with meaning for misspelt word, display words meaning and it coincidences by types of "figure of speech". Display word not found error message and returns display menu. Handles and disables PyDictionary errors message</td>
    <td>Function runs and loads as expected, with exception of a single character being converted to i</td>
    <td>pass</td>
    </tr>
  <tr>
    <td>Save log - option 2</td>
    <td>"s","2", "yes", "no", "y", "n", "YES", "NO", "t", "b"</td>
    <td>Prompt user input "y/n", for whether they would like to save their word. If yes, triggers the worksheet log, and word is saved to worksheet. If no is chosen, asks for a second confirmatory input to either save and return to the display menu or exit the program. Display invalid input error message. If invalid entry, prompt for another attempt</td>
    <td>Function run and validates input as expected</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>worksheet log - option 2</td>
    <td>""2""</td>
    <td>Takes data and log it via API in the "vocabulary_log" worksheet, appends a new row with the word and meaning of word
    looked up by the user. Triggered by save log function</td>
    <td>Run as expected. Data is viewable in the worksheet</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>display log words - option 3</td>
    <td>"3"</td>
    <td>Retrieve lists of saved words
    from "vocabulary-log" worksheet's words column and display back the to user. Prompt user input "Enter" to return to display menu.</td>
    <td>Run as expected. List of saved words display on screen.</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>display last 2 logs - option 4</td>
    <td>"4"</td>
    <td>Retrieve the last 2 saved words from "vocabulary-log" worksheet's words and meaning column and display back the to user. 
    Prompt user input "Enter" to return to display menu.<td>
    <td>Run as expected. List of last 2 saved words and meaning displayed on screen.</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>exit program - option 5</td>
    <td>"f","5", "yes", "no", "y", "n", "YES", "NO", "m", ""</td>
    <td>Prompt user input "y/n", for whether they would like to stay or leave the program. If yes, return to display menu. If no is chosen, asks for a second confirmatory input, for validation of input to allow for intentional exit of the program. Display invalid entry error message for wrong input and repeats user input request</td>
    <td>Run as expected</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>title page</td>
    <td>N/A</td>
    <td>Displays the opening page title using the ascii art</td>
    <td>Run as expected in the standard art print</td>
    <td>Pass</td>
  </tr>
</table>
[<< Back to ReadMe](README.md)
