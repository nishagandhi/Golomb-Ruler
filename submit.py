def rec_BT(L, M, V, D):
	for d in D:
		dist=[]		
		if(len(V)!=M): 
			if not V:
				V.append(d)
				D.remove(d)
				x,V=rec_BT(L,M,V,D)
				if len(V)!=M:#To check the exhaustive condition below which the function wont have markers possible
					return -1,[]
			else:
				V.append(d)
				D.remove(d)	
				for i in range(0,len(V)-1) :
					for j in range (i+1,len(V)):
						break_point=0
						m=(abs(V[i]-V[j]))
		                                if m not in dist:
							dist.append(m)		
						else:
							V.remove(d)
							D.append(d)
							break_point=1
							break
					if break_point==1:
						break
				if break_point==0:
					x,V=rec_BT(L,M,V,D)
					#Backtracking Part 
					if len(V)!=M: 
						V.remove(d)
						D.append(d)
		else:
			break
	return 1,V



def rec_FC(L, M, V, D):	
	for d in D:
		dist=[]
		count=0
		if(len(V)!=M): 
			if not V:
				V.append(d)
				D.remove(d)		
				x,V=rec_BT(L,M,V,D)
				if len(V)!=M:#To check the exhaustive condition below which the function wont have markers possible
					return -1,[]				
			else:
				V.append(d)
				D.remove(d)	
				for i in range(0,len(V)-1) :
					for j in range (i+1,len(V)):
						break_point=0
						m=(abs(V[i]-V[j]))
		                                if m not in dist:
							dist.append(m)	
						else:
							V.remove(d)
							D.append(d)
							break_point=1
							break
					if break_point==1:
						break
				if break_point==0:
				# Foward Checking Part : Each element forward checks and eliminates the element from the domain
		
					for i in range(0,len(V)-1) :
						for j in range (len(V)-1,len(D)+1):
							m=abs(V[i]-D[j])
							if m in dist:
								D.remove(D[j])			
					x,V=rec_FC(L,M,V,D)
					if len(V)!=M: 
						V.remove(d)
						D.append(d)
		else:
			break
	return 1,V

def BT(L, M):
	m=0
	"*** YOUR CODE HERE ***"
	while m!=-1:
		domain = []
		var = []

		for i in range(0, L+1):
			domain.append(i)
		
		m,V=rec_BT(L, M, var, domain)
		if m==-1:
			domain = []
			var = []
			for i in range(0, L+2):
				domain.append(i)
			
			temp,V=rec_BT(L+1, M, var, domain)
		else:
			m=0
		L= L-1
	return V
	

def FC(L, M):

	"*** YOUR CODE HERE ***"
	m=0
	while m!=-1:
		domain = []
		var = []

		for i in range(0, L+1):
			domain.append(i)
		
		m,V=rec_FC(L, M, var, domain)
		if m==-1:
			domain = []
			var = []
			for i in range(0, L+2):
				domain.append(i)
			
			temp,V=rec_BT(L+1, M, var, domain)
		else:
			m=0
		L= L-1
	return V
	
 



