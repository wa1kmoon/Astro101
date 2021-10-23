import json as js
import argparse

parser=argparse.ArgumentParser(prog='md2js',description='from md note to json file')
parser.add_argument('md', nargs='?',type=str, help='md note file from which json file was generated', metavar='mdfile') # 对于位置参数, add_arguement的第一个参数就是赋给变量的名字.
md=parser.parse_args().md

artlist=[]
mdfile=open(md,'r')
isart=False
for line in mdfile.readlines():
    if isart == False:
        artdict={"title":"", "type":"", "comment":"","article link":"","local note":"", "external links":"","abstract":"","index":""}
    if '###' in line:
        isart == True
        title=line.split('###')[-1].strip(' \n').split(']')[0].strip('[')
        #print(title)
        #print(artdict)
    if 'arxiv.org/abs' in line[:22]:
        link=line.strip(' `\n')
        #print(link)
        #print(artdict)
    if 'type' == line[:4]:
        typ = ':'.join(line.split(':')[1:]).strip(' \n')
        #print(typ)
    if 'comment' == line[:7]:
        comment = ':'.join(line.split(':')[1:]).strip(' \n')
        #print(comment)
    if '</details>' in line:
        isart == False
        note = md.split('-')[0]+'_lx.pdf'
        #print(note+'\n')
        artdict['title']=title
        artdict['article link']=link
        artdict['type']=typ
        artdict['comment']=comment
        artdict['local note']=note
        typ=comment=''
        #print(artdict)
        artlist.append(artdict)

with open(md.split('_')[0]+'_lx.json','w') as newjs:
    js.dump(artlist,newjs,ensure_ascii=False, indent=4)
