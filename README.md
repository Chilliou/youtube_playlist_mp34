# YouTube Playlist Downloader

Un script Python simple et efficace pour télécharger des playlists YouTube en format MP3 (audio uniquement) ou MP4 (vidéo).

## Fonctionnalités

- Téléchargement de playlists YouTube complètes
- Choix entre format MP3 (audio uniquement) ou MP4 (vidéo avec audio)
- Affichage de la progression en temps réel
- Gestion des erreurs (continue même si une vidéo pose problème)
- Création automatique de dossiers organisés
- Nommage des fichiers avec numéros d'index pour préserver l'ordre
- Installation automatique des dépendances

## Prérequis

- Python 3.6 ou supérieur
- Connexion Internet

## Installation

1. Clonez ce dépôt ou téléchargez le fichier `youtube_playlist_downloader.py`

2. Installer les dépendances requises :
```bash
pip install yt-dlp
```
*Note : Le script peut également installer automatiquement les dépendances nécessaires.*

## Utilisation

1. Exécutez le script :
```bash
python youtube_playlist_downloader.py
```

2. Suivez les instructions à l'écran :
   - Entrez l'URL de la playlist YouTube
   - Spécifiez le dossier de destination (ou appuyez sur Entrée pour utiliser 'downloads')
   - Choisissez le format (1: MP3, 2: MP4)

3. Le téléchargement commencera et affichera la progression en temps réel

## Exemple d'utilisation

```
Entrez l'URL de la playlist YouTube: https://www.youtube.com/playlist?list=PLxxxxxxxxxxxxxxxx
Entrez le dossier de destination (par défaut: 'downloads'): mes_musiques
Choisissez le format (1: MP3, 2: MP4): 1
Format choisi: MP3 (audio uniquement)
Démarrage du téléchargement de la playlist: https://www.youtube.com/playlist?list=PLxxxxxxxxxxxxxxxx
Les fichiers seront enregistrés dans: mes_musiques/playlist_mp3_20250414_123456
```

## Structure des dossiers

Les téléchargements sont organisés comme suit :
```
dossier_destination/
└── playlist_[format]_[timestamp]/
    ├── 1-titre_video.mp3 (ou .mp4)
    ├── 2-titre_video.mp3
    └── ...
```

## Dépannage

Si vous rencontrez des erreurs :

1. **Erreur HTTP 400 ou 403** : YouTube modifie parfois son API. Essayez de mettre à jour yt-dlp :
   ```
   pip install --upgrade yt-dlp
   ```

2. **Le fichier spécifié est introuvable** : Assurez-vous que Python est correctement installé et dans votre PATH système.

3. **Erreurs de conversion** : Pour les conversions MP3, assurez-vous que FFmpeg est installé sur votre système.

## Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

## Remerciements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Bibliothèque utilisée pour le téléchargement des vidéos YouTube
