# LocalEatz

![image](https://github.com/user-attachments/assets/f5184f1e-4087-4a1c-a49a-33cd1dfedf5f) 

## Admin Login
Username: gitpod
Password: Maynooth1



# Overview
LocalEatz is a web application designed to simplify the process of booking tables at restaurants. Users can easily register on the website, book tables, and manage their bookings with ease. Whether it's making a new reservation, editing an existing one, or canceling a booking, LocalEatz provides a seamless experience. The platform also keeps users informed with email notifications for every booking action.

# Features

## For Users:

Registration and Login: Create an account to access all features.
![image](https://github.com/user-attachments/assets/a8f9c7ee-c663-4a9b-8692-90d2f67f3c02)  ![image](https://github.com/user-attachments/assets/f63e4495-7389-4aa3-aa97-a65be50b5a5d)

Table Booking: Book tables at various restaurants.

![image](https://github.com/user-attachments/assets/ac91a581-afa1-41f5-8afb-1a2707fe259b)  ![image](https://github.com/user-attachments/assets/d7cd3f1f-a673-4259-8685-509a9e84718c)

Manage Bookings: Edit or cancel existing reservations.

![image](https://github.com/user-attachments/assets/896ae900-2634-4464-a512-1b5743dd52ae)


Email Notifications: Receive updates via email for bookings, changes, or cancellations.

![image](https://github.com/user-attachments/assets/2405a5f2-dab7-4d70-aba2-bd0508c9b380) ![image](https://github.com/user-attachments/assets/b3e1fb60-f019-4fad-8637-b021119547de)
![image](https://github.com/user-attachments/assets/a8e9174c-806b-4121-9afa-7206a91182cd)




Partnership Opportunities: Prospective partners can use the contact form to list their restaurant on LocalEatz.

## For Admins:
Admin Dashboard: Access a dedicated admin interface.

![image](https://github.com/user-attachments/assets/76baefd2-11b9-43c2-9682-690fdba2d124)

Restaurant Management: Add new restaurants or delete existing ones. 

![image](https://github.com/user-attachments/assets/4959aecb-0568-4227-9769-3ecd0b183ee9)

Users: Add or delete users.

![image](https://github.com/user-attachments/assets/882fabd7-274f-4ddf-9ec2-7b7d0c9d6054)


Booking Management: View and manage all bookings, with the ability to delete them if necessary and also a view for contacts from prospective partners.

![image](https://github.com/user-attachments/assets/0eb9fad2-521e-411b-be60-d1b94c7b1fb3)

# Authentication

### Email Requirement
For my application, email addresses are a mandatory part of the user setup process. This ensures that users receive important emails regarding any changes to bookings. During registration, users must provide a valid email address, which is used for email verification and other account-related notifications.

![image](https://github.com/user-attachments/assets/89e35bd0-7c2f-4465-b374-6d3a978919d7)


### Form Validation
To maintain the integrity of the data, all forms on the website incorporate authentication checks on the email fields. This validation prevents the entry of incorrect or invalid email addresses, ensuring that users provide a valid and reachable email address during registration and other interactions.

![image](https://github.com/user-attachments/assets/998f6a5e-cd81-4439-96ec-b2e07f3af9d5)


![image](https://github.com/user-attachments/assets/689ad1e7-35ea-4d41-8544-ebc4cc32bf0a)

### Booking Restrictions

To ensure an optimal dining experience, we have implemented a policy that restricts the minimum party size to 2 and the maximum party size to 8 for bookings. This helps manage restaurant capacities and ensures that all guests receive the best possible service.


![image](https://github.com/user-attachments/assets/be1b376f-377a-47da-ae56-5c24f55eba81) ![image](https://github.com/user-attachments/assets/22fa91d6-1db6-4c56-8f1e-6c8ddcf420be)



### Password Reset
I understand that users may forget their passwords. Hence, I have implemented a straightforward password reset mechanism via email. Users can request a password reset, and an email will be sent to their registered email address with a link to reset their password. Additionally, if users forget their username, the password reset email will also include their username as a reminder. This feature helps users regain access to their accounts quickly and efficiently.

![image](https://github.com/user-attachments/assets/0847a0ab-48b8-47e9-a79d-e24fc0acbfa3)

### Implementation Details

Form Authentication: All forms requiring email input use Django's built-in form validation to check for the correctness and validity of the email addresses. This step is crucial in preventing invalid email addresses from being submitted.

### Password Reset Workflow:

Users can initiate a password reset request from the login page.
An email containing a password reset link is sent to the user's registered email address.
The email template for the password reset includes the following:
A message informing the user about the password reset request.
A link to reset the password.
The user's username for reference.
Users can click the link, set a new password, and regain access to their account.
Email Template Customization
The email templates used for notifications and password resets are customized to provide a seamless and user-friendly experience. Below is an example template for the password reset email:

By implementing these authentication measures, we ensure a secure and user-friendly experience for our users, making it easy for them to manage their accounts and bookings.



# Technology Stack
Backend: Powered by Django, ensuring a robust and scalable backend.
Frontend: The user interface is designed for an intuitive user experience.

# Design Overview

## Minimalistic and User-Friendly Approach
The design of this application is centered around minimalism and usability. Key aspects include:

### Clean Aesthetic: 
The design uses a dark background (#1c1c1c) with light text (#e0e0e0) to create a high-contrast, easy-to-read interface. This not only enhances readability but also provides a sleek, modern look.

![image](https://github.com/user-attachments/assets/5272d075-555d-4596-80bc-01d6578be148)


### Consistent Color Scheme:
A vibrant pink (#ff4081) is used as the primary color for buttons, headers, and other interactive elements. This choice adds a touch of personality and visual interest, while ensuring that key actions and elements stand out.

### Fixed Navigation: 
The header and footer are fixed, providing constant access to navigation and important information without scrolling. This design choice enhances usability and keeps essential elements within easy reach.

![image](https://github.com/user-attachments/assets/cf287d1c-1e07-4175-a772-34fff51a7f9c)  ![image](https://github.com/user-attachments/assets/317dd503-8d89-4d75-a2f0-47313b736a53)


### Responsive Design: 
Media queries ensure the application is accessible and visually appealing across various devices, from mobile phones to large desktop monitors. This includes adjustments to padding, font sizes, and layout to accommodate different screen sizes.

![image](https://github.com/user-attachments/assets/dc853295-65c7-40a4-aad7-336c02aea325)


### Interactive Elements:
Buttons and interactive elements feature smooth transitions and hover effects to enhance user engagement and provide visual feedback. This makes the application feel more dynamic and responsive.

Overall, the design focuses on simplicity and ease of use, creating an intuitive and aesthetically pleasing user experience.

# Automated Testing

## Overview
Automated tests were created to ensure the correct functionality of the core models within the application. The tests.py file includes tests for the ContactQuery, Restaurant, and Booking models.

### Tests for ContactQuery Model
Contact Query Creation: Verifies that a ContactQuery object is created correctly with the specified attributes.
String Representation: Ensures the ContactQuery object’s string representation matches the expected format (e.g., "John Doe - john.doe@example.com").
Creation Time: Confirms that the created_at field is set to the current time upon creation.

### Tests for Restaurant Model

Restaurant Creation: Verifies that a Restaurant object is created correctly and that all attributes are properly set.
String Representation: Ensures the Restaurant object’s string representation matches the expected value (e.g., "Pizza Haven").

### Tests for Booking Model
Booking Creation: Verifies that a Booking object is created correctly with the specified user, restaurant, name, date, time, and party size.
String Representation: Ensures the Booking object’s string representation matches the expected format (e.g., "Booking for John Doe at Test Restaurant on 2024-08-01 at 19:00").

### Conclusion

These tests help maintain the integrity and reliability of the application's core functionalities, ensuring that critical operations related to contact queries, restaurants, and bookings perform as expected.

# Manual Test Cases

### User Registration and Login
Verified user can register and log in without issues.
Checked validation messages for incorrect login attempts.
Forgot Password Functionality
Ensured the forgot password link is visible on the login page.
Verified the password reset email is sent and the reset process works correctly.

### Booking a Table
Tested the table booking process for authenticated users.
Ensured date and time selection works correctly and displays available slots.
Booking Management
Verified that users can view, update, and cancel their bookings.
Ensured the cancellation confirmation prompt appears and functions correctly.

### Admin Functionality

Tested the CRUD operations for managing restaurants and bookings.
Verified that admins can view, create, update, and delete restaurants and bookings.
Responsive Design
Checked the layout and functionality on different screen sizes.
Ensured no elements overlap or break on smaller screens.
Verified touch interactions on mobile devices.

### Performance Testing
Ensured pages load quickly and efficiently.
Checked that JavaScript functionality, such as dynamic form updates, performs well across different browsers and devices.
Cross-Browser Compatibility
Verified consistent look and feel across all tested browsers.
Ensured all interactive elements function correctly in each browser.
Ran Lighthouse on devtools to get a performance score.

![image](https://github.com/user-attachments/assets/bd27258a-00d0-452a-8fbf-6e400da9e57e)

### CSS Validator

![image](https://github.com/user-attachments/assets/28f360de-7fff-4b87-9e8c-f862399e7a8a)


### Conclusion

Manual testing across various browsers and devices helps ensure the application is user-friendly and functional for all users, regardless of their preferred platform. This comprehensive approach helps catch issues that may not be covered by automated tests, providing a robust and reliable user experience.

# Known Issues and Bugs

## Image Upload for Restaurants in Admin Site

One known issue that remains unresolved is the inability to upload images for restaurants via the admin site. Despite multiple attempts to integrate image upload functionality, this feature remains unimplemented due to various challenges encountered during development.

### Attempts Made
Integration with Cloudinary:
Cloudinary was chosen as the service for managing image uploads.
Despite following the setup and integration guidelines, the implementation did not function as expected.
Troubleshooting the integration consumed a significant amount of development time without yielding a workable solution.

### Alternative Solutions:
Other solutions and third-party packages were considered, but they either did not meet the project requirements or introduced new complications.

### Decision
Given the limited development resources and the prioritization of other critical features, the decision was made to deprioritize the image upload functionality. It was determined that the inclusion of images, while beneficial, was not essential for the core functionality of the application.

### Future Considerations
Revisiting Image Upload:
Future iterations of the project may revisit this feature.
Additional resources or a different approach might be allocated to ensure seamless integration of image upload capabilities.

### Workaround
Text Descriptions:
Currently, restaurants can include detailed text descriptions to provide users with necessary information.
This ensures that users still have a clear understanding of what each restaurant offers.

## AllAuth Sign-Up Page HTML Validation
Another known issue is that the AllAuth sign-up page does not pass HTML validation. This issue arises from the HTML generated by the AllAuth package, which does not fully conform to HTML standards.

### Attempts Made
HTML Validation:

The AllAuth sign-up page was tested against standard HTML validators, which highlighted several validation errors.
Efforts were made to identify and correct these errors directly within the AllAuth templates, but the necessary modifications were not straightforward.

![image](https://github.com/user-attachments/assets/05849b76-d2ef-4ca6-b25a-0622db9d2e50)


### Custom Sign-Up Page:
Considered creating a custom sign-up page to ensure full HTML compliance.
This approach introduced significant development challenges and potential issues with maintaining compatibility with AllAuth's backend processes.

### Decision
After thorough consideration and research, it was decided to continue using the default AllAuth sign-up page despite the HTML validation issues. Creating a custom sign-up page posed too many risks and complexities, which could potentially impact the overall functionality and user experience of the site.

### Future Considerations
Contributing to AllAuth:
Future efforts might include contributing to the AllAuth project to help improve its HTML output.
Alternatively, the project may explore other user authentication packages that offer better HTML compliance.

### Workaround
The sign up page while functional still has these vaildation errors but they are not noticeable from a user perspective and as it is a third party add in I decided to keep it in.

## JavaScript File Issue

One of the known issues with the website is related to the JavaScript file responsible for showing available times on the booking form. The code works correctly when included directly within the HTML files for making or editing a booking. However, when the same code is moved to an external JavaScript file, it fails to function as expected.

Despite several attempts to resolve this issue, including collecting static files and verifying the paths, the script in the external file still did not work. Interestingly, other JavaScript functionalities, such as the cancel button, which also use external JavaScript files, are working correctly.

### Temporary Solution
Given the constraints and time spent trying to fix this issue, the decision was made to keep the time availability script directly in the relevant HTML files. This approach ensures that the functionality works as intended, even though it is not the ideal solution of using an external JavaScript file.

### Additional Details

Static File Collection: Ensured that static files were correctly collected and served by the Django application. Despite this, the time availability script in the external file did not function.
Script Inclusion: Verified that the external JavaScript file was correctly linked in the HTML files and loaded without errors.
Code Consistency: Confirmed that the same code block works within the HTML files, indicating that the issue lies with the external file inclusion rather than the script itself.
By keeping the script within the HTML files, we maintain the necessary functionality for users to see available times when making or editing a booking. This workaround allows the website to operate smoothly while ensuring a good user experience.


# Future Plans
As LocalEatz continues to grow and more restaurants join the platform, several exciting features and improvements are planned to enhance user experience and provide more value to both users and restaurant partners.

## Enhanced Search Functionality
To help users find the perfect dining experience, we plan to implement advanced search criteria, including:

## Location-Based Search:
Users will be able to search for restaurants based on their location, making it easier to find nearby dining options.

## Cuisine Type:
Users will have the ability to filter restaurants by cuisine type, such as Italian, Chinese, Indian, etc., to match their culinary preferences.

## Rating System
Introducing a rating system will allow users to provide feedback on their dining experiences and help others make informed decisions. Key features include:

## User Ratings and Reviews:
Users will be able to rate restaurants on a scale (e.g., 1 to 5 stars) and leave detailed reviews.

## Search by Popularity:
The search functionality will include options to filter and sort restaurants based on their ratings and popularity, highlighting top-rated establishments.

## Restaurant Menus
To assist users in making decisive choices when picking a restaurant, we will add the functionality to display restaurant menus. This feature will include:

## Menu Listings:
Restaurants will have the option to upload their menus, including details on dishes, prices, and specials.

## User Interaction:
Users can browse menus before making a reservation, ensuring they select a restaurant that meets their dietary preferences and budget.

# Agile Development Approach

During the development of LocalEatz, an agile approach was followed to ensure flexibility and continuous improvement. User stories were created and managed using GitHub Projects to guide the development process. This allowed for iterative cycles of planning, development, testing, and feedback, ensuring that the platform evolved in response to user needs and feedback.

![image](https://github.com/user-attachments/assets/8ad8a68e-b164-4b6a-8271-1bb26f7feb60)

# Cloning and Forking the Project from GitHub
To get a copy of the LocalEatz project up and running on your local machine, follow these steps:

## Cloning the Repository

Navigate to the GitHub Repository:
Go to the GitHub repository page for LocalEatz.

https://github.com/cmoynan/LocalEatzApp

## Clone the Repository:

Click on the "Code" button on the repository page.
Copy the HTTPS or SSH URL provided.

## Open Your Terminal:
Open your terminal or command prompt.

Run the Clone Command:
git clone https://github.com/your-username/LocalEatzApp.git
Replace https://github.com/your-username/LocalEatzApp.git with the URL you copied.

## Navigate to the Project Directory:

cd LocalEatzApp
Forking the Repository

Navigate to the GitHub Repository:
Go to the GitHub repository page for LocalEatz.

## Fork the Repository:

Click on the "Fork" button in the top-right corner of the repository page.
This will create a copy of the repository under your own GitHub account.
Clone Your Forked Repository:

Go to your GitHub profile and find the forked repository.
Click on the "Code" button on your forked repository page.
Copy the HTTPS or SSH URL provided.
Open Your Terminal:
Open your terminal or command prompt.

Run the Clone Command:

git clone https://github.com/your-username/LocalEatzApp.git
Replace https://github.com/your-username/LocalEatzApp.git with the URL you copied.

Navigate to the Project Directory:
cd LocalEatzApp

# Deploying the Project to Heroku
To deploy the project to Heroku, follow these steps:

## Log In to Heroku:
I logged into my Heroku account and created a new app for the Europe region.

## Connect to GitHub:
I linked the Heroku app to my GitHub repository and deployed the branch.

## Configure Static Files:
Initially, I added DISABLE_COLLECTSTATIC as a config variable to handle static files during deployment.

## Update settings.py:
Add Heroku to ALLOWED_HOSTS: I updated ALLOWED_HOSTS in settings.py to include the Heroku app domain.

## Install Required Packages:
I installed the following packages:
gunicorn
whitenoise

## Create a Procfile:
In Gitpod, I created a Procfile with the following content:
web: gunicorn localeatz.wsgi

## Set Debug Mode:
I ensured that DEBUG was set to False in settings.py to configure the app for production.

## Finalize Deployment:
After the initial deployment, I removed the DISABLE_COLLECTSTATIC config variable

By following these steps, the Django project was successfully deployed to Heroku.

## Heroku deployed app:
https://local-eatz-app-c7341f4affc4.herokuapp.com/

## Github Repo :
https://github.com/cmoynan/LocalEatzApp







