import os
import sys
from datetime import datetime

def download_playlist():
    """Télécharge les vidéos d'une playlist YouTube en format MP3 ou MP4"""
    try:
        # Tenter d'importer yt-dlp
        try:
            import yt_dlp
        except ImportError:
            print("Installation du module yt-dlp...")
            import pip
            pip.main(['install', 'yt-dlp'])
            import yt_dlp
            print("yt-dlp a été installé avec succès.")
        
        # Demander l'URL et le dossier de destination
        playlist_url = input("Entrez l'URL de la playlist YouTube: ")
        output_dir = input("Entrez le dossier de destination (par défaut: 'downloads'): ") or "downloads"
        
        # Choix du format
        while True:
            format_choice = input("Choisissez le format (1: MP3, 2: MP4): ").strip()
            if format_choice in ['1', '2']:
                break
            print("Choix invalide. Veuillez entrer 1 pour MP3 ou 2 pour MP4.")
        
        # Création du dossier de sortie s'il n'existe pas
        os.makedirs(output_dir, exist_ok=True)
        print(f"Dossier de sortie: {output_dir}")
        
        # Nom du sous-dossier avec horodatage pour éviter les conflits
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        format_name = "mp3" if format_choice == '1' else "mp4"
        subfolder = f"playlist_{format_name}_{timestamp}"
        output_template = os.path.join(output_dir, subfolder, "%(playlist_index)s-%(title)s.%(ext)s")
        
        # Configuration des options pour yt-dlp
        ydl_opts = {
            'outtmpl': output_template,
            'restrictfilenames': True,       # Évite les caractères problématiques dans les noms
            'nooverwrites': True,            # Ne pas écraser les fichiers existants
            'ignoreerrors': True,            # Ignorer les erreurs et continuer
            'continuedl': True,              # Continuer les téléchargements partiels
            'sleep_interval': 2,             # Attendre entre les téléchargements
            'max_sleep_interval': 5,
            'min_sleep_interval': 1,
            'verbose': True,                 # Mode verbeux pour voir la progression
            'progress_hooks': [lambda d: print_progress(d)]
        }
        
        # Configuration spécifique selon le choix du format
        if format_choice == '1':  # MP3
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
            print("Format choisi: MP3 (audio uniquement)")
        else:  # MP4
            ydl_opts.update({
                'format': 'best[height<=720][ext=mp4]/best[height<=720]/best[ext=mp4]/best',
            })
            print("Format choisi: MP4 (vidéo avec audio)")
        
        print(f"Démarrage du téléchargement de la playlist: {playlist_url}")
        print(f"Les fichiers seront enregistrés dans: {os.path.dirname(output_template)}")
        
        # Création de l'objet downloader et téléchargement
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(playlist_url, download=True)
            
            # Afficher le résumé
            if info and 'entries' in info:
                # Compter les téléchargements réussis
                successful = sum(1 for entry in info['entries'] if entry is not None)
                
                print(f"\nTéléchargement terminé!")
                print(f"Playlist: {info.get('title', 'Playlist inconnue')}")
                print(f"Nombre de vidéos traitées avec succès: {successful}/{len(info['entries'])}")
                print(f"Format: {format_name.upper()}")
                print(f"Emplacement: {os.path.dirname(output_template)}")
            else:
                print("\nAucune vidéo n'a été trouvée dans la playlist ou erreur lors de l'extraction des informations.")
                
    except Exception as e:
        print(f"Une erreur est survenue: {str(e)}")
        print("Traceback complet:")
        import traceback
        traceback.print_exc()

def print_progress(d):
    """Affiche la progression du téléchargement"""
    if d['status'] == 'downloading':
        filename = d.get('filename', '').split('/')[-1].split('\\')[-1]
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        
        print(f"\rTéléchargement: {filename} | {percent} | {speed} | ETA: {eta}", end='')
    
    elif d['status'] == 'finished':
        filename = d.get('filename', '').split('/')[-1].split('\\')[-1]
        print(f"\nTéléchargement terminé: {filename}")
        if filename.endswith('.mp4'):
            print("Traitement terminé.\n")
        else:
            print("Conversion audio en cours...\n")

if __name__ == "__main__":
    download_playlist()