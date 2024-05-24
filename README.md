# Tiny Bites

Tiny Bites is more than just a food website; it's a culinary community where users can unleash their creativity by crafting their own delectable bites to share with the platform.

Whether it's a gourmet twist on instant noodles or a cherished lunchtime BLT spot, Tiny Bites invites users to explore and celebrate the world of snacks and tiny delights. With a focus on user-friendly design, the platform aims to provide a seamless experience for posting recipes and sharing ratings. It's not just about food; it's about sharing thoughts, emotions, and experiences surrounding everyone's ultimate passion: food.

## User Needs

- **Cross-Device Accessibility**: Users expect seamless access to the website from any device, whether it's a smartphone, laptop, tablet, or desktop.
- **Responsive Design**: A responsive design is crucial to ensure that the website adapts and delivers an optimal viewing experience across all screen sizes, ensuring readability and usability.
- **Easy Posting**: Users should be able to effortlessly share their culinary creations with clear, intuitive posting guidelines.
- **Efficient Account Creation**: A quick and hassle-free account creation process is essential to encourage user participation.
- **Visual Appeal**: Users want to showcase their culinary creations through captivating images that highlight the aesthetic appeal of their bites.
- **User-centric Navigation**: Users need to easily navigate through their own posts, find specific recipes, and manage their comments and posts effectively.

## Planning

Before embarking on the development journey, meticulous planning was undertaken to conceptualize the layout, define essential fields, and establish the Database Schema.

### Planned Design

#### Large Screen Layout

- The large screen layout provides ample space for users to navigate comfortably, with distinct sections for easy access to various features and functionalities.

![Large Screen Layout](docs/large_screen_layout.png)

#### Types of Elements

- Different types of elements, including cards, forms, and navigation menus, were meticulously designed to ensure consistency and cohesiveness throughout the platform.

![Types Layout](docs/types_layout.png)

#### Small Screen Layout

- The small screen layout prioritizes readability and usability, with optimized design elements to enhance the mobile browsing experience.

![Small Screen Layout](docs/small_screen_layout.png)

## Features

### Existing Features

#### Home Page / Index

##### Navbar

- The navbar was created with ease of access in mind using bootstrap. It provides a responsive navigation bar that displays all the website's different pages, with space to read and navigate clearly. On smaller screens, it neatly tucks together, hidden away until the burger icon is selected.
  - Contains:
    - **Feed**
    - **My Bites**
    - **To be Approved**
    - **Create**
    - **Login**, **Sign up**, and **Log out** (Based on if you are logged in or not)
    - If the user is logged in the navbar will display their username which acts as a link to the **Profile**.

![Navbar Small Screen](docs/navbar_small_screen.png)

![Navbar Big Screen](docs/navbar_big_screen.png)

- Because most of the nav items are for a user who is logged in, it was best to hide all nav links for a non-logged-in user as they would have little need for any of the functionality provided.
- The account login and sign up links remain active for non-logged-in users.

![Navbar Logged out](docs/navbar_logged_out.png)

##### Feed

- The main point of the website is the feed; this is where the user will spend a lot of their time (assuming they are casual viewers; more specific users would enjoy the search bar below more). Because the target audience for this section is casual, there is quite a bit of white space to avoid crowding and intimidation for some users.

![Feed Big Screen](docs/feed_big_screen.png)

- Each recipe card is generously sized to give a feel of one at a time. This makes it more readable for the user and enables them to focus on each recipe individually to find what they are looking for or something they might want to try.

![Feed Small Screen](docs/feed_small_screen.png)

##### Search Bar

- The search bar is a necessary feature for this type of website, enabling users to find specific recipes based on their preferences. The search bar runs a query on the Create model by 'name', and it is set to contain so that even if a user has no idea how to spell a dish, as long as they are close enough, they will find it.

![Search Bar](docs/search_bar.png)

##### Recipe Cards

- The recipe card is designed with the idea of a scroller in mind, similar to those on social media platforms like Facebook or Instagram. It provides a little preview to pique the reader's interest.
- Each card, at first glance, features an image of the post, the dish's name, the author's username, and the creation date/time.

![Card Top](docs/card_top.png)

- Recognizing that sometimes a post might catch your eye but not immediately draw you in with just the information above, the description button reveals a box on the card with the description the user set for the recipe, along with another button that leads to the post's detailed page. This creates a step-by-step journey for the user, rather than overwhelming them with all the information at once or making them hunt for it at the end.

![Card Bottom](docs/card_bottom.png)

##### Pagination

- Pagination breaks up the number of posts displayed on the feed at one time.
- The arrow icon showcases the buttons for the next and previous pages, providing a more user-friendly approach for users who might not be very good at reading or understanding the function.
- The page number is displayed for easy navigation and understanding of their position within the feed.

![Pagination](docs/pagination.png)

#### Post Detail

##### Recipe Card

- All the information is kept in one card, similar to the home page, avoiding the need for users to poke around for content.
- The card is titled with the name of the dish, and just under that, it shows "by 'username' | the date of creation," giving off an article feel.

##### Comment Sections

- The comment section is divided into two: posted comments and the comment creation form.

![Comment Section](docs/images)

###### Comments Post

- Here, all the comments posted by other users so far are displayed.
- The rounded corners and bubbly effect give the comments a social media feel.
- Each comment card contains:
  - Username
  - Comment Body
  - Date of Creation

![Comment Card](docs/images)

- Unapproved comments are only visible to the post owner and the comment author, styled faintly to indicate their pending status.

![waiting for approval](docs/images)

- Logged-in users can edit or delete their comments, even if awaiting approval, using the provided buttons.

![edit/delete buttons](docs/images)

- The section is scrollable to keep the page tidy and maintain focus on the recipe.

![comment scroll](docs/images)

###### Comments Creation

- Only available to logged-in users.
- The creation bubble is styled similarly to the comment cards for consistency.
- The text area can be stretched for additional space.

![comment creation](docs/images)

![streched comment creation](docs/images)

### My Bites

##### Card Layout

- The card layout provides a visually appealing presentation of each user's post, with clear separation between different pieces of information.
- Two cards are displayed per row, and they are brighter than those on the home page.
- The featured image is prominently displayed, maintaining aspect ratio consistency.
- The layout adapts seamlessly to different screen sizes.

##### Pagination

- Clear indication of the current page number and total pages helps users understand their position.
- Arrow icons enhance intuitive navigation.
- Informative alerts guide users when no posts are available, encouraging participation.

### To Be Approved

- A streamlined interface for managing comments awaiting approval on user posts.

##### Card Layout

- Comments awaiting approval are presented within a card layout for clear and structured information.

##### Action Buttons

- Action buttons for approving or deleting comments directly from the interface streamline the moderation process.

##### Modal Confirmation

- Modal dialogs for both approval and deletion actions prevent accidental actions and ensure accountability.

### Create Bite Form

### Carousel Form Navigation
- The form is divided into multiple slides using Bootstrap's carousel feature. This design choice was made to prevent users from feeling overwhelmed by a lengthy form. By breaking the form into manageable sections, users can focus on one task at a time, reducing cognitive load and improving the overall user experience.
- Ensuring that the form is fully responsive was a key consideration. The carousel controls adjust based on the screen size:
  - **Mobile Views**: For smaller screens, internal buttons are provided within each slide to navigate between sections, making it easy to use on touch devices.
  - **Larger Screens**: For desktop and larger screens, external controls are positioned outside the form to provide a clean and uncluttered interface. These controls are strategically placed to enhance usability without obstructing the form content.

### Form Sections
The form is divided into four distinct sections, each represented by a carousel slide. This segmentation ensures clarity and focus, guiding users through the process step-by-step.

**First Slide**
  - **Name Field**: A text input for the name of the bite. This field is crucial as it helps users to clearly identify their post.
  - **Featured Image**: An image upload field for adding a featured image of the bite. Visual appeal is essential in culinary communities, and this feature allows users to showcase their creations attractively.

**Second Slide**
  - **Description**: A text area for the description of the bite. This section allows users to provide context and background for their creation, engaging the community with their story or inspiration behind the dish.

**Third Slide**
  - **Ingredients**: A text area for listing the ingredients required for the bite. Clear and detailed ingredient lists are vital for users who wish to recreate the dish, ensuring that all necessary components are listed.

**Fourth Slide**
  - **Instructions**: A text area for providing the instructions to prepare the bite. Step-by-step instructions help users to follow along and replicate the recipe accurately.
  - **Submit Button**: A button to submit the form and create the post. Placing the submit button at the end of the carousel ensures that users have completed all necessary sections before submission, reducing the likelihood of incomplete posts.

- Overall, the design aims to balance aesthetic appeal with functional efficiency, creating a pleasant and intuitive experience for users. The use of Bootstrap's carousel and responsive design principles ensures that the form is accessible and easy to use across all devices.

### Profile

#### Page Layout

- The profile page allows users to edit their information, including first and last name, email, and password.
- The input for the password on the profile page is for design and is disabled.

![Profile Form](docs/images)

#### Password Modal

- The password change is done via a modal containing a form.
- JavaScript logic ensures a smooth process with password strength checks and validation.

## Account Pages

### Login

### Logout

### Sign up

### Forgot password

## Features Left to Implement


# Testing


### Conclusion


### User testing


### Validator Testing

### Bugs I Faced Along The Way


### Bugs I did not get to fix


## Deployment

This section describes how to create a new repository.

- This repository was created using [GitHub](https://github.com/) The steps are as followed:
  - I went to the [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template)
  - I selected the green button labeled 'Use this template'
  - Then, Create a new repository.
  - Then I was brought to a new page to set the name and setting for my new repository.
  - I named my repository 'R.P.S.L.S'

This section describes how I set up my workspace, Once my repository has been created.

- The workspace I used for this project was [codeanywhere](https://app.codeanywhere.com/). The steps are as follows:
  - I opened [GitHub](https://github.com/) and went to the 'R.P.S.L.S' repository
  - To get the link for codeanywhere I clicked the green button '<>code'.
  - Here under local, I could copy the link needed: <https://github.com/JAmcevoy/R.P.S.L.S.git>
  - Then I went to code anywhere.
  - In workplaces, I selected new workspaces
  - Here I copied the link from the git hub and clicked to create to make my workspace.

This section describes the commands I used in code anywhere to push my code and changes to GitHub.

    -  I created the files and folders needed for my project.
    - I used the git add . command to add all changes above.
    - Using the git commit command I committed the change and used -m to attach a message to the commit.
    - When I was finished with the creation I used git push to push all these files and folders to GitHub.
    - I used these same 3 commands through the creation and modification

This section should describe the process I went through to deploy the project to a hosting platform.

- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - <>

## Heroku
<!-- Edit with detail -->
Part 1 - Create the Heroku app:
10/04/2024, 13:40 Challenge: Deploy the project | Getting set up | FSD101_WTS Courseware | Code Institute
https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+2023_Q3/courseware 2/2
1. Have you referred back to the deploying to Heroku text step topic to create
your Heroku app?
2. Have you added a key of DISABLE_COLLECTSTATIC and a value of 1 and
clicked Add?
Find this in the Config Vars section of the Settings tab.
Part 2 - Update your code for deployment:
1. Have you pip3 installed the webserver gunicorn and added it to the project
requirements?
pip3 install gunicorn~=20.1
pip3 freeze --local > requirements.txt
2. Have you created a Procfile at the root directory of the project, declared the
process as web and added a start command?
web: gunicorn codestar.wsgi
Hint: Note there is a space after the colon.
Hint: The Procfile has no file extension.
3. Have you changed DEBUG to False and added , '.herokuapp.com' to
the ALLOWED_HOSTS?
DEBUG = False
,'.herokuapp.com'
Hint: Remember the comma and the dot before herokuapp.
4. Push the code to GitHub.
git add .
git commit -m "readies code for deploy"
git push origin main
Part 3 - Deploy to Heroku:
1. Have you clicked on the Deploy tab in your Heroku app dashboard,
connected to your GitHub repo and clicked on Deploy Branch?
1. Hint: Start typing your project repo name into the search box and click on the
GitHub repo you want to deploy from.
2. After manually deploying the main branch, you can view the build output in the
application’s Activity tab in the dashboard.
1. Have you clicked the Open app button to see your deployed app?
Hint: The build must be complete before you can open the app.
Hint: You will see an error that the current path didn’t match any of the URL
patterns as you have not written the urlpattern yet

## Credits

- I used these resources to research and develop my understanding of JavaScript, as well as get inspiration for my own code. During this research, I have borrowed some ideas and modified the code to suit my project. No code was used unedited

### Design

- All the design screenshots from above came from [Wirframe](https://wireframe.cc/)

### Code


### Content

