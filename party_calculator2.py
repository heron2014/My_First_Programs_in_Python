def people_per_squeare_m(space):
    space = int(raw_input('How big is your space for a party in square meters?: Type a rough number:  '))
    return space * 2


def people_plus_one(party_space):
    guest = raw_input('Do you allow people to come with their partner?: ')
    if guest == 'yes':
        guest_plus_one = int(party_space * 2)
        return guest_plus_one
    else:
        return party_space


#this number 2 is just a default which will be not taken anyway because we will ask the user for a number
party_space = people_per_squeare_m(2)
people_p = people_plus_one(party_space)

print "Thats a great space for a party. So that means you will have %d people.\n" % party_space

print "If people will come with their partner, you expect about %d people. Ohh boy that's a big party!! \n" % people_p


def wine_drinkers(party_space):
    return int(float((30 * party_space) / 100)) * 250


def wine_drinkers_plus_partner(people_p):
    return int(float((30 * people_p) / 100)) * 250


wine = wine_drinkers(party_space)
wine_plus_partner = wine_drinkers_plus_partner(people_p)


print "Ok!lets break the scenario's. \n"
print "First one: the less expensive for you! \n"
print "How much wine do You need!\n"
print "If people come without their partners and lets say 30% of them is a wine drinkers..\n"
print "You need roughly %d ml of wine! I know I know... that means nothing to you! \n" % wine
print "Good you have me!! That is about %d bottles of wine!\n\n" % (wine / 750)

print "Now second scenerio! A bit more expensive but more fun too!\n"
print "If people come with their partners and lets say 30% of them is a wine drinkers..\n"
print "You need roughly %d ml of wine! I know I know... that means nothing to you! \n" % wine_plus_partner
print "Good you have me!! That is about %d bottles of wine!\n\n" % (wine_plus_partner / 750)





