# Tiny Bites

Tiny Bites is more than just a food website; it's a culinary community where users can unleash their creativity by crafting their own delectable bites to share with the platform.

Whether it's a gourmet twist on instant noodles or a cherished lunchtime BLT spot, Tiny Bites invites users to explore and celebrate the world of snacks and tiny delights. With a focus on user-friendly design, the platform aims to provide a seamless experience for posting recipes and sharing ratings. It's not just about food; it's about sharing thoughts, emotions, and experiences surrounding everyone's ultimate passion: food.

# User Needs

- As a user, I would want the website to be accessible from different devices (Phone, Laptop, PC, Tablet).
- As a user, I would like it to be responsive to all screens, ensuring the information is readable and understandable.
- As a user, I would want to easily be able to post my bites.
- As a user, I would need to be able to create an account quickly and easily.
- As a user, I would want to be able to post pictures of my bites.
- As a user, I would want to be able to see a collection of my posts.
- As a user, I would need to be able to edit or delete my comments and posts.

# Planning

- Before I could start this project, I first needed to get the planned layout, the fields I required, and the Database Schema.

## Planned Design

### Large Screen Layout

![Large Screen](docs/)

### Types of Elements

![Types Layout](docs/)

### Small Screen Layout

![Small Screen](docs/images)

# Features

## Existing Features

### Navbar

- The navbar was created with ease of access in mind using bootstrap. It provides a responsive navigation bar that displays all the website's different pages, with space to read and navigate clearly. On smaller screens, it neatly tucks together, hidden away until the burger icon is selected.
  - Contains:
    - Feed
    - My Bites
    - To be Approved
    - Create
    - Login, Sign up, and log out (Based on if you are logged in or not)

![Navbar Small Screen](docs/images)

![Navbar Big Screen](docs/images)

### Feed

- The main point of the website is the feed; this is where the user will spend a lot of their time (assuming they are casual viewers; more specific users would enjoy the search bar below more). Because the target audience for this section is casual, there is quite a bit of white space to avoid crowding and intimidation for some users.
  
![Feed Big Screen]()

- Each recipe card is generously sized to give a feel of one at a time. This makes it more readable for the user and enables them to focus on each recipe individually to find what they are looking for or something they might want to try.
  
- Because of the list-type view on the page, I thought it would be good UI to add pagination. The pagination is set to 10; this number allows the user a few minutes of recipe surfing before they have to change the page, but not so little time that they have to change every few seconds.

![Feed Small Screen](docs/images)

### Search Bar

- The search bar is a necessary feature for this type of website, enabling users to find specific recipes based on their preferences. The search bar runs a query on the Create model by 'name', and it is set to contain so that even if a user has no idea how to spell a dish, as long as they are close enough, they will find it.

![Search Bar](docs/images)


### Recipe Cards

- I designed the recipe card with the idea of a scroller in mind, similar to those on social media platforms like Facebook or Instagram. It's good to give a little preview, something to pique the reader's interest.
- Each card, at first glance, features an image of the post, the dish's name, the author's username, and the creation date/time.

![Card Top]()

- Recognizing that sometimes a post might catch your eye but not immediately draw you in with just the information above, I added the description button. This button reveals a little box on the card with the description the user set for the recipe, along with another button that leads to the post's detailed page. This creates a sort of step-by-step journey for the user, rather than overwhelming them with all the information at once or making them hunt for it at the end.
- I believe this styling would help users avoid getting bogged down with recipes they might not even like. The summary style of the cards allows users to get in and out without having to leave their current page.

![Card bottom]()


### Pagination 

- As I mentioned above I added some pagination so I could break up the number of post displayed on the feed at one time. 
- I used the arrow icon to show case the buttons for next and previous page I thought it was a more user freindly approach so as not to disculed any users that might not be very good at reading or understanding the fucntion. 
- I added the page number to this too. I am not sure on what exact role it would play but as a user of the website myself through testing and building I found it much easier when I knew the page I was on and how many there was in total.
- It just seemed like a fitting feature to the page and gave the layout a more legit look and feel.

![Pagination]()




## Features Left to Implement


# Testing


### Choices test

#### Aim - To test that the computer is selecting different options and using each value of the user's options for one full game (up to 7 wins)

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

