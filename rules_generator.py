#！/usr/bin/env python
# -*- coding:utf-8 -*-
import pyperclip
import sys
import os
import math

cmd=['route print','exit']
url="https://ssrtool.us/tool/routeToRules"
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

print('turn on the game accelerator on L2TP/PPTP/OpenVPN mode. yes continue or no exit... y/n')
grant=input('')
while True:
    if grant=='y' or grant=='Y' or grant=='Yes' or grant=='YES':
        break
    elif grant=='n' or grant=='N' or grant=='No' or grant=='NO':
        sys.exit()
    else:
        print('unexpexted input! try again')
# 将路由表复制到剪贴板
    

route=os.popen('route print').read()
os.system('exit')


#0,127,192,10,ip>=224,172.16~31,169.254不代理
forbid_ip=['0','127','192','10']
def get_ip_from_route(s=''):
    output=''
    list=s.splitlines()
    n=0
    # print(list)
    while True:
        if list[n]=='':
            n+=1
            continue
        elif list[n][0]=='网':
            start=n+1
            break
        else:
            n+=1
    while True:
        if list[n]=='':
            n+=1
            continue
        elif list[n][0]=='=':
            end=n
            break
        else:
            n+=1
    for q in range(start,end):
        info=list[q].split()
        ip=info[0]
        ips=ip.split('.')
        if ips[0] in forbid_ip or int(ips[0])>=224:
            continue
        elif ips[0]=='172' and int(ips[1])>=16 and int(ips[1])<=31:
            continue
        elif ips[0]=='169' and ips[1]=='254':
            continue
        else:
            mask=info[1]
            masks=mask.split('.')
            masks.reverse()
            count=0
            ips.reverse()
            count=0
            for o in ips:
                if o=='0':
                    count+=1
                else:
                    break
        if count==0:
            cidr=32
            output=output+ip+'/'+str(cidr)+'\n'
        elif ips[3]==ips[2]==ips[1]:
            cidr=24
            output=output+ips[3]+'.'+ips[2]+'.'+ips[1]+'.0'+'/'+str(cidr)+'\n'
        else:
            cidr=32-(8*count)
            output=output+ip+'/'+str(cidr)+'\n'
    sort=output.splitlines()
    fir=[]
    sec=[]
    thir=[]
    four=[]
    for i in sort:
        id=i[-1]
        if id=='8':
            fir.append(i)
        elif id=='6':
            sec.append(i)
        elif id=='4':
            thir.append(i)
        else:
            four.append(i)
    re=fir+sec+thir+four
    re='\n'.join(re)
    return re

data=get_ip_from_route(route)    
        

 
# 获取路径创建文件

while True:
    print('1.sstap or 2.netch 1/2')
    choice=input('')
    if choice=='2':
        print('The game name:')
        game_name=input('')
        
        file_name=game_name+'.txt'
        
        title='#'+game_name+','+'1'+'\n'
        
        file_path = os.path.join(application_path,file_name)
        
        file=open(file_path,'w')
        file.write(title+data)
        file.close
        break
    elif choice=='1':
        print('The game name:')
        game_name=input('')

        print('section:')
        section=input('')
        
        print('游戏中文名:')
        game_name_cn=input('')
        
        en=game_name.replace(' ','-').title
        ch=game_name_cn.replace(' ','-').title
        
        title='#'+en+','+ch+',0,0,1,0,1,0,By-Auto-generator'+'\n'
        
        file_name=game_name+section+'.rules'
        
        file_path = os.path.join(application_path,file_name)
        file=open(file_path,'w')
        file.write(title+data)
        file.close
        break
    else:
        print('unexpected input,try again!')
        continue
print('finished')







