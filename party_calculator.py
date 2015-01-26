"""
This function will calculate how many beers you need to buy for your party
"""
print """
\t #### Party calculator will tell you exactly how many people \n
\t \tare gonna be in your place and \n
\t \t how many beers you \n
\t \t need to buy!! #### \n

\t \t #########################\n
\t \t So start planning!!
"""


square_meters_place = int(raw_input('How many square meters is your place?, type just a number:  '))

guests = raw_input('Do you allow people to come with theirpartner? ')

alco = int(raw_input('How many bottles of beers you will have for 1 person: '))


def party_calc_supllier(*args):
    square_meters_place, guests, alco = args
    people_per_one_squeare_meter = square_meters_place * 2
    if guests == 'yes':
        guests_p = int(2 * people_per_one_squeare_meter)
    else:
        pass

    print "For %d square meter place, you will have a quite a party!\n " % square_meters_place
    print "So roughly you expect %d people.\n" % people_per_one_squeare_meter
    print "But if they come with a partner - that's the different story!\n"
    print "If people will come with partner, you will expect %d people\n" % guests_p

    print "For party with people plus 1 , you need to buy: %d bottles of beer.\n" % (alco * guests_p)
    print "If nobody will come with a partner, you need to buy only %d bottles of beers\n" % (alco * people_per_one_squeare_meter)
    print "Anyway it is gonna be a great party!"

party_calc_supllier(square_meters_place, guests, alco)