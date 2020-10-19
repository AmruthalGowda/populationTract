import csv
#result Dictionary
result = {}
# open input file
with open('input/censustract-00-10.csv', mode='r') as f:
	file = csv.DictReader(f)
	#checking each row and extracting population data and percentage change
	for data in file:
		pop2000 =0
		pop2010 = 0
		percentage=0
		# handling missing/garbage value 
		try:
			#removing comma from the numeric data
			pop2000 =int(data['POP00'].replace(',' , ''))
			pop2010 = int(data['POP10'].replace(',' , ''))
			percentage_Str= (data['PPCHG']).replace(',' , '')
			percentage=float(percentage_Str)
		except:
			pass
		# main code	
		try:
			CBSA09 = data['CBSA09']
			CBSA_T = data['CBSA_T']
			#checking for valid CSBA data
			if CBSA09: 
				if result.get(CBSA09) == None:
					result[CBSA09] = {'CBSA_T':CBSA_T,  'tracts':1, 'population_2000':pop2000, 'population_2010':pop2010, 'percent_change':percentage}

				else:
					#if CSBA_T is missing in result dictionary for previous rows
					if not result[CBSA09]['CBSA_T']:
						result[CBSA09]['CBSA_T']= CBSA_T
					#calculating tracts
					tracts = result[CBSA09]['tracts']
					result[CBSA09]['tracts'] = tracts+1
					#calculating population for 2010
					population2010= result[CBSA09]['population_2010']
					result[CBSA09]['population_2010']= population2010 + pop2010
					#calculating population for 2000
					population2000= result[CBSA09]['population_2000']
					result[CBSA09]['population_2000']= population2000 + pop2000
					#caculate percentage change
					per= result[CBSA09]['percent_change']
					result[CBSA09]['percent_change']= per + percentage
		except:
			print('missing data')

#writing output report.csv
with open('output/report.csv', mode='w') as f:
    #Sorted result dictionary with Keys
    for x in sorted(result.keys()):
    	#calculating average percentage change and rounding
    	avg= (result[x]['percent_change'])/(result[x]['tracts'])
    	avg= round(avg, 2)
    	f.write(x + ',' + '"%s"' % result[x]['CBSA_T'] + ',' + str(result[x]['tracts']) + ' ,' + str(result[x]['population_2000']) +','+ str(result[x]['population_2010']) +','+ str(avg) )
    	f.write('\n')
# END



