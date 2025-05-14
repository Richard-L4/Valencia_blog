from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_category_post_categories'),  # change to your actual last migration
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(
                to=settings.AUTH_USER_MODEL,
                on_delete=django.db.models.deletion.CASCADE,
                default=1,  # TEMPORARY default to allow migration
            ),
            preserve_default=False,
        ),
    ]
