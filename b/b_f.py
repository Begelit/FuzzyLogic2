import pandas as pd

dfR = pd.read_csv("/home/koza/idz2/b/R.csv", sep = ',')
print(dfR,'\n')
nameStrokesR = [] #dfR['R'].reset_index(drop=True)
for i in range(len(dfR['R'])):
	nameStrokesR+=[dfR.loc[i]['R']]
nameColumnsR = dfR.columns.values[1:]
dfR.pop('R')
columR = 1
for i in dfR.columns:
	dfR.rename(columns={i:str(columR)}, inplace=True)
	columR+=1
dfR = dfR.rename(index = lambda x: x + 1) 
dfR.to_csv("/home/koza/idz2/b/R1.csv")
	
dfS = pd.read_csv("/home/koza/idz2/b/S.csv", sep = ',')
print(dfS,'\n')
nameStrokesS = dfS['S']
nameColumnsS = dfS.columns.values[1:]
dfS.pop('S')
columS = 1
for i in dfS.columns:
	dfS.rename(columns={i:str(columS)}, inplace=True)
	columS+=1
dfS = dfS.rename(index = lambda x: x + 1) 
dfS.to_csv("/home/koza/idz2/b/S1.csv")

dfR2 = pd.read_csv("/home/koza/idz2/b/R2.csv", sep = ',')
dfR2 = dfR2.set_index(dfR2.columns[0])
dfR2.index.names=[None]
dfS2 = pd.read_csv("/home/koza/idz2/b/S2.csv", sep = ',')
dfS2 = dfS2.set_index(dfS2.columns[0])
dfS2.index.names=[None]

print('\n---------Отношение R---------\n')
print(dfR2)
print('\n---------Отношение S---------\n')
print(dfS2)

print('\n--------- max-min Композиция ---------\n')

lst3=[]
for x in dfR.index:
	lst2=[]
	for z in dfS.columns:
		lst1=[]
		strprint1='Max( '
		strprint2='Max( '
		for y in dfR.columns:
			strprint1+='min( '+'FpR(X'+str(x)+',Y'+y+') , FpS(Y'+str(y)+','+'Z'+z+') )'
			strprint2+='min( '+str(dfR.loc[x][y])+' , '+str(dfS.loc[int(y)][z])+' )'
			if y != str(len(dfR.columns)):
				strprint1+=', '
				strprint2+=', '
			lst1+=[min(dfR.loc[x][y],dfS.loc[int(y)][z])]
		lst2+=[max(lst1)]
		strprint1+=' )='
		strprint2+=' )='
		print(strprint1)
		print(' = '+strprint2,'Max(',lst1,')=',max(lst1), ' ----> FpZ(X'+str(x)+',Z'+z+') = ', max(lst1),'\n')
	lst3+=[lst2]
dfZ1 = pd.DataFrame(lst3, columns=nameColumnsS, index = nameStrokesR)
print(dfZ1)

print('\n--------- max-prod Композиция ---------\n')

lst4=[]
for x in dfR.index:
	lst2=[]
	for z in dfS.columns:
		lst1=[]
		strprint1='Max( '
		strprint2='Max( '
		for y in dfR.columns:
			strprint1+='FpR(X'+str(x)+',Y'+y+') * FpS(Y'+str(y)+','+'Z'+z+')'
			strprint2+=str(dfR.loc[x][y])+' * '+str(dfS.loc[int(y)][z])
			if y != str(len(dfR.columns)):
				strprint1+=','
				strprint2+=','
			lst1+=[round(float(dfR.loc[x][y]*dfS.loc[int(y)][z]),3)]
		lst2+=[max(lst1)]
		strprint1+=' )='
		strprint2+=' )='
		print(strprint1)
		print(' = '+strprint2,'Max(',lst1,')=',max(lst1), ' ----> FpZ(X'+str(x)+',Z'+z+') = ', max(lst1),'\n')
	lst4+=[lst2]
dfZ2 = pd.DataFrame(lst4, columns=nameColumnsS, index = nameStrokesR)
print(dfZ2)


