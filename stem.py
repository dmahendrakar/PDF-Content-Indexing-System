
def contains_vowel(s):
	vowels=['a','e','i','o','u']
	while 'y' in s:
		i=s.index('y')
		if s[i-1] not in vowels:
			return True
	for ch in s:
		if ch in vowels:
			return True
	return False

def get_measure(s):
	vowels=['a','e','i','o','u']
	l=""
	is_vowel=False
	switch=False
	if s[0] in vowels: 
		is_vowel=True
		l+="V"
	else:
		is_vowel=False
		l+="C"

	for i in range(1,len(s)):		
		if s[i]=='y':
			if s[i-1] not in vowels:
				switch=True
				is_vowel=True			
		else:
			if s[i] in vowels:
				if is_vowel is False: switch=True
				is_vowel=True
			else:
				if is_vowel is True: switch=True
				is_vowel=False

		if switch is True:
			if l[-1]=='C':l+="V"
			else: l+="C"
			switch=False	

	if l[0]=='C':
		if len(l)%2==0:m=(len(l)-2)/2
		else:m=(len(l)-1)/2
	else:
		if len(l)%2==0:m=len(l)/2
		else:m=(len(l)-1)/2
	
	return m

def step_1a(s,m):
	if len(s)>4 and s[len(s)-4:len(s)]=='sses':
		s=s[0:len(s)-4]+"ss"
	elif len(s)>3 and s[len(s)-3:len(s)]=='ies':
		s=s[0:len(s)-3]+"i"
	elif len(s)>2 and s[len(s)-2:len(s)]=='ss':
		s=s[0:len(s)-2]+"ss"
	elif len(s)>1 and s[len(s)-1:len(s)]=='s':
		s=s[0:len(s)-1]
	return s

def step_1b(s,m):
	if m>0:
		if len(s)>3 and s[len(s)-3:len(s)]=='eed':
			s=s[0:len(s)-3]+'ee'
	if len(s)>2 and s[len(s)-2:len(s)]=='ed':
		l=s[0:len(s)-2]
		if contains_vowel(l):
			s=l	
	if len(s)>3 and s[len(s)-3:len(s)]=='ing':		
		l=s[0:len(s)-3]
		if contains_vowel(l):			
			s=l
	return s

def step_2(s,m):
	if m>0:
		if len(s)>7:
			dict={'ational':'ate',
				'ization':'ize',
				'iveness':'ive',
				'fulness':'ful',
				'ousness':'ous'}
			if s[len(s)-7:len(s)] in dict:
				s=s[0:len(s)-7]+dict[s[len(s)-7:len(s)]]
		if len(s)>6:
			dict={'tional':'tion',
				'ation':'ate',
				'bility':'ble',
				'ality':'al'}
			if s[len(s)-6:len(s)] in dict:
				s=s[0:len(s)-6]+dict[s[len(s)-6:len(s)]]
		if len(s)>5:
			dict={'entli':'ent',
				'ously':'ous',
				'alism':'al',
				'ality':'al',
				'ivity':'ive'}
			if s[len(s)-5:len(s)] in dict:
				s=s[0:len(s)-5]+dict[s[len(s)-5:len(s)]]
		if len(s)>4:
			dict={'ency':'ence',
				'ancy':'ance',
				'ably':'able',
				'ally':'al',
				'ator':'ate'}
			if s[len(s)-4:len(s)] in dict:
				s=s[0:len(s)-4]+dict[s[len(s)-4:len(s)]]			
		if len(s)>3:
			if s[len(s)-3:len(s)]=='ely':
				s=s[0:len(s)-4]+"e"
	return s

def step_3(s,m):
	if m>0:
		if len(s)>5:
			dict={'icate':'ic',
				'ative':'',
				'alize':'al',
				'iciti':'ic'}
			if s[len(s)-5:len(s)] in dict:
				s=s[0:len(s)-5]+dict[s[len(s)-5:len(s)]]
		if len(s)>4:
			if s[len(s)-4:len(s)]=='ical':
				s=s[0:len(s)-4]+"ic"
			if s[len(s)-4:len(s)]=='ness':
				s=s[0:len(s)-4]
			if s[len(s)-4:len(s)]=='iful':
				s=s[0:len(s)-4]+'y'
		if len(s)>3:
			if s[len(s)-3:len(s)]=='ful':
				s=s[0:len(s)-3]
	return s

def step_4(s,m):
	if m>1:
		if len(s)>5:
			if s[len(s)-5:len(s)]=='ement':
				s=s[0:len(s)-5]
		if len(s)>4:
			dict=['ance','ence','able','ible','ment','tion','sion']
			if s[len(s)-4:len(s)] in dict:
				s=s[0:len(s)-4]
		if len(s)>3:
			dict=['ant','ent','ism','ate','iti','ous','ive','ize']
			if s[len(s)-3:len(s)] in dict:
				s=s[0:len(s)-3]
		if len(s)>2:
			if s[len(s)-2:len(s)]=='ou':
				s=s[0:len(s)-2]
	return s

def step_5a(s,m):
	if m>1:		
		if len(s)>1:
			if s[-1]=='e':
				s=s[0:len(s)-1]
	if m==1 and len(s)>2 and s[-2]!='o' and s[-1]=='e':
		s=s[0:len(s)-1]
	return s

def step_5b(s,m):
	if m>1:
		if len(s)>1:
			if s[-1]=='l' or s[-1]=='d':
				s=s[0:len(s)-1]
	return s

def stem(s):
	m=get_measure(s)	
	s=step_1a(s,m)
	#print s
	s=step_1b(s,m)
	#print s
	s=step_2(s,m)
	#print s
	s=step_3(s,m)
	#print s
	s=step_4(s,m)
	#print s
	s=step_5a(s,m)
	#print s
	s=step_5b(s,m)
	print s
	
	return s
