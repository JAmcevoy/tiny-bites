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

#### User Stories 

- I came up with the following user stories, I am going to use these stories to put myself in the position of the user and allow but to keep UI in mind at all stages during development. 
- Also, they will allow me to use an Agile Devlopment, Agile promotes iterative development, where features are delivered incrementally in short cycles called sprints. This allows for regular feedback from stakeholders and users, leading to quicker adjustments and improvements. With this in mind I tackled one issue at a time and took time after each session to reflect and compare to other social media sites along with research.

```
Feed In Admin
Ability to create users
Display my feed
View Scroll list of posts
Open a post
View A Comment
Comment on a post
Pagination on List view like index and My Bites
To be Approved page
Approve Comments
Edit Post
Navbar Show Actice
Edit Comments
Delete Comments
Search Bar
Pagination - page number
Profile Setting
Delete post
```

## Planning

Before embarking on the development journey, meticulous planning was undertaken to conceptualize the layout, define essential fields, and establish the Database Schema.

### Planned Design

- Because there was some many pages within this project I didnt find a need to map out each page instead once I established the theme of the page with the index/home I would fit the other pages around this.
- In the following parraghraphs I want to show you the index and how it contributed to the my bites and to be approved page

#### Large Screen Layout

- The large screen layout provides ample space for users to navigate comfortably, with distinct sections for easy access to various features and functionalities.

![Large Screen Layout](docs/images/large-wir.JPG)


#### Small Screen Layout

- The small screen layout prioritizes readability and usability, with optimized design elements to enhance the mobile browsing experience.

![Small Screen Layout](docs/images/small-wir.JPG)

- For the smaller screen I am planning to hide all the nav items in a menu activated by a burger icon.

![Small Screen Nav](docs/images/navmenu-small.JPG)

- As mention at the start of the sections I wanted to get the index page down first, The reason being is through to the process of trying to create a view I thought would fit this purpose I createda few mock ups in which I will use to create my_bites and to be approved.
- My first idea for the index was to make it minial as possible more compact. I did think that page deserved a little more effort and it difinately would bring more apeal. However, the to be approved section is best suited to be compact and shouldnt use much imformation in fact it would take away from the purpose of the page if I added any more. I just needed to add some aprrove abnd delete buttons
  ![To be Approved](docs/images/to-be-approved-wir.JPG)
- The my bites if felt held a similar purposes so I propoed a similar style but I wanted to make a backup design, so I could mock up both stlye and see if it is best to set that page apart or keep it similar.

##### Choice  1 :
![Choice 1](docs/images/my_bites_choice_1-wir.JPG)

##### Choice 2 : 
![Choice 2](docs/images/my_bites_choice_2-wir.JPG)

- I don't want to get stuck on the planning to long so I decided to try both in the bulid stage and see which one suits better, maybe get a second option on it.

### Database Schema

- Here is the database schema I created. I later took the review sections out so below you will need the old and new schema.

![Orignal Design](docs/images/database-schema.JPG)

![After Removal of Review](docs/images/update-schema.JPG)



#### Fonts

- Through google searchs I tried to find different font to fit differnt place instead of having them all under one.
  - Anton
  - Figtree
  - Raleway 
##### Anton
- **Usage**: Best suited for headings and titles.
- **Description**: Anton is a bold, attention-grabbing typeface with high contrast and distinct characters. It is characterized by its thick strokes and narrow spacing, making it perfect for headlines and emphasis.
- **Why it's good for headings (body)**: With its bold and impactful appearance, Anton commands attention and ensures that headings stand out prominently on the page. It adds a sense of authority and modernity to the text, making it ideal for grabbing the reader's attention at a glance.

##### Raleway
- **Usage**: Suitable for body text and paragraphs.
- **Description**: Raleway is a versatile sans-serif font known for its clean lines and geometric shapes. It offers a modern and sophisticated look while maintaining excellent readability across different screen sizes and resolutions.
- **Why it's good for paragraphs (p)**: Raleway's simplicity and clarity make it an excellent choice for body text and paragraphs. Its clean design ensures that text remains legible even when presented in large blocks, enhancing the readability of the content and providing a pleasant reading experience for users.

##### Figtree
- **Usage**: Ideal for buttons.
- **Description**: Figtree is a distinctive font with a unique style, characterized by its elegant curves and playful appearance. It brings a touch of creativity and sophistication to any design, making it particularly well-suited for adding visual interest to buttons and other interactive elements.
- **Why it's good for buttons**: Figtree's stylish and artistic design makes it a perfect choice for buttons. Its eye-catching aesthetic draws attention and encourages user interaction, enhancing the overall appeal and usability of the interface.

 


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
- This page is not paginated, I felt because it was a search it would be best for users to just have all their search results on the one page without splitting it out into multiple. I believe this has 2 benefits. 
  - This will encourage to the user to better define their search to find exactly what they want. 
  - For the more indecive people it will give them a larger section to run through opening up their own ideas like if I was to search chicken I would find all the chicken dishes in one place and a list in full so not so much time is wasted on reloading the next page.

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

#### My Bites

##### Card Layout

- The card layout provides a visually appealing presentation of each user's post, with clear separation between different pieces of information.
- Two cards are displayed per row, and they are brighter than those on the home page.
- The featured image is prominently displayed, maintaining aspect ratio consistency.
- The layout adapts seamlessly to different screen sizes.

###### View button

- I thought the view button was cruital as it give the my bites page a dictoionary like feel to it. You find when you need quickly and have the option to bring you to the details.

###### Edit button

- The my bites page acts as almost an admin center for the users. 
- The edit buttons functions allows the user to update any of their existing posts.

###### Delete button
- I have also added the delete function for posts to this page. This allows the user to manage all aspects of their post from the one place. 
- I made the delete button to a 'x' symbol in the corner of the card. I believe this to be a more understandable button for users. 
- When the button is selected it bring up a modal to ensure the user are aware of their current actions and preventing accident deletation.


##### Pagination

- Clear indication of the current page number and total pages helps users understand their position.
- Arrow icons enhance intuitive navigation.
- Informative alerts guide users when no posts are available, encouraging participation.

#### To Be Approved

- A streamlined interface for managing comments awaiting approval on user posts.

##### Card Layout

- Comments awaiting approval are presented within a card layout for clear and structured information.

##### Action Buttons

- Action buttons for approving or deleting comments directly from the interface streamline the moderation process.

##### Modal Confirmation

- Modal dialogs for both approval and deletion actions prevent accidental actions and ensure accountability.

#### Create Bite Form

#### Carousel Form Navigation
- The form is divided into multiple slides using Bootstrap's carousel feature. This design choice was made to prevent users from feeling overwhelmed by a lengthy form. By breaking the form into manageable sections, users can focus on one task at a time, reducing cognitive load and improving the overall user experience.
- Ensuring that the form is fully responsive was a key consideration. The carousel controls adjust based on the screen size:
  - **Mobile Views**: For smaller screens, internal buttons are provided within each slide to navigate between sections, making it easy to use on touch devices.
  - **Larger Screens**: For desktop and larger screens, external controls are positioned outside the form to provide a clean and uncluttered interface. These controls are strategically placed to enhance usability without obstructing the form content.

#### Form Sections
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

#### Profile

#### Page Layout

- The profile page allows users to edit their information, including first and last name, email, and password.
- The input for the password on the profile page is for design and is disabled.

![Profile Form](docs/images)

#### Password Modal

- The password change is done via a modal containing a form.
- JavaScript logic ensures a smooth process with password strength checks and validation.

#### Account Pages

#### Login

- I wanted the login page to be a simple process so I went for a plain view with the username and password fields.
- The login is a sepperate page so with use of the login_view I was able to allow the page to redirct to previous page when relavant. For example, the detail view has its own login button for the comments. Before after a successful a user would be redircted to home based of the configurations in the setting.py file, I believe this to be fustrating for the user as they would need to go back and find the post they wished to comment on. With the next method the login link grabs the slug of the post then after login the user will be brought back to the post.

![Login](docs/images/)

#### Logout

- Just as the login I wanted the logout to be simple and easy to do. 
- The logout is handled by a modal on the base. When the users wants to logout no matter the page the modal will pop up and it is just a simple click of a button. 
- Because the user is logging out I found no need to redirct them to the previous page, as most of the pages (my bites, to be approved, create, and profile) require the user to be logged in I thought it would prevent any confusion or error for the user by bringing them back to home.

![Logout](docs/images/)

#### Sign up

- The sign up is again a simple process the form consist of Username, email, and password. 
- I thought not to add in the first and last name fields to speed the sign up process, only including the information not needed. The first name and last name can be added to the users profile after sign up using the profile page.
- This form is close to the django allauth form so most of the error handling is there to be used preventing the user to submit if:
  - Username is taken
  - The emails is not the correct format
  - Password and current password match. 
- Because of all these actions I though it would be best to focus any custom error handling like password strenght to the profile page.
- Just in case the sign up link was select by addicdent I add the login link at the bottom with a text where the user can notice it.

![signup](docs/images/)

#### Forgot password

- I spent the least amount of time of this page, Again this is django aullauths template. I just added some bootstrap style to the page to fit in with the the base and the rest of the site.

![forgot password](docs/images/)

### Features Left to Implement

- As stated in the beginging I wanted this site to be both a recipe and review website however, I had some difficulties added the review section. I felt my time was being wasted trying to get this section in, I felt my website had a clear enough function by this time. The review section was similar to the create but allowed the users to review with a star option making the user more interactive with the theme of Little bites. I feel with more time and experience I feel I could accomplish this.
- I wanted to add in socail media logins, allowing the users to connect their other socail profile but again my current knowledge and time frame I felt I couldnt get this done to an acceptable level.
- I wanted to incorporate Tailwind CSS styles into my project to separate it from other projects, but as this was new to me, I felt the time would have been wasted focusing so much on style. Additionally, I found the verbosity of HTML classes in Tailwind CSS to be less visually appealing or harder to read compared to Bootstrap's more structured HTML markup. This made the learning curve steeper and the transition more challenging.

## Testing

### Logic testing

- Because the majority of this projects time was spent on the python I found it necessacary to test the Django view and forms. Using djangos test functionality I ran a number of test.
- After I setup each test I ran the tests using python3 manage.py test.
- There is a total of 36 tests

#### Proformance

##### SecurityTest
- **setUp**
  - Sets up the client and the URL for the home page.
- **test_csrf**
  - Tests the Cross-Site Request Forgery (CSRF) protection.
  - Verifies that the CSRF token is present in the response.

##### PerformanceTest
- **setUp**
  - Sets up the client and the URL for the home page.
- **test_query_count**
  - Tests the performance by checking the number of queries.
  - Verifies that only one query is executed when accessing the home page.

#### Forms

##### CommentFormTest
- **test_comment_form_fields**
  - Checks if the `CommentForm` contains the 'body' field.
  - Verifies that the label for the 'body' field is 'Comment'.
- **test_comment_form_valid_data**
  - Tests the `CommentForm` with valid data.
  - Verifies that the form is valid when provided with valid data.
- **test_comment_form_invalid_data**
  - Tests the `CommentForm` with invalid data.
  - Verifies that the form is invalid when provided with empty 'body' data.

##### PostFormCreateTest
- **test_post_form_create_fields**
  - Checks if the `PostFormCreate` contains all expected fields.
- **test_post_form_create_widgets**
  - Checks if the widgets for certain fields in `PostFormCreate` are instances of `SummernoteWidget`.
- **test_post_form_create_valid_data**
  - Tests the `PostFormCreate` with valid data.
  - Verifies that the form is valid when provided with valid data.
- **test_post_form_create_invalid_data**
  - Tests the `PostFormCreate` with invalid data.
  - Verifies that the form is invalid when provided with empty data for all fields.

#### Views

##### PostListViewTest
- **setUp**
  - Sets up the client and the URL for the home page.
- **test_post_list_view**
  - Tests the behavior of the post list view.
  - Verifies that the response status code is 200 (OK).
  - Verifies that the correct template is used for rendering.

##### SearchFeatureViewTest
- **setUp**
  - Sets up the client, URL for the search feature, and creates test data.
- **test_search_feature_post**
  - Tests the behavior of the search feature when using the POST method.
  - Verifies various aspects of the response.
- **test_search_feature_get**
  - Tests the behavior of the search feature when using the GET method.
  - Verifies various aspects of the response.

##### PostDetailViewTest
- **setUp**
  - Sets up the client, user, post data, and URL for the post detail view.
- **test_post_detail_view**
  - Tests the behavior of the post detail view.
  - Verifies various aspects of the response.
- **test_post_detail_view_post_comment**
  - Tests the behavior of the post detail view when posting a comment.
  - Verifies various aspects of the response.

##### PostCreationViewTest
- **setUp**
  - Sets up the client, URL for the post creation view, and creates a test user.
- **test_post_creation_view_get**
  - Tests the behavior of the post creation view when accessing via GET request.
  - Verifies various aspects of the response.
- **test_post_creation_view_post**
  - Tests the behavior of the post creation view when submitting a POST request.
  - Verifies various aspects of the response.

##### EditPostViewTest
- **setUp**
  - Sets up the client, creates a test user and a post, and defines the URL for editing the post.
- **test_edit_post_view_get**
  - Tests the behavior of the edit post view when accessing via GET request.
  - Verifies various aspects of the response.
- **test_edit_post_view_post**
  - Tests the behavior of the edit post view when submitting a POST request.
  - Verifies various aspects of the response.

##### DeletePostsTest
- **setUp**
  - Set up the client, create a test user, and a test post.
- **test_delete_posts**
  - Tests the delete_posts function.
  - Verifies that a post is deleted successfully.

##### MyBitesViewTest
- **setUp**
  - Sets up the client, creates a test user, a test post, and defines the URL for accessing user's saved posts.
- **test_my_bites_view_authenticated**
  - Tests the behavior of the my bites view when the user is authenticated.
  - Verifies various aspects of the response.
- **test_my_bites_view_unauthenticated**
  - Tests the behavior of the my bites view when the user is unauthenticated.
  - Verifies various aspects of the response.

##### ToBeApprovedViewTest
- **setUp**
  - Sets up the client, creates a test user, a test post, and a pending comment.
- **test_to_be_approved_view_authenticated**
  - Tests the behavior of the to-be-approved view when the user is authenticated.
  - Verifies various aspects of the response.
- **test_to_be_approved_view_unauthenticated**
  - Tests the behavior of the to-be-approved view when the user is unauthenticated.
  - Verifies various aspects of the response.

##### ApproveCommentViewTest
- **setUp**
  - Sets up the client, creates a test user, a test post, and a pending comment.
- **test_approve_comment_view**
  - Tests the behavior of the approve comment view.
  - Verifies various aspects of the response.

##### DeleteCommentViewTest
- **setUp**
  - Sets up the client, creates a test user, a test post, and a comment to delete.
- **test_delete_comment_view_get**
  - Tests the behavior of the delete comment view for GET request.
  - Verifies various aspects of the response.

##### EditCommentViewTest
- **setUp**
  - Sets up the client, creates a test user, a test post, and a comment to edit.
- **test_edit_comment_view_get**
  - Tests the behavior of the edit comment view for GET request.
  - Verifies various aspects of the response.
- **test_edit_comment_view_post**
  - Tests the behavior of the edit comment view for POST request with valid data.
  - Verifies various aspects of the response.
- **test_edit_comment_view_post_invalid**
  - Tests the behavior of the edit comment view for POST request with invalid data.
  - Verifies various aspects of the response.

##### LoginViewTestCase
- **test_login_view**
  - Test whether the login view returns the login page.
- **test_login_unsuccessful**
  - Test login with incorrect credentials.
- **test_login_next_url**
  - Test login with redirection to a next URL.

##### ProfileViewTest
- **setUp**
  - Set up the client and URL for profile view.
- **test_profile_view_authenticated**
  - Test profile view for authenticated user.
- **test_profile_view_unauthenticated**
  - Test profile view for unauthenticated user.
- **test_profile_view_post**
  - Test profile view for POST request.

##### CustomPasswordChangeViewTest
- **setUp**
  - Set up the test environment.
- **test_password_change_view_post_valid**
  - Test password change with valid input.
- **test_password_change_view_post_invalid_old_password**
  - Test password change with invalid old password.




### User testing

- The user testing was also important as my users needs was that the website was easy to understand. I felt human error would be a big factor in issues with this project. 
- To allow for user testing I will encourage user to:
  - Sign up using the sign up page. 
  - Login using the login page. 
  - Edit information from the profile page.
  - Browser through the feed while also making use of the search bar. 
  - Comment on a users post while making sure they are aware they can edit and delete said comments
  - Review the my bites page and post edit page.
  - Delete or approve comments I have made on their post using the to be approved page.
  - Logout using the logout modal
- I will ask the test users to answer these questions to review the website:
  1. **How easy was it to sign up for an account on the website?**
  2. **Did you encounter any difficulties while logging in?**
  3. **Were you able to easily edit your information from the profile page?**
  4. **How intuitive was it to browse through the feed and utilize the search bar?**
  5. **Were you able to comment on a user's post and understand how to edit or delete your comments?**
  6. **What are your thoughts on the "My Bites" page and post edit page in terms of usability?**
  7. **Did you find it straightforward to delete or approve comments made on your posts?**
  8. **What was your experience with logging out of the website using the logout modal?**
  9. **Overall, how would you rate the ease of use and intuitiveness of the website?**
  10. **Is there any specific feedback or suggestions you have for improving the website's usability?**


#### User 1
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
#### User 2
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
#### User 3
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
#### User 4
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.


### Validator Testing

##### HTML Validator

- I used [W3C HTML](https://validator.w3.org/) to validate my app to bypass the ginja errors that might come with it I used the URL to validate the HTML

![HTML Validation](docs/images/html_val.JPG)

##### CSS Validator

- I didnt have any worries with the css so I was able to just copy and paste the file into [W3C CSS](https://jigsaw.w3.org/css-validator/)

![CSS Validation](docs/images/css_val.JPG)


## Bugs

### Bugs I Faced Along The Way

- When there was a user with no post yet and they try to log out the modal is not accessible but the user due to the over-lay sittng on the page. This was a bit of an oversite when I was creating this. To fix this bug I removed the following styles.
    ``` 
    /* .full-page-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 9999;
      margin: 70px 0;
    } */

    /* .water-text::before {
      content: attr(data-text);
      position: absolute;
      top: -2px;
      left: -2px;
      color: rgba(0, 0, 0, 0.1);
    } */
    ```
- When a user adds a post with a substanal amount of text it makes the post card longers which is fine however this has an effect on the image. I believe this is because the image is size.
- My first style idea for the creation form was a lot simpler but I found it necessary for the users to have the summer note field for formating thier posts. However, this caused a lot of issues with the card that held the form on smallers screens. The fields went over the bound of the card and it just looked a mess. I tried to reszie the fields but that was proving difficult so I decided to reimagine the form page with I belive is a lot more interactive. 
- The password change was suppose to be part of the profile page but the issue was the password would update anytime the profile was updated even if you did not wish to change it. Also, it didnt ask for current password to confirm the user was aware of the change so it definely casued some security concerns. I decided a modal was a better idea as I still wanted the password change to be on the same page.
- All the current data was brought into the system using a json file so all the post formats were incorrect and the were missing images. 
  - I thought a default image was the best way to approach the image issue, by setting a default image I could see how each  post card looked with a image witout having to go through each one by one but it also made the pressure of uploading a image with your post a little less as there would but something visiually pleasing at least.
    - The default image I picked was
    ![Defualt Image](docs/images/default_2.jpg)
  - I had have such an easy choice with the text so I decided I put aside some time to go through this but when I update the text it appeared to put it through as HTML with tags like <p> and <h3> I belive this was due to using the summernote. As I mentioned already I thought this was an important part of the create process so I couldnt just change it. After some research I found summernote, like many other rich text editors, automatically converts input into HTML format to preserve formatting such as bold, italics, headers, and paragraphs. Using | safe, it tells the system to treat the text as safe HTML, preventing it from escaping HTML characters and rendering them as text. This approach ensures that the HTML tags are interpreted correctly and displayed as intended, rather than as plain text.
  - The process of login redirection became a significant focus of my attention. Initially, the login functionality would consistently redirect users to the home page upon successful login, which wasn't problematic. However, a significant issue arose when users attempted to log in to post a comment on a specific post—they were redirected to the home page instead of returning to the post they were engaging with. This discrepancy posed a considerable inconvenience, as hours of research or interaction could be undone by a simple login. To address this, I implemented the "next" method, which appends the current page's URL to the login link. This ensures that users are redirected back to their original page after logging in.
  ```
  {% url 'account_login' %}?next={{ request.path }}
  ```
  - However, this solution unearthed another issue: if a user mistyped their password and the login page refreshed, the "next" URL would be lost. To mitigate this problem, I adjusted the login page's return statement to include a dictionary containing the "next" URL as context. This approach ensured that even if the login attempt failed, the "next" URL would persist, allowing users to be redirected back to their intended page upon successful login.
  ```
  return render(request, "account/login.html", {'next': next_url})
  ```

### Bugs I did not get to fix

- The images only certain images for posts work with the post detail and the post list view if the photo is too big its is hidden or makes the card appear bigger, I fear this will cause issue for the users as most users not not have the abilty to reize their images. I feel like this is an easily solved issue however I didnt notice this till late in the project and I had not enough time investigate and correct this.
- When the image is too big it mishapes the image circle on the post detail card.
- The password reset section is incomplete, Everytime I try email from the page it throws a error. Unfortunately, I dont have the knowledge to fufill this function before my projects dead line. So for testing purposes I will removed the forgot password fucntion.
- I couldnt quite get the time or focus to apply the socials authentication, I really wanted to add this hence the enteries in the setting.py file however they were only added back in to prevent an error I know it is not a bug but I thought it was worth mention.


## Deployment

This section describes how to create a new repository.

- This repository was created using [GitHub](https://github.com/) The steps are as followed:
  - I went to the [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template)
  - I selected the green button labeled 'Use this template'
  - Then, Create a new repository.
  - Then I was brought to a new page to set the name and setting for my new repository.
  - I named my repository 'tiny-bites'

This section describes how I set up my workspace, Once my repository has been created.

- The workspace I used for this project was [codeanywhere](https://app.codeanywhere.com/). The steps are as follows:
  - I opened [GitHub](https://github.com/) and went to the 'tiny_bites' repository
  - To get the link for codeanywhere I clicked the green button '<>code'.
  - Here under local, I could copy the link needed: <https://github.com/JAmcevoy/tiny_bites.git>
  - Then I went to code anywhere.
  - In workplaces, I selected new workspaces
  - Here I copied the link from the git hub and clicked to create to make my workspace.

  - The type of project was django so I had a different file creatation process that usual.
    ##### Create the project
    - First I type the following command in the terminal to install the Django Python package: pip3 install Django~=4.2.1
    - Once the package is installed, I add it to the requirements.txt file with the following command: pip3 freeze --local > requirements.txt
    - Then I Return to the terminal. In the terminal, create a Django project called tiny-bites in the current directory. django-admin startproject tiny-bites .
    - Click on Open Browser.
    - **DisallowedHost at /Invalid HTTP_HOST header: '8000-jamcevoy-tiny-bites-jdbmznt5m7.us1.codeanyapp.com'. You may need to add '8000-jamcevoy-tiny-bites-jdbmznt5m7.us1.codeanyapp.com' to ALLOWED_HOSTS.**. This means Django doesn't recognise the hostname - the server name your project is running on.
    - I selected and copied the hostname after "Invalid HTTP_HOST header:". In this case, that is '8000-jamcevoy-tiny-bites-jdbmznt5m7.us1.codeanyapp.com'.
    - In the my_project/settings.py file, I pasted the hostname between the square brackets of ALLOWED_HOSTS and save. For the above case, this looked like: ALLOWED_HOSTS = ['8000-nielmc-django-project0kylrta3cs.us2.codeanyapp.com']. 
    
    ##### Create the App
    - Now I have a Django project created, I  need to make an app. To do this, I use the manage.py file. In the terminal, type: python3 manage.py startapp feed. 


This section describes the commands I used in code anywhere to push my code and changes to GitHub.

    - I used the git add . command to add all changes once the project and app was created.
    - Using the git commit command I committed the change and used -m to attach a message to the commit.
    - When I was finished with the creation I used git push to push all these files and folders to GitHub.
    - I used these same 3 commands through the creation and modification

This section should describe the process I went through to deploy the project to a hosting platform.

Create the Heroku app:
- I went to https://dashboard.heroku.com/apps to create my new app. Once I got to this page I selected new > Create new app.
- I had to give the app a name so I decided to name it after the repository 'tiny-bites'
- I picked the closest region to me, in this case 'Europe'
- Then I hit create app to confirm the creation of my app.

Preparing the code for deployment:
- I had to use pip3 install gunicorn~=20.1 to install gunicorn then used pip3 freeze --local > requirements.txt to added it to the requirements.txt.
- I need to create a procfile (Note: Conventionally, the Procfile is spelled with an uppercase "P" to adhere to a widely accepted naming convention.)
- The contents of the Profile should be as follows 'web: gunicorn tiny-bites.wsgi'
- Because I am deployment to Heroku I need to allow the domain in the allowed host section of the settings.py. Like so .. ALLOWED_HOSTS = ['8000-jamcevoy-tiny-bites-jdbmznt5m7.us1.codeanyapp.com', '.herokuapp.com']
- I had to make sure the Debug was set the False as it is recommended not to push your project to deployment with this True. When DEBUG is set to True, Django will display detailed error pages with sensitive information about your application, including stack traces and environment variables. This information can be useful for debugging during development but poses a security risk if exposed in a production environment.
- Lastly I git add, commt -m, and pushed my code to github.

Deploying in Heroku: 
- Once my code was pushed to github then I need to deploy it from my tiny-bites app.
Firstly, I need to add all of the varables of the env.py file to the Config Vars. I opened my app then navigated to the setting tab and then the 'Config Vars' section. Here I added the following: 
  - CLOUDINARY_URL
  - DATABASE_URL
  - DISABLE_COLLECTSTATIC ( Set to the value of '1')
  - SECRET_KEY
- Finally once these vars were configured I need to connect my github to heroku. I done this from the 'Deploy' tab within in heroku app.
- In the deployment method section I selected Github. Once signed in I used the search bar to locate my repository and connected my app.
- Last but not least, I manually deployed the app using 'Manual deploy' so I could see a log of the ddeployment incase of any errors. I selected the main branch and then once I was sure I selected 'Deploy Branch' button to start the process.
- The process is as follows:
  - Receive code from GitHub
  - Build main efe7e624
  - Release phase
  - Deploy to Heroku, this is the final step and once done click view to see your result.

## Credits

- I used these resources to research and develop my understanding of the Django framework, as well as get inspiration for my own code. During this research, I have borrowed some ideas and modified the code to suit my project. No code was used unedited

### Design/Style

- I used the bootsrap 5.1.3 Documentation to research the inspiration of my design.
- All the design screenshots from above came from [Wirframe](https://wireframe.cc/)
- All images come from [Pexels](https://www.pexels.com/)
- The fonts were taking from [Google Fonts](https://fonts.google.com/)

### Code

- All my main code inspiration and ideas came from my reasearch into the Django Documentation [Django Documentation](https://docs.djangoproject.com/)
- The idea behind the Search bar was taken from [Make Use Of](https://www.makeuseof.com/add-search-functionality-to-django-apps/#:~:text=Create%20a%20View%20for%20the%20Search&text=%23%20Check%20if%20the%20request%20is%20a%20post%20request.&text=In%20request.,your%20search%20bar's%20input%20field.&text=Finally%2C%20the%20function%20renders%20a,and%20filtered%20model%20as%20context.)
- The if next functionality for redircting users back to a page after a login was part taken from this post [Django Forms](https://forum.djangoproject.com/t/redirecting-user-to-page-after-login/14603/10)


