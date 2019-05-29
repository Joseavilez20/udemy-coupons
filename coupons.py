#Author Jose Aviles, Date: 29/05/2019
import http.client,sys 
if __name__ == "__main__":

	#Here you User-Agent click in Inspect element->Network->Request Headers  
	#look for User-Agent  usually  in the final part of the header 
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.109'}
			
	links = list()
	#Add the links of the courses by example 
	#links = ['https://www.udemy.com/100-105-netcert-interconnecting-cisco-networking-exam/?couponCode=100-105','https://www.udemy.com/100onlinebusiness/?couponCode=M3DIUM']

	links = [] #Here links
	
	#f = open(sys.argv[1])
	g = open("couponAvaliable.txt","w")
	
	for item in links:
			
		try:

	
			url = item
			
			site = url.replace("https://","").rsplit("/")
			url_domain =  site[0]
			url_request = "/"+ site[1] + "/" + site[2]
			connection = http.client.HTTPSConnection(url_domain)
			connection.request("GET",url_request, headers=headers)
			response = connection.getresponse()
			
			
			if response.status == 200:
				g.write(url)
				print ("%s %s %s" % (url, response.status, response.reason))
			#print(result.content.decode())
			
				
		except http.client.BadStatusLine as e:
		           
			print(str(e))
g.close()
			
	

