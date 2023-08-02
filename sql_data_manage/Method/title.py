def getValidQueryTitleList(title_list, query_title_list=None):
    if query_title_list is None:
        return title_list

    if len(query_title_list) == 0:
        print('[WARN][title::getValidQueryTitleList]')
        print('\t query title list is empty!')
        return query_title_list

    valid_query_title_list = []
    for query_title in query_title_list:
        if query_title not in title_list:
            print('[WARN][title::getValidQueryTitleList]')
            print('\t query title [' + query_title + '] not valid!')
            continue

        valid_query_title_list.append(query_title)

    if not valid_query_title_list:
        print('[WARN][title::getValidQueryTitleList]')
        print('\t valid query title list is empty!')

    return valid_query_title_list
