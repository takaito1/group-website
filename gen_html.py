fn='ODImages/fn.txt'
f=open(fn,'r')
txt1='        <article class="col-sm-4">' 
txt3=['          <a href="ODImages/','">','</a></p>']
txt4=['          <img class="mx-auto" src="ODImages/','">']
txt5='        </article>'



for d in f:
   print(txt1)
   dd=d.replace("\n","")
   print(txt3[0]+dd+txt3[1]+dd+txt3[2])
   print(txt4[0]+dd+txt4[1])
   print(txt5+"\n")

