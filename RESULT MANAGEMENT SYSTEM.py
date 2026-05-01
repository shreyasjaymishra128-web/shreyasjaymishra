def add():
	import pickle
	with open('results.rec','wb') as f:
		l=[]
		d={}
		while True:
			r=int(input("Enter the roll no."))
			while True:
				s=input("Enter the subject name")
				m=int(input("Enter the marks"))
				l.append([s,m])
				i=input('Continue entering marks for this record?')
				if i[0] not in 'yY':
					break
			d[r]=tuple(l)
			l=[]
			p=input('Continue entering marks?')
			if p[0] not in 'yY':
				break
		pickle.dump(d,f)
def update():
	import pickle
	import os
	with open('results.rec','rb') as f,open('resultant.rec','wb') as g:
		a=pickle.load(f)
		h={}
		r=int(input('Enter roll no.'))
		s=input('Enter subject name')
		m=int(input('Enter changed marks'))
		l=a.keys()
		for i in l:
			if i!=r:
				h[i]=a[i]
			else:
				for j in list(a[r]):
					if j[0]==s:
						j[1]=m
				h[r]=tuple(a[r])
		pickle.dump(h,g)
		os.remove('results.rec')
		os.rename('resultant.rec','results.rec')
def search():
	import pickle
	with open('results.rec','rb') as f:
		a=pickle.load(f)
		r=int(input('Enter roll no.'))
		print(a.get(r))
def delete():
	import pickle
	import os
	with open('results.rec','rb') as f,open('resultant.rec','wb') as g:
		h={}
		r=int(input('Enter roll no.'))
		a=pickle.load(f)
		l=a.keys()
		for i in l:
			if i!=r:
				h[i]=a[i]
		pickle.dump(h,g)
		os.remove('results.rec')
		os.rename("resultant.rec",'results.rec')
def teacher():
	i=input('Enter 4 digit teacher ID to proceed')
	if len(i)==4:
		print('Enter 1 to open Teachers tab', 'Enter 2 to open Students tab',sep="\n")
		j=int(input('Enter the corresponding no.'))
		if j==1:
			print("Enter 1 to add record","Enter 2 to update record","Enter 3 to delete record",sep='\n')
			while True:
				n=int(input('Enter number'))
				if n==1:
					add()
				elif n==2:
					update()
				elif n==3:
					delete()
				else:
					break
		if j==2:
			search()
	else:
		print('You are a student and by mistake came here, check your results')
		search()
def student():
	print('All your hardwork and efforts boil down to this very moment when your results are declared. We are delighted to do so. To check your result, enter your roll no.')
	search()
print('Enter 1 if you are a teacher')
print('Enter 2 if you are a student')
i=int(input('Enter corresponding no. to proceed'))
if i==1:
	teacher()
if i==2:
	student()