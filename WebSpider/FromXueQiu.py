import urllib.request
import json

def main(page):
	try:
		url = "http://xueqiu.com/v4/statuses/user_timeline.json?user_id=8255849716&page="+str(page)
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
		'Cookie':'s=bc912sh1dq; xq_a_token=c85da224aae4cc9d740751e9f6afae2bf21b6c0d; xq_r_token=f4bb48c6d1e1b6ab8b4dd21cc06986a4bdae48e4; u=6990328147; xq_token_expire=Sun%20Apr%2017%202016%2014%3A12%3A45%20GMT%2B0800%20(CST); xq_is_login=1; bid=116d37dc630a436a825797475da6532a_im4ge6ut; webp=0; snbim_minify=true; __utmt=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1459127361,1459316348,1459407852,1459477035; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1459493237; __utma=1.445073094.1458713553.1459480119.1459493131.13; __utmb=1.5.10.1459493131; __utmc=1; __utmz=1.1458713553.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'}  
		req = urllib.request.Request(url, headers=headers)		
		response = urllib.request.urlopen(req).read()
		jsondata = json.loads(response.decode('utf-8'))
		fileName = '../genshu/Page1.txt'
		dataFile = open(fileName,'a',encoding='utf-8')
		allobjs = jsondata['statuses']
		for obj in allobjs:
			# print(obj['text'])
			dataFile.write(obj['text']+"\n")	
		
		dataFile.close()
		#print(jsondata)
	except Exception as err:
		print(err)


if __name__ == '__main__':
	for x in range(161,1,-1):
		main(x)
