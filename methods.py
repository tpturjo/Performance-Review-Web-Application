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
        new_tuple.append(myString1)
        new_tuple.append(myString2)
        new_tuple.append(myString3)
        new_tuple.append(myString4)
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
    Handles None values by converting them to the string "none".
    Helper function for format_list_for_public(list).

    Args:
        element: The value to handle.

    Returns:
        str: The converted value.

    """
    if element == None:
        return "not rated ☆"
    elif element == 1:
        return "★"
    elif element == 2:
        return "★★"


def average_ratings(ratings):


   if ratings:
       total_rating = sum(ratings[0] for i in ratings)
       average_rating = total_rating / len(ratings)
       return average_rating
   else:
       return None
