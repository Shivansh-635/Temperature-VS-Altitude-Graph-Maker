import matplotlib.pyplot as plt

n=float(input("Enter Altitude (In KM):"))

if 0<= n <=11 :
    t1 = 288.16 + (-6.5)*(n)
    print(t1)
elif 11< n <=25 :
    t1 = 216.66
    print(t1)
elif 25 < n <= 47 :
    t1 = 216.66 + 3*(n - 25)
    print(t1)
elif 47 < n <= 53 :
    t1 = 282.66
    print(t1)
elif 53 < n <= 79 :
    t1 = 282.66 + (-4.5)*(n - 53)
    print(t1)
elif 79 < n <= 90 :
    t1 = 165.66
    print(t1)
elif  90 < n <= 105 :
    t1 = 165.66 + 4*(n - 90)
    print(t1)
elif  n < 0 :
    print("Invalid Altitude")

Y = [0,11,25,47,53,79,90,105]
X = [288.16,216.66,216.66,282.66,282.66,165.66,165.66,225.66]

plt.plot(X,Y)
plt.scatter(X,Y,color="black",marker="o")
plt.scatter(t1,n,color="red",marker="x")
T1 = round(t1,2)
plt.annotate(f"{T1}\n{n}",(t1,n),textcoords="offset points",xytext=(3,7),fontweight="bold")
for i in range(len(Y)):
    plt.annotate(f"{Y[i]}\n{X[i]}",(X[i],Y[i]),textcoords="offset points",xytext=(3,7))
plt.xlabel("Temperature (In K)",fontsize=14,fontweight="bold")
plt.ylabel("Altitude (In KM)",fontsize=14,fontweight="bold")
plt.ylim(0,120)
plt.xlim(150,300)
plt.show()
