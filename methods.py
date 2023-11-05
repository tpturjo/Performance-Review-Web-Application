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
        myString1 = "Author: " + handle_none_variables(element[0])
        myString2 = "Title: " + handle_none_variables(element[1])
        myString3 = "Content: " + handle_none_variables(element[2])
        new_tuple.append(myString1)
        new_tuple.append(myString2)
        new_tuple.append(myString3)
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
