# APP NAME

![Am I Responsive](docs/imgs/responsive.jpg)

**Developer: Christopher Jimerson**

💻 [Visit live website](https://pp4-enigma-machine.herokuapp.com/)



## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

### About

Enigma Machine is a fictitious business where users can learn about escape rooms, view the current room offerings, create and manage an account, and make bookings for escape room events. 
<hr>

### User Goals

- Create bookings for escape room games.
- Educate themselves on what an escape room is.
- View the current rooms that the company has available for booking.
- View promotions or sales currently going on.
- Easily communicate with business.

### Site Owner Goals

- Allow users to create accounts and make reservations.
- Be able to track booking data in an easy way.
- Provide responsive and quality applications to drive sales and user engagement.
- Make it as simple and clear as possible for users to book.
- Track communication through the website 
- Advertise news, promotions, or sales in a clear and easy way.


<hr>


## User Experience

### Target Audience

- Corporate clients who are looking for team building events
- Escape Room enthusiasts
- Families looking for events for their families, of all ages. 
- Tourists looking for things to do in the city.
- Friends looking for unique experiences for their next bachelor or bachelorette party. 
- Teachers or schools looking for age appropriate activities.

### User Requirements and Expectations

- Easy to use and navigable site.
- Responsive design.
- Easy to understand and labeled information channels.
- Accessable.
- Account management with booking history.
- Edit/Cancel bookings.
- Easily and clear communication channels.

##### Back to [top](#table-of-contents)<hr>


## User Stories

### Users

1. As a user, I want to be able to view the availability and schedule of each escape room game in real-time on the booking website, so that I can select a time slot that works best for me.
2. As a user, I want to be able to view all available escape room games on the booking website, including their descriptions, difficulty levels, and any other information so that I can make an informed decision on which game to reserve.
3. As a user, I want to be able to reserve multiple escape room games for different time slots in a single booking transaction, so that I can plan a day of fun-filled activities with my friends or family.
4. As a user, I want to be able to create an account on the booking website to store my booking history so that I can easily track my previous experiences to ensure no booking errors in the future.
5. As a user, I want to be able to easily cancel or reschedule my escape room game reservations through the booking website, so that I can adjust my plans quickly if needed.
6. As a user, I want to be able to leave reviews and ratings for escape room games that I have played, so that I can share my feedback and experiences with other users, and help them make informed decisions when booking games.
7. As a user, I want to be able to view special promotions, discounts, or packages for escape room games on the booking website, so that I can take advantage of any available deals and save on my bookings.
8. As a user, I want to be able to access the booking website on different devices, including desktops, laptops, tablets, and smartphones, with a responsive and user-friendly design, so that I can make bookings anytime and anywhere.
9. As a user, I want to be able to view detailed information about the escape room game venues, such as their locations, facilities, parking options, and accessibility, so that I can plan my visit accordingly and have a smooth experience.
10. As a user, I want to be able to contact the escape room game venue or customer support through the booking website, with options for email, or phone support, so that I can get assistance or information whenever I need it.
11. As a user, I want to be able to view photos of the escape room game themes and rooms on the booking website, so that I can get a sneak peek of the games and get excited about the experience.
12. As a user, I want to be able to customize my escape room game experience by requesting special arrangements for birthdays, team-building events, or other occasions, through my booking so that I can get more out of my event planning.
13. As a user I want to be able to delete my own account and request all my data be removed from your servers/databases so that I can exercise my data protection rights.
14. As a user I want to be able to edit my account details so that I can keep the booking process smooth and easy even if my email or other data changes.
15. As a user I want to be able to create a reservation using my account information, and having all the applicable data visible such as group sizes, date, time, etc so that I can quick and easily secure a booking.


### Admin / Site Owner

16. As an admin user, I want to be able to view a list of all upcoming escape room events booked by customers, including their details such as date, time, game theme, and customer information, so that I can have an overview of the bookings and manage them efficiently.
17. As an admin user, I want to be able to add, edit, or cancel escape room bookings on behalf of customers, including updating the date, time, or game theme, so that I can accommodate their requests or resolve any issues.
18. As an admin user, I want to be able to *manage customer accounts and profiles, including creating, updating, or deleting customer information, and viewing their booking history, so that I can provide personalized and efficient customer service.
19. As an admin user, I want to be able to manage special promotions, discounts, or packages for escape room games, including creating, updating, or expiring promotions so that I can attract more customers and boost sales.
20. As an admin user I want to be able to add new games to the website as the company builds and expands so that we can have the newest and most up to date information about our games immediately visible to our customer.
21. As an admin user I want to be able to add or remove time slots available for booking so that we can adjust our business hours to match the flow of the business traffic to our location.



### Kanban, Epics & User Stories
- GitHub Kanban was used to track all open User Stories. 
- Epics were created throuhg the Milestone functionality.

<details><summary>Epics</summary>

![Epics](docs/imgs/epics.jpg)

</details>

<details><summary>Kanban</summary>

![Kanban in Progress](docs/imgs/kanban.jpg)
![Kanban Done](docs/imgs/kanbandone.jpg)


</details>


##### Back to [top](#table-of-contents)<hr>


## Design

### Colours


<details><summary>See colour pallet</summary>
<img src="">
</details>

### Fonts


### Structure

#### Website pages

The site was designed for the user to be familiar with the layout such as a navigation bar along the top of the pages and a hamburger menu button for smaller screen.

The footer...

- The site consists of the following pages:
    - Home:
    - FAQ:
    - Rooms:
    - Blog:
    - Book Now:
    - Contact:
    - Sign Up:
    - Login/Logout:
    - Account: 

#### Database

- Built with Python and the Django framework with a database of a Postgres for the deployed Heroku version(production)

<details><summary>Show diagram</summary>
<img src="docs/imgs/db_diagram.jpg">
</details>



####  Reservation
The Reservation Model contains the following:
 - id
 - customer_name
 - customer_email
 - player_number
 - price
 - date
 - time_slot
 - room_choice
 - comment
 - user_id

#### Room
The Room Model contains the following:
 - id
 - room_name
 - slug
 - short_room_description 
 - room_description
 - small_image
 - detail_image

#### GameTime
The GameTime Model contains the following:
  - id
  - game_slot 

 With choices:
  - 00:00	
  - 02:00	
  - 04:00	
  - 06:00	
  - 08:00	
  - 10:00	
  - 12:00	
  - 14:00	
  - 16:00	
  - 18:00	
  - 20:00	
  - 22:00	


#### Blog
The Blog Model contains the following:
 - id
 - blog_title
 - slug
 - tags
 - blog_image
 - blog_small_image
 - blog_blurb
 - blog_content
 - posted_date
 - meta_tags

 With Choices: 
  - Blog	
  - Promotion	
  - Sale	
  - News	
  - Partner Advert	
  - Holiday	
  - B.T.S	
  - Meet the Staff	

#### Contact
The Contact Model contains the following:
 - inquiry_id
 - inquiry_name
 - inquiry_email
 - phone_number
 - created_date
 - inquiry_message

#### FAQ
The FAQ Model contains the following:
 - id
 - question 
 - answer


### Wireframes
The wireframes were created using Balsamiq
<details><summary></summary>
<img src="">
</details>


## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django


### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [jQuery](https://jquery.com)
- [Postgres](https://www.postgresql.org/)
- [ElephantSQL](https://www.elephantsql.com/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [CI Validator(PEP8)](https://pep8ci.herokuapp.com//)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

##### Back to [top](#table-of-contents)


## Features

### Featre
- Description


<details><summary>See feature images</summary>

![Feature](img)
</details>





##### Back to [top](#table-of-contents)<hr>


## Validation

The W3C Markup Validation Service
<details><summary>Home</summary>
<img src="docs/html_validation/index_w3s_validation.jpg">
</details>
<hr>
<details><summary>FAQ</summary>
<img src="docs/html_validation/faq/faq_w3s_validation.jpg">
</details>
<hr>

<details><summary>Room</summary>
<img src="docs/html_validation/rooms/rooms_html_valid.jpg">
</details>
<details><summary>Room(Detail View)</summary>
<img src="docs/html_validation/rooms/rooms_detail_html_valid.jpg">
</details>
<hr>

<details><summary>Blog</summary>
<img src="docs/html_validation/blog/blog_html_valid.jpg">
</details>
<details><summary>Blog(Detail View)</summary>
<img src="docs/html_validation/blog/blog_detail_html_valid.jpg">
</details>
<hr>

<details><summary>Book Now</summary>
<img src="docs/html_validation/bookings/reservation_ws3_validation.jpg">
</details>
<details><summary>Reservation Choice</summary>
<img src="docs/html_validation/bookings/reservation_res_choice_ws3_validation.jpg">
</details>
<details><summary>Reservation Booking Form</summary>
<img src="docs/html_validation/bookings/bookings_bookingform_w3s_validation.jpg">
</details>
<details><summary>Reservation Confirmation</summary>
<img src="docs/html_validation/bookings/reservation_confirmation_ws3_validation.jpg">
</details>
<details><summary>Contact</summary>
<img src="docs/html_validation/contact/contact_html_valid.jpg">
</details>
<hr>

<details><summary>Sign Up</summary>
<img src="docs/html_validation/user_profiles/signup_w3s_validation.jpg">
</details>
<details><summary>Logout</summary>
<img src="docs/html_validation/user_profiles/logout_w3s_validation.jpg">
</details>
<details><summary>Login</summary>
<img src="docs/html_validation/user_profiles/login_w3s_validation.jpg">
</details>
<hr>

<details><summary>Account</summary>
<img src="docs/html_validation/user_profiles/account_html_validation.jpg">
</details>
<details><summary>Account Info Edit</summary>
<img src="docs/html_validation/user_profiles/account_edit_html_valid.jpg">
</details>
<details><summary>Account Booking List</summary>
<img src="docs/html_validation/user_profiles/account_res_view_html_valid.jpg">
</details>
<details><summary>Account Booking Edit</summary>
<img src="docs/html_validation/user_profiles/account_res_edit_ws3_validation.jpg">
</details>
<details><summary>Account Booking Edit Confirm</summary>
<img src="docs/html_validation/user_profiles/account_res_edit_confirm_ws3_validation.jpg">
</details>
<hr>

<details><summary>403</summary>
<img src="">
</details>
<details><summary>404</summary>
<img src="">
</details>
<details><summary>500</summary>
<img src="">
</details>


### CSS Validation
The W3C Jigsaw CSS Validation Service

<details><summary>CSS</summary>
<img src="docs/css_validation/css_validation.jpg">
</details><hr>

### JavaScript Validation
JSHint JS Validation Service

<details><summary>FILE</summary>
<img src="">
</details><hr>

### PEP8 Validation


##### Blog App
<hr>

<details><summary>Files</summary>
<details><summary>views.py</summary>
<img src="docs/python_validation/blog/blog_view_py_validated.jpg">
</details>
<details><summary>urls.py</summary>
<img src="docs/python_validation/blog/blog_url_py_validated.jpg">
</details>
<details><summary>tests.py</summary>
<img src="">
</details>
<details><summary>models.py</summary>
<img src="docs/python_validation/blog/blog_models_py_validated.jpg">
</details>
<details><summary>admin.py</summary>
<img src="docs/python_validation/blog/blog_admin_py_validated.jpg">
</details>
</details>
<hr>

##### Booking App

<details><summary>Files</summary>
  <details><summary>views.py</summary>
  <img src="docs/python_validation/bookings/booking_view_py_validation.jpg">
  </details>
  <details><summary>urls.py</summary>
  <img src="docs/python_validation/bookings/bookings_urls_py_validated.jpg">
  </details>
  <details><summary>tests.py</summary>
  <img src="">
  </details>
  <details><summary>forms.py</summary>
  <img src="docs/python_validation/bookings/bookings_forms_py_validated.jpg">
  </details>
  <details><summary>models.py</summary>
  <img src="docs/python_validation/bookings/bookings_models_py_validated.jpg">
  </details>
  <details><summary>admin.py</summary>
  <img src="docs/python_validation/bookings/bookings_admin_py_validated.jpg">
  </details>
  <details><summary>res_tags.py</summary>
  <img src="docs/python_validation/bookings/bookings_res_tags_py_validated.jpg">
  </details>
</details>
<hr>

##### Contact App

<details><summary>Files</summary>
  <details><summary>views.py</summary>
  <img src="docs/python_validation/contact/contact_views_py_validated.jpg">
  </details>
  <details><summary>urls.py</summary>
  <img src="docs/python_validation/contact/contact_urls_py_validated.jpg">
  </details>
  <details><summary>tests.py</summary>
  <img src="">
  </details>
  <details><summary>forms.py</summary>
  <img src="docs/python_validation/contact/contact_forms_py_validated.jpg">
  </details>
  <details><summary>models.py</summary>
  <img src="docs/python_validation/contact/contact_models_py_validated.jpg">
  </details>
  <details><summary>admin.py</summary>
  <img src="docs/python_validation/contact/contact_admin_py_validated.jpg">
  </details>
</details>
<hr>

##### FAQ App

<details><summary>Files</summary>
  <details><summary>views.py</summary>
  <img src="docs/python_validation/faq/faq_views_py_validation.jpg">
  </details>
  <details><summary>urls.py</summary>
  <img src="docs/python_validation/faq/faq_urls_py_validation.jpg">
  </details>
  <details><summary>tests.py</summary>
  <img src="">
  </details>
  <details><summary>models.py</summary>
  <img src="docs/python_validation/faq/faq_models_py_validation.jpg">
  </details>
  <details><summary>admin.py</summary>
  <img src="docs/python_validation/faq/faq_models_py_validation.jpg">
  </details>
</details>
<hr>

##### Rooms App

<details><summary>Files</summary>
  <details><summary>views.py</summary>
  <img src="docs/python_validation/rooms/rooms_views_py_validated.jpg">
  </details>
  <details><summary>urls.py</summary>
  <img src="docs/python_validation/rooms/rooms_urls_py_validated.jpg">
  </details>
    <details><summary>tests.py</summary>
  <img src="">
  </details>
</details>
<hr>

##### User Profile App

<details><summary>Files</summary>
  <details><summary>views.py</summary>
  <img src="docs/python_validation/user_profiles/user_profile_views_py_validated.jpg">
  </details>
  <details><summary>urls.py</summary>
  <img src="docs/python_validation/user_profiles/user_profile_urls_py_validated.jpg">
  </details>
  <details><summary>tests.py</summary>
  <img src="">
  </details>
</details>
<hr>

### Lighthouse

Performance, best practices and SEO was tested using Lighthouse.

#### Desktop
<details><summary>Home</summary>
<img src="docs/lighthouse/index_lighthouse.jpg">
</details>

<details><summary>FAQ</summary>
<img src="docs/lighthouse/faq_lighthouse.jpg">
</details>

<details><summary>Rooms</summary>
<img src="docs/lighthouse/room_lighthouse.jpg">
<details><summary>Rooms Detail</summary>
<img src="docs/lighthouse/room_detail_lighthouse.jpg">
</details>

</details>

<details><summary>Blog</summary>
<img src="docs/lighthouse/blog_lighthouse.jpg">
<details><summary>Blog Detail</summary>
<img src="docs/lighthouse/blog_detail_lighthouse.jpg">
</details>

</details>

<details><summary>Book Now</summary>
<img src="docs/lighthouse/booking_lighthouse.jpg">
</details>

<details><summary>Contact</summary>
<img src="docs/lighthouse/contact_lighthouse.jpg">
</details>

<details><summary>PAGE</summary>
<img src="docs/lighthouse/account_lighthouse.jpg">
</details>






### Wave
WAVE was used to test the websites accessibility.

<details><summary>Home</summary>
<img src="docs/wave_validation/index_wave_validation.jpg">
</details>
<hr>

<details><summary>FAQ</summary>
<img src="docs/wave_validation/faq/faq_wave_validation.jpg">
</details>
<hr>

<details><summary>Room</summary>
<img src="docs/wave_validation/rooms/rooms_list_wave_validation.jpg">
</details>
<details><summary>Room(Detail View)</summary>
<img src="docs/wave_validation/rooms/rooms_detail_wave_validation.jpg">
</details>
<hr>

<details><summary>Blog</summary>
<img src="docs/wave_validation/blog/blog_bloglist_wave_validation.jpg">
</details>
<details><summary>Blog(Detail View)</summary>
<img src="docs/wave_validation/blog/blog_blogpost_wave_validation.jpg">
</details>
<hr>

<details><summary>Book Now</summary>
<img src="docs/wave_validation/bookings/bookings_res_wave_validation.jpg">
</details>
<details><summary>Reservation Choice</summary>
<img src="docs/wave_validation/bookings/bookings_res_choice_wave_validation.jpg">
</details>
<details><summary>Reservation Booking Form</summary>
<img src="docs/wave_validation/bookings/bookings_bookingform_wave_validation.jpg">
</details>
<details><summary>Reservation Confirmation</summary>
<img src="docs/wave_validation/bookings/bookings_bookingform_confirmed_wave_validation.jpg">
</details>
<hr>

<details><summary>Contact</summary>
<img src="docs/wave_validation/contact/contact_wave_validation.jpg">
</details>
<hr>

<details><summary>Sign Up</summary>
<img src="docs/wave_validation/user_profiles/account_signup_wave_validation.jpg">
</details>
<details><summary>Logout</summary>
<img src="docs/wave_validation/user_profiles/account_logout_wave_validation.jpg">
</details>
<details><summary>Login</summary>
<img src="docs/wave_validation/user_profiles/account_login_wave_validation.jpg">
</details>
<hr>

<details><summary>Account</summary>
<img src="docs/wave_validation/user_profiles/account_wave_validation.jpg">
</details>
<details><summary>Account Info Edit</summary>
<img src="docs/wave_validation/user_profiles/account_edit_wave_validation.jpg">
</details>
<details><summary>Account Booking List</summary>
<img src="docs/wave_validation/user_profiles/account_bookings_wave_validation.jpg">
</details>
<details><summary>Account Booking Edit</summary>
<img src="docs/wave_validation/user_profiles/account_bookings_edit_wave_validation.jpg">
</details>
<details><summary>Account Booking Edit Confirm</summary>
<img src="docs/wave_validation/user_profiles/account_bookings_edit_confirm_wave_validation.jpg">
</details>



##### Back to [top](#table-of-contents)<hr>


## Testing

1. Manual testing
2. Automated testing

### Manual testing

1. User Story

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 | #### | #### | #### |

<details><summary></summary>
<img src="">
</details>


### Automated testing

- Testing was done using the built in Django module, unittest.
- Coverage was also usesd to generate a report


<details><summary>APP test.py</summary>
<img src="">
</details>


### Device Testing & Browser compatibility


The following devices were used for tests:

<details><summary>DEVICE</summary>
<img src="">
</details>


##### Back to [top](#table-of-contents)<hr>


## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| #### | #### |

##### Back to [top](#table-of-contents)<hr>


### Heroku Deployment

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
<details>
<img src="">
</details>

2. Create an app, give it a name for such as ci-pp4-the-diplomat, and select a region
<details>
<img src="">
<img src="">
</details>

3. Under resources search for postgres, and add a Postgres database to the app
<details>
<img src="">
</details>

Heroku Postgres

1. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
<details>
<img src="">
<img src="">
</details>

2. Install the plugins dj-database-url and psycopg2-binary.

3. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
<details>
<img src="">
</details>

4. Create a Procfile with the text: web: gunicorn APPNAME.wsgi
<details>
<img src="">
</details>

5. In the settings.py ensure the connection is to the Heroku postgres database
<details>
<img src="">
<img src="">
</details>

6. Ensure debug is set to false in the settings.py file
<details>
<img src="">
</details>

7. Add localhost, and ##### to the ALLOWED_HOSTS variable in settings.py

8. Run "python3 manage.py showmigrations" to check the status of the migrations

9. Run "python3 manage.py migrate" to migrate the database

10. Run "python3 manage.py createsuperuser" to create a super/admin user

11. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories

12. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products

13. Install gunicorn and add it to the requirements.txt file using the command pip3 freeze > requirements.txt

14. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a ci-pp4-the-diplomat
<details>
<img src="">
<img src="">
</details>


15. Ensure the following environment variables are set in Heroku
<details>
<img src="">
</details>

16. Connect the app to GitHub, and enable automatic deploys from main if you wish
<details>
<img src="">
<img src="">
</details>

17. Click deploy to deploy your application to Heroku for the first time

18. Click on the link provided to access the application

19. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue
<hr>

### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner
<hr>

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.

##### Back to [top](#table-of-contents)<hr>


## Credits

### Images


### Code


##### Back to [top](#table-of-contents)<hr>

## Acknowledgements

### Special thanks to the following:
