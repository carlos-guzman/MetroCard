# 2014 Carlos Guzman
# 
# Given how much money you have in your card and how much you are willing to spend, calculate the optimal recharge amounts to pay only for what you use.
# 

current = int(float(raw_input("How much do you already have in your card?\n"))*100)
max = int(float(raw_input("How much are you willing to spend? ($)\n"))*100)

print("RECHARGE   RIDES   REMAINDER\n")
# Amount to recharge on the card
add = 0

# Rides after recharge
rides = current/250

# Least amount of money left in the card, out of all the options
least_remainder = 0


while(add<=max):
    rides = int(round(current+add*1.05)/250)
    # Amount left in the card after recharging the certain amount
    remainder = round(current+add*1.05)%250

    # Keep track of the best option
    if remainder<=least_remainder:
        should = add
        least_remainder = remainder

    print("%8.2f%7d%10.2f\n"
     % (add/100.0, rides, remainder/100.0))

    # Calculate the amount needed to get to one more ride
    add = int(round(((rides+1)*250-current)/1.05))
    
    # Round to 5 cents
    add+= (5-add%5)%5

print("You should recharge %.2f dollars\n\n" % (should/100.0))

