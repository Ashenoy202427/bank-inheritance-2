from secuSave import bankSave, savAcc, chekAcc, superAcc
#import those classes!

#testing code and function calls go below here!
print("Welcome to SecuSave credit union!!")
#WELCOME to secuSave (name of bank)
acc1= superAcc("Alan", 4000, 600)
#create a sample testing account object
acc2 = superAcc("Obama", 15000, 2000 )
#creating another sample testing account object to test the transfer limitation functionality

acc1.deposit()
acc1.withdraw()

acc2.deposit()
acc2.withdraw()
#here I just test basic deposit withdraw for both bank account objects

acc1.transfer(acc2)
acc2.transfer(acc1)
#here I test the transfer method from chekAcc subclass

# acc3 = savAcc("Alan", 4000, 600)
# acc4 = savAcc("Obama", 15000, 2000 )
# acc3.interestFee()
# acc4.interestFee()

acc1.interestFee()
acc2.interestFee()

#here it gets a little messy, to test the interestFee method from savAcc subclass
#we need to recreate the objects using savAcc

acc1.print_customer_information()
acc2.print_customer_information()
#here we print the customers bank accounts to verify success

