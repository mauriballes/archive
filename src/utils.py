from urllib.parse import urlparse, parse_qs

def parse_youtube_link(link):
    EMBED_URL = 'https://www.youtube.com/embed/{}'
    THUMBNAIL_URL = 'http://img.youtube.com/vi/{}/sddefault.jpg'
    
    parse_url = urlparse(link)
    qs = parse_qs(parse_url.query)

    yt_id = qs.get('v')[0]
    embed_link = EMBED_URL.format(yt_id)
    thumbnail_link = THUMBNAIL_URL.format(yt_id)

    return (yt_id, embed_link, thumbnail_link)