def format_list_for_public(list):
    """
    Formats the list of published reviews for the public page.

    Args:
        lst (list): The list of published reviews.

    Returns:
        list: The formatted list of reviews.

    """
    new_list = []
    for element in list:
        new_tuple = []
        myString1 = "Author: " + handle_none_variables(element[1])
        myString2 = "Title: " + handle_none_variables(element[2])
        myString3 = "Content: " + handle_none_variables(element[3])
        myString4 = "Rating: " + handle_reviews(element[4])
        # element[0] is the submission id
        myString5 = element[0]
        new_tuple.append(myString1)
        new_tuple.append(myString2)
        new_tuple.append(myString3)
        new_tuple.append(myString4)
        new_tuple.append(myString5)
        new_list.append(new_tuple)
    return new_list

def format_list_with_comments_for_public(list):
    """
    Formats the list of published reviews for the public page.

    Args:
        lst (list): The list of published reviews.

    Returns:
        list: The formatted list of reviews.

    """
    new_list = []
    for element in list:
        new_tuple = []
        myString1 = "Author: " + handle_none_variables(element[1])
        myString2 = "Title: " + handle_none_variables(element[2])
        myString3 = "Content: " + handle_none_variables(element[3])
        myString4 = "Rating: " + handle_reviews(element[4])
        # element[0] is the submission id
        myString5 = element[0]
        comments = handle_none_variables(element[5])
        new_tuple.append(myString1)
        new_tuple.append(myString2)
        new_tuple.append(myString3)
        new_tuple.append(myString4)
        new_tuple.append(myString5)
        new_tuple.append(comments)
        new_list.append(new_tuple)
    return new_list


def handle_none_variables(element):
    """
    Handles None values by converting them to the string "none".
    Helper function for format_list_for_public(list).

    Args:
        element: The value to handle.

    Returns:
        str: The converted value.

    """
    if element == None:
        return "none"
    else:
        return element

def handle_reviews(element):
    """
    Handles the ratings of each review.

    Args:
        str: string representation of a rating.

    Returns:
        str: The converted value.

    """
    if element == None:
        return "not rated"
    elif element == 1:
        return "★"
    elif element == 2:
        return "★★"
    elif element == 3:
        return "★★★"
    elif element == 4:
        return "★★★★"
    elif element == 5:
        return "★★★★★"


