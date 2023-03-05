#Problem 4
NORMAL_RANGES = {"m1": (0,10), "m2": (-5, 5), "m3": (100, 200)}

class Reading:
    def __init__(self, machine, level):
        assert machine in NORMAL_RANGES
    
        self.__machine = machine
        self.__level = level
    
    def should_ring_alarm(self):
        ###Your method here
        return

class Lab:
    def __init__(self):
        self.__notebook = []
    
    def add_reading(self, machine, level):
        ###Your method here
        return
    
    def count_alarms(self):
        ###Your method here
        return


#Problem 6
class AltBoolTree:

    def __init__(self, tag, children=None):
        self.tag = tag
        self.children = children
    
    def eval(self):
        return


#The tests - if you get no assertion errors, your code works (you should run it and nothing happens in the terminal)
m1 = Reading("m1", 10)
m2 = Reading("m2", -6)
m3 = Reading("m3", 201)

test_lab = Lab()
test_lab.add_reading("m1", 10)
test_lab.add_reading("m2", -6)
test_lab.add_reading("m3", 201)

assert not m1.should_ring_alarm()
assert m2.should_ring_alarm()
assert m3.should_ring_alarm()
assert test_lab.count_alarms() == 2




test1 = AltBoolTree(True)
test2 = AltBoolTree(False)
test3 = AltBoolTree("or", [AltBoolTree(True), AltBoolTree(False), AltBoolTree(False)])
test4 = AltBoolTree("and", [AltBoolTree(True), AltBoolTree(True), AltBoolTree(True)])
test5 = AltBoolTree("or", [AltBoolTree("and", [AltBoolTree(True), AltBoolTree(False)]), \
                            AltBoolTree(False), AltBoolTree("and", [AltBoolTree("or", \
                            [AltBoolTree(True), AltBoolTree(False)]), AltBoolTree(True)])])
test6 = AltBoolTree("or", [AltBoolTree(False), AltBoolTree("and", [AltBoolTree(True), AltBoolTree(False)])])

assert test1.eval()
assert not test2.eval()
assert test3.eval()
assert test4.eval()
assert test5.eval()
assert not test6.eval()


