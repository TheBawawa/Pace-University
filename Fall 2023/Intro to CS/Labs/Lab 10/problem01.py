#a) - name[1]
#   - name[1:len(name):-8]
#   - name[0:5]

#b) - name[0].upper +  name[1:4]
#   - name[5].upper + name[6:len(name)]

#c) - S[0:len(S):2]
#   - s.slice(0,4) + s.slice(9, 12)

#d) - place[-7::]
#   - print(place[::-1])