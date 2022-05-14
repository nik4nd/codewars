def domain_name(url):
    for i in ['www.', '//']:
        if i in url:
            return url.split(i)[1][:url.split(i)[1].find('.')]
    return url[:url.find('.')]
