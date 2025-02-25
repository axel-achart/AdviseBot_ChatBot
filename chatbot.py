import random

#Réponses simples
reponses = {
    "Bonjour" : "Hey je suis AdvisorBot ! En quoi je peux te conseiller ?",
    "ça va ?" : "Oui ça va super, toujours au top pour discuter et t'aider",
    "quoi tu sers ?" : "Je suis là pour discuter avec toi et te conseiller sur des films par exemple"
}

#Listes des recommandations
films=["Interstellar", "Avatar 2 La Voie de l'Eau"]
aliments=["Fruits", "Légumes", "Légumineuses", "Oléagineux", "Produits laitiers"]
investissements=["les placements immobiliers", "les différents livrets bancaires", "les ETF et Actions",
                 "les cryptomonnaies", "les livres pour davantages de connaissances"]
rappeursfr=["PNL", "Zola", "Werenoi", "SDM", "KobaLaD", "LaMano1.9", "JRK19", "RK", "MHD", "Ninho", "Niska",
            "Kerchak", "L2B", "Kaaris", "Booba", "Tiakola", "Rsko", "NTM", "MC Solaar", "Leto", "Hamza",
            "Gazo", "Favé", "Naps", "Jul", "SCH", "IAM", "AKHENATON", "Shuriken", "Guizmo"]
rappeurseng=["Lil TJay", "Central Cee", "Metro Boomin", "Travis Scott", "DaBaby", "50Cent"]

def repondre(question):
    # Réponses de base basées sur les mots-clés
    for mot_cle, reponse in reponses.items():
        if mot_cle in question.lower():
            return reponse

    if "film" in question.lower():
        return f"Je te recommande ce film : {random.choice(films)}."
    elif "aliment" in question.lower():
        return f"Je te recommande de tester : {random.choice(aliments)}."
    elif "investissement" in question.lower():
        return f"Je te préconise d'investir dans {random.choice(investissements)}."
    elif "rappeurs français" in question.lower():
        return f"Je te conseille d'écouter {random.choice(rappeursfr)}."
    elif "rappeurs anglophones" in question.lower():
        return f"Je te conseille d'écouter {random.choice(rappeurseng)}."
    elif "bye" in question.lower():
        return f"Au revoir et à plus tard !"
    elif "Au revoir" in question.lower():
        return f"Au revoir et à plus tard !"
    elif "plus tard" in question.lower():
        return f"Au revoir et à plus tard !"
    elif "adieu" in question.lower():
        return f"Au revoir et à plus tard (j'espère) !"

    return "Désolé je ne comprend pas ce que tu recherches."

    # La Conversation
print("Salut ! Je suis là pour te conseiller sur différents sujets comme le rapFR, l'investissements, les aliments sains à manger mais également les films")
while True:
    question=input("AdvisorBot : Sur quel sujet veux-tu que je te conseille :")
    reponse = repondre(question)
    print(f"AdvisorBot : {reponse}")