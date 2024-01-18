import random
import pickle
import webbrowser
import os



def welcome():
    print('Welcome to the Music Management Program')
    print('Please choose one of the following:')
    print()
    print()
    print('To Login to your existing account:')
    print('Press the Number "1"')
    print()
    print()
    print("To Create a New Account:")
    print('Press the Number "2"')
    print()
    print()
    true=True
    while true:
        choice=input("Enter your choice: ")
        if choice=='1':
            usernamepassword()
            break
        elif choice=='2':
            createusernamepassword()
            break
        elif choice not in '12':
            print('Please Enter the given numbers only')
            true=True
            

def usernamepassword():
    print()
    print('Hello there listener, Hope you are having a great day')
    print("So let's start")
    print()
    n=1
    true=True
    while true:
        global un
        un=input("Enter your username: ")
        
        fr=open('Usernames and Passwords.dat','rb')
        found=0
        fr.seek(0,2)
        eof=fr.tell()
        fr.seek(0,0)
        while fr.tell()<eof:
            k=pickle.load(fr)
            if k[0]==un:
                found=1
                pw=input("Enter your Password: ")
                if pw==k[1]:
                    print('Welcome', un)
                    interface(un)
                    true=False
                else:
                    print('Your Username-Password pair seems incorrect. Would you like to try again?')
                    print('Press "1" for "YES" or Press "2" for "NO"')
                    true3=True
                    while true3:
                        choice=input("Enter your choice: ")
                        if choice=='1':
                            true=True
                            true3=False
                        elif choice=='2':
                            print('Thank you, Have a Nice Day, See you again soon.')
                            true=False
                            true3=False
                        else:
                            print('Dear User, Please Enter the value 1 or 2 for the respective need')
                            true3=True

                            
            else:
                 continue
        if found==0:
                    print('It seems this username does not exist.')
                    print("You can do the following: ")
                    print("1. Retry Logging In")
                    print("2. Create a New Account")
                    print("3. Leave the Program")
                    true4=True
                    while true4:
                        try:
                            choice4=int(input("Enter [1,2,3]: "))
                            if choice4==1:
                                true=True
                                true4=False
                            elif choice4==2:
                                createusernamepassword()
                                true4=False
                            elif choice4==3:
                                print("Thank you, Have a Nice Day")
                                true=False
                            
                                true4=False
                            elif choice4 not in [1,2,3]:
                                print("Please Enter from the above numbers only")
                                true4=True
                        except ValueError:
                            print('Please Enter A Numeric Value')
                            true4=True
        
def createusernamepassword():
    print()
    print()
    print('Hello there, Hope you are having a great day')
    print('To create an account, please enter the following details')
    print()
    fname=input("Enter your First Name: ")
    lname=input("Enter your Last Name: ")
    print()
    print('Now you have to make your username')
    print()
    print('There are some rules that you must follow in order to have a valid username')
    print('1. The Username should not contain any special characters except userscore(_) or at sign(@)')
    print('2. It should be atleast 8 characters long')
    print('3. It should contain atleast one Uppercase and atleast one Lowercase character')
    print('4. It should contain atleast one digit')
    print("Choose a Username that would define you, in a fun way, make yourself unique!!")
    true=True
    while true:
        username=input("Enter Username Now: ")
        f=open('Usernames and Passwords.dat','rb')
        f.seek(0,2)
        eof=f.tell()
        repeat=0
        f.seek(0,0)
        while f.tell()<eof:
            k=pickle.load(f)
            if k[0]==username:
                repeat=1
                print("This Username is already in use")
                break
        if repeat==1:
            print("You can either create account using new username or login using the same")
            true5=True
            while true5:
                w=input("1. Use New Username or 2. Try Logging In: ")
                if w=='1':
                    true=True
                    true5=False
                elif w=='2':
                    usernamepassword()
                    true5=False
                elif w not in '12':
                    print("Please enter '1' or '2' only")
                    true5=True
        elif repeat==0:
                

            j=len(username)
            uc=lc=di=sp1=sp=0
            if j>=8:

                for y in username:
                    if 'A'<=y<='Z':
                        uc+=1
                    elif 'a'<=y<='z':
                        lc+=1
                    elif '0'<=y<='9':
                        di+=1
                    elif y in '@_':
                        sp1+=1
                    else:
                        sp+=1

                if lc==0:
                    print('Please enter atleast one lowercase character (Check Rule No. 3)')
                    true=True
                elif uc==0:
                    print('Please enter atleast one Uppercase character (Check Rule No. 3)')
                    true=True
                elif di==0:
                    print('Please enter atleast one digit character (Check Rule No. 4)')
                    true=True
                elif sp>=1:
                    print('No special chacters except underscore(_) and at sign(@) are allowed (Check Rule No. 1)')
                else:
                    print('Your Username is Valid by above instructions')
                    validun=username
                    break
            else:
                print('Please Enter a Username longer than 8 characters (Check Rule No. 2)')
                true=True
    print()
    print('Now, you have to make a password')
    print()
    print('Please know that the password should not be shared with anyone else unless necessary.')
    print('Sorry for the boring part but even Password has some rules to be followed: ')
    print('1. The password should be atleast 8 characters long')
    print('2. The password should contain atleast 1 uppercase character, 1 lowercaase character, 1 digit, 1 special character')
    true1=True
    while true1:
        password=input('Enter Password Now: ')
        j=len(password)
        uc=lc=di=sp1=sp=0
        if j>=8:
            for y in password:
                if 'A'<=y<='Z':
                    uc+=1
                elif 'a'<=y<='z':
                    lc+=1
                elif '0'<=y<='9':
                    di+=1
                elif y in '@_':
                    sp1+=1
                else:
                    sp+=1
            if lc==0:
                print('Please enter atleast one lowercase character (Check Rule No. 2)')
                true1=True
            elif uc==0:
                print('Please enter atleast one Uppercase character (Check Rule No. 2)')
                true1=True
            elif di==0:
                print('Please enter atleast one digit character (Check Rule No. 2)')
                true1=True
            elif (sp+sp1)==0:
                print('Please enter atleast one special character (Check Rule No. 2)')
            else:
                print('Your Password is Valid')
                validpw=password
                break
        else:
            print('Please Enter a Password longer than 8 characters (Check Rule No. 1)')
            true1=True
    fa=open('Usernames and Passwords.dat','ab')
    fr=open('Usernames and Passwords.dat','rb')
    l=[validun,validpw,fname,lname]
    
    fr.seek(0,2)
    fr.seek(0,2)
    eof=fr.tell()
    fr.seek(0,0)
    while fr.tell()<eof:
        k=pickle.load(fr)
        if k!='':
            if k[0]==validun:
                print('This username already exists')
                print('Please try logging in instead')
                
    fr.close()
    pickle.dump(l,fa)
    fa.close()
    un=validun
    fg=open('List of Playlists'+'_'+un+'.dat','wb')
    fg.close
    j1='My Likes'+'_'+un+'.dat'
    j2='My Disikes'+'_'+un+'.dat'
    fh=open(j1,'wb')
    fh.close()
    fi=open(j2,'wb')
    fi.close()
    interface(un)

def title(s):
    sum1=''
    s1=s[1::]
    if s[-1]==' ':
        s1=s[1:-1:]
    t=ord(s[0])
    if t>=97 and t<=122:
        s1=chr(t-32)+s1
    else:
        s1=chr(t)+s1
    l=[]
    for x in s1:
        l.append(x)
    for j in range(1,len(l)):
        h=ord(l[j])
        if h>=65 and h<=90:
            l[j]=chr(h+32)
        else:
            l[j]=chr(h)
    for k in range(len(l)):
        if l[k]==' ' and l[k+1]!='':
            g=ord(l[k+1])
            if g>=97 and g<=122:
                l[k+1]=chr(g-32)
            else:
                l[k+1]=chr(g)
    for i in l:
        sum1+=i
    return sum1

def inputsongs(n):
    print()
    f=open('Mixed Moods 1.dat','rb')    
    f.seek(0,2)
    eof=f.tell()
    f.seek(0,0)
    c=0
    while f.tell()<eof:
        l=pickle.load(f)
        c+=1
    sr=c
    f.close()
    fw=open('Mixed Moods 1.dat','ab')
    for k in range(n):
        sr+=1
        sname=input("Enter Song Name: ")
        sname=title(sname)
        artist=input("Enter Artist Name: ")
        artist=title(artist)
        album=input("Enter Album Name: ")
        album=title(album)
        t1=True
        while t1:
            gen=int(input("Enter Number of Genre: "))
            if gen>0:
                t1=False
            elif gen<0:
                print('Please Enter A Positive Integer')
                t1=True
            elif gen==0:
                print("Please Enter Some Genre")
                t1=True
            
        genres=[]
        for h in range(gen):
            genre=input("Enter the Genre: ")
            genre=title(genre)
            genres.append(genre)
        print('Enter Language by Entering the Respective Numbers')
        language=''
        true5=True
        while true5:
            lang=input("English : 1,    Hindi : 2, Other : 3   :  ")            
            if lang=='1':
                language='English'
                true5=False
            elif lang=='2':
                language='Hindi'
                true5=False
            elif lang=='3':
                language=input("Enter Language: ")
                language=title(language)
                true5=False
            else:
                print('Please enter [1,2,3] only')
                true5=True           
            
        print("If you do not know the year, enter 0")
        true1=True
        while true1:
            year=int(input("Enter Year: "))
            if year<0 and year>2022:
                print('Please Enter A Valid Year before 2022')
                true1=True
            else:
                true1=False
        link=input("Enter Youtube Link for the Song: ")
        lsong=[sr,sname,artist,album,genres,language,year,link]
        pickle.dump(lsong,fw)
    fw.close()

def displaysongs(w1='Mixed Moods 1.dat'):
    print()
    fr=open(w1,'rb')
    fr.seek(0,2)
    eof=fr.tell()
    fr.seek(0,0)
    sr='Serial Number'
    name='Name'
    art='Artist'
    alb='Album'
    gen='Genre'
    lang='Language'
    yr='Year'
    print(f'{sr:20}\t{name:50}\t{art:30}\t\t{alb:50}\t{gen:62}\t{lang:20}\t{yr:4}')
    print()
    while fr.tell()<eof:
        k=pickle.load(fr)
        print(f'{k[0]:^20d}\t{k[1]:<50}\t{k[2]:<30}\t{k[3]:<50}\t{str(k[4]):<62}\t{k[5]:<20}\t{k[6]:<4d}')
        print()
    fr.close()



    
def searchsimrec(g,r3='Mixed Moods 1.dat',e=1):
    fr=open(r3,'rb')
    print('Were You Looking For: ')
    l1=[]
    recs=[]
    for t in g:
        t1=''
        if t==' ':
            pass
        else:
            l1.append(t.upper())
    fr.seek(0,2)
    eof=fr.tell()
    fr.seek(0,0)
    while fr.tell()<eof:
        k=pickle.load(fr)
        rec=[]
        l2=[]
        for m in k[e]:
            m1=''
            if m==' ':
                pass
            else:
                l2.append(m.upper())
        n1=len(l1)
        n2=len(l2)
        q1=0
        for r in range(n1):
            if l1[r] in l2:
                q1+=1
        rec=[k[0],k[e],(q1)]
        recs+=[rec]
    n=len(recs)
    for x in range(1,n):
        for k1 in range(n-x):
            if recs[k1][2]<recs[k1+1][2]:
                recs[k1],recs[k1+1]=recs[k1+1],recs[k1]
    d=5
    if len(recs)<5:
        d=2
    for w in range(d):
        print(recs[w][0],recs[w][1])
    fr.close()
    fr2=open(r3,'rb')
    print("Enter 0 if you cannot find the song here to retry the function")
    t1=int(input("Enter Serial Number if you want to find that Title: "))
    
    print()
    fr2.seek(0,2)
    eof=fr2.tell()
    fr2.seek(0,0)
    while fr2.tell()<eof:
        l=pickle.load(fr2)
        if t1==l[0]:
            print(l[0],l[1],l[2],l[3],l[4],l[5],l[6],sep='\t')
            print()
            break
    fr2.close()

def searchsimreclinks(g,r3='Mixed Moods 1.dat'):
    fr=open(r3,'rb')
    print('Were You Looking For: ')
    l1=[]
    recs=[]
    for t in g:
        t1=''
        if t==' ':
            pass
        else:
            l1.append(t.upper())
    fr.seek(0,2)
    eof=fr.tell()
    fr.seek(0,0)
    while fr.tell()<eof:
        k=pickle.load(fr)
        rec=[]
        l2=[]
        for m in k[1]:
            m1=''
            if m==' ':
                pass
            else:
                l2.append(m.upper())
        n1=len(l1)
        n2=len(l2)
        q1=0
        for r in range(n1):
            if l1[r] in l2:
                q1+=1
        rec=[k[0],k[1],(q1)]
        recs+=[rec]
    n=len(recs)
    for x in range(1,n):
        for k1 in range(n-x):
            if recs[k1][2]<recs[k1+1][2]:
                recs[k1],recs[k1+1]=recs[k1+1],recs[k1]
    d=5
    if len(recs)<5:
        d=len(recs)
    for w in range(d):
        print(recs[w][0],recs[w][1])
    fr.close()
    fr2=open(r3,'rb')
    print("Enter 0 if you cannot find the song here to retry the function")
    t1=int(input("Enter Serial Number if you want to find that Title: "))
    print()
    fr2.seek(0,2)
    eof=fr2.tell()
    fr2.seek(0,0)
    while fr2.tell()<eof:
        l=pickle.load(fr2)
        if t1==l[0]:
            webbrowser.open(l[7])
            break
    fr2.close()

def  searchsongsbyname(j):
    print()
    fr=open('Mixed Moods 1.dat','rb')
    fr.seek(0,2)
    eof=fr.tell()
    fr.seek(0,0)
    f=0
    while fr.tell()<eof:
        k=pickle.load(fr)
        if k[1]==j: 
            print(k[0],k[1],k[2],k[3],k[4],k[5],k[6],sep='\t')
            f=1

    if f==0:
        searchsimrec(j)
    fr.close()

def  searchsongsbyalbum(j):
    print()
    fr=open('Mixed Moods 1.dat','rb')
    fr.seek(0,2)
    eof=fr.tell()
    fr.seek(0,0)
    f=0
    while fr.tell()<eof:
        k=pickle.load(fr)
        if k[3]==title(j): 
            print(k[0],k[1],k[2],k[3],k[4],k[5],k[6],sep='\t')
            print()
            f=1
    if f==0:
        searchsimrec(j,e=3)
    fr.close()


def searchsongbysrno(j):
    print()
    fr=open('Mixed Moods 1.dat','rb')
    fr.seek(0,2)
    eof=fr.tell()
    fr.seek(0,0)
    f=0
    while fr.tell()<eof:
        k=pickle.load(fr)
        if k[0]==j:
            print(k[0],k[1],k[2],k[3],k[4],k[5],k[6],sep='\t')
            print()
            f=1
    if f==0:
        print('Sorry, Song Serial Number Not Found')
    fr.close()
    

def searchsongsbyyear(y):
    print()
    fr=open('Mixed Moods 1.dat','rb')
    fr.seek(0,2)
    eof=fr.tell()
    f=0
    fr.seek(0,0)
    while fr.tell()<eof:
        k=pickle.load(fr)
        if k[6]==y:
            print(k[0],k[1],k[2],k[3],k[4],k[5],k[6],sep='\t')
            print()
            f=1
    if f==0:
        print("No songs of this year found")


def playsongs(w1='Mixed Moods 1.dat'):
    print()
    fr2=open(w1,'rb')
    c=[]
    fr2.seek(0,2)
    eof=fr2.tell()
    fr2.seek(0,0)
    while fr2.tell()<eof:
        k=pickle.load(fr2)
        c.append(k[0])
    fr2.close()
    fr=open(w1,'rb')
    fr.seek(0,2)
    eof=fr.tell()
    fr.seek(0,0)
    print('You can select song by Name or Serial Number')
    displaysongs(w1)
    t1=True
    while t1:
        try:
            choice=int(input("Enter 1 for Name and Enter 2 for Serial Number: "))
            if choice==1:
                j=input("Enter Song Name: ")
                j=title(j)
                f=0
                while fr.tell()<eof:
                    k=pickle.load(fr)
                    if k[1]==title(j):
                        webbrowser.open(k[7])
                        f=1
                        break
                if f==0:
                    searchsimreclinks(j,w1)
                t1=False
            if choice==2:
                t1=False
                t2=True
                while t2:
                    try:
                        r=int(input("Enter Serial Number: "))
                        if r<0:
                                print('Please Enter Value from the provided Serial Numbers. There are no negative Serial Numbers')
                                t2=True  
                        fr3=open(w1,'rb')
                        fr3.seek(0,2)
                        eof=fr3.tell()
                        fr3.seek(0,0)
                        while fr3.tell()<eof:
                            k=pickle.load(fr3)
                            if k[0]==r:
                                webbrowser.open(k[7])
                                t2=False
                                break
                    except ValueError:
                        print("Enter Numeric Value Please")
                        t2=True
            elif choice not in [1,2]:
                print('Dear User,',un,', Please Enter the values "1" or "2" only for the respective need')
                t1=True
        except ValueError:
            print("Enter Numeric Value [1,2] only")
            t1=True
    fr.close()

def createplaylistbygenre(un):
    o='List of Playlists'+'_'+un+'.dat'
    fr=open('Mixed Moods 1.dat','rb')
    cp=input("Enter Name for New Playlist: ")
    gen=input('Enter Genre For New Playlist: ')
    fa=open(o,'ab')
    pickle.dump(cp,fa)
    fa.close()
    l=[]
    fr.seek(0,2)
    eof=fr.tell()
    fr.seek(0,0)
    while fr.tell()<eof:
        k=pickle.load(fr)
        if gen in k[4]:
            t=[k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7]]
            l+=[t]
    fw=open(cp+'_'+un+'.dat','ab')
    for h in l:
        pickle.dump(h,fw)
    fw.close()
    

def createcustomplaylists(un):
    o='List of Playlists'+'_'+un+'.dat'
    fr=open('Mixed Moods 1.dat','rb')
    cp=input("Enter Name for New Playlist: ")
    fa=open(o,'ab')
    pickle.dump(cp,fa)
    fa.close()
    displaysongs()
    t1=True
    while t1:
        try:
            r=int(input("How many songs do you want to choose: "))
            t1=False
        except ValueError:
            print("Please Enter Numeric Value")
            t1=True
    l=[]
    for w in range(r):
        try:
            e=int(input("Enter Serial Number of the Song: "))
            fr.seek(0,2)
            eof=fr.tell()
            fr.seek(0,0)
            while fr.tell()<eof:
                k=pickle.load(fr)
                if k[0]==e:
                    l.append(k)
        except ValueError:
            print('Oh you did not enter appropriate numeric value')
            print('Your turn to enter song for this time hence did not work')
    fr.close()
    fw=open(cp+'_'+un+'.dat','ab')
    for h in l:
        pickle.dump(h,fw)
    fw.close()
        
            
def displayplaylists(un):
    o='List of Playlists'+'_'+un+'.dat'
    fg=open(o,'rb')
    fg.seek(0,0)
    tell1=fg.tell()
    fg.seek(0,2)
    tell2=fg.tell()
    if tell1==tell2:
        print('Seems like you have not made any playlists yet.')
        print('Use The Menu Option No. 5 or Option No. 6 for the same')
    fr=open(o,'rb')
    pl=[]
    fr.seek(0,2)
    eof=fr.tell()
    fr.seek(0,0)
    c=0
    t=0
    while fr.tell()<eof:
        k=pickle.load(fr)
        c+=1
        t=[c,k]
        pl+=[t]
        print(c,'. ',k,sep='')
    i=c
    true1=True
    while true1:
        try:
            choose=int(input("Enter Serial Number of the Playlist: "))
            for q in pl:
                if q[0]==choose:
                    j=q[1]+'_'+un+'.dat'
                    displaysongs(j)
                    true1=False
            if choose not in range(1,i+1):
                print('Please Enter the Serial Number from the given list')
                true1=True
        except ValueError:
            print("Please Enter Numeric Value")
            true1=True
    print('Do you want to play any song from it?')
    true3=True
    while true3:
        try:
            choice1=int(input("Enter 1 for 'Yes' and Enter 2 for 'No': "))
            if choice1==1:
                print('You can select song by Name or Serial Number')
                true1=True
                while true1:
                    try:
                        choice=int(input("Enter 1 for Name and Enter 2 for Serial Number: "))
                        if choice==1:
                            j1=input("Enter Song Name: ")
                            j1=title(j1)
                            f=0
                            frp1=open(j,'rb')
                            frp1.seek(0,2)
                            eof=frp1.tell()
                            frp1.seek(0,0)
                            while frp1.tell()<eof:
                                k=pickle.load(frp1)
                                if k[1]==title(j1):
                                    webbrowser.open(k[7])
                                    f=1
                                    true1=False
                                    true3=False
                                    break
                            if f==0:
                                r2=j
                                searchsimreclinks(j1,r2)
                                true1=False
                                true3=False
                        elif choice==2:
                                true1=False
                                true2=True
                                while true2:
                                    r=int(input("Enter Serial Number: "))
                                    if r<0:
                                            print('Please Enter Value from the provided Serial Numbers. There are no negative Serial Numbers')
                                            true2=True
                                    fr3=open(j,'rb')
                                    fr3.seek(0,2)
                                    eof=fr3.tell()
                                    fr3.seek(0,0)
                                    while fr3.tell()<eof:
                                        k=pickle.load(fr3)
                                        if k[0]==r:
                                            webbrowser.open(k[7])
                                            true1=False
                                            true2=False
                                            true3=False
                                            break
                        elif choice not in [1,2]:
                                print('Dear User,',un,', Please Enter the values "1" or "2" only for the respective need')
                                true1=True
                        elif choice not in [1,2]:
                            print('Please Enter "1" or "2" for the respective need')
                            true1=True
                    except ValueError:
                        print('Please Enter Numeric Values')
                        true1=True
            elif choice1==2:
                    print("Thank you, Have a Nice Day")
                    true3=False
            elif choice1 not in [1,2]:
                    print("Please Enter '1' for 'Yes' or '2' for 'No'")
                    true3=True
        except ValueError:
            print('Please Enter Numeric Values')
            true3=True
    fr.close()
    
    
                    
    

                    
def likesdislikes(un):
    fr=open('Mixed Moods 1.dat','rb')
    j1='My Likes'+'_'+un+'.dat'
    j2='My Disikes'+'_'+un+'.dat'
    fl=open(j1,'ab')
    fd=open(j2,'ab')
    found=0
    displaysongs()
    print('You Can Select Song by Serial Number or Name: ')
    true1=True
    while true1:
        try:
            h=int(input("Serial Number : 1, Name: 2:   "))
            fr.seek(0,2)
            eof=fr.tell()
            fr.seek(0,0)
            nl=[]
            while fr.tell()<eof:
                k=pickle.load(fr)
                nl+=[k]
            if h==1:
                true2=True
                while true2:
                    try:
                        j=int(input("Enter the Song's Serial Number: "))
                        for k in nl:
                            if k[0]==j:
                                print("You have selected this song")
                                print(k[0],k[1],k[2],k[3],k[4],k[5],k[6])
                                print("Do You Like this Song or Dislike this Song")
                                g=int(input("Like : 1, Dislike : 2:     "))
                                if g==1:
                                    t=[k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7]]
                                    pickle.dump(t,fl)
                                    print('Song Added to My Likes')
                                elif g==2:
                                    t=[k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7]]
                                    pickle.dump(t,fd)
                                    print('Songs Added to My Dislikes')
                        true1=False
                        true2=False
                    except ValueError:
                         print('Please Enter Numeric Value')
                         true2=True
            if h==2:
                j=input("Enter Song Name: ")
                j=title(j)
                for k in nl:
                    if k[1]==j:
                        found=1
                        print("You have selected this song")
                        print(k[0],k[1],k[2],k[3],k[4],k[5],k[6])
                        print("Do You Like this Song or Dislike this Song")
                        g=int(input("Like : 1, Dislike : 2:      "))
                        if g==1:
                            t=[k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7]]
                            pickle.dump(t,fl)
                            print('Song Added to My Likes')
                        elif g==2:
                            t=[k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7]]
                            pickle.dump(t,fd)
                            print('Songs Added to My Dislikes')
                if found==0:
                    print("Song Not Found")
                true1=False
                true2=False
        except ValueError:
            print('Please Enter Numeric Value')
            true1=True

def readlikes(un):    
    j='My Likes'+'_'+un+'.dat'
    fg=open(j,'rb')
    fg.seek(0,0)
    tell1=fg.tell()
    fg.seek(0,2)
    tell2=fg.tell()
    if tell1==tell2:    
        print('Seems like you have not liked any songs yet.')
        print('Use The Menu Option No. 8 for the same')
    else:
        displaysongs(j)
        print('Do you want to play any song from it?')
        true3=True
        while true3:
            try:
                choice1=int(input("Enter 1 for 'Yes' and Enter 2 for 'No': "))
                if choice1==1:
                    print('You can select song by Name or Serial Number')
                    true1=True
                    while true1:
                        try:
                            choice=int(input("Enter 1 for Name and Enter 2 for Serial Number: "))
                            if choice==1:
                                j1=input("Enter Song Name: ")
                                j1=title(j1)
                                f=0
                                frp1=open(j,'rb')
                                frp1.seek(0,2)
                                eof=frp1.tell()
                                frp1.seek(0,0)
                                while frp1.tell()<eof:
                                    k=pickle.load(frp1)
                                    if k[1]==title(j1):
                                        webbrowser.open(k[7])
                                        f=1
                                        true1=False
                                        true3=False
                                        break
                                    if f==0:
                                        r2=j
                                        searchsimreclinks(j1,r2)
                                        true1=False
                                        true3=False
                            elif choice==2:
                                    true1=False
                                    true2=True
                                    while true2:
                                        r=int(input("Enter Serial Number: "))
                                        if r<0:
                                                print('Please Enter Value from the provided Serial Numbers. There are no negative Serial Numbers')
                                                true2=True
                                        '''elif r>0:
                                            print('Please Enter Value from the provided Serial Numbers. There is no Serial Number,',r,'in this Public Music Database')
                                            true2=True'''
                                        fr3=open(j,'rb')
                                        fr3.seek(0,2)
                                        eof=fr3.tell()
                                        fr3.seek(0,0)
                                        while fr3.tell()<eof:
                                            k=pickle.load(fr3)
                                            if k[0]==r:
                                                webbrowser.open(k[7])
                                                true2=False
                                                true3=False
                                                break
                            elif choice not in [1,2]:
                                    print('Dear User,',un,', Please Enter the values "1" or "2" only for the respective need')
                                    true1=True
                            elif choice not in [1,2]:
                                print('Please Enter "1" or "2" for the respective need')
                                true1=True
                        except ValueError:
                            print('Please Enter Numeric Value')
                elif choice1==2:
                        print("Thank you, Have a Nice Day")
                        true3=False
                elif choice1 not in [1,2]:
                        print("Please Enter '1' for 'Yes' or '2' for 'No'")
                        true3=True
            except ValueError:
                print('Please Enter Numeric Value')
                true3=True



def filelistofartists():
    fr=open('Mixed Moods 1.dat','rb')
    fr.seek(0,2)
    eof=fr.tell()
    fr.seek(0,0)
    al=[]
    while fr.tell()<eof:
        k=pickle.load(fr)
        al.append(k[2])
    for f in al:
        t=al.count(f)
        while t>1:
            al.remove(f)
            t-=1               
                
    n=len(al)
    for x in range(1,n):
        for k in range(n-x):
            if al[k]>al[k+1]:
                al[k],al[k+1]=al[k+1],al[k]
            
    fa=open('Artist.dat','wb')
    c=0
    AL=[]
    for s in al:
        c+=1
        AL+=[[c,s]]
        
    for h in AL:
        pickle.dump(h,fa)

def artiststations():
    filelistofartists()
    g=''
    Artistlist=[]
    print("Welcome to Artist Stations")
    print()
    ch=input("Press Enter to view the list of Artists: ")
    if ch=='':
        frp2=open('Artist.dat','rb')
        frp2.seek(0,2)
        eof=frp2.tell()
        frp2.seek(0,0)
        c=0
        while frp2.tell()<eof:
            c+=1
            k=pickle.load(frp2)
            print(k[0],'.',' ',k[1])
            print()
    print("Would You Like to Play or View one of the Artist's Music?")
    true1=True
    while true1:
        try:
            ch1=int(input('Enter "1" for "Yes" and "2" for "No": '))
            if ch1==1:
                print("You can select the artist using the respective serial number")
                true2=True
                while true2:
                    try:
                        ch2=int(input("Enter the Serial Number: "))
                        if ch2<0:
                            print("Serial Numbers are not negative, Please enter again.")
                            true2=True
                        frp1=open('Mixed Moods 1.dat','rb')
                        frp4=open('Artist.dat','rb')
                        frp4.seek(0,2)
                        eof=frp4.tell()
                        frp4.seek(0,0)
                        while frp4.tell()<eof:
                            k2=pickle.load(frp4)
                            if k2[0]==ch2:
                                g=k2[1]
                        frp1.seek(0,2)
                        eof=frp1.tell()
                        frp1.seek(0,0)
                        while frp1.tell()<eof:
                            k3=pickle.load(frp1)
                            if k3[2]==g:
                                Artistlist.append(k3)
                        gf=g+'_'+un+'.dat'
                        frp5=open(gf,'wb')
                        for h in Artistlist:
                            pickle.dump(h,frp5)
                        frp5.close()
                        true1=False
                        true2=False
                        playsongs(gf)
                    except ValueError:
                        print("Please Enter Numeric Value")
                        true2=True
            elif ch1==2:
                print("Thank you, Have a Nice Day")
                true1=False
            elif ch1 not in [1,2]:
                print("Please Enter '1' for 'Yes' or '2' for 'No' only as needed")
                true1=True
        except ValueError:
            print("Please Enter Numeric Value")
            true1=True



def modify(f1='Mixed Moods 1.dat'):
    print("Welcome, You can modify the songs details here: ")
    print('The basis for identification for modification can be the following: ')
    print('By Serial Number: Enter "1"')
    print('By Name: Enter "2"')
    choice1=int(input("Enter your choice for identification for modification: "))
    choice2=input("Enter Yes or Y if you want to view all the song's details before modifying, otherwise Enter anything else: ")
    if choice2.lower()=='yes' or choice2.lower()=='y':
        displaysongs(f1)
    else:
        pass
    fr1=open(f1,'rb')
    fr1.seek(0,2)
    eof=fr1.tell()
    fr1.seek(0,0)
    found1=0
    found2=0
    songlist=[]
    true1=True
    while true1:
        try:
            if choice1==1:
                serial=int(input("Enter Serial Number: "))
                while fr1.tell()<eof:
                    k1=pickle.load(fr1)
                    if serial==k1[0]:
                        found1=1
                        print('So what do you want to change? ')
                        print('1. Change Artist Name')
                        print('2. Change Album Name')
                        print('3. Change Genres')
                        print('4. Change Language')
                        print('5. Change Year of Release')
                        print('6. Change Youtube Link for the song')
                        true4=True
                        while true4:
                            choice3=input("Enter Operation Choice [1-6]: ")
                            if choice3=='1':
                                newartist=input("Enter New Artist Name: ")
                                k1[2]=title(newartist)
                                true4=False
                            elif choice3=='2':
                                newalbum=input("Enter New Album Name: ")
                                k1[3]=title(newalbum)
                                true4=False
                            elif choice3=='3':
                                newgenre=[]
                                ng=int(input("Enter No. of Genres you want for this song: "))
                                for k in range(ng):
                                    g=input("Enter Genre: ")
                                    newgenre.append(title(g))
                                k1[4]=newgenre
                                true4=False
                            elif choice3=='4':
                                newlang=input("Enter New Language: ")
                                k1[5]=title(newlang)
                                true4=False
                            elif choice3=='5':
                                newyear=int(input("Enter New Year of Release: "))
                                k1[6]=newyear
                                true4=False
                            elif choice3=='6':
                                newlink=input("Enter New Link for the Song (It can also be a link for any subscription service which might work if you have already signed in to your account): ")
                                k1[7]=newlink
                                true4=False
                            elif choice3=='7':
                                newname=input("enter name: ")
                                k1[1]=title(newname)
                                true4=False
                            else:
                                print('Please Enter Proper Choice [1-7]: ')
                                true4=True
                    songlist+=[k1]
                if found1==0:
                    print("Serial Number Not Found")
                fr1.close()
                fr2=open(f1,'wb')
                for song in songlist:
                    pickle.dump(song,fr2)
                fr2.close()
                true1=False
                
                
                
            
            elif choice1==2:
                name=input("Enter Song Name: ")
                name=title(name)
                while fr1.tell()<eof:
                    k2=pickle.load(fr1)
                    if name==k2[1]:
                        found2=1
                        print('So what do you want to change? ')
                        print('1. Change Artist Name')
                        print('2. Change Album Name')
                        print('3. Change Genres')
                        print('4. Change Language')
                        print('5. Change Year of Release')
                        print('6. Change Youtube Link for the song')
                        true4=True
                        while true4:
                            choice3=input("Enter Operation Choice [1-6]: ")
                            if choice3=='1':
                                newartist=input("Enter New Artist Name: ")
                                k2[2]=newartist
                                true4=False
                            elif choice3=='2':
                                newalbum=input("Enter New Album Name: ")
                                k2[3]=newalbum
                                true4=False
                            elif choice3=='3':
                                newgenre=[]
                                ng=int(input("Enter No. of Genres you want for this song: "))
                                for k in range(ng):
                                    g=input("Enter Genre: ")
                                    newgenre.append(g)
                                k2[4]=newgenre
                                true4=False
                            elif choice3=='4':
                                newlang=input("Enter New Language: ")
                                k2[5]=newlang
                                true4=False
                            elif choice3=='5':
                                newyear=int(input("Enter New Year of Release: "))
                                k2[6]=newyear
                                true4=False
                            elif choice3=='6':
                                newlink=input("Enter New Link for the Song (It can also be a link for any subscription service which might work if you have already signed in to your account): ")
                                k2[7]=newlink
                                true4=False
                            else:
                                print('Please Enter Proper Choice [1-6]: ')
                                true4=True
                    songlist+=[k2]
                if found2==0:
                    print('Song Not Found, Spelling might be incorrect')
                    print('Please Try Again')
                
                fr1.close()
                fr2=open(f1,'wb')
                for song in songlist:
                    pickle.dump(song,fr2)
                fr2.close()
                true1=False
            elif choice1 not in [1,2]:
                    print("Please Enter '1' for Serial Number or '2' for Name")
                    true1=True
        except ValueError:
            print("Please Enter Numeric Value")
            

def deletesong(f1='Mixed Moods 1.dat'):
    print('Welcome')
    print("You can delete record of some specific song")
    print('The basis for identification for modification can be the following: ')
    print('By Serial Number: Enter "1"')
    print('By Name: Enter "2"')
    choice1=int(input("Enter your choice for identification for deletion: "))
    choice2=input("Enter Yes or Y if you want to view all the song's details before deleting, otherwise Enter anything else: ")
    if choice2.lower()=='yes' or choice2.lower()=='y':
        displaysongs(f1)
    else:
        pass
    fr1=open(f1,'rb')
    fr1.seek(0,2)
    eof=fr1.tell()
    fr1.seek(0,0)
    found1=0
    found2=0
    songlist=[]
    true1=True
    while true1:
        try:
            if choice1==1:
                serial=int(input("Enter Serial Number: "))
                while fr1.tell()<eof:
                    k1=pickle.load(fr1)
                    if serial==k1[0]:
                        found1=0
                    else:
                        songlist+=[k1]
                fr1.close()
                fr2=open(f1,'wb')
                for song in songlist:
                    pickle.dump(song,fr2)
                fr2.close
                true1=False
            elif choice1==2:
                name=input("Enter Song Name: ")
                name=title(name)
                while fr1.tell()<eof:
                    k2=pickle.load(fr1)
                    if name==k2[1]:
                        found2=0
                    else:
                        songlist+=[song]
                fr1.close()
                if found2==0:
                    print('Song Not Found, Spelling might be incorrect')
                    print('Please Try Again')
                fr2=open(f1,'wb')
                for song in songlist:
                    pickle.dump(song,fr2)
                fr2.close
                
                true1=False
            elif choice1 not in [1,2]:
                print("Please Enter '1' for Serial Number or '2' for Name")
                true1=True
        except ValueError:
            print("Please Enter Numeric Value")
            true1=True
            
def modifyplaylist():
    o='List of Playlists'+'_'+un+'.dat'
    fg=open(o,'rb')
    fg.seek(0,0)
    tell1=fg.tell()
    fg.seek(0,2)
    tell2=fg.tell()
    found=0
    if tell1==tell2:
        print('Seems like you have not made any playlists yet.')
        print('Use The Menu Option No. 5 or Option No. 6 for the same')
    fr=open(o,'rb')
    pl=[]
    fr.seek(0,2)
    eof=fr.tell()
    fr.seek(0,0)
    c=0
    t=0
    while fr.tell()<eof:
        k=pickle.load(fr)
        c+=1
        t=[c,k]
        pl+=[t]
        print(c,'. ',k,sep='')
    i=c
    true1=True
    while true1:
        try:
            choose=int(input("Enter Serial Number of the Playlist: "))
            if choose>c or choose<0:
                print("Enter Valid Playlist Serial Number")
                
            for q in pl:
                if q[0]==choose:
                    found=1
                    j=q[1]+'_'+un+'.dat'
                    true1=False
            if found==0:
                print("Playlist Serial Number Not Found")
                true1=True
        except ValueError:
            print("Please Enter Numeric Value")
            true1=True
    modify(j)
    
    
def deletesongplaylist():
    o='List of Playlists'+'_'+un+'.dat'
    fg=open(o,'rb')
    fg.seek(0,0)
    tell1=fg.tell()
    fg.seek(0,2)
    tell2=fg.tell()
    if tell1==tell2:
        print('Seems like you have not made any playlists yet.')
        print('Use The Menu Option No. 5 or Option No. 6 for the same')
    fr=open(o,'rb')
    pl=[]
    fr.seek(0,2)
    eof=fr.tell()
    fr.seek(0,0)
    c=0
    t=0
    while fr.tell()<eof:
        k=pickle.load(fr)
        c+=1
        t=[c,k]
        pl+=[t]
        print(c,'. ',k,sep='')
    i=c
    true1=True
    while true1:
        try:
            choose=int(input("Enter Serial Number of the Playlist: "))
            if choose>c or choose<0:
                print("Enter Valid Playlist Serial Number")
                
            for q in pl:
                if q[0]==choose:
                    found=1
                    j=q[1]+'_'+un+'.dat'
                    true1=False
            if found==0:
                print("Playlist Serial Number Not Found")
                true1=True
        except ValueError:
            print("Please Enter Numeric Value")
            true1=True
            
    deletesong(j)


def filterbylanguage(f1='Mixed Moods 1.dat'):
    print()
    lang=''
    print("You can filter songs by Language")
    print("Select Language: ")
    print("1. English")
    print("2. Hindi")
    print("3. Other")
    true1=True
    while true1:
        choice=input("Enter your language choice: ")
        if choice=='1':
            lang='English'
            true1=False
        elif choice=='2':
            lang='Hindi'
            true1=False
        elif choice=='3':
            lang=input("Type the language name: ")
            lang=title(lang)
            true1=False
        elif choice not in '123':
            print('Please Enter "1", "2" or "3" only')
            true1=True
    fr1=open(f1,'rb')
    fr1.seek(0,2)
    eof=fr1.tell()
    found=0
    fr1.seek(0,0)
    while fr1.tell()<eof:
        k=pickle.load(fr1)
        if k[5]==lang:
            found=1
            print(k[0],k[1],k[2],k[3],k[4],k[5],k[6],sep='\t')
            print()
    if found==0:
        print("Language Not Found")
        print("Please Try Again")
        true1=True


    
            
            
    





                    
def interface(un):
    print()
    print()
    print('Hello There, so what do you wanna do?')
    print()
    while True:
        print()
        print()
        print('MENU')
        print()
        print('1. Check out the List of All the Songs')
        print('2. Input Songs into the List of All the Songs')
        print('3. Search Songs')
        print('4. Play Songs from the List of All the Songs')
        print('5. Create a Playlist by Genre')
        print('6. Create Custom Playlist')
        print('7. Display all the Playlists Made')
        print('8. Like or Dislike a Song')
        print('9. Check the list of Likes')
        print('10. Check out Artist Stations')
        print('11. Filter Songs by Year')
        print('12. Search by Albums')
        print('13. Modify')
        print('14. Delete Song')
        print('15. Modify Song in a playlist')
        print('16. Delete Song in a playlist')
        print('17. Filter by Language')
        print('0. Exit and Update')
        print()
        choice=input("Enter your choice of operation [0-17]: ")
        if choice=='1':
            displaysongs()
        if choice=='2':
            true6=True
            while true6:
                try:
                    n=int(input("Enter No. of Inputs you want to do: "))
                    inputsongs(n)
                    true6=False
                except ValueError:
                    print("Please Enter Numeric Value")
                    true6=True
                
        if choice=='3':
            print('How would you like to search songs from the List of All Songs')
            print('1. By Name')
            print('2. By Number')
            true2=True
            while true2:
                choose=input("Choose [1,2]: ")
                if choose=='1':
                    j=input("Enter Name of the Song: ")
                    j=title(j)
                    searchsongsbyname(j)
                    break
                elif choose=='2':
                    j2=int(input('Enter Serial Number of the Song: '))
                    searchsongbysrno(j2)
                    break
                else:
                    true2=True
        if choice=='4':
            playsongs()

        if choice=='5':
            createplaylistbygenre(un)

        if choice=='6':
            createcustomplaylists(un)

        if choice=='7':
            displayplaylists(un)

        if choice=='8':
            likesdislikes(un)
            
        if choice=='9':
            readlikes(un)

        if choice=='10':
            filelistofartists()
            artiststations()

        if choice=='11':
            y=int(input("Enter Year to Filter Out the Songs: "))
            searchsongsbyyear(y)
            
        if choice=='12':
            j=input("Enter Album Name: ")
            searchsongsbyalbum(j)
            
        if choice=='13':
            modify()
            
        if choice=='14':
            deletesong()
            
        if choice=='15':
            modifyplaylist()
            
        if choice=='16':
            deletesongplaylist()

        if choice=='17':
            filterbylanguage()
            
        if choice=='0':
            filelistofartists()
            print('Thank you',un)
            print("Please return soon to enjoy more music")
            print("Have A Nice Day")
            break
        
                
            


    


    

    
    
    
welcome()

    
            
            

    
        



          


    
                
        
    

    
