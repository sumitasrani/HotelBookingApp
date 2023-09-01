import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
print(df)

df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
print(df_cards)

df_cards_security = pd.read_csv("card_security.csv", dtype=str)
print(df_cards_security)


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
        df.loc[df["id"] == self.hotel_id, "available"] = 'no'
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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class CardSecurityCheck(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


hotel_Id = input("Enter the Hotel id: ")
hotel = Hotel(hotel_Id)

if hotel.available():
    credit_card = CardSecurityCheck(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name for reservation: ")
            reserve_booking = Reservation(cust_name=name, hotel_name=hotel)
            print(reserve_booking.generate())
        else:
            print("Authentication failed")
    else:
        print("There was a problem in your payment")

else:
    print("Hotel is not available")
