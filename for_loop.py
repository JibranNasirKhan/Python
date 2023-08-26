# name = "Jibran"
# for i in name:
#     print(i,"\n")
#
# city = ["delhi", "punjab", "pune", "mumbai"]
#
# for i in city:
#     print(i)
#
# total_price = [[45,52], [36,42], [50,55], [82,90]]
# for price, mrp in total_price:
#     print("Price is "+str(price)+" and their MRP is " + str( mrp))

# type casting into dictionary

Places = [['Afghanistan','Kabul'],['Albania','Tirana (Tirane)'],['Algeria','Algiers'],['Andorra',' Andorra la Vella'],['Angola','Luanda'],['Antigua and Barbuda','Saint John'],['Argentina','Buenos Aires'],['Armenia','Yerevan']]

my_dictionary = dict(Places)
print(my_dictionary)
for country, capitals in my_dictionary.items():
    print(country, capitals)
    for s in country:
        print(country)

