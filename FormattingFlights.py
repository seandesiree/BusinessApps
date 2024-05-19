itinerary = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def formatter(itinerary):
    num = 0
    for flight in itinerary:
        num += 1
        print(f"Itinerary {num} : {flight[0]} - From {flight[1]} to {flight[2]}")

formatter(itinerary)