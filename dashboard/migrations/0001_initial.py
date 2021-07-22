# Generated by Django 3.2.3 on 2021-07-22 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('royalties', models.PositiveIntegerField()),
                ('content_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visibility', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MarketPlaceItem',
            fields=[
                ('guid', models.UUIDField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('price_is_visible', models.BooleanField(default=True)),
                ('asset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='dashboard.asset')),
                ('series', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='dashboard.series')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='dashboard.marketplaceitem'),
        ),
    ]
