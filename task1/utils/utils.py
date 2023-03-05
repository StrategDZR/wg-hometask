import re


def clean_str_for_int(string):
    """
    Clean provided string from links, dots, commas and words in round brackets for successful parce to int
    :param string: string with dots, commas, links, words in round brackets
    :return: string ready to be parsed to int
    """
    return re.sub(r"\[\d+\]|\((.*)\)|,|\.", "", string)


def clean_str_for_str(string):
    """
    Clean provided string from links like [34]
    :param string: string with links
    :return: reformatted string without links
    """
    return re.sub(r"\[\d+\]", "", string)
