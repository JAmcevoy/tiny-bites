# Tiny Bites

Tiny Bites is more than just a food website; it's a culinary community where users can unleash their creativity by crafting their own delectable bites to share with the platform.

Whether it's a gourmet twist on instant noodles or a cherished lunchtime BLT spot, Tiny Bites invites users to explore and celebrate the world of snacks and tiny delights. With a focus on user-friendly design, the platform aims to provide a seamless experience for posting recipes and sharing ratings. It's not just about food; it's about sharing thoughts, emotions, and experiences surrounding everyone's ultimate passion: food.

 ## User Needs

- **Cross-Device Accessibility**: Users expect seamless access to the website from any device, whether it's a smartphone, laptop, tablet, or desktop. 
- **Responsive Design**: A responsive design is crucial to ensure that the website adapts and delivers an optimal viewing experience across all screen sizes, ensuring readability and usability. 
- **Easy Posting**: Users should be able to effortlessly share their culinary creations with clear, intuitive posting guidelines. - **Efficient Account Creation**: A quick and hassle-free account creation process is essential to encourage user participation. 
- **Visual Appeal**: Users want to showcase their culinary creations through captivating images that highlight the aesthetic appeal of their bites. 
- **User-centric Navigation**: Users need to easily navigate through their own posts, find specific recipes, and manage their comments and posts effectively.

## Planning 

Before embarking on the development journey, meticulous planning was undertaken to conceptualize the layout, define essential fields, and establish the Database Schema

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
    - If the user is logged in the navbar will display their username which act as a link to the **Profile**.

![Navbar Small Screen](docs/navbar_small_screen.png)

![Navbar Big Screen](docs/navbar_big_screen.png)

- Because most of the nav items are for a user who is logged in, I decided it was best to hide all nav links for a none login user as they would have little need for any of the functionality provided.
- I did leave the account login and sign up links active.

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

- I designed the recipe card with the idea of a scroller in mind, similar to those on social media platforms like Facebook or Instagram. It's good to give a little preview, something to pique the reader's interest.
- Each card, at first glance, features an image of the post, the dish's name, the author's username, and the creation date/time.

![Card Top](docs/card_top.png)

- Recognizing that sometimes a post might catch your eye but not immediately draw you in with just the information above, I added the description button. This button reveals a little box on the card with the description the user set for the recipe, along with another button that leads to the post's detailed page. This creates a sort of step-by-step journey for the user, rather than overwhelming them with all the information at once or making them hunt for it at the end.
- I believe this styling would help users avoid getting bogged down with recipes they might not even like. The summary style of the cards allows users to get in and out without having to leave their current page.

![Card Bottom](docs/card_bottom.png)

##### Pagination 

- As I mentioned above I added some pagination so I could break up the number of post displayed on the feed at one time. 
- I used the arrow icon to show case the buttons for next and previous page I thought it was a more user friendly approach so as not to disculed any users that might not be very good at reading or understanding the fucntion. 
- I added the page number to this too. I am not sure on what exact role it would play but as a user of the website myself through testing and building I found it much easier when I knew the page I was on and how many there was in total.
- It just seemed like a fitting feature to the page and gave the layout a more legit look and feel.

![Pagination](docs/pagination.png)

#### Post Detail

##### Recipe Card

- I decided to keep all the information in one card just like I have done the home page keeping with the thought of not having the user poking and search around for the content. 
- The card is titled with the name of the dish and just under that we have by 'username' | the date of creation. I think it give off a artical feel with this layout which I believe is another feature to draw in readers. The information is neat and tidy.
- The section below is where the important info is held is we have the the description then the ingredients and final the step or instructions. 
- They also share a row with the image allow users to quick check what their dish should looking like without having to stray too far from the information of the recipe.

##### Comment Sections

- Again to make the page less bulky and intimadating I have made the secoing section a smal and comfortable place. 
- This section is broke into two the comments posted and the comment creation form. 

![Comment Section](dco/images)

###### Comments Post.

- Here you will see all the comments the comment that have been posted by other users so far. 
- I felt the rounded corners and buddly effect would be more user friendly and make givve the comments that social media feel. 
- each comment is held within a card and that card contains:
  - Username
  - Comment Body
  - Date of Creation

![Comment Card](docs/images)

- Now the card are configured to only display to user if they approved. 
- this approval process will be discussed in detail when we get to the 'to be approved' page. However, only the post own and the author of the comment can see un-approved comments. they are similar to standard comment but I added some style to make to faint and display a message to let the user know the comment is awaiting to be approved. 

![waiting for approval](docs/images)

- If a user is logged in and they have commented on a post they have to chance to edit or delete their comments using the two edit and delete buttons placed on each card I thought it best to allow this funtion even when awaiting approval because we all make mistakes. So at any time user has a chance to correct or eject themselve from the comments.

![edit/delete buttons](docs/images)

- I made the section scrollable as I felt it made it neater but also hide an old comments from instant sight so as not to ruin the page with comments. It is import the recipe is the main focus of the page.

![comment scroll](docs/images)

###### Comments Creation.

- This sections is only avaible when a user is logged in. 
- I treid to make the creation buddle as close to the comment cards as I could. Just so users understood the purpose of it but also to fit with the theme of the section. 
- In saying that it is a very basic setup just a feild to type and a button to submit. 

![comment creation](docs/images)

- However the section is setup to be stretched so if the user needed addtional space for their comments then they can just grab the corner of the text area and pull. 

![streched comment creation](docs/images)

### My Bites

##### Card Layout

- The card layout provides a visually appealing presentation of each user's post, with clear separation between different pieces of information such as the dish name, description, author, and creation date.
- It is a bit smilar to the home page but the cards are two a row and they are brighter. Because these are the users ricpes I felt the idea of comfortable ricpe surfing wasnt need they know what they want here.
- By prominently displaying the featured image of each post, users can quickly identify their dishes and visually assess their appeal. The use of a container ensures that images maintain their aspect ratio, maintaining consistency across different posts.
- The card layout adapts seamlessly to different screen sizes, ensuring a consistent user experience across devices, whether users are browsing on a desktop or a mobile device.


##### Pagination

- Just like the home page clear Indication with the pagination section. Clearly indicating the current page number and the total number of pages, providing users with context and helping them understand their position within their post collection.
- The use of arrow icons for navigating to the previous and next pages enhances the intuitive nature of the pagination controls, making it easy for users to understand how to move between pages.
- When users have not yet created any posts, an informative alert informs them of this fact, reducing confusion and providing clear guidance on the next steps they can take.
- Even when users have no posts to display, the alert message is designed to encourage them to start sharing their culinary creations, fostering engagement and participation within the community.
- The watermark overlay just makes the page looks more empty to encourage users to fill it up.

### To Be Approved

- In the "To Be Approved" section, we provide users with a streamlined interface for managing comments awaiting approval on their posts. Allow the user to to control what is seen on their post.

##### Card Layout

- Each comment awaiting approval is presented within a card layout, providing a clear and structured view of essential information such as the comment content, associated post, author, and creation date.
- The use of different text styles and colors helps establish the sepperation of information, with prominent highlighting of key details such as the post name and author's username, enhancing readability and user comprehension.

##### Action Buttons

- For each pending comment, user are provided with action buttons to either approve or delete the comment directly from the interface, streamlining the moderation process and reducing the need for navigating to separate pages.

##### Modal Confirmation 

- To prevent accidental actions, modal dialogs are there for both the approval and deletion actions, requiring administrators to confirm their decision before proceeding. This helps prevent unintentional data loss and ensures accountability in the moderation process.

- When there are no comments awaiting approval, an informative alert message is displayed, informing administrators that no further action is required. This helps reduce ambiguity and provides clear feedback on the current state of the moderation queue.


###  Create Bite Form

- In the "Create Bite" form section, users are provided with a user-friendly interface for submitting their culinary creations to the community. Here's a breakdown of the design elements and considerations:

#### Card Layout

- The form is presented within a card layout, providing a structured and visually appealing container for the form elements. The use of shadows adds depth to the card, enhancing its prominence on the page.
- The card header is styled with a primary background color and white text, creating a visually striking header that clearly indicates the purpose of the form ("Create Bite").
- To further distinguish the form from surrounding content, a "form-bubble" container is added, creating a visually distinct area for the form elements. This helps focus the user's attention on the form and enhances its visual prominence.
- The Django Crispy Forms library is utilized to render the form fields in a clean and structured manner, improving readability and user experience. Crispy Forms automatically handles field rendering, error display, and layout configuration, streamlining the form creation process.
- The submit button is prominently displayed at the bottom of the form, with a primary color to indicate its importance. This encourages users to complete the form and submit their posts, facilitating user engagement and participation within the community.


### Profile

#### Page Layout
- The profile pages purpose is to give the user the abilty to edit their own information. 
  - First and Last Name
  - Email
  - Password.
- The page is built as a form that hold to current values for the logged in user, to edit name and email you just type the new value in and save. 
- The input for password on the profile page is just for design and is disabled.

![Profile Form](docs/images)

#### Password Modal
- The password change is done by using a modal holding a form. This modal is actived by clicking the change password link. 
- The modal  contains:
  - Currrent Password
  - New Password
  - Confirm Password.
- Using javascript I made some logic to make the change password process less prone to error
  - Using calculatePasswordStrength() I check the password strenght based on predefined rules. If the password meet one the rule it adds 1 to the strenght variable. This reflects in the strenght message that shows under the password field. 
    - <span style="color:red">Weak</span> is 0-1
    - <span style="color:yellow">Moderate</span> is 2-3
    - <span style="color:green">Strong</span> is 4 and higher
  - Using validatePasswordsMatch() to check if new password and password confirm match. Untill they match the submit button is hidden. Also, show a passwordMismatchMessage, 'New password and confirmation do not match.'.
- I used a lot of the color red in this modal to let the user know this is a major change and they must think carefully before procceding. This applies to the 'Change Password' link and the modal title. 

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
      - index.html
      - assets folder
        - css folder
          - style.css
        - icon folder
        - js folder
          - script.js
        - images
      - Docs
        - images
    - I used the git add . command to add all changes above.
    - Using the git commit command I committed the change and used -m to attach a message to the commit.
    - When I was finished with the creation I used git push to push all these files and folders to GitHub.
    - I used these same 3 commands through the creation and modification

This section should describe the process I went through to deploy the project to a hosting platform.

- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - <https://jamcevoy.github.io/RPSLS/>

## Credits

- I used these resources to research and develop my understanding of JavaScript, as well as get inspiration for my own code. During this research, I have borrowed some ideas and modified the code to suit my project. No code was used unedited

### Design

- All the design screenshots from above came from [Wirframe](https://wireframe.cc/)

### Code


### Content

