from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import unicodedata
import porter as stemmer
import itertools
from Tkinter import *

book=""
book_trie={}
chapters={}
sections={}
ch_map = {} 
sec_map = {}
para_map = {}
count={}
question=""
param=3
valid_letters='- \' a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
stopwords="?,a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your".split(',')


def process_text():
    global count,ch_map,sec_map,para_map,book_trie,book

    fp = open('Algorithms.pdf', 'rb')
    parser = PDFParser(fp)
    document = PDFDocument(parser, "secret")
    outlines = document.get_outlines()

    #get index contexts
    i=j=0
    for (level,title,dest,a,se) in outlines:
        if level==1:
            if i<9:
                i+=1
                chapters[i]=unicodedata.normalize('NFKD', title).encode('ascii','ignore')
        else:
            if j< 44:
                j+=1
                sections[j]=unicodedata.normalize('NFKD', title).encode('ascii','ignore')
    

    with open('Algorithms.txt','rb') as f:
        book=f.read()       

    a=0
    for j in chapters:
        ch_map[j]=book.index(chapters[j])
        a=ch_map[j]

    a=0
    for j in sections:
        sec_map[j]=book.index(sections[j])
        a=sec_map[j]

    i=1
    a=0
    para_map[i]=a
    i+=1
    while(a<len(book)):
        try:
            a=book.index('\n\n',a+1)
        except:
            break
        para_map[i]=a+2
        i+=1

    count[1]=len(ch_map)
    count[2]=len(sec_map)
    count[3]=len(para_map)
    book_trie=make_trie()


def get_chap(i):
    global ch_map

    for j in range(2,len(ch_map)):
        if i<ch_map[j]: 
            return j-1


def get_sec(i):
    global sec_map

    for j in range(2,len(sec_map)):
        if i<sec_map[j]: return j-1


def get_para(i):
    global para_map

    for j in range(2,len(para_map)):
        if i<para_map[j]: return j-1


def make_trie():
    global valid_letters,book
    root={}
    cur=root
    escape=[' ','\n']
    _end='_end'
    with open('Algorithms.txt','rb') as f:
        book=f.read()
    for i in range(len(book)):
        letter=book[i].lower()
        if letter in valid_letters:
            if letter in cur:
                cur = cur[letter]
            else:
                cur[letter]={}
                cur=cur[letter]
        else:
            if '_end' not in cur:
                cur['_end'] = ([],[],[])
            ch=get_chap(i)
            if ch not in cur['_end'][0]:
                cur['_end'][0].append(ch)
            sec=get_sec(i)
            if sec not in cur['_end'][1]:
                cur['_end'][1].append(sec)
            para=get_para(i)
            if para not in cur['_end'][2]:
                cur['_end'][2].append(para)
    
            cur = root
        i+=1
    return root


res=([],[],[])
def find_leaf_cspl(cur):
    global res
    for i in cur:
        if i is not '_end':
            find_leaf_cspl(cur[i])
        else:
            for k in cur['_end'][0]:
                if k not in res[0]:
                    res[0].append(k)
            for k in cur['_end'][1]:
                if k not in res[1]:
                    res[1].append(k)
            for k in cur['_end'][2]:
                if k not in res[2]:
                    res[2].append(k)


def in_trie(trie, word):
    global res,param

    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return False
    else:
        if '_end' in current_dict:
            return current_dict['_end']
        else:
            res=([],[],[])
            find_leaf_cspl(current_dict)
            return res


def binomial_coeff(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result


def content_indexing_algorithm(word_cpsl):
    global count
    #keywordcount
    kwc=len(word_cpsl)
    j=word_cpsl.keys()[0]
    union=set(word_cpsl[j])
    for i in word_cpsl:
        union|=set(word_cpsl[i])
    union=sorted(list(union))
    m=len(union)
    
    #rank vector,X
    X=[]
    res=0
    k=kwc
    for i in range(kwc,0,-1):
        j=binomial_coeff(kwc,i)
        for _ in range(j):X.append(k)
        k-=1
        res+=j
    n=res

    #cspl matrix,M
    M=[]
    for i in range(m):
        M.append([0]*n)
    a=[]
    for i in range(kwc):
        a.append(i)

    c=0
    for i in range(kwc,0,-1):
        j=itertools.combinations(a,i)
        for k in j:
            res=set([i for i in range(count[param])])
            for l in k:
                res&=set(word_cpsl[l])
            for l in res:
                M[union.index(l)][c]=1
            c+=1
    I=[]
    for i in range(m):
        c=0
        for j in range(n):
            c+=M[i][j]*X[j]
        I.append(c)

    #sort routine
    for i in range(m):
        v=I[i];j=i-1;u=union[i]
        while j>=0 and I[j]<v:
            I[j+1]=I[j]
            union[j+1]=union[j]
            j-=1
        I[j+1]=v
        union[j+1]=u

    return union


def process_input():
    global question,param,valid_letters,book_trie
    
    question=raw_input("Enter your question\n")
    param=int(raw_input("Search parameter: \n1.Chapter\n2.Section\n3.Paragraph\nEnter your choice:"))
    print

    words=question.split(' ')

    for i in range(len(words)):
        s=""
        for j in range(len(words[i])):
            if words[i][j] in valid_letters:
                s+=words[i][j]
        words[i]=s

    j=0
    keywords={}
    for i in words:
        if i not in stopwords:
            s=stemmer.stem(i)
            keywords[j]=s
            j+=1

    word_cpsl={}

    for i in keywords:
        cspl=in_trie(book_trie,keywords[i])
        if cspl:
            word_cpsl[i]=cspl[param-1]
    return word_cpsl


def display(solution_set):
    global ch_map,sec_map,para_map,question,param
    s="SEARCH RESULTS-\nSearch Question: "+question+"\nSearch Parameter: "
    if param==1:
        s+="Chapter\n\n"
    elif param==2:
        s+="Section\n\n"
    elif param==3:
        s+="Paragraph\n\n"
    for i in solution_set:
        if i is not None:
            if param==1:
                s+="--> In chapter: "+chapters[get_chap(ch_map[i])]+"\n"
                #s+= book[ch_map[i]:ch_map[i+1]]
            elif param==2:
                s+="--> In section: "+sections[get_sec(sec_map[i])]+"\n"
                #s+= book[sec_map[i]:sec_map[i+1]]
            elif param==3:
                sec=get_sec(para_map[i])
                if sec is not None:
                    s+="--> In section: "+sections[sec]+"\n"
                s+= book[para_map[i]:para_map[i+1]]
            s+="-------------------------------------------------------------------------------------------------------------------------------\n\n"
    print "output redirected to output.txt file"
    f = open('output.txt','w')
    f.write(s)
    f.close() 


def main():
    process_text()
    word_cpsl=process_input()
    if(len(word_cpsl)>0):
        solution_set=content_indexing_algorithm(word_cpsl)
        print "solution set: \n",solution_set
        display(solution_set)
    else:
        f = open('output.txt','w')
        f.write('keywords not found in the text.')
        f.close() 


if __name__=='__main__':
    main()

