# Generated by Django 3.0.5 on 2020-05-21 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20200521_1819'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('age', models.CharField(max_length=50, null=True)),
                ('height', models.CharField(max_length=50, null=True)),
                ('weight', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('bmi', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
            ],
            options={
                'db_table': 'customer_informations',
            },
        ),
        migrations.CreateModel(
            name='RecommendedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
                ('image_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=200)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('content', models.TextField()),
                ('highlight', models.CharField(max_length=500)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
            ],
            options={
                'db_table': 'recommended_products',
            },
        ),
        migrations.CreateModel(
            name='ResultList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'result_lists',
            },
        ),
        migrations.CreateModel(
            name='SurveyAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('placeholder', models.CharField(max_length=50)),
                ('next_question', models.IntegerField(default=0)),
                ('box', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'survey_answers',
            },
        ),
        migrations.CreateModel(
            name='SurveyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'survey_types',
            },
        ),
        migrations.CreateModel(
            name='SurveyResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_information', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.CustomerInformation')),
                ('recommended_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.RecommendedProduct')),
                ('result_list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.ResultList')),
            ],
            options={
                'db_table': 'survey_results',
            },
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('detail_question', models.CharField(max_length=200)),
                ('sub_question', models.CharField(max_length=200)),
                ('image_url', models.URLField(max_length=2000, null=True)),
                ('limit', models.CharField(max_length=30, null=True)),
                ('percentage', models.IntegerField(default=0)),
                ('survey_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.SurveyType')),
            ],
            options={
                'db_table': 'survey_questions',
            },
        ),
        migrations.CreateModel(
            name='SurveyComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('survey_answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.SurveyAnswer')),
            ],
            options={
                'db_table': 'survey_coments',
            },
        ),
        migrations.AddField(
            model_name='surveyanswer',
            name='survey_question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.SurveyQuestion'),
        ),
        migrations.CreateModel(
            name='SuitablePill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommended_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.RecommendedProduct')),
                ('survey_answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.SurveyAnswer')),
            ],
            options={
                'db_table': 'suitable_pills',
            },
        ),
        migrations.AddField(
            model_name='recommendedproduct',
            name='recommendedproduct_surveyanswer',
            field=models.ManyToManyField(through='survey.SuitablePill', to='survey.SurveyAnswer'),
        ),
        migrations.CreateModel(
            name='ProductContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=1000)),
                ('highlight', models.CharField(max_length=500)),
                ('link', models.TextField()),
                ('recommended_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.RecommendedProduct')),
            ],
            options={
                'db_table': 'product_contents',
            },
        ),
        migrations.CreateModel(
            name='ImageDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('recommended_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.RecommendedProduct')),
            ],
            options={
                'db_table': 'image_descriptions',
            },
        ),
        migrations.AddField(
            model_name='customerinformation',
            name='customerinformation_recommendedproduct',
            field=models.ManyToManyField(through='survey.SurveyResult', to='survey.RecommendedProduct'),
        ),
        migrations.AddField(
            model_name='customerinformation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User'),
        ),
        migrations.CreateModel(
            name='CustomerAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.IntegerField(default=0)),
                ('answer', models.IntegerField(default=0)),
                ('customer_information', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.CustomerInformation')),
            ],
            options={
                'db_table': 'customer_answers',
            },
        ),
    ]
