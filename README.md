# M15 Assignment : Build an Employee Management Application
You are the CEO of XYZ Company, and you need an application to manage your employees' data. You have been given the following requirements for the application, and your task is to build this using Django.



## Application Requirements:



1. Add Employees’ Information via a Form:
 - You need to create a form to add employee details to the system.
 - The form must include the following fields:
 - Name (Text input)
 - Address (Text input)
 - Phone Number (Text input)
 - Salary (Numeric/ Text input, but non-editable after saving)
 - Designation (Dropdown or text, but non-editable after saving)
 - Short description (Text area input for a brief profile summary)


2. Unique Employee Profile:
 - Each employee should have a unique profile. You can use their ID or any other method to ensure that no two profiles are identical.
3. Employee Data Updates:
 - Employees should be able to update their information (e.g., Name, Address, Phone Number, Short description).
 - Important: Employees cannot change their Designation & Salary once their profile has been created. This field should be locked from editing after initial submission.
4. Delete Employee Profile:
 - There must be an option to delete an employee's profile from the system.


5. Display All Employees on the Homepage:
 - The homepage should list all the employee’s profiles.
 - Each employee’s profile should display their Name, Designation, and short description at minimum.
6. Navigation Bar:
 - Add a navigation bar at the top of your website. This navbar should have links to:
 - Home (Shows all employee profiles)
 - Add Employee (Form to create a new employee)
 - Update/Delete Employee (Page to update or remove an existing employee)
 - (Any other pages you think are necessary)


7. Superuser Login:
 - You must create a superuser with the following login details:
 - Username: admin
 - Password: 123



 Note: If the superuser is not created exactly as specified, your assignment marks will be 0.



## Additional Instructions:
- This assignment should be developed using Django.
- Make sure to include proper error handling and validation for all form fields (e.g., phone numbers should contain only digits).
- Use Django’s built-in authentication system to manage user logins and permissions.

 


Good luck, and remember that all requirements must be met for full marks!