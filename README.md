# APP NAME

![Am I Responsive]()

**Developer: Christopher Jimerson**

💻 [Visit live website]()



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

<hr>

### User Goals

- 

### Site Owner Goals

- 

<hr>


## User Experience

### Target Audience
- 

### User Requirements and Expectations

- 

##### Back to [top](#table-of-contents)<hr>


## User Stories

### Users

1. 




### Admin / Authorised User

1. 



### Site Owner  

1. 

### Kanban, Epics & User Stories
- GitHub Kanban was used to track all open user stories
- Epics were created using the milestones feature
- Backlog, In Progress, Done headings were used in the kanban

<details><summary>Epics</summary>

![Epics]()

</details>

<details><summary>User Stories</summary>

![User stories]()

</details>

<details><summary>Kanban</summary>

![Kanban finish]()

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
    - 

#### Database

- Built with Python and the Django framework with a database of a Postgres for the deployed Heroku version(production)

<details><summary>Show diagram</summary>
<img src="">
</details>


##### User Model
The User Model contains the following:
- user_id
- password
- last_login
- is_superuser
- username
- first_name
- last_name
- email
- is_staff
- is_active
- date_joined

#####  Model
The ### Model contains the following:
 - 



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
- [ElephantSQL]()
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
<details><summary>Page</summary>
<img src="">
</details>
<details><summary>Subpage</summary>
<img src="">
</details>

### CSS Validation
The W3C Jigsaw CSS Validation Service

<details><summary>FILE</summary>
<img src="">
</details><hr>

### JavaScript Validation
JSHint JS Validation Service

<details><summary>FILE</summary>
<img src="">
</details><hr>

### PEP8 Validation


<hr><summary>APP/PAGE</summary><hr>


<details><summary>####.py</summary>
<img src="">
</details>



### Lighthouse

Performance, best practices and SEO was tested using Lighthouse.

#### Desktop
<details><summary>PAGE</summary>
<img src="">
</details>



#### Mobile
<details><summary>PAGE</summary>
<img src="">
</details>



### Wave
WAVE was used to test the websites accessibility.

<details><summary>PAGE</summary>
<img src="">
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
