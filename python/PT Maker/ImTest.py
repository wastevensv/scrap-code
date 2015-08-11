from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from periodic.table import element
#elements= [H , He , Li , Be , B , C , N , O , F , Ne , Na , Mg , Al , Si , P , S , Cl , Ar , K , Ca , Sc , Ti , V , Cr , Mn , Fe , Co , Ni , Cu , Zn , Ga , Ge , As , Se , Br , Kr , Rb , Sr , Y , Zr , Nb , Mo , Tc , Ru , Rh , Pd , Ag , Cd , In , Sn , Sb , Te , I , Xe , Cs , Ba , La , Ce , Pr , Nd , Pm , Sm , Eu , Gd , Tb , Dy , Ho , Er , Tm , Yb , Lu , Hf , Ta , W , Re , Os , Ir , Pt , Au , Hg , Tl , Pb , Bi , Po , At , Rn , Fr , Ra , Ac , Th , Pa , U , Np , Pu , Am , Cm , Bk , Cf , Es , Fm , Md , No , Lr , Rf , Db , Sg , Bh , Hs , Mt , Ds , Rg , Cn , Uut , Uuq , Uup , Uuh , Uus , Uuo]
atomicrad=[37, 32, 134, 90, 82, 77, 75, 73, 71, 69, 154, 130, 118, 111, 106, 102, 99, 97, 196, 174, 144, 136, 125, 127, 139, 125, 126, 121, 138, 131, 126, 122, 119, 116, 114, 110, 211, 192, 162, 148, 137, 145, 156, 126, 135, 131, 153, 148, 144, 141, 138, 135, 133, 130, 225, 198, 169, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0160, 150, 138, 146, 159, 128, 137, 128, 144, 149, 148, 147, 146, 0, 0, 145, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

font = ImageFont.truetype("sans-serif.ttf", 96)
bigfont = ImageFont.truetype("sans-serif.ttf", 192)

for an in range(1,117):
    el = element(an).symbol
    ar = atomicrad[an]
    print an, el, ar
    
    if(ar == 0):
        img=Image.open("radioactive.png")
    else:
        img=Image.new("RGBA", (480,480),"white")
    draw = ImageDraw.Draw(img)
    draw.ellipse((240-ar,240-ar,240+ar,240+ar), fill = (255,255-ar,255-ar))
    
    w, h = draw.textsize(el, font=bigfont)
    draw.text((240-(w/2),96),str(an),"black",font=font)
    draw.text((240-(w/2),192),el,"black",font=bigfont)
    
    img.save(str(an)+"_"+el+".png")