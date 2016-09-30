



# dic = {'0':1, '1':2,'2':3}
# print (dic)

# toset = set(dic)
# print ("kesy", toset)

# setval = set(dic.values())
# print("val", setval)


l = [[1,2],[2,3],[3,4]]
for i in range(0,len(l)):
	# for j in range(0,len(l[i])):
	valuemax = 0
	value1 = l[i][1]
	value2 = l[i+1][1]
	if value1 > value2:
		valuemax = value1
	elif value2 > value1:
		valuemax = value2
	elif value1==value2:
		valuemax = 'tie'





# print len(l)










# # t=input()
# # v=raw_input()

# # print ("t is %s"%type(t))



# # print ("v i %s"%type(v))


# # def gcd(num1,num2):
# # 	rem=num1%num2
# # 	while rem!=0 :
# # 	    num1=num2
# # 	    num2=rem
# # 	    rem=num1%num2
# # 	return num2

# # def lcm(num1,num2):
# # 	lcm = (num1*num2)/gcd(num1, num2)
# # 	return lcm

# # def main():
# # 	t = input()
# # 	while t:
# # 		# pass
# # 		num1,num2 = raw_input().split()
# # 		num1 = int(num1)
# # 		num2 = int(num2)
# # 		try:
# # 			g = str(gcd(num1, num2))
# # 			l = str(lcm(num1, num2))
# # 			print g,l
# # 		except:
# # 			return 0

# # 		t-=1
# # main()


# # def gl(a,b):
# # 	i=1
# # 	gcd = 1.0
# # 	# lcm = 0
# # 	try:
# # 		if i<=a and i<=b:
# # 			if a%i==0 and b%i==0:
# # 				gcd=i
# # 			# lcm = (a*b)/gcd

# # 		return gcd
# # 	except:
# # 		return 0

# # t = input()
# # while t:
# # 	a,b = raw_input().split()
# # 	a=float(a)
# # 	b=float(b)
# # 	gcd = gl(a,b)
# # 	lcm = (a*b)/gcd
# # 	print gcd,"%.0f"%lcm
# # 	t-=1

# def primeGenerator():
# 	j=1
# 	for i in range(1,10):
# 		# for i in range(a,b+1):
# 		if i%!=0:
# 			print i
# 		j+=1


# # def prime(a,b):
# # 	a=int(a)
# # 	b=int(b)
# # 	prime = 1
# # 	for i in range(a,b):



# primeGenerator()

# def flip1(strnum):
# 	count = 0
# 	# strnum = str(number)
# 	isTrue = False
# 	# newstr = ''
# 	for i in range(0,len(strnum)):
# 		if strnum[i] is '0':
# 			count+=1


# 	if count==1:
# 		isTrue = True
# 	else:
# 		isTrue = False
# 	return isTrue

# def flip0(strnum):
# 	count = 0
# 	isTrue = False
# 	# strnum = str(number)
# 	# newstr = ''
# 	for i in range(0,len(strnum)):
# 		if strnum[i] is '1':
# 			count+=1


# 	if count==1:
# 		isTrue =True
# 	else:
# 		isTrue = False
# 	return isTrue

# def main():
# 	t = input()

# 	while t:
# 		strnum = raw_input()

# 		if flip0(strnum):
# 			print('Yes')
# 		elif flip1(strnum):
# 			print('Yes')
# 		else:
# 			print('No')

# 		t-=1

# main()




# def pall(w):
# 	alphaList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# 	if '.' in w[:]:
# 		for i in range(0,25):
# 			if w.replace('.',alphaList[i])==(w.replace('.',alphaList[i]))[::-1]:
# 				w = w.replace('.',alphaList[i])
# 				break

# 	elif '.' in w[:]:
# 		pall(w)
# 	else:
# 		return w
# 	return w

# 	# 	else:
# 	# 		return '-1'

# 	# elif w==w[::-1]:
# 	# 	return w
# 	# else:
# 	# 	return '-1'
# 	# return w

# def main():
# 	t =input()
# 	while t:
# 		w = raw_input()
# 		print (pall(w))

# 		t-=1
# 	return 0
# main()
































