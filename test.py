
class flight:
    def __init__(self, duration, destination):
        self.duration=duration
        self.destination=destination
 
def main():
    f=flight(duration=456,destination="paris")



    print(f.duration)
main()