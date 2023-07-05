# Friend Recommendation System

A program that suggests the most recommended friend for a user by identifying individuals with the greatest number of mutual friends.

## Description

The friend recommendation system is designed to analyze a social network and provide users with a friend suggestion based on the number of mutual friends. The program reads a file containing information about the connections between network members and calculates a similarity score for each pair of members. The user can then enter a member ID to receive a friend recommendation based on the calculated scores.

## Sample Output

    Facebook friend recommendation.
    
    Please input the name of the file: network.txt
    
    Enter an integer in the range 0 to 5: 2
    The suggested friend for 2 is 4
    Do you want to continue (enter y for yes)? y
    
    Enter an integer in the range 0 to 5: 0
    The suggested friend for 0 is 3
    Do you want to continue (enter y for yes)? n
