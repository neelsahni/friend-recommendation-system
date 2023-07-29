# Friend Recommendation System

## Description

The friend recommendation system is designed to analyze a social network and provide users with a friend suggestion based on the number of mutual friends. The program reads a file containing information about the connections between network members and calculates a similarity score for each pair of members. Then, the user enters a member ID to receive a friend recommendation based on the calculated scores. The recommended friend has the most connections with the user.

## Running the Program

Ensure that a file is entered with the following format to properly run the program:

    <number_of_users>
    <friend_a> <friend_b>
    <friend_c> <friend_d>
    ...

Note that each friend pair indicates a connection between 2 friends. 

When prompted, input the ID number of the user that is looking for a friend suggestion.

## Sample Output

    Facebook friend recommendation.
    
    Please input the name of the file: network.txt
    
    Enter an integer in the range 0 to 5: 2
    The suggested friend for 2 is 4
    Do you want to continue (enter y for yes)? y
    
    Enter an integer in the range 0 to 5: 0
    The suggested friend for 0 is 3
    Do you want to continue (enter y for yes)? n
