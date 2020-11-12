import requests

while True: 

	ChoixAffichage = raw_input("1 = affichage de tous les produits, 2 = affichage d'un seul produit, 3 = ajouter un produit, q = quitter :  ")

	if ChoixAffichage == '1' :
		print ("Voici le resultat de l'affichage de tous les produits : ")
		response = requests.get("http://localhost:8989/tous")
		print(response.text)
	#print(response.json())

	if ChoixAffichage =='2' :
        	ChoixCode = str(input("Entrer votre numero de produit: "))
        	response = requests.get("http://localhost:8989/produit/"+ChoixCode)
        	print(response.text)
        #print(response.json())

	if ChoixAffichage =='3' :
        	NvxCode = raw_input("Entrer votre nouveau code produit: ")
		NvxProduit =raw_input("Designation produit: ")
		NvxPrix = raw_input("Entrer le prix de votre produit: ")

		response = requests.post("http://localhost:8989/ajouter", data ={'code': NvxCode, 'designation': NvxProduit, 'prix':NvxPrix})
		print("Votre produit a ete ajoute: " + NvxCode+ "/"+NvxProduit+"/"+NvxPrix)

	if ChoixAffichage=='q' or ChoixAffichage=='Q' or ChoixAffichage=='quitter':
		break

	


