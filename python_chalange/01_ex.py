from string import ascii_lowercase
# Zadanie 1
a = 2 ** 38
print(a)
# Zadanie 2
# abcdefghijklmnopqrstuvwxyz
# yzabcdefghijklmnopqrstuvwx
shift = 2
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
shifted_ascii = "yzabcdefghijklmnopqrstuvwx"
text = 'map'
out = ""
for l in text:
    if l in ascii_lowercase:
        i = shifted_ascii.index(l)
        out += ascii_lowercase[i]
    else:
        out += l
print(out)
