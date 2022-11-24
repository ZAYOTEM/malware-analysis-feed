import sys
my_dict = {"i":'l',"9":'p',"o":'6',"c":'b',"L":"N","-":"H","u":'U',"E":'G',"V":'b',"a":'D',"f":'x'
,"p":'.',"G":'1',"H":"k","Z":'y',"e":'j',"n":'g',"I":'h',"y":'0',"3":'-',"h":'2',"O":'4',"t":'9',
"7":'q',"N":'3',"k":'z',"C":'a',"X":'i',"w":'k',"l":'m',"2":"v","s":'p',"r":'R',"Q":'u',"R":'n',
"P":'C',"Q":'u',"0":'r',"d":'e',"5":'t',"z":'V',"6":'s',"4":'i',"W":'o',"U":'W',"S":'d',"g":'w',
"F":'M',"Y":'c',"8":'f',"M":'S',"T":'O',"_":'F',"q":'T',"r":'R',"D":'A',"j":'E',".":"."}

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
  
for line in lines:
    text = ""
    for i in line:
        try:
            text=text+my_dict[i]
        except KeyError:
            text=text
    text_file = open("cozum.txt", "a")
    text_file.writelines (text +" === "+ line)
text_file.close()

