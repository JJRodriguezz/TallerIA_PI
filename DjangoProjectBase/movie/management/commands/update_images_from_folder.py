import os
import re
from django.core.management.base import BaseCommand
from movie.models import Movie
from django.conf import settings

class Command(BaseCommand):
    help = "Update movie images in the database from the media/movie/images folder"

    def clean_filename(self, title):
        # Reemplazar ':' con '_'
        title = title.replace(":", "_")
        
        # Si las comillas simples rodean todo un segmento de texto, reemplazarlas con '_'
        title = re.sub(r"'([^']+)'", r"_\1_", title)  # Cambia 'Texto' → _Texto_

        title = title.replace("?", "&")
        
        return title

    def handle(self, *args, **kwargs):
        # 📂 Ruta de la carpeta donde están almacenadas las imágenes
        images_folder = os.path.join(settings.MEDIA_ROOT, 'movie', 'images')
        
        if not os.path.exists(images_folder):
            self.stderr.write(f"Image folder '{images_folder}' not w
            return

        updated_count = 0
        
        # 🔄 Recorre todas las películas en la base de datos
        for movie in Movie.objects.all():
            # 🔍 Limpiar el nombre de la película solo para ':' y comillas rodeando texto
            safe_title = self.clean_filename(movie.title)
            image_filename = f"m_{safe_title}.png"  # Mantiene espacios y otros caracteres
            image_path = os.path.join(images_folder, image_filename)

            if os.path.exists(image_path):
                # 📝 Actualizar la película con la ruta de la imagen
                movie.image = f"movie/images/{image_filename}"
                movie.save()
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f"Updated image for: {movie.title}"))
            else:
                self.stderr.write(f"Image not found for: {movie.title}")
        
        # ✅ Mostrar cuántas películas se actualizaron
        self.stdout.write(self.style.SUCCESS(f"Finished updating {updated_count} movie images."))
