# Testing

Back to [README.MD](README.MD)

## CONTENTS

- [Manual Testing](#manual-testing)
- [Browser Testing](#browser-testing)
- [Validator Testing](#validator-testing)
- [Accessibility Testing](#accessibility-testing)
- [Bugs](#bugs)

## Manual Testing
|User Story:             |As a user, I want the navigation to be clear and visible so that I can easily navigate through the website|
|:--                     |:--                                                                                                       |
|**Acceptance Criteria:**|The site navigation should be easily accessible and consistent on every page so the user can visit all pages|
|**Summary**             |- When a user visits the site, the navigation is at the top of every page<br>- When a user scrolls down the page, the navigation stays fixed at the top of the screen<br>- When a user navigates through the pages on the site, the navigation remains in the same place<br>- When a user is logged in, the Register and Login links are replaced with the appropriate profile (either Profile or Staff Management) link and a log out link<br>- The user's current page is clearly marked in the navigation|     
|**Outcome**             |All features tested and passed.|     
|**User Story:**        |**As a user, I want to see the restaurant’s contact details**|
|**Acceptance Criteria:**|The user should be able to easily find the contact details so that they can contact the restaurant|
|**Summary**             |- The contact details are positioned within the footer of each page|     
|**Outcome**             |All features tested and passed.|  
|**User Story:**         |**As a user, I want to see the restaurant’s opening and closing times**|
|**Acceptance Criteria:**|The user should be able to easily find the opening and closing times|
|**Summary**             |- The opening and closing times are positioned within the footer of each page|     
|**Outcome**             |All features tested and passed.| 
|**User Story:**         |**As a user, I want to see the restaurant's location**|
|**Acceptance Criteria:**|The user should be able to easily find the restaurant's location|
|**Summary**             |- The address of the restaurant is positioned within the footer of each page|     
|**Outcome**             |All features tested and passed.| 
|**User Story:**         |**As a user, I want to see relevant information on the website**|
|**Acceptance Criteria:**|The user should be able to easily find information about the restaurant and the food they serve so that they can make an informed choice as to whether to make a reservation|
|**Summary**             |- On the home page there is some text that gives a brief overview of the restaurant<br>- There is a menu page which details all of the food served|     
|**Outcome**             |All features tested and passed.| 
|**User Story:**         |**As a user, I want a pleasant UX experience so that I am encouraged to make a booking**|
|**Acceptance Criteria:**|Create an attractive, intuitive design that will make a user want to return|
|**Summary**             |- The home page is a simple, clean design that immediately encourages a user to view the menu or book a table<br>- The user only has to scroll down a little to view more information about the restaurant and to see all of the relavant information<br>- The colours are warm and welcoming which enhance the feeling of a family run restaurant<br>- The logo contains a picture of a cow which suggests the nature of the restaurant<br>- Alerts are provided as feedback to user actions|     
|**Outcome**             |All features tested and passed.| 
|**User Story:**         |**As a user, I can create an account so that I can make a reservation**|
|**Acceptance Criteria:**|A user should be able to register for an account by filling in a form|
|**Summary**             |- The user can navigate to the Register page which displays a form for the user to fill out<br>- The user can enter a username, email and password<br>- Once the form has been completed and submitted an entry is created in the database<br>- A popup alert message appears to confirm that the user is signed in|     
|**Outcome**             |All features tested and passed.| 
|**User Story:**         |**As a user, I can login to my account using my username and password so that my account is secure**|
|**Acceptance Criteria:**|A user should be able to login by entering their username and password|
|**Summary**             |- The user can login by navigating to the Login page where a form is displayed allowing the user to login with their username and password<br>- A popup alert message appears to confirm that the user is signed in|     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a user, I can log out of my account at any time so that my account is secure**|
|**Acceptance Criteria:**|A user should be able to log out|
|**Summary**             |- When a user is logged in, there is a Logout link in the navigation<br>- When the Logout link has been clicked it takes you to a logout confirmation page for the user to confirm that they wish to log out<br>- A popup alert message appears to confirm that the user has been signed out|     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a user, I can reset my password so that I can keep my account secure and if I have forgotten my password**|
|**Acceptance Criteria:**|A user should be able to reset their password|
|**Summary**             |- On the Login page there is a 'Forgot Password' link<br>- There is the facility within the allauth package for a reset password link to be emailed to the user but in order to set this up there needs to be an smtp server so as a workaround for this project password reset links are saved in a file|     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a logged in user, I want to be able to make a reservation for a specific date and time**|
|**Acceptance Criteria:**|A logged in user should be able to complete a form to make a reservation|
|**Summary**             |- If a user clicks on the Book page they will be prompted to either register or login<br>- Once logged in, the user will be able to complete a form, entering their name, phone number, date, time, number of guests and notes<br>- When the form has been completed a check will be made to see if the date/time combination already exists in the database<br>- If there is an existing reservation in the database for that date/time combination an error message will pop up informing the user that slot is not available<br>- If there is no existing reservation in the database a success message will pop up and the user redirected to their Profile page|     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a logged in user, I want to be able to make a reservation for x number of people**|
|**Acceptance Criteria:**|A logged in user should be able to make a reservation for as many people as they need|
|**Summary**             |Within the booking form there is a field for number of guests|     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a logged in user, I want to be able to add a note to my reservation detailing any specific requests or details regarding any allergies**|
|**Acceptance Criteria:**|A logged in user should be able to add a note for staff when making a reservation|
|**Summary**             |Within the booking form there is a field for users to add a note|     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a logged in user, I want to be able to view my reservation**|
|**Acceptance Criteria:**|There should be a page where a the user's reservations are displayed which is only visible to a logged in user|
|**Summary**             |- The Profile page is visible to logged in users but not available to staff members<br>- This page contains a list of all reservations made by the logged in user<br>- Each reservation contains all the details originally entered in the booking form|     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a logged in user, I want to be able to update my reservation**|
|**Acceptance Criteria:**||
|**Summary**             ||     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a logged in user, I want to be able to delete my reservation**|
|**Acceptance Criteria:**||
|**Summary**             ||     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a logged in staff member, I want to be able to see all reservations**|
|**Acceptance Criteria:**||
|**Summary**             ||     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a logged in staff member, I want to be able to filter the reservations by a specific date so that I can prepare for that day**|
|**Acceptance Criteria:**||
|**Summary**             ||     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a logged in staff member, I want to be able to update reservations on behalf of customers so that I can make the process as easy as possible for a customer**|
|**Acceptance Criteria:**||
|**Summary**             ||     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a logged in staff member, I want to be able to delete reservations on behalf of customers so that I can make the process as easy as possible for a customer**|
|**Acceptance Criteria:**||
|**Summary**             ||     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a user, I want to see menus so I can decide whether I would like to make a reservation**|
|**Acceptance Criteria:**||
|**Summary**             ||     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a logged in staff member, I want to be able to add new menus**|
|**Acceptance Criteria:**||
|**Summary**             ||     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a logged in staff member, I want to be able to edit menus**|
|**Acceptance Criteria:**||
|**Summary**             ||     
|**Outcome**             |All features tested and passed.|
|**User Story:**         |**As a logged in staff member, I want to be able to delete menus**|
|**Acceptance Criteria:**||
|**Summary**             ||     
|**Outcome**             |All features tested and passed.|

Back to [README.MD](README.MD)
