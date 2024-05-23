our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def flight_comparison(our_routes, competitor_routes):
    
    print(f"Both airlines fly to {our_routes.intersection(competitor_routes)} ")
    print(f"Our airline flies to {our_routes.difference(competitor_routes)} and our competitor does not. ")
    print(f"These destinations are not shared by neither airpline {our_routes.symmetric_difference(competitor_routes)} ")

flight_comparison(our_routes, competitor_routes)

