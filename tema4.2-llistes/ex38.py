compra = ["Aigua", "Ous", "Oli", "Sal", "Llimona"]
detalls = ["amb gas", "fregits", "d'oliva", "grossa", "amb mel"]

for products,detalls in zip(compra,detalls):
    print(products,detalls)