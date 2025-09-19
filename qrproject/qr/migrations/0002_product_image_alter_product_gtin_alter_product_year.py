from django.db import migrations, models
import django.core.validators

class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0002_product_image_alter_product_gtin_alter_product_year'),
        ('qr', '0003_alter_product_year'),
    ]

    operations = [
        # image sahəsi artıq mövcud olduğuna görə onu əlavə etməyə ehtiyac yoxdur
        # migrations.AddField(
        #     model_name='product',
        #     name='image',
        #     field=models.ImageField(blank=True, null=True, upload_to='media/'),
        # ),
        # Yalnız digər sahələr üzrə dəyişiklikləri saxlayın
        migrations.AlterField(
            model_name='product',
            name='gtin',
            field=models.CharField(
                max_length=14,
                unique=True,
                validators=[django.core.validators.RegexValidator('^\\d{8,14}$', 'GTIN yalnız 14 rəqəm ola biler.')]
            ),
        ),
        migrations.AlterField(
            model_name='product',
            name='year',
            field=models.IntegerField(blank=True, null=True),  # max_length silindi, IntegerField-də lazım deyil
        ),
    ]
