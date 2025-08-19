from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from apps.posts.models import PostsModel as Post
from apps.comments.models import CommentsModel as Comment
from apps.accounts.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_groups_and_permissions(sender, instance, created, **kwargs):
    if created and instance.is_superuser and User:
        try:
            post_content_type = ContentType.objects.get_for_model(Post)
            comment_content_type = ContentType.objects.get_for_model(Comment)

            # Permisos de POST
            view_post_permission = Permission.objects.get(
                codename='view_postmodel', content_type=post_content_type)
            add_post_permission = Permission.objects.get(
                codename='add_postmodel', content_type=post_content_type)
            change_post_permission = Permission.objects.get(
                codename='change_postmodel', content_type=post_content_type)
            delete_post_permission = Permission.objects.get(
                codename='delete_postmodel', content_type=post_content_type)

            # Permisos de COMMENT
            view_comment_permission = Permission.objects.get(
                codename='view_commentsmodel', content_type=comment_content_type)
            add_comment_permission = Permission.objects.get(
                codename='add_commentsmodel', content_type=comment_content_type)
            change_comment_permission = Permission.objects.get(
                codename='change_commentsmodel', content_type=comment_content_type)
            delete_comment_permission = Permission.objects.get(
                codename='delete_commentsmodel', content_type=comment_content_type)

            # Crear grupos de usuarios registrados
            registered_group, created = Group.objects.get_or_create(
                name="Registered"
            )
            registered_group.permissions.add(
                view_post_permission,  # permiso para ver post
                view_comment_permission,  # permiso para ver comentarios del post
                add_comment_permission,  # permiso para crear comentarios del post
                change_comment_permission,  # permiso para actualizar de su comentario en un post
                delete_comment_permission,  # permiso para borrar su comentario en un post
            )

            # Crear grupos de usuarios colaboradores
            collaborators_group, created = Group.objects.get_or_create(
                name="Collaborators"
            )
            collaborators_group.permissions.add(
                view_post_permission,  # permiso para ver post
                add_post_permission,  # permiso para crear post
                change_post_permission,  # permiso para actualizar su post
                delete_post_permission,  # permiso para borrar su post
                view_comment_permission,  # permiso para ver comentarios del post
                add_comment_permission,  # permiso para crear comentarios del post
                change_comment_permission,  # permiso para actualizar de su comentario en un post
                delete_comment_permission,  # permiso para borrar su comentario en un post
            )

            # Crear grupos de usuarios administradores
            admins_group, created = Group.objects.get_or_create(
                name="Admins"
            )
            admins_group.permissions.add(
                view_post_permission,  # permiso para ver post
                add_post_permission,  # permiso para crear post
                change_post_permission,  # permiso para actualizar su post
                delete_post_permission,  # permiso para borrar cualquier post
                view_comment_permission,  # permiso para ver comentarios del post
                add_comment_permission,  # permiso para crear comentarios del post
                change_comment_permission,  # permiso para actualizar de su comentario en un post
                delete_comment_permission,  # permiso para borrar su comentario de cualquier post
            )

            print("Grupos y Permisos creados exitosamente.")
        except ContentType.DoesNotExist:
            print("El tipo aun no se encuentra disponible.")
        except Permission.DoesNotExist:
            print("Uno o mas permisos no se encuentran disponibles")