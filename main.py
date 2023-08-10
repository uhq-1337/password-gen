import random

mots = [
    "codeine", "promethazine", "euphon", "xanax", "lyn", "jmcorda", "enfant",
    "turbulant", "framboise", "radiateur", "chips", "melon", "cascade", "congolais",
    "joueur", "azure", "securepass", "3dsecure", "jesaispas", "absolument",
    "horizontal", "oasis", "tropical", "mickael", "damien", "2meodmt", 
    "tarax", "topax", "benzo", "ddb", "topic", "vocaroo", "postoucancer",
    "tortue", "lasalle", "confiture", "abribus", "dragibus", "troposphere",
    "artificielle", "zinzolax"
]

def gen(length=5):
    password = '-'.join(random.choice(mots) for _ in range(length))
    return password

def save(filename, num_passwords):
    with open(filename, 'w') as file:
        for _ in range(num_passwords):
            password = gen()
            file.write(password + '\n')

if __name__ == "__main__":
    num_passwords = int(input("[+] Combien de mots de passe veux-tu générer ? "))
    save('passwords.txt', num_passwords)
    print(f"[+] {num_passwords} mots de passe ont été généré dans le fichier 'passwords'.txt")
