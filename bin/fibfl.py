#!/usr/bin/python3
#
#

import sys
from flask import Flask,request,jsonify
app=Flask(__name__)

# use a dictionary to store values so we don't have to calculate the same value over and over; as sequence length get larger this is extremely fast
tab={} 

@app.route('/fibcal',methods=['POST','GET'])
def genFibSeq():

	def fib(n):
		if n == 0:
			tab[n]=0
			return tab[n]
		if n == 1:
			tab[n]=1
			return tab[n]
		if n in tab:
			return tab[n]
		else:
			var1=fib(n-1)
			var2=fib(n-2)
			tab[n]=var1+var2
			return tab[n]


	inval=request.args.get('seq','')
	# make sure a value was passed
	try:
		inval
	except:
		data="{'error': no sequence length passed}"
		return jsonify(data)

	# see if the value passed is an integer
	try:
		seqlen=int(inval)
	except:
		data="{'error': sequence value passed is not an integer}"
		return jsonify(data)

	# make sure integer is greater than 0
	if ( seqlen < 1 ):
		data="{'error': sequence value passed is less than one. Please pass an integer greater than zero}"
		return jsonify(data)

		
	# array to hold the output of our fib function
	seq=[]
	for i in range(0,seqlen,1):
		seq.append(fib(i))

	dlm=','
	ostr=dlm.join(str(e) for e in seq)
	data="{'sequence': [" + ostr  + "]}"
	return jsonify(data)

