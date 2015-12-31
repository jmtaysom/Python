import httplib
from urlparse import urlparse

sites = ['rg', 'psi', 'eo', 'fict', 'cwc', 'fc', 'sg', 'sh', 'tt', 'vv',
         'ebxe', 'sh', 'si', 'ebmoh', 'ee', 'ds', 're']

example = r'http://archive.wizards.com/dnd/files/articles/dnd_re_20040412x.zip'



def checkUrl(url):
    p = urlparse(url)
    conn = httplib.HTTPConnection(p.netloc)
    conn.request('HEAD', p.path)
    resp = conn.getresponse()
    return resp.status < 400



if __name__ == '__main__':
    print checkUrl('http://www.stackoverflow.com') # True
    print checkUrl('http://stackoverflow.com/notarealpage.html') # False
    print checkUrl('http://archive.wizards.com/dnd/files/articles/dnd_re_20040412x.zip')
