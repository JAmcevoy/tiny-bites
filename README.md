# Tiny Bites

Tiny Bites is more than just a food website; it's a culinary community where users can unleash their creativity by crafting their own delectable bites to share with the platform.

Whether it's a gourmet twist on instant noodles or a cherished lunchtime BLT spot, Tiny Bites invites users to explore and celebrate the world of snacks and tiny delights. With a focus on user-friendly design, the platform aims to provide a seamless experience for posting recipes and sharing ratings. It's not just about food; it's about sharing thoughts, emotions, and experiences surrounding everyone's ultimate passion: food.

## User Needs

- As a user, I would want the website to be accessible from different devices (Phone, Laptop, PC, Tablet).
- As a user, I would like it to be responsive to all screens, ensuring the information is readable and understandable.
- As a user, I would want to easily be able to post my bites.
- As a user, I would need to be able to create an account quickly and easily.
- As a user, I would want to be able to post pictures of my bites.
- As a user, I would want to be able to see a collection of my posts.
- As a user, I would need to be able to edit or delete my comments and posts.

## Planning

Before I could start this project, I first needed to get the planned layout, the fields I required, and the Database Schema.

### Planned Design

#### Large Screen Layout

![Large Screen Layout](docs/large_screen_layout.png)

#### Types of Elements

![Types Layout](docs/types_layout.png)

#### Small Screen Layout

![Small Screen Layout](docs/small_screen_layout.png)

## Features

### Existing Features

#### Home Page / Index

##### Navbar

- The navbar was created with ease of access in mind using bootstrap. It provides a responsive navigation bar that displays all the website's different pages, with space to read and navigate clearly. On smaller screens, it neatly tucks together, hidden away until the burger icon is selected.
  - Contains:
    - Feed
    - My Bites
    - To be Approved
    - Create
    - Login, Sign up, and log out (Based on if you are logged in or not)

![Navbar Small Screen](docs/navbar_small_screen.png)

![Navbar Big Screen](docs/navbar_big_screen.png)

- Because most of the nav items are for a user who is logged in, I decided it was best to hide anything a user without an account wouldn't need.

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

#### My Bites

##### Card Layout

- The card layout provides a visually appealing presentation of each user's post, with clear separation between different pieces of information such as the dish name, description, author, and creation date.
- It is a bit smilar to the home page but the cards are two a row and they are brighter. Because these are the users ricpes I felt the idea of comfortable ricpe surfing wasnt need they know what they want here.
- By prominently displaying the featured image of each post, users can quickly identify their dishes and visually assess their appeal. The use of a container ensures that images maintain their aspect ratio, maintaining consistency across different posts.
- The card layout adapts seamlessly to different screen sizes, ensuring a consistent user experience across devices, whether users are browsing on a desktop or a mobile device.


## 2. Pagination

- Just like the home page clear Indication with the pagination section. Clearly indicating the current page number and the total number of pages, providing users with context and helping them understand their position within their post collection.
- The use of arrow icons for navigating to the previous and next pages enhances the intuitive nature of the pagination controls, making it easy for users to understand how to move between pages.
- When users have not yet created any posts, an informative alert informs them of this fact, reducing confusion and providing clear guidance on the next steps they can take.
- Even when users have no posts to display, the alert message is designed to encourage them to start sharing their culinary creations, fostering engagement and participation within the community.
- The watermark overlay just makes the page looks more empty to encourage users to fill it up.







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

