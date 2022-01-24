import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import cm
#graph = nx.Graph()

def idz2A(filenames):
	for f in filenames:
		df = pd.read_csv("/home/koza/idz2/a/"+f+".csv", sep = ',')
		name = df.columns[0]
		df = df.set_index(df.columns[0])
		df.index.names=[None]
		lst = [] 
		lst_graph = []
		binPropRelation={}
		color_map = []
		print("\n<------------------------- Отношение "+name+" ------------------------->\n")
		print("В виде матрицы:\n")
		print(df)
		reflex=0
		lovReflex=0
		strongReflex=0
		antiReflex = 0
		symmetry = 0
		antisymmetry = 0
		asymmetry = 0
		properties = {}
		color_map = []
		x = []
		y = []
		z = []
		print("\nУзлы графа, ребра и их вес\n")
		for i in range(1,len(df['1'])+1):
			#<<<nodeGraph
			#graph.add_node('X'+str(i))
			#color_map.append('red')
			#nodeGraph>>>
			lst_graph = []
			for l in df.columns:
				if df.loc[i][l] != df.loc[int(l)][str(i)]:
					symmetry+=1
				if i == int(l):
					if df.loc[i][l] != 1:
						reflex+=1
						if df.loc[i][l] == 0:
							antiReflex +=1
				else:
#					print(i,l,min(float(df.loc[i][l]),float(df.loc[int(l)][str(i)])),min(float(df.loc[i][l]),float(df.loc[int(l)][str(i)]))==0)		
					if min(float(df.loc[i][l]),float(df.loc[int(l)][str(i)])) != 0:
						antisymmetry+=1
				if min(float(df.loc[i][l]),float(df.loc[int(l)][str(i)])) != 0:
					asymmetry+=1
				#<<<edgeGraph
				#graph.add_node('Y'+str(l))
				#if i ==1:
					#color_map.append('yellow')
				#graph.add_edge('X'+str(i),'Y'+str(l),weight=round(float(df.loc[i][l]),2))
				#edgeGraph>>>
				lst+=[([i,int(l)],round(float(df.loc[i][l]),2))]
				lst_graph+=['X'+str(i)+"<==>"+'Y'+str(l)+": "+str(df.loc[i][l])]
				#<<<plot
				#x+=[i]
				#y+=[int(l)]
				#z+=[float(df.loc[i][l])]
				#plot>>>
			print(lst_graph)
		#<<<edgeGraph
		#nx.draw(graph,node_color=color_map,with_labels=True)
		#edgeGraph>>>
		#plt.show()
#		print("Antireflex - "+str(antiReflex)+" dflen - "+str(len(df.columns)))
		if reflex == 0:
			properties['simpleReflex'] = '+'
			for i in range(1,len(df['1'])+1):
				for l in df.columns:
					if i == int(l):
						for k in range(1,len(df['1'])+1):
							for n in df.columns:
								if k != int(n) and df.loc[i][l] == df.loc[k][n]:
									strongReflex+=1
			if strongReflex > 0 :
				properties['strongReflex'] = '-'
			else: 
				properties['strongReflex'] = '+'
			properties['antiReflex'] = '-'
			properties['lovReflex'] = '-'	
		elif antiReflex < len(df.columns):
			for i in range(1,len(df['1'])+1):
				for l in df.columns:
					if i == int(l):
						for k in range(1,len(df['1'])+1):
							for n in df.columns:
								if k != int(n) and df.loc[i][l] < df.loc[k][n]:
									lovReflex+=1
			if lovReflex == 0:
				properties['lovReflex'] = '+'
				properties['simpleReflex'] = '-'
				properties['strongReflex'] = '-'
				properties['antiReflex'] = '-'
			else:
				properties['lovReflex'] = '-'
				properties['simpleReflex'] = '-'
				properties['strongReflex'] = '-'
				properties['antiReflex'] = '-'
		elif antiReflex == len(df.columns):
			properties['strongReflex'] = '-'
			properties['simpleReflex'] = '-'
			properties['antiReflex'] = '+'
			properties['lovReflex'] = '-'		
		if symmetry == 0:
			properties['symmetry'] = '+'
		else:
			properties['symmetry'] = '-'
		if antisymmetry == 0:
			properties['antisymmetry'] = '+'
		else:
			properties['antisymmetry'] = '-'
		if asymmetry == 0:
			properties['asymmetry'] = '+'
		else:
			properties['asymmetry'] = '-'
			
		print("\nВ виде списка кортежей:\n")
		print(lst)
		print("\n-----Свойства----\n")
		print("Классическая рефлексивность: " + properties['simpleReflex']+"\n")
		print("Строгая рефлексивность: " + properties['strongReflex']+"\n")
		print("Слабая рефлексивность: " + properties['lovReflex']+"\n")
		print("Антирефлексивность: "+properties['antiReflex']+"\n")
		print("Симметричность: "+properties['symmetry']+"\n")
		print("Антисимметричность: "+properties['antisymmetry']+"\n")
		print("Асимметричность: "+properties['asymmetry']+"\n")
		
		print("****************************")
		print("****** Транзитивность ******\n")
		transList =[]
		for i in range(1,len(df['1'])+1):
			transList+=[str(min(df['1'][i],df[str(i)][1]))]
			print("min(FP("+"X1,"+"Y"+str(i)+"),FP(X"+str(i)+",Y1)) = min("+str(df['1'][i])+","+str(df[str(i)][1])+") = "+str(min(df['1'][i],df[str(i)][1]))+"\n")
		print("max(",transList,")="+str(max(transList)))
		if float(df['1'][1]) >= float(max(transList)):
			print("\n(FP(X1,Y1) >= " + str(max(transList)) + ") ==> ("+ str(df['1'][1]) + " >= " + str(max(transList)) + ") - Отношение транзитивно")
		else:
			print("\n(FP(X1,Y1) >= " + str(max(transList)) + ") ==> ("+ str(df['1'][1]) + " >= " + str(max(transList)) + ") - Отношение нетранзитивно")
		print("\n****************************")
		print("****************************")
		#fig = plt.figure()
		#ax = fig.add_subplot(111, projection='3d')
		#surf = ax.plot_trisurf(x,y,z,cmap=cm.jet, linewidth=0)
		#fig.colorbar(surf)
		#fig.tight_layout()
		#plt.show()
		#plt.show()

idz2A(['R','S'])
