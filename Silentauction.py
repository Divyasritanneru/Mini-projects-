import os
print("*******WELCOME TO THE SILENT AUCTION PROGRAM******")
def find_winner(bidder_details):#divya:1000 #tagore:500 #nagu:2000
  highest_bid=0
  for bidder in bidder_details:
    bidding_price=bidder_details[bidder]
    if bidding_price>highest_bid:
      highest_bid=bidding_price
      winner=bidder
  print(f"the winner is {winner} with the highest bidding price {highest_bid}")  


bidders_data={}
end_of_bidding=False
while not end_of_bidding:
   name=input("enter a name:")
   bid_price=int(input("enter the bid price:"))
   bidders_data[name]=bid_price
   more_bidders=input("are there any bidders type 'yes' or 'no': ")
   if more_bidders=="no":
    end_of_bidding=True
    find_winner(bidders_data)
   elif more_bidders=="yes":
     os.system('cls')
