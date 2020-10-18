import csv


result = {};

with open('input/censustract-00-10.csv', mode='r') as f:
	file = csv.DictReader(f)
	#checking each row and extracting product and date 
	for data in file:
		#CBSA09 = data['CBSA09']
		#CBSA_T = data['CBSA_T']
		#pop2000 =int(data['POP00'])
		#pop2010 = int(data['POP10'])
		pop2000 =0
		pop2010 = 0
		percentage=0
		
		try:

			pop2000 =int(data['POP00'].replace(',' , ''))

			pop2010 = int(data['POP10'].replace(',' , ''))
 
			percentage_Str= (data['PPCHG']).replace(',' , '')
			percentage=float(percentage_Str)

			#print(type(percentage))
		except:
			
			#print('percentage=' + percentage_Str)
			#print('pop_2000=' + data['POP00'])
			#print('pop_2010=' + data['POP10'])
			pass	

		
	
		try:
			CBSA09 = data['CBSA09']
			CBSA_T = data['CBSA_T']
			
			if CBSA09: 
				if result.get(CBSA09) == None:
					result[CBSA09] = {'CBSA_T':CBSA_T,  'tracts':1, 'population_2000':pop2000, 'population_2010':pop2010, 'percent_change':percentage}
					#print(result)
				else:
					if not result[CBSA09]['CBSA_T']:
						result[CBSA09]['CBSA_T']= CBSA_T




					tracts = result[CBSA09]['tracts']
					#print(tracts)
					result[CBSA09]['tracts'] = tracts+1

					population2010= result[CBSA09]['population_2010']
					result[CBSA09]['population_2010']= population2010 + pop2010

					population2000= result[CBSA09]['population_2000']
					result[CBSA09]['population_2000']= population2000 + pop2000




					per= result[CBSA09]['percent_change']
					result[CBSA09]['percent_change']= per + percentage

		except:
			print('missing data')


		









#print(result,'\n')
#writing a report.csv
with open('output/report.csv', mode='w') as f:
    #Sorted result dictionary with Keys
    for x in sorted(result.keys()):
    	avg= (result[x]['percent_change'])/(result[x]['tracts'])
    	avg= round(avg, 2)
    	#print(avg)
    	#print(x + ',' + '"%s"' % result[x]['CBSA_T'] + ',' + str(result[x]['tracts']) + ' ,' + str(result[x]['population_2000']) +','+ str(result[x]['population_2010']) +','+str(result[x]['percent_change']) +','+ str(avg) )
    	#f.write(x + ',' + '"%s"' % result[x]['CBSA_T'] + ',' + str(result[x]['tracts']) + ' ,' + str(result[x]['population_2000']) +','+ str(result[x]['population_2010']) +','+ str(result[x]['percent_change'] )+','+ str(avg) )
    	
    	#print(x + ',' + '"%s"' % result[x]['CBSA_T'] + ',' + str(result[x]['tracts']) + ' ,' + str(result[x]['population_2000']) +','+ str(result[x]['population_2010'])  +','+ str(avg) )
    	f.write(x + ',' + '"%s"' % result[x]['CBSA_T'] + ',' + str(result[x]['tracts']) + ' ,' + str(result[x]['population_2000']) +','+ str(result[x]['population_2010']) +','+ str(avg) )
    	

    	f.write('\n')





