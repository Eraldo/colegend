
def extract_file(info, index=0):
    """
    Extract a file from a multi-part form graphQL response.
    :param info:
    :return:
    """
    files = info.context.FILES
    if files:
        file = files.get(str(index))
        return file
