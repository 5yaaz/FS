while True:
	try:
		P,Q= raw_input().split()
		P=int(P)
		Q=int(Q)
		break
	except:
		print("Invalidinput")
		break
C=1
for x in range(Q):
	C=C*P
print(C)
