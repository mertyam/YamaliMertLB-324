# LB 324

## Aufgabe 2
### Installation und Nutzung von pre-commit
```bash
pip install pre-commit
pre-commit install --hook-type pre-commit --hook-type pre-push
pre-commit run --all-files 
```
Eine Konfigurationsdatei .pre-commit-config.yaml im Repo anlegen.
-  Bei jedem Commit wird der Code automatisch formatiert.
-  Bei jedem Push laufen die Tests mit pytest. Schlägt ein Test fehl, wird der Push blockiert.
## Aufgabe 4
Passwort aus .env auf Azure übertragen
Im Azure Portal unter Einstellungen → Umgebungsvariabeln eine neue Variable erstellt:

Name: ```PASSWORD```

Wert: ```mertyam``` (gemäss LB Vorgabe)


Name: ```SECRET_KEY```

Wert: ```ein zufälliger String``` 

Danach gespeichert → die App wurde neu gestartet.
Bei jedem Merge nach main läuft ein automatisches Deployment auf Azure. (https://yamali-mert-lb324-fhfqg7heh6edbtct.switzerlandnorth-01.azurewebsites.net/)
