hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def is_available(hotel, room_number):
    return hotel.get(room_number, False)

def book_room(hotel, room_number, guest):
    if is_available(hotel, room_number):
        hotel[room_number] = False
        print(f"Great! {guest} have booked {room_number}!")
    else:
        print(f"Sorry {guest} room {room_number} is not available")

def checkout_customer(hotel, room_number, guest):
    if room_number in hotel:
        guest = hotel[room_number]
        print(f"Checking out customer '{guest}' from room {room_number}.")
        del hotel[room_number]
        print(f"Room {room_number} is now available.")
    else:
        print(f"Room {room_number} is already available.")

def display_room(hotel):
    for room, available in hotel.items():
        status = "Available" if available else "Booked"
        print(f"Room {room}: {status}")


