# Valencia_blog ![Alt text](static/favicon.ico/favicon-16x16.png)

## Overview

This project is a simple, easy-to-use blog designed for visitors to the city and surrounding area. The blog highlights key points of interest, offering an overview of each location. It also encourages user interaction through a comment section on each post, along with the ability to like or dislike both posts and comments.

The design and development follow best practices in user experience, CRUD principles, mobile-first responsiveness, and Agile methodology.

Live link to project [Valencia_Blog](https://valencia-blog-c8aa0f69cb17.herokuapp.com/)

# City Visitor Blog 
![Alt text](static/images/Large-screen-view.png)

---

## Mobile Screen Size appearance

![Alt text](static/images/Mobile-view.png)

## Tablet / Medium Screen Size appearnance

![Alt text](static/images/Tablet-view.png)

## Wireframe Designs

### Home Page

Laptop

 ![Alt text](static/images/Blog-home-wire.png) 

Mobile 

![Alt text](static/images/Blog-home-mob.png)

### Blog Post Detail Page

Laptop  

![Alt text](static/images/Blog%20post.png) 

Mobile  

![Alt text](static/images/Blog%20post%20mobile.png)

[Back to Top](#top)

## User Stories

User Stories can be found [here](https://github.com/users/Richard-L4/projects/8) on my GitHub profile.

---

## 1. User Experience (UX)

This platform focuses on providing an intuitive, accessible experience for all users:

- **Simplicity**: Clean interface with clearly labelled sections and content.
- **Accessibility**: Information is easy to find and written in a clear, engaging style.
- **Interaction**: Users can comment on posts and express opinions through a like / dislike feature.
- **Responsiveness**: Developed with a **mobile-first approach**, ensuring the site works flawlessly on phones and tablets before scaling up to larger screens.

---

## 2. CRUD Principles

The platform supports full **CRUD functionality**, enabling interactive and dynamic content:

- **Create**: Users can add (create) comments on posts.
- **Read**: All site visitors can read posts and their associated comments.
- **Update**: Logged-in users can edit their own comments; admin users can update blog posts.
- **Delete**: Users can delete their own comments; admin users can delete posts.

This structure ensures flexibility and control over user-generated content.

---

## 3. Five Planes of User Experience Design

The site was planned and built following the **Five Planes of UX Design**:

### 🔹 Strategy Plane
- Clear goal: to inform and engage city visitors with useful, local insights.

### 🔹 Scope Plane
- Features include: post listings, post detail pages, comment forms, and like / dislike buttons.
- Content includes: short overviews of points of interest, post images, and user interaction.

### 🔹 Structure Plane
- Clear navigation and flow: from homepage to individual posts to comments.
- Logical categorisation of content by location or type of attraction.

### 🔹 Skeleton Plane
- Wireframes and layout prioritised **mobile-first** usability.
- Focused on minimal scrolling, easy-to-tap buttons, and fast-loading elements.

### 🔹 Surface Plane
- Visual design is clean and welcoming.
- Consistent fonts, colours, and spacing create a calm, informative atmosphere.

---

[Back to Top](#top)

## 4. Agile Development Principles

This project was developed using **Agile principles**, including:

- **Iterative process**: New features were developed in stages, tested, and refined.
- **Continuous feedback**: Feedback from test users influenced improvements in usability.
- **User-focused**: Priorities were based on what would best support visitors to the city.
- **Responsive to change**: The design was flexible and evolved based on both technical and user needs.

---

## Mobile-First Focus

The entire project adheres to a **mobile-first** design strategy:

- Layouts were initially built for smaller screens and enhanced for larger devices using media queries.
- Elements like buttons, menus, and content blocks are optimised for touch input and smaller viewports.
- Lightweight assets and prioritised content loading enhance performance on mobile networks.

---

## Summary

This city visitor blog offers a functional, engaging, and responsive platform that serves both informative and interactive purposes. With a clear focus on user experience, flexible content management, and scalable design, it provides a solid foundation for future expansion or integration with other local services.

[Back to Top](#top)

## Content of Blog Site

### Home Page

![alt text](static/images/Laptop-view.png)

#### Footer / Pagination

Just above the Footer there is a Next and Prev button on respective pages for Pagination, which is set to 2 rows of 3 posts per page, 6 in total and will automatically create a new page with the appropriate Next / Prev buttons once this is exceeded.

![alt text](static/images/Index-footer.png)

### Post Page

![alt text](static/images/Post-tp.png)

### About Page

![alt text](static/images/About-top.png)

### Register Page

![alt text](static/images/Register.png)

### Login Page

![alt text](static/images/Sign-in.png)

### Logout Page

![alt text](static/images/Logout.png)

## Detailed Features of the Blog Site

This blog site is designed with a focus on seamless user experience and intuitive interaction, following the five planes of user experience: strategy, scope, structure, skeleton, and surface. Every element is crafted to be immediately clear and easy to navigate.

### 1. Homepage and Navigation

#### Favicon Icon

The favicon icon is the Flag of the Valencian Community 

![Alt text](static/favicon.ico/apple-touch-icon.png)

### Span class Tanslatable "A guide to the Valencian Community"

The span class is interchangeable between English and Spanish (Castellano)

#### English

![Alt text](static/images/Guide-english.png)

#### Spanish

![Alt text](static/images/Guide-spanish.png)

Home Page

![Alt text](static/images/Laptop-view.png)

The homepage provides an immediate understanding of the site’s purpose, giving users an overview of blog content and essential sections. Clear labels and an intuitive navigation bar make the layout user-friendly. The active tab is highlighted, guiding the user to their current page. This design ensures that users know where they are and where to go next, creating an engaging and efficient experience.

#### Top of Cards

![alt text](static/images/Index-top-of-card.png)

#### Bottom of Cards

![alt text](static/images/Index-bm-card.png)

### 2. Post Pages and Categories

![Alt text](static/images/Post-tp.png)

Each blog post is directly related to its category, and the category description is visible, offering context on the topic and encouraging further exploration. The post pages themselves are designed to be clean and readable, ensuring that the content is the focal point. Posts are easy to navigate with clear headings, like / dislike buttons, and an intuitive comment system.

### 3. Comment System & User Interaction

![Alt text](static/images/Post-btm-sub.png)
---
![Alt text](static/images/Post-btm-update.png)

A robust commenting system allows users to engage with content. Registered users can add, edit, and delete their comments, making it easy to provide feedback or update their opinions. This encourages real-time discussions. Each comment also includes like / dislike buttons that show the popularity of specific comments, making it a dynamic space for interaction. For admin users, the ability to manage posts and comments enhances the site’s functionality, ensuring content stays fresh and relevant.

### 4. User Registration & Personalization

![Alt text](static/images/Register.png)

The user registration system is straightforward, allowing new users to sign up and log in with minimal steps. This enables them to interact with posts and comments directly. Unregistered users can still view the content but are prompted to sign in to comment. 

### 5. Admin Control and Post Management

- Top of Post detial page for Admin Authorised User's.

![Alt text](static/images/Post-tp-edit.png)

---

### 6. Admin users have the ability to edit or delete posts 'on the go', without the need to rely on the Django admin panel. This allows for quick content moderation and real-time updates to blog posts.

#### Post Edit Page

- Top of Post Edit page for Admin Authorised User's.

![Alt text](static/images/Edit-post-tp.png)

- Bottom of Post Edit page for Admin Authorised User's.

![alt text](static/images/Edit-post-btm.png)

### 7. Post Delete Page

![alt text](static/images/Post-delete-page.png)

### 8. Collaborate Form

![Alt text](static/images/Collaborate.png)

The Collaboate form provides users with a clear, accessible way to reach out to the blog team. A fun headline message and friendly welcoming 'blurb' inviting  user's to make contact and contribute to the site with minimal  personal information required.

### 9. Like / Dislike Buttons

For non logged in user's the like / dislike buttons are disabled.

![alt text](static/images/Post-cont.png)

For logged in user's the buttons are active. Please see below image for further details.

![alt text](static/images/Post-btm-sub.png)

The like / dislike functionality associated with the comments allows users to express their opinions quickly. This feedback mechanism not only enhances user interaction but also provides admins and users with a clear picture of what content is resonating with the audience. The counters next to these buttons track the popularity of the comments, creating a dynamic environment for user-driven content.

### 10. Default Image on creation / adding of Posts.

Default image.

![Alt text](static/images/default.jpg)

---

## UX Principles Behind the Features

The design of these features adheres to the five planes of user experience:

- **Strategy**: The website is strategically focused on content discovery and user interaction, with features like the comment system, like / dislike buttons, and admin management supporting these goals.
  
- **Scope**: The scope of the website ensures that users can easily sign up, interact with content, and provide feedback, while admins can moderate and manage posts efficiently.

- **Structure**: Clear navigation, accessible posts, and an easy-to-use comment system create a solid structural foundation.

- **Skeleton**: The user interface skeleton is minimal and clean, designed for readability and ease of navigation.

- **Surface**: Visually, the blog site uses clear, intuitive design elements like the highlighted active tabs, buttons and highlight on hover content on the index page to help users feel confident and engaged while navigating the site.

By focusing on these UX principles, the blog site ensures a cohesive, user-friendly experience for both general users and admins, making it easy to interact with, moderate, and manage content on the go.

[Back to Top](#top)

## Manual Testing

Each major feature of the blog site was manually tested to verify that it worked as intended. This included:

- **Post Listing Page**: Displays posts in a 3x2 layout. All blog titles, images, and "Read More" links were verified to ensure correct routing to the detail view.

- **Post Detail Page**: Displays full content, author, comment section, and thumbs up / down buttons. Each feature was tested for display accuracy and interactivity.

- **Comment Functionality**:
  - Submitting comments as a logged-in user was tested and confirmed to show the comment after comment approval in Django admin.
  - Editing and deleting user's own comments worked correctly after form validation checks.
  - Thumbs up / down buttons gave instant feedback without page reload via JavaScript and AJAX, and could be toggled.

- **Forms (Login, Registration, Comment)**: All forms were tested for validation, error messaging, and proper redirection.

- **Navigation and Footer**: All links and social icons were tested for accurate routing and responsiveness.

### Responsiveness Testing

####

- Tested on Google Chrome and Firefox, site works as expected.

- Tested across several screen sizes (mobile, tablet, desktop) using browser developer tools and manual resizing.

---

### Bugs Found and Fixes

| Bug Description | Fix Applied | Status |
|------------------|-------------|--------|
| "Gunicorn not recognised" warning in Heroku | Uninstall and reinstall | Fixed |
| "Cannot parse Procfile" warning in Heroku | File update had not pushed to GitHub, delete file and create and push again. | Fixed |
| Comment delete button showed for all users | Conditional check added to show only for comment owner | Fixed |


**Note on Documentation**:  
Due to the focus of the development of the site, and uncertanty as to the scale of bugs (whether very minor, or more complex), screenshots of bugs were not taken. However, descriptions and outcomes of each fix have been recorded.

---

### Conclusion

The testing procedures demonstrate that the blog site is functional, user-friendly, and responsive across all devices. All bugs that I am aware of have been fixed. 


## Functionality Test Table

| Page Name       | Feature / Button / Function                        | Expected Outcome                                                                 | Actual Outcome |
|----------------|-----------------------------------------------------|----------------------------------------------------------------------------------|----------------|
| **Home**        | Navbar: Home                                       | Redirects to homepage                                                            | Passed         |
|                 | Navbar: About                                      | Redirects to About page                                                          | Passed         |
|                 | Navbar: Login                                      | Redirects to Login page                                                          | Passed         |
|                 | Navbar: Register                                   | Redirects to Register page                                                       | Passed         |
|                 | Navbar: Logout (when logged in)                    | Logs out user and redirects to homepage                                          | Passed         |
|                 | View Post button / link                              | Opens selected post's detail page                                                | Passed         |
| **Register**    | Form: Username, Email, Password                    | Creates a new user account and redirects to homepage or login page               | Passed         |
|                 | Register / Sign Up button                            | Submits form data and triggers account creation                                  | Passed         |
| **Login**       | Login form Submit                                  | Logs in user and redirects to homepage or `next` page                            | Passed         |
|                 | Signup link                                        | Redirects to Signup / Register page                                                | Passed         |
| **Logout**      | Logout confirmation button                         | Logs out user and redirects to homepage                                          | Passed         |
| **About**       | Static content visible                             | Displays author or site info clearly                                             | Passed         |
|                 | Collaborate form (name, email, message)            | Submits message, success message shown                                           | Passed         |
|                 | Send button (collaborate form)                     | Triggers form submission                                                         | Passed         |
| **Post Detail** | Add Comment form (auth users only)                 | Submits comment and displays it below the post                                   | Passed         |
|                 | Submit Comment button                              | Sends comment via POST, updates without refresh (if AJAX), or reloads page       | Passed         |
|                 | Edit Comment button (comment author only)          | Opens comment in edit mode, allows update                                        | Passed         |
|                 | Delete Comment button (comment author only)        | Deletes the comment and removes it from view                                     | Passed         |
|                 | Edit Post button (admin only)                      | Opens edit form with current post pre-filled                                     | Passed         |
|                 | Delete Post button (admin only)                    | Deletes the post after confirmation                                              | Passed         |
|                 | Like button (all users)                            | Increases like count by 1, toggles icon state                                    | Passed         |
|                 | Dislike button (all users)                         | Increases dislike count by 1, toggles icon state                                 | Passed         |
|                 | Like / Dislike counters                              | Quantities reflect actual values and update on click                             | Passed         |
|                 | Prevent multiple **likes** (auth users only)       | Logged-in user can like only once  | Passed         |
|                 | Prevent multiple **dislikes** (auth users only)    | Logged-in user can dislike only once | Passed         |
|                 | **Like button (unauthenticated users)**            | Hidden & disabled; unauthenticated users can't like                             | Passed         |
|                 | **Dislike button (unauthenticated users)**         | Hidden & disabled; unauthenticated users can't dislike                          | Passed         |
| **Edit Post**   | Post title / body edit fields                        | Allows admin to modify post content                                              | Passed         |
|                 | Save / Submit Changes button                       | Saves changes and redirects to post detail                                       | Passed         |
| **All Pages**   | Social icons (footer)                              | Opens correct social links in new tabs                                            | Passed         |
|                 | Message alert close button                         | Closes success / error messages without reloading page                             | Passed         |


##  Data Schema Description

This project uses a **relational database schema** designed to manage blog content, user interaction, and site communication. It includes the following models:

---

### 1. **User**
Stores user account data. Each user has a unique `username`, `email`, and a hashed `password`, along with optional `first_name` and `last_name`. The `is_active` and `date_joined` fields support user management and registration tracking.

---

### 2. **Post**
Represents individual blog posts. Each post is authored by a single user (`author_id` foreign key), and includes:

- `title`
- `slug`
- `content`
- `created_on`
- `updated_on`
- `featured_image` (optional)
- `excerpt`

Posts can be linked to multiple **Categories** via a many-to-many relationship through the `PostCategory` join table.

---

### 3. **Category**
Used to group posts. Each category has:

- a unique `name`
- an optional `description`

Categories are linked to posts via a many-to-many relationship using `PostCategory`.

---

### 4. **PostCategory** (Join Table)
Intermediate table for the many-to-many relationship between **Post** and **Category**. Each row connects one post to one category.

- `post_id` (FK to Post)
- `category_id` (FK to Category)

---

### 5. **Comment**
Captures user feedback on posts. Each comment is associated with:

- one **Post**
- one **User**

Fields include:

- `body`
- `approved` (Boolean)
- `likes`
- `dislikes`
- `created_on`

---

### 6. **CommentReaction**
Tracks individual user reactions (like / dislike) on comments.

- `user` (FK to User)
- `comment` (FK to Comment)
- `action`: `"like"` or `"dislike"`

Each user can only react once per comment (`unique_together` constraint).

---

### 7. **About**
Stores static content for the "About" page:

- `title`
- `profile_image`
- `content`
- `updated_on`

This allows easy updates without changing the source code.

---

### 8. **CollaborateRequest**
Captures messages submitted via a contact form:

- `name`
- `email`
- `message`
- `read` (Boolean flag for admin tracking)

---

##  Relationships Summary

- **Post → User**  
  Each post is written by one user.  
  `Post.author_id → User.id`

- **Comment → Post**  
  Each comment belongs to one post.  
  `Comment.post_id → Post.id`

- **Comment → User**  
  Each comment is written by one user.  
  `Comment.author_id → User.id`

- **CommentReaction → Comment**  
  Each reaction is linked to one comment.  
  `CommentReaction.comment_id → Comment.id`

- **CommentReaction → User**  
  Each reaction is made by one user.  
  `CommentReaction.user_id → User.id`

- **Post ↔ Category**  
  Many-to-many relationship via `PostCategory`.  
  `PostCategory.post_id → Post.id`  
  `PostCategory.category_id → Category.id`


## Database Schema

### About

| Field           | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| `id`            | PK       | Primary Key                          |
| `title`         | String   | Title of the about page              |
| `updated_on`    | DateTime | Last updated timestamp               |
| `profile_image` | String   | URL or path to profile image         |
| `content`       | Text     | Content of the about page            |

---

### CollaborateRequest

| Field       | Type     | Description                          |
|-------------|----------|--------------------------------------|
| `id`        | PK       | Primary Key                          |
| `name`      | String   | Name of the requester                |
| `email`     | String   | Email of the requester               |
| `message`   | Text     | Message from the requester           |
| `read`      | Boolean  | Flag indicating if read              |

---

### User

| Field         | Type     | Description                          |
|---------------|----------|--------------------------------------|
| `id`          | PK       | Primary Key                          |
| `username`    | String   | Username of the user                 |
| `email`       | String   | Email of the user                    |
| `password`    | String   | Hashed password                      |
| `first_name`  | String   | User's first name                    |
| `last_name`   | String   | User's last name                     |
| `is_active`   | Boolean  | Whether the user is active           |
| `date_joined` | DateTime | Timestamp when user joined           |

---

### Post

| Field            | Type       | Description                          |
|------------------|------------|--------------------------------------|
| `id`             | PK         | Primary Key                          |
| `title`          | String     | Title of the post                    |
| `slug`           | String     | URL-friendly identifier              |
| `author_id`      | FK         | Foreign Key to `User`                |
| `featured_image` | String     | URL or path to featured image        |
| `content`        | Text       | Content of the post                  |
| `created_on`     | DateTime   | Date the post was created            |
| `status`         | Integer    | Post status (e.g., draft/published)  |
| `excerpt`        | String     | Excerpt of the post                  |
| `updated_on`     | DateTime   | Last updated timestamp               |
| `categories`     | ManyToMany | Categories associated with the post  |

---

### Category

| Field         | Type   | Description                            |
|---------------|--------|----------------------------------------|
| `id`          | PK     | Primary Key                            |
| `name`        | String | Unique category name                   |
| `description` | Text   | Optional category description          |

---

### Comment

| Field        | Type     | Description                            |
|--------------|----------|----------------------------------------|
| `id`         | PK       | Primary Key                            |
| `post_id`    | FK       | Foreign Key to `Post`                  |
| `author_id`  | FK       | Foreign Key to `User`                  |
| `body`       | Text     | Content of the comment                 |
| `approved`   | Boolean  | Whether the comment is approved        |
| `created_on` | DateTime | Timestamp of comment creation          |
| `likes`      | Integer  | Number of likes                        |
| `dislikes`   | Integer  | Number of dislikes                     |

---

### CommentReaction

| Field        | Type   | Description                                                           |
|--------------|--------|-----------------------------------------------------------------------|
| `id`         | PK     | Primary Key                                                           |
| `user_id`    | FK     | Foreign Key to `User`                                                 |
| `comment_id` | FK     | Foreign Key to `Comment`                                              |
| `action`     | String | Reaction type: `"like"` or `"dislike"`                                |

> **Note:** Each user can only react once per comment. This is enforced with a unique constraint on (`user_id`, `comment_id`).

---

### Relationships

- **Post** belongs to **User** (`author_id` → `User.id`)
- **Comment** belongs to **Post** (`post_id` → `Post.id`)
- **Comment** belongs to **User** (`author_id` → `User.id`)
- **Post** has many **Category** through `ManyToManyField` (`Post.categories` ↔ `Category.id`)
- **CommentReaction** belongs to **User** (`user_id` → `User.id`)
- **CommentReaction** belongs to **Comment** (`comment_id` → `Comment.id`)
- **CommentReaction** enforces unique reaction per user per comment (`unique_together`)

---

### ERD Diagram

![Alt text](static/images/ERD-diagram.png)

[Back to Top](#top)

---

### Future Features

- 🔹 **Comment notifications**  

Users will receive a notification when someone replies to their comment. This helps keep conversations going and improves user engagement.

- 🔹 **Follow users or topics**  

Users will be able to follow specific authors or blog themes so they can easily keep up with new content they’re interested in.

- 🔹 **Newsletter subscription** 
 
Users can sign up to receive regular email updates with the latest posts and news from the blog.

---

### Deployment

##  [PostgreSQL](https://www.postgresql.org) Database Setup & Connection

This guide outlines how to set up a PostgreSQL database (via Code Institute) and connect it to your Django project.

---

###  Create the [PostgreSQL](https://www.postgresql.org) Instance

1. Go to **[PostgreSQL from Code Institute](https://pg-database-codeinstitute.herokuapp.com/)**.
2. Enter your email and click **Submit**.
3. Wait for the confirmation and check your inbox for the database URL.

---

###  Connect Django to [PostgreSQL](https://www.postgresql.org)

1. **Set DEBUG to True** (for development):

    ```python
    # valencia/settings.py
    DEBUG = True
    ```

2. **Create `env.py`** in your project root:

    ```python
    import os

    os.environ.setdefault("DATABASE_URL", "your-database-url")
    ```

3. **Update `.gitignore`** to include:

    ```
    env.py
    ```

4. **Install required packages**:

    ```bash
    pip install dj-database-url~=0.5 psycopg2~=2.9
    pip freeze > requirements.txt
    ```

5. **Modify `settings.py`**:

    - Add these imports at the top:

        ```python
        import os
        import dj_database_url

        if os.path.isfile('env.py'):
            import env
        ```

    - Comment out the default SQLite config.

    - Add the following to connect Django to PostgreSQL:

        ```python
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
        ```

6. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

7. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

---

###  Prepare for Deployment

1. Set `DEBUG = False` in `settings.py`.

2. Push changes to GitHub:

    ```bash
    git add .
    git commit -m "Connect to PostgreSQL"
    git push
    ```

3. On **Heroku**:
    - Open your app dashboard.
    - Go to the **Deploy** tab.
    - Trigger a **Manual Deploy**.

---

###  Configure [Heroku](https://www.heroku.com) Database

1. Navigate to **Settings** > **Reveal Config Vars**.

2. If a Heroku `DATABASE_URL` already exists:
    - Go to the **Resources** tab.
    - Delete the Heroku Postgres add-on.
    - Confirm removal by entering your app name.

3. Go back to **Settings** > **Reveal Config Vars**.
    - Add a new config variable:

        ```
        Key: DATABASE_URL
        Value: your-postgresql-url
        ```

    - (Use the URL from your `env.py` or the email — without quotes.)

---

 Your deployed app is now connected to the free PostgreSQL database provided by Code Institute.

### [Cloudinary](https://cloudinary.com) API

This project uses the Cloudinary API to manage and store media files online, since Heroku does not support persistent media storage.

To set up your own Cloudinary API key:

1. Create a free [Cloudinary](https://cloudinary.com/) account and log in.
2. For your **Primary Interest**, choose **Programmable Media** (for image and video handling).
3. *(Optional)* Rename your assigned **cloud name** to something more memorable.
4. Go to your **Cloudinary Dashboard** and locate your **API Environment Variable**.
5. Copy the variable, but **remove the `CLOUDINARY_URL=` prefix** — the remaining part is your actual API key.

---

[Back to Top](#top)

## Validations

For details about input validations, see [Validations and Lighthouse Testing](./validations.md).

---

# [Heroku](https://www.heroku.com) Deployment

---

This project uses **[Heroku](https://www.heroku.com)**, a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

## Deployment Steps

---

1. Log into your [Heroku Dashboard](https://dashboard.heroku.com/), click **New** in the top-right corner, and select **Create new app**.
2. Enter a **unique app name**, choose the region closest to you (Europe or USA), and click **Create App**.
3. In your new app's **Settings** tab, click **Reveal Config Vars** and add the following environment variables:

| Key | Value |
|:---|:---|
| CLOUDINARY_URL | your own value |
| DATABASE_URL | your own value |
| DISABLE_COLLECTSTATIC | 1 (temporary; remove before final deployment) |
| SECRET_KEY | your own value |

4. Ensure your project has the following two files:
   - `requirements.txt`
   - `Procfile`

To install requirements:

```
pip install -r requirements.txt
```

To update `requirements.txt` if you installed new packages:

```
pip freeze --local > requirements.txt
```

To create the `Procfile`:

```
echo web: gunicorn app_name.wsgi > Procfile
```
> Replace `app_name` with the name of your Django app (the folder containing `settings.py`).

---

## Connecting to [GitHub](https://github.com/)
---

You can connect your Heroku app to your GitHub repository either:

- Via the Heroku dashboard by selecting **Deploy > GitHub > Connect to GitHub Repository > Enable Automatic Deploys**.

Or via the command line:

```
heroku login -i
heroku git:remote -a your-app-name
```

After committing your changes to [GitHub](https://github.com/), deploy to [Heroku](https://www.heroku.com) using:

```
git push heroku main
```

The project should now be deployed!

---

# Local Deployment
---

## Running Locally
---

1. Clone or fork the repository (instructions below).
2. Install dependencies from `requirements.txt`:

```
pip install -r requirements.txt
```

3. Create a `env.py` file at the root of your project and add your environment variables:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "your own value")
os.environ.setdefault("DATABASE_URL", "your own value")
os.environ.setdefault("SECRET_KEY", "your own value")

# Local development only
os.environ.setdefault("DEBUG", "True")
```

4. Run the project:

```
python manage.py runserver
```

5. To apply database changes:

```
python manage.py makemigrations
python manage.py migrate
```

6. To create a superuser for Django Admin:

```
python manage.py createsuperuser
```

7. If you have any fixture data to load:

```
python manage.py loaddata filename.json
```

---

# Cloning the Repository
---

To clone the project:

1. Navigate to the [Richard-L4](https://github.com/Richard-L4/Valencia_blog).
2. Click the **Code** button.
3. Copy the URL for **HTTPS**, **SSH**, or **GitHub CLI**.
4. Open your terminal and navigate to your desired directory.
5. Clone the repository:

```
git clone (https://github.com/Richard-L4/Valencia_blog)
```

6. Press **Enter** to create your local copy.

---


# Forking the Repository
---

To create your own fork of this repository:

1. Log in to GitHub and navigate to the [Richard-L4](https://github.com/Richard-L4/Valencia_blog).
2. Click the **Fork** button at the top right of the repository page (next to "Settings").
3. This will create a copy of the repository under your own GitHub account.

You can now freely make changes without affecting the original project!

---

[Back to Top](#top)

## Languages Used

- **HTML**:  
  Used for the main site content, including the structure of each page.
  
- **CSS**:  
  Used for the main site design and layout, providing styling for elements like headings, text, images, and buttons.
  
- **JavaScript**:  
  Used for user interaction on the site, adding interactivity like form validation and dynamic content changes.
  
- **Python**:  
  Used as the back-end programming language, handling server-side logic, database operations, and dynamic content generation.

---

###  Blog Project – Tech Stack Overview

| Category              | Tools & Technologies                    | Purpose / Description                                                |
|-----------------------|------------------------------------------|----------------------------------------------------------------------|
| Core Languages & Frameworks | Python, [Django](https://www.djangoproject.com)                        | Backend development and web framework                                |
| Frontend             | HTML, CSS, JavaScript                    | Markup, styling, and interactivity                                   |
| Styling & UI         | [Bootstrap](https://getbootstrap.com)                               | Responsive design and layout system                                  |
|                      | Django Crispy Forms                      | Clean and flexible form rendering, Bootstrap-friendly                |
|                      | [google fonts](https://fonts.google.com/)                             | Custom typography for enhanced visual design                         |
|                      |[Font awesome](https://fontawesome.com/)                             | Icons and symbols for enhanced UI                                    |
| Development Tools    | [Git](https://git-scm.com),[GitHub](https://github.com)                             | Version control and code hosting                                     |
|                      | [VS Code](https://code.visualstudio.com/)                                  | Integrated development environment (IDE)                             |
| Production & Deployment |[Heroku](https://www.heroku.com)                                | Hosting and deploying the Django project                             |
|                      |[Gunicorn](https://gunicorn.org/)                                 | WSGI server to run Django on Heroku                                  |
|                      | Whitenoise                               | Serves static files efficiently in production                        |
|                      | dj-database-url                          | Parses database configuration from environment variables (Heroku)    |
|                      | Psycopg2                                 | PostgreSQL adapter for Django                                        |

---

## Credits & Acknowledgements

### All photo's [Getty Images](https://www.gettyimages.co.uk/search/2/image?phrase=spain)

### Entire site: [Bootstrap](https://getbootstrap.com)

### Entire site: [Django documentation](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#ref-templates-builtins-tags)

### Entire site: [Code institute walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101N+3/courseware/713441aba05441dfb3a7cf04f3268b3f/824fccecd0fe4e44871eeabcbf69d830/)

**Note:** Chat Gpt used for spelling and grammar checks as a result of increased Microsoft subscription charges, and as an aid for general troubleshooting suggestions.

---

### My mentor Brian Macharia for his continued support and guidance.

---

[Back to Top](#top)

---
