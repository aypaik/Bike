

class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print 'This bike is $' + str(self.price) + "."
        print 'Max speed is ' + str(self.max_speed) + 'MPH.'
        print 'This bike has ' + str(self.miles) + ' miles.'

    def ride(self):
        print "Riding..."
        self.miles += 10

    def reverse(self):
        print "Reversing..."
        if self.miles >= 5:
            self.miles -= 5

bike1 = Bike(100, 12)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

bike2 = Bike(199.99, 15)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()