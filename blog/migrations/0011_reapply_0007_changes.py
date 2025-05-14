from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_featured_image'),  # Reference to the migration before 0007
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default="No content"),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
