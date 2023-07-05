# NAME: NEEL SAHNI
# ID: 2791114924
# DATE: 2023-04-14
# DESCRIPTION: Program in which the user is provided their most recommended friend by finding individuals with
# the greatest number of mutual friends

from typing import IO, List, Dict


def open_file() -> IO:
    """
    Return a pointer to the file the user inputs if the file exists in that folder.
    In the case in which the file does not exist, print an error message and prompt the user for a file until
    it is valid
    """

    # loop through inputted files until valid one is provided
    file_pointer = None
    while file_pointer is None:
        filename = input("Please input the name of the file: ")
        try:
            file_pointer = open(filename, "r")
        except FileNotFoundError:
            print("The file cannot be opened")
    return file_pointer


def create_network(fp: IO) -> Dict[int, List[int]]:
    """
    Read through file and create dictionary using provided file pointer.
    Return dictionary with key of member id and value of list of member friends
    """

    size = int(fp.readline())
    network = {}

    for i in range(size):
        network[i] = []

    # read through user-inputted file and accordingly fill in dictionary
    for line in fp:
        split_line = line.split()
        mem_id_1 = int(split_line[0])
        mem_id_2 = int(split_line[1])
        network[mem_id_2].append(mem_id_1)
        network[mem_id_1].append(mem_id_2)

    return network


def init_matrix(size: int) -> List[List[int]]:
    """
    Return size x size matrix, using nested lists, initialized with values of 0
    """

    matrix = []

    # iterate through size x size and fill in values with 0
    for row in range(size):
        matrix.append([])
        for col in range(size):
            matrix[row].append(0)

    return matrix


def common_degree(list1: List, list2: List) -> int:
    """
    Return an integer indicating number of common friends from the 2 friend lists provided (list1 and list2)
        >>> common_degree([1, 2, 3], [1, 2, 3])
        3
        >>> common_degree([5, 6, 7], [7, 8, 9])
        1
    """
    # iterate through two lists and increment degree when a common friend is found
    degree = 0
    for i in range(len(list2)):
        if list2[i] in list1:
            degree += 1

    return degree


def calc_similarity_scores(network: Dict[int, List[int]]) -> List[List[int]]:
    """
    Return a nested list matrix indicating overlap of member_1's and member_2's friends
    """
    # iterate through network and fill network with degree of shared friends
    similarity_matrix = init_matrix(len(network))
    for i in range(len(network)):
        for j in range(i, len(network)):
            degree = common_degree(network[i], network[j])
            similarity_matrix[i][j] = degree
            similarity_matrix[j][i] = degree

    return similarity_matrix


def recommend(member_id: int, friend_list: List[int], similarity_list: List[int]) -> int:
    """
    Recommend friend with most overlaps in mutual friends and returns friend with most mututals
    """

    # find the maximum similarity score and its corresponding member id
    max_sim = -1
    max_id = -1
    for i in range(len(similarity_list)):
        if i != member_id and i not in friend_list and similarity_list[i] > max_sim:
            max_sim = similarity_list[i]
            max_id = i
    # find the first member that is not already in friend_list
    for i in range(len(similarity_list)):
        if i != member_id and i != max_id and i not in friend_list:
            return i
    # if all candidates are already in friend_list, return -1 to indicate no recommendation
    return -1


def main():
    print("Facebook friend recommendation.")

    network = create_network(open_file())
    similarity_matrix = calc_similarity_scores(network)

    # prompt user for number and suggest friend for friend associated with that number based on similarity score
    # if user responds with Y, 
    n = len(network) - 1
    response = "Y"
    while response.upper() == "Y":
        member_id = input(f"Enter an integer in the range 0 to {n}: ")
        if not member_id.isdigit() or not (0 <= int(member_id) <= n):
            print(f"Error: input must be an int between 0 and {n}")
        else:
            member_id = int(member_id)
            suggested_friend_id = recommend(member_id, network[member_id], similarity_matrix[member_id])
            print(f"The suggested friend for {member_id} is {suggested_friend_id}")
            response = input("Do you want to continue (enter y for yes)?").strip().lower()


if __name__ == "__main__":
    main()
    import doctest
    doctest.testmod()
