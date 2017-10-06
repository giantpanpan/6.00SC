digits_before="011111101111110"
digits=list(digits_before)
digits=[int(i) for i in digits]


def bitfitting(Digits):
    j=0
    k=0
    for i in range(len(Digits)):

        if Digits[i]==1:
            j+=1
            if j==6:
                Digits=Digits[:i]+[0]+Digits[i:]
                return bitfitting(Digits)    
        else:
            k+=1
            j=0
    return Digits

digits=bitfitting(digits)
digits_after=''.join(str(i) for i in digits)
after_framing = "01111110"+digits_after+"01111110"

print("Before studding: ",digits_before," -- ",len(digits_before)," characters")
print("After studding: ",digits_after," -- ", len(digits_after)," characters")
print("after_framing: ",after_framing)

    
