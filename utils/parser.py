def parse(resp_data, *args):
    """
    Example RESP Array
        *2\r\n$4\r\nECHO\r\n$3\r\nhey\r\n
    """
    data_list = resp_data.split("\r\n")
    items = []
    for idx in range(1, len(data_list)):
        if data_list[idx-1][0] == "$":
            items.append(data_list[idx])

    return items


