# Development Diary
This is a *template* for your dev diary in PS2.
Feel free to edit as you see fit e.g., based on your progress updates, hurdles encountered and circumnvented.
Make sure to log one comprehensive update per student, per each week of our teaching term.
Please, get in touch with teaching staff for any questions around this or otherwise post on Microsoft Teams.

# Mandatory Student's contributions
Please, specify your individual contributions to the project **as a percentage**. 
Default is a *25% contribution for each student*. However, please modify as necessary, if that is not the case.

# Development Diary Activities
Please, report your key activities in each week this assignment is running.  

**Week 1**
* Student 1 (Alexander Stevensen)
    * Read chapter 1 & 2 on textbook
    * Setup VS Code, and Minecraft on my Linux distro
    * Implemented Hello Minecraft!
    * Implemented a basic function that generates a house that will face only one direction (at the moment)
    * Completed all the workshop preparation with some alterations made to the original code shown by Michael, such as instead of the stairwell being a solid stairwell it has been made to be a single step per y level
* Student 2 (Liam Whitaker)
    * Read chapter 1 & 2 on textbook
    * Setup VS Code, and Minecraft on Windows 11
    * Implemented Hello Minecraft!
    * Started work on house generation function
        - Randomised size
        - Randomised windows and door
        After some discussion, we decided to explore the idea of making a script that copies a premade house to a csv file, to then place randomly for our village. However, this ended up projecting to be a more difficult task than to build the house purely from code, since the house ddn't have to be incredibly detailed. Building it from code also allowed for very intricate randomisations to be made.
* Student 3 (Mohammed Usman E Ghani)
    * Read chapter 1 & 2 on textbook
    * Setup VS Code, and Minecraft on Mac OS
    * Implemented Hello Minecraft!
    * Implemented stairway to heaven
    * started discussion around randomisation of houses and roads
    * All programming studio activities completed
* Student 4 (Eray Cekic)
    * Read chapter 1 & 2 on textbook
    * Setup VS Code on Windows, as well as Minecraft Pi on Raspberry Pi OS (on Raspberry Pi 400)
    * Implemented Hello Minecraft!
    * Created a basic function of a common house with a roof, door, 4 walls and a base
    * Implemented stairway to heaven
    * Programming studio activities completed

**Week 2**

* Student 1 (Alexander Stevensen)
    * Implemented a randomised house placement system
    * Implemented a road path to surround the house, acting as a perimter
    * Attempting to curve road from current house to the previous house's path
    * Need to work on height variances, to maintain the natural terrain
    * Got road generation to work depending on the randomised house generation and connecting to the previous house (adjusting with rough curvature according to (y=mx+c))
      - Need to connect road path that is dependent on the previous house's door position to the curved road
      - Need to connec the curved road to the houses front door of the house that is currently being generated at run time
    * Connected the road path that is dependent on the previous house's door position to the curvy road
    * Connected the curved road to the houses front door of the house that is currently being generated at run time
    * Future Improvements
      - Could have implemented A* Path finding alg in place of the y=mx+c function for a more adaptable solution 
    * Bugs
      - Rare buffer error related to house gen and randInt()
    * Implemented the generate road function with main village.py file
* Student 2 (Liam Whitaker)
    * Randomisations have been made to the house's building materials
    * Pool placement within the specified house chunk has also been implemented.
        - Along the longer edge of the house, a pool will spawn with a fence surrounding its perimeter with a gate. It is created with a randomised size and is placed randomly.
* Student 3 (Mohammed Usman E Ghani)
    * Implemented furnitures to place inside houses
    * Attempted to build a stiarway connecting ground floor to a room
    * Implemented natual air filters around the house to make the village more nature friendly.
    * Need to work on randomising the size of the furniture
       - Implement a book case under the staircase
       - Implement a couch at the front of the bookshelf
       - Implemented a tree at the front of each house that places a tree on different side each time

* Student 4 (Eray Cekic)
    * Decided to not proceed with stilts and vertical access
    * Instead proceed with implementing second floor, pitched roof, staircase and trees for the road
    * Implemented a second floor for the village houses
    * Implemented a stair case to access the second floor
    * Implemented a pitched roof for the village houses
        - Implement trees for hte road side to make it more natural.
    
**Week 3**

* Student 1 (Alexander Stevensen)
    * Made Road.py object oriented and able to be run through the village.py file
* Student 2
    * ...
* Student 3 (Mohammed Usman E Ghani)
    * Checked all test to make sure the village is working according to the plan
    * Recorded a video explaining a part of the village structure
         - How furniture is generated
         - How the village meets the aesthetic and cretivity criteria
         - And about the village foundation
    * 
* Student 4 (Eray Cekic)
    * Ran multiple test runs on the village
    * Created a video to explain part of the village structuring
