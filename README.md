# __Journee__

Journee is a platform that gives you the freedom to journal the important parts of your life, either just for you or for others to share in. It’s a great way to capture a single page for that day along with a photo and selfie, if you wish. You then have a chronological history of all the things you want to look back on in years to come. It’s a great way to stay connected with your journey through life and share it with others!

![Main Image](docs/main_image.webp)

## Planning

I thought a lot about how I could bring to life my idea of an online journal where users could document their journey through life. It came from reading old diaries my father kept, they were a portal into the past, with a simplistic charm. I wanted to create something modern but connected to the spirit of the past where you had one day of condensed notes.
The name comes from a combination of...

* Journal
* Journey
* Journée (French for day)

The initial plan for the site was to include more interaction features such as comments and reactions, along with notifications and approval mechanisms. After careful consideration I decided that these features would actually detract from the simplicity of the application, after seeing friends and family with various social media apps that bombarded them with notifications and reminders I decided this is not what I wanted.
A journal is really about you and documenting your story. I didn’t want it to become a race to build followers/friends or to tailor your content to please or attract others.
I did want to give users the ability to share their journal with others but not for this to be the default, when a user creates a new journal page it's private by default and they have to choose to publish it for others to see.

I also wanted to give user the choice of including media but didn’t want it to become of massive collection. Like the journal entry I have limited it to one per day so the users will think carefully about what they upload

### Target Audience

* Anyone that wants to keep a journal of their life
* This site is aimed at all ages. This was a big driver in how focused the user interface is.

### Core Features

* Frictionless Sign Up & Sign In
* View/search public journals without an account (Entices Sign Up)
* Showcase journal entries on the landing page
* Abilty to switch site style (light/dark/custom colour modes)
* Add/edit/delete journal pages
* Limit of 1 page per day
* Limit of 1 photo and Selfie per day
* Default images for those that do not want to add photos
* Ability to make journals private/public
* Extended profile that alows a users private/public publishing preference to be stored 

### User Interface

When I was working on the concept for Journee I wanted to present the user with an experience that was similar to a traditional diary. I wanted to keep the interface very clean and focus the users attention on the main content of the journal entry.
To that end, each page has a title, content, and an optional selfie/photo.

### Colour Theme

I played with multiple different colour ideas for the site and in version 1 of the site I have utilized a simple light and dark interface that embraces the standard bootstrap colour mode that is tried and tested. A future enhancement would be to create further customized colour modes and CSS that allow for theming of "Sci-fi" or "Retro" type looks.

The primary acent colour I used for the logo/favicon is an amber orange yellow #FFC000. This is a nod to yellow writing paper and old books.

![Logo](docs/logo_color.JPG)

### Agile Planning ###

I used the agile method to plan out Journee and you can review all my Epics and User Stories in the Project linked to this repo [__Here__](https://github.com/users/Will-Griffiths-Ireland/projects/2/views/2)

* I took the role > action > benefit approach to writing my user stories.
* I used a customized list view and Kanban for planning.
* 4 sprints of 1 week each were planned and assigned to each item 

I won't repeat all the details here as you can view the public project but here are a few screens of the project in flight.

![Project list](docs/mid_project_list.JPG)

![Project kanban](docs/mid_project_Kanban.JPG)



## Database Design Schema

After descoping features that would have made the application more noisy to users I ended up with a a straighforward schema.
I have omitted the fields in the all-auth table that are unused.

![DB Schema](docs/DB_Schema.webp)

## User interface Design

All my intial wireframe concepts can be found here in a [PDF](docs/Journee_wireframes.pdf).

The basic layout of the site aims to be simple and intuitive for anyone to pickup and use within seconds.

## Features

### Showcase Page

The showcase page is designed as the landing spot for all users. It helps make the site come to life and encourages people to take a look at others’ journals, then hopefully sign up and start their own.

* Top 8 most viewed public journal pages
* Displayed to both unauthenticated and authenticated users
* Future enhancements would include an element of user customisation such as selecting what type of content to show

![Showcase Page](docs/showcase_white.webp)

### Theme Mode

I utilised bootstraps new colour mode to include both a light and dark mode.
The screenshots througout the readme have a mix of the modes

* All user can chose their preference and it is stored/retrieved in local storage
* Auto will detect the users current system preference

![Nav Theme](docs/nav_theme.webp)

![Theme](docs/theme.webp)

### User Account Creation

The user account creation utlizes django-allauth

* The username must be unique to this system and the user will get a warning if its in use.
* Email is an optional field but please note this is only for testing and review. For the production website I would enable email verification to avoid account spamming and enable password resets via email
* The password field applies the standard security hardening for length and complexity.

![Account Create](docs/create_account.JPG)

### Message Notifications

All user interactions with the database will result in an onscreen message that is diaplyed in the top center of the screen for 3 seconds before it fades away.

* Sign in / out
* Adds
* Edits
* Deletes

![Account Create](docs/Message_notifications.webp)

### User Login

* The user login screen asks for the username and password
* A message is shown to the user if their credentials do not match any stored records

![Account Sign In](docs/login.JPG)

### Adding A Journal Page

Once a user has an account and is signed in they can create a journal entry.

* The title and journal entry are mandatory fields
* The title is limited 30 characters and the journal entry is 15000
* I used the django richtextfield widget for the journal entry to allow for a little formatting
* The user has the option to make the entry public, without any extended profile preference the default is private. I did this on a per page level to give the user full control of what they want to make public or not
* The self image is optional and will be replaced by the Journee logo if the user does not upload one. I have this for users that want to track their how they look/age
* The day image is basically for the photo the user thinks will sum up their day. Again if they choose not to then the logo is used.
* Users are blocked from uploading files other than image files
* Images are resized to 200px for self images and 800px width for day images and encoded as webp for optimum file sizes
* The user is limited to a single journal page per day and will get a warning if they already have one whihc has a link to it. Please note that while I was testing and creating content to fill the site I disabled the date check so thats why you will see some users with multiple pages for the same day.

![Page Exists warning](docs/add_page.JPG)

![Journal Page Add](docs/page_exists.JPG)

### User Journal View

The Journal view is the users collection of journal pages

* They are brought to this view when they submit a new journal page
* The journal view is paginated to 4 preview cards per page
* The total number of pages is displayed in the heading
* Previous and next buttons allow the user to flick through their journal
* This page is private to the user so they will be able to see all of their pages irrespective of if they are set public or private

![Journal View](docs/journal_view.JPG)

## Journal Page View

The journal page view is where the user views and reads that page

* The self image is displayed at the top
* The title, public/private status and view count are alongside
* The day photo is next with the journal entry below it.
* If the user is the creator of the page then they will have edit/delete buttons at the bottom of the page

Below are Desktop and Mobile Screenshots

![Journal Page View Desktop](docs/journal_page_view_desktop.JPG)

![Journal Page View Mobile](docs/journal_page_view_mobile.JPG)

Example of page with no images upload that is automatically using the placeholder logo images

![Journal Page View Mobile No Images](docs/journal_page_view_mobile_noimages.JPG)

### Editing A journal Page

When editing a page

### Deleting A Journal Page

### Journal Search

### View Count

* Each journal entry has functionality to track how many views it has had.
* This allows a user to know how many others viewed their public journal page.
* The count is also used in picking content for the showcase page.
* The logic delibrately counts every single view to allow for a simulated production expereince during testing and review.
* With a launched site this functionality would be modified to use something like Django-Hitcount so that only unique views per IP would be counted

### Customer Error Messages

Standed errors such as 500, 404 and 403 have custom templates

### Security

Across the site there are checks to see who the user is and who owns a page

## Testing

All details on testing can be found [here](TESTING.MD)

## Technoligies & Tools

* Bootstrap 5.3
* Jquery 3.7.0
* Django

## Deployment

* fork repo 
* 
* setup postgress or db of choice
* setup cloud storage of choice
deploy to Heroku

* create a env.py file locally with these settings, or alter them depending on your choice of cloud storage and db

>import os

>os.environ['SECRET_KEY'] = '--UNIQUE SECRET KEY--'  
>os.environ['DEV'] = 'True'  
>os.environ['CLOUDINARY_URL'] = '--URL TO ACCESS CLOUDINARY--'  
os.environ['DB_PASSWORD'] = '--PASSWORD FOR DB CONNECTION--'



## Future Enhancements

* Full encrption of all user journal and profile information
* Ability to search users based on their description words
* Ability to follow other users and have a dedicated page view of their pages

## Credits & Acknowlegements

* Boot strap docs
* Django docs