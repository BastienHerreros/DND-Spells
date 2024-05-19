import json
import string
 
def isFromClass(spellName: string):
    fileToSearch = ["Artificier", "Barde", "Clerc", "Druide", "Ensorceleur", "Magicien", "Occultiste", "Paladin", "Rodeur"]
    classes = []

    for className in fileToSearch:
        with open('html/' + className +'.txt') as file:
            content = file.read()
            
            if spellName.rstrip() + "\n" in content: 
                classes.append(className)
        
    return classes

def main():

    lineTemplate = "{lvl};{name};{school};{incant};{range};;{effect};{save};;{concentration};{ritual};;;;{link};{artificier};{mystificateur};{barde};{clerc};{druide};{chevalier};{paladin};{rangeur};{ensorceleur};{occultiste};{magicien}\n"

    with open('result.txt', 'w') as resultFile:
        with open('json/Full.json') as fullJsonFile:
            fullJson = json.load(fullJsonFile)

            for elem in fullJson:
                classes = isFromClass(elem['Sort '])

                saveValue = ""

                desc = elem['Description '] if 'Description ' in elem else ""
                if 'JdS de ' in desc:
                    pos = desc.find('JdS de')
                    saveValue = desc[pos+7:pos+10]

                if 'JdS d\'' in desc:
                    pos = desc.find('JdS d\'')
                    saveValue = desc[pos+6:pos+9]

                line = lineTemplate.format( 
                    lvl = elem['Niv '],
                    name = elem['Sort '],
                    school = elem['École '],
                    incant = elem['Incantation '],
                    range = elem['Portée '],
                    effect = desc,
                    save = saveValue,
                    concentration = "Concentration" if 'Concentration ' in elem else "",
                    ritual = "Rituel" if 'Rituel ' in elem else "",
                    link = "https://www.aidedd.org/dnd/sorts.php?vf=" + elem['Sort '].replace(" ", "-").replace("'", "-").lower(),
                    artificier = "VRAI" if "Artificier" in classes else "FAUX",
                    mystificateur = "VRAI" if "Magicien" in classes else "FAUX",
                    barde = "VRAI" if "Barde" in classes else "FAUX",
                    clerc = "VRAI" if "Clerc" in classes else "FAUX",
                    druide = "VRAI" if "Druide" in classes else "FAUX",
                    chevalier = "VRAI" if "Magicien" in classes else "FAUX",
                    paladin = "VRAI" if "Paladin" in classes else "FAUX",
                    rangeur = "VRAI" if "Rodeur" in classes else "FAUX",
                    ensorceleur = "VRAI" if "Ensorceleur" in classes else "FAUX",
                    occultiste = "VRAI" if "Occultiste" in classes else "FAUX",
                    magicien = "VRAI" if "Magicien" in classes else "FAUX")
                
                resultFile.write(line)

main()