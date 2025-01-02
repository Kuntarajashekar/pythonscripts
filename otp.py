import secrets

otp = '' .join([str(secrets.randbelow(10)) for _ in range(6)])

#print(otp)

print(f"Your OTP is: {otp} please do not share with anyone")


