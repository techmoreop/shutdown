a = input("do you want to shutdown there are some conditions (yes/no)")
def shutdown(a):
 if a == "yes":
    print("shutting down...")
 elif a == "no":
    print("aborting shutdown")
 else:
    print("srry error")
shutdown(a)