import pandas as pd

df = pd.read_csv("HotelBooking/hotels.csv", dtype={"id": str})
print(df)


class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def available(self):

        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()

        if availability == "yes":
            return True
        else:
            return False

    def hotel_list(self):
        pass

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] == "no"
        df.to_csv("hotels.csv", index=False)


class Reservation:

    def __init__(self, cust_name, hotel_name):
        self.cust_name = cust_name
        self.hotel = hotel_name
        pass

    def generate(self):
        content = f""" 
        Thank you for reservation with us. 
        Here's your booking detail:
        Your Name: {self.cust_name}
        Hotel: {self.hotel.name} is booked 
        """
        return content


hotel_Id = input("Enter the Hotel id: ")
hotel = Hotel(hotel_Id)

if hotel.available():
    hotel.book()
    name = input("Enter your name for reservation: ")
    reserve_booking = Reservation(cust_name=name, hotel_name=hotel)
    print(reserve_booking.generate())

else:
    print("Hotel is not avaiable")
