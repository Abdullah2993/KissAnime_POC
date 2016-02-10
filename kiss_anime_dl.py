import cfscrape
import bs4
import base64

base_link = 'http://kissanime.to'

name = input('Anime Name:')

name_esc = name.replace(' ', '-')
link_anime_rel = '/anime/' + name_esc
link_anime_abs = base_link + link_anime_rel

scraper = cfscrape.create_scraper()
source = scraper.get(link_anime_abs).content.decode('utf-8')

soup_s = bs4.BeautifulSoup(source, 'html.parser')

for row in reversed(soup_s('table')[0].findAll('tr')[2:]):
    tds = row.findAll('td')
    ep_link = base_link + tds[0].a['href']
    ep_source = scraper.get(ep_link).content.decode('utf-8')
    soup_e = bs4.BeautifulSoup(ep_source, 'html.parser')
    for opt in soup_e('select', {'id': 'selectQuality'})[0].findAll('option'):
        print('Episode: ', tds[0].a.string.strip())
        print('Quality: ', opt.string)
        print('Link: ', base64.b64decode(opt['value']))