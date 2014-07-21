import json
import urllib.request, urllib.parse

def showsome(searchfor):
    query = urllib.parse.urlencode({'q': searchfor})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    search_response = urllib.request.urlopen(url)
    search_results = search_response.read().decode("utf8")
    results = json.loads(search_results)
    data = results['responseData']
    print('Resultados Totales: %s' % data['cursor']['estimatedResultCount'])
    hits = data['results']
    print('%d Resultados Principales:' % len(hits))
    for h in hits: print(' ', h['url'])
    print('Para más resultados, ver %s' % data['cursor']['moreResultsUrl'])

showsome('Resultados del Mundial de fútbol')