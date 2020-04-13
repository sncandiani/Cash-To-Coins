dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}
# Function makeChange takes in the dollar amount 
def makeChange(r):
    # Converts to make calculations easier
    cents = int(r*100) 
# Does appropriate arithmetic for each to change value in piggyBank and affect remainder
    piggyBank["quarters"] = cents // 25 
    cents -= piggyBank["quarters"] * 25
    
    piggyBank["dimes"] = cents // 10 
    cents -= piggyBank["dimes"] * 10
    
   
    piggyBank["nickels"] = cents //5  
    cents -= piggyBank["nickels"] * 5
  
    piggyBank ["pennies"] = cents //1  
    print(piggyBank)
       
makeChange(dollarAmount)


    
       