# prints results of add function generator

from generator import add

generator = add()

# app decorator for memory profiling
# @profile
def dothething():
    for result in generator:
        print(result)

if __name__ == '__main__':
    dothething()

