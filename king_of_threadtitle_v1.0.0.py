import re
import html
import requests

print("西暦何年のコテ雑？（4桁の数字）")
year = input()
print("何月のコテ雑？（1～2桁の数字）")
month = input().zfill(2)

page = 1
pattern = r'<a class="thread".+?title="(.+?)">.+?<td class="date">.+?(\d{4})-(\d{2})-(\d{2})'
path = './result.txt'

r = html.unescape(requests.get('https://www.logsoku.com/search?q=%E3%82%B3%E3%83%86%E9%9B%91&sort=create&board=news4vip&p='+str(page)+'&site=2ch.sc').text)
threads = re.findall(pattern, r)

while (int(threads[-1][1]) >= int(year)) | (int(threads[-1][2]) >= int(month)):
    page = page + 1
    r = html.unescape(requests.get('https://www.logsoku.com/search?q=%E3%82%B3%E3%83%86%E9%9B%91&sort=create&board=news4vip&p='+str(page)+'&site=2ch.sc').text)
    threads.extend(re.findall(pattern, r))

with open(path, mode='w', encoding='utf_8') as f:
    for _ in threads:
        if (_[1] == year) & (_[2] == month):
            f.write(_[2]+'/'+_[3]+' '+_[0]+'\n')