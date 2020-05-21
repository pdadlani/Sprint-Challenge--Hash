def finder(files, queries):

    """
    Input: list of file paths, and list of filenames 
    Output: file paths that match filenames

    Make a queries dict.
    Iterate through all the file paths, getting the end of file path, and check if it exists in the query dict
    """

    result = []
    query_dict = dict()

    for query in queries:
        query_dict[query] = query

    for one in files:
        val = one.split('/')[-1]
        if val in query_dict:
            result.append(one)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
