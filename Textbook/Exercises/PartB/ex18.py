# defining a function:
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# the *args is actually pointless, instead use:
# skips unpacking args
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothin'."

print_two("pineapple","muncher")
print_two_again("yum","yumm")
print_one("Hoopla!")
print_none()
