import os
from datetime import datetime
from shutil import copyfile


#On crée la liste des fichiers
listeFichiers = os.listdir("source\\")


# Pour chaque fichier
for f in listeFichiers:

	
	#Si le nom du fichier permet le classement

	# On récupère le nom
        fr = f[4:12]
        # On en determine le nom du dossier
        nomDossier = fr[:4]+"-"+fr[4:6]+"-"+fr[6:8]

        
        # Si les métadonnées du fichiers permettent le classement
        #date = os.path.getmtime("source\\"+f)
        #date1 = datetime.fromtimestamp(date)
        #dossier = date1.isoformat(sep='T', timespec='auto')
        #nomDossier = dossier[:10]
	
	




	# Si le dossier existe déjà, on y copie le fichier
        if(os.path.exists("rangement\\"+nomDossier+"\\")):
                copyfile("source\\"+f, "rangement\\"+nomDossier+"\\"+f)


        # Si le dossier n'existe pas, on le crée et on y copie le fichier.
        else:
                os.mkdir("rangement\\"+nomDossier+"\\")
                copyfile("source\\"+f, "rangement\\"+nomDossier+"\\"+f)

	
        print(f + " déplacé dans le dossier : "+  nomDossier)

os.system("pause")



