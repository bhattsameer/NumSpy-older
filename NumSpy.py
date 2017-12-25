import re,sys,time,urllib.parse
from urllib.request import Request, urlopen

print ("""
	##     #   #     #   ##        ##   ######  ######  #     #
	# #    #   #     #   # #      # #   #       #    #   #   #
	#  #   #   #     #   #  #    #  #    #      #    #    # #
	#   #  #   #     #   #   #  #   #      #    ######     #
	#    # #   #     #   #    ##    #        #  #          #
 	#     ##   #######   #          #   ######  #          #""")


url = "https://www.tricksfolks.com/truecaller/search.php?ccode=IN&number="
with open("numbers.list","r") as f:
    print ("")
    print ("Searching....")
    print ("")
    time.sleep(4)
    store = open('output.txt','w')
    for line in f:
        url1 = urllib.parse.quote_plus(url) + line
        req = Request(urllib.parse.unquote(url1), headers={'User-Agent': 'Mozilla/5.0'})
        data = urlopen(req).read()
        data1 = data.decode("utf-8")
        
        m = re.search('h2',data1)
        start = m.start()+3
        end = start + 30
        newString = data1[start:end]
        store.write(str("\n"+newString+'\n'))
        
        m= re.search('Name',data1)
        start = m.start()+13
        end= start + 12 
        Name = data1[start:end]
        store.write(str("Name : "+Name+'\n'))
        
        m = re.search('Carrier',data1)
        start = m.start()+16
        end = start + 6
        Carrier = data1[start:end]
        store.write(str("Carrier : "+Carrier+'\n'))
        
        m = re.search('City',data1)
        start = m.start()+13
        end = start + 7
        City = data1[start:end]
        store.write("City : "+City+'\n')
print('done')


