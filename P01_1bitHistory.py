"""

# File name: P01_1bitHistory.py
#
# Python version: 3.6

"""

#"""
# THIS IS A 1 LEVEL LOCAL BRANCH PREDICTOR
#"""

f = open('./P01_1bit.in', 'r')
lines = f.readlines()
index=0

pht=[0] * 1024								#List used to simulate the behaviour of pattern history table

mispredict=0 								#Used for the misprediction counter
linectr=0 									#Counts the number of lines present in the trace file
bitwidth=0 									#Used to take the bitwidth for the saturating counter, from the user
centerval=0 								#Calculates the center value for a particular bit counter size(eg: 1 for a 2 bit counter)
raw_input=20
print("Enter the counter size as 2,4,6,8 or 10 (bits)")
#bitwidth=int(raw_input())
print ("Calculating the prediction rate....")
centerval =(((2**bitwidth)-1)/2)




for line in lines:
	line=line.rstrip()						#Used to strip the newline character at the end
	words=line.split(' ')					#Used to split the addressess and 'T' or 'N' tag
#print(words)

	index=int(words[0])%1024 				#Calculates the index used to index the Pattern/Branch history table
	if words[1]=='N':						#Check for 'N' or 'T' in the file
		if pht[index]<=centerval and pht[index]>0: 
			pht[index]=pht[index]-1 		#Decrement the saturating counter
		elif pht[index]>centerval:	
			pht[index]=pht[index]-1
			mispredict=mispredict+1 		#Increment the misprediction counter in case the saturating counter value is greater than centervalue 
	elif words[1]=='T':
		if pht[index]<=centerval:
			pht[index]=pht[index]+1
			mispredict=mispredict+1 		#Increment the misprediction counter in case the saturating counter value is lesser than centervalue 
		elif pht[index]>centerval and pht[index]<((2**bitwidth)-1):
			pht[index]=pht[index]+1
	linectr=linectr+1

pred=format(100-(100*(mispredict/(linectr*1.0))),'0.02f')
print ("The prediction rate for a ",bitwidth," bit counter is:", pred, "%")
print ("The misprediction rate for a ",bitwidth," bit counter is:", (100-float(pred)), "%")

f.close()