# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
import pprint
 
def main():
    query = "cardale jones"
    bing_search(query, 'News', None)
    # bing_search(query, 'News', 15)
    # print bing_search(query, 'Image')
 
def bing_search(query, search_type, skip):
    #search_type: Web, Image, News, Video
    key= 'rqDuS7lFLg8AMzF/kfIRgEODMpf3zhSGIvhOpkx9tWQ='
    query = urllib.quote(query)
    # create credential for authentication
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials

    # NewsSortBy=%27Date%27
    # NewsSortBy=%Relevance%27


    if skip:
        news = '$NewsSortBy=%27Date%27'
        url = 'https://api.datamarket.azure.com/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$skip=15&NewsSortBy=%27Date%27&$format=json'
    else:
        url = 'https://api.datamarket.azure.com/Bing/Search/'+search_type+'?Query=%27'+query+'%27&NewsSortBy=%27Date%27&$format=json'

    print url
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request) 
    response_data = response.read()
    json_result = json.loads(response_data)
    result_list = json_result['d']['results']
    

    # for result in result_list:
    #     print result['Title']
    #     print result['Url']
    #     print result['Source']
    #     print result['Date']

    # # pp = pprint.PrettyPrinter(indent=4)
    # # pp.pprint(json_result)
    # # print result_list
    return json_result
 
if __name__ == "__main__":
    main()