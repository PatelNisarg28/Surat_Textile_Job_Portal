# Generated by Django 4.2.9 on 2024-01-22 12:16

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("is_owner", models.BooleanField(default=False)),
                ("is_worker", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="home_OwnerUser_groups",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="home_OwnerUser_user_permissions",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="WorkerProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone_number", models.CharField(max_length=20)),
                ("living_area", models.CharField(max_length=100)),
                (
                    "work_location",
                    models.CharField(
                        choices=[
                            ("Bhagvati", "Bhagvati"),
                            ("Pramukh", "Pramukh"),
                            ("Sonal", "Sonal"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "area_of_work",
                    models.CharField(
                        choices=[
                            ("Bobin", "Bobin"),
                            ("TFO", "TFO"),
                            ("Master", "Master"),
                        ],
                        max_length=20,
                    ),
                ),
                ("open_to_work", models.BooleanField(default=True)),
                ("currently_working", models.BooleanField(default=False)),
                (
                    "worker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OwnerPublish",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "industrial_park_name",
                    models.CharField(
                        choices=[
                            ("Bhagvati", "Bhagvati"),
                            ("Pramukh", "Pramukh"),
                            ("Sonal", "Sonal"),
                        ],
                        max_length=20,
                    ),
                ),
                ("owner_name", models.CharField(max_length=100)),
                ("firm_number", models.CharField(max_length=100)),
                ("mobile_number", models.CharField(max_length=20)),
                ("number_of_machines", models.PositiveIntegerField()),
                ("requirement_bobin_checkbox", models.BooleanField(default=False)),
                ("requirement_tfo_checkbox", models.BooleanField(default=False)),
                ("requirement_karigar_checkbox", models.BooleanField(default=False)),
                (
                    "requirement_bobin",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                ("requirement_tfo", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "requirement_karigar",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                ("submitted", models.BooleanField(default=False)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]