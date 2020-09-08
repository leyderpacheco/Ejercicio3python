#primer y ultimo valor de una palabra

def palabra():
    print("Palabra")
    a=input("Palabra :")
    b=len(a)
    palabra1=str(print(a[0]+a[b-1]))

    return palabra1


if __name__ == '__main__':
    palabra()
