# Generated by Django 4.0.3 on 2022-03-18 09:13

from django.db import migrations, models
import simetra_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('simetra_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='area_active_zone',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='area_metro_coverage',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='area_stops_coverage_active_zone',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='avrg_age_bus',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='avrg_age_electrobus',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='avrg_age_metro_car',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='avrg_age_tramway_car',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='avrg_age_trolleybus',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='bool_day_tariff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='city',
            name='bool_long_time_tariff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='city',
            name='bool_nfc_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='city',
            name='bool_online_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='city',
            name='bool_transfer_tariff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='city',
            name='bool_universal_transport_card',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='city',
            name='cost_one_travel_ticket',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='cost_transfer_ticket',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='density_stops_active_zone',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='income_avrg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='length_UDS',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='length_avrg_between_stops',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='length_avrg_bus_route',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='length_avrg_tramway_route',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='length_avrg_trolleybus_route',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='length_existing_tramway_routes',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='length_existing_trolleybus_routes',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='length_in_use_tramway_routes',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='length_in_use_trolleybus_routes',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='length_overall_unrailed_path',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_accidents',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_accidents_per_unit',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_big_buses_registry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_big_tramway_cars_registry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_big_trollebuses_registry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_buses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_buses_registry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_death_toll',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_electrobuses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_in_use_bus_routes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_in_use_overall_routes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_in_use_tramway_routes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_in_use_trolleybus_routes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_low_profile_buses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_low_profile_electrobuses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_low_profile_tramway_cars',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_low_profile_trolleybuses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_medium_buses_registry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_metro_cars',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_new_GET',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_new_buses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_of_apartments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_people_metro_access',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_people_transport_access',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_population',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_regulated_routes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_routes_with_ticket',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_routes_with_transfer_ticket',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_small_buses_registry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_tramway_cars',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_tramway_cars_registry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_trollebuses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_trollebuses_registry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_unregulated_routes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_very_big_buses_registry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_very_big_tramway_cars_registry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_very_big_trollebuses_registry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_wndd_n_dead_per_people',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_working_buses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_working_electrobuses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_working_metro_cars',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_working_stops_active_zone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_working_stops_overall',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_working_tramway_cars',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_working_trollebuses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_wounded',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='num_wounded_per_accident',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_big_capacity_transport',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_elctro_transport',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_low_profile_transport',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_metro_covered_area',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_people_metro_access',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_people_transport_access',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_renew_program',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_tramway_net_use',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_tramway_routes_isolation',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_transport_covered_area',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_trolleybus_net_use',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_working_buses',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_working_electrobuses',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_working_metro_cars',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_working_tramway_cars',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_working_transport',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='percent_working_trollebuses',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='rating_affordability',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='rating_comfort_n_convenience',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='rating_physical_availability',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='rating_route_network_efficiency',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='rating_security_n_development',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='ratio_ticket_cost_income',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='real_time_internet_movement_information',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='route_coefficient',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='salary_avrg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='share_unregulated_routes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='time_avrg_waiting_any_transport',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='time_avrg_waiting_specific_transport',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='traffic_metro',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='traffic_transport',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='transport_app_existance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='transport_movement_schedule_website',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='transport_route_net_map',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='city',
            name='unique_transporte_style',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='boss',
            name='image',
            field=models.ImageField(default='default-boss.jpg', upload_to=simetra_app.models.Boss.get_upload_path),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='default-employee.jpg', upload_to=simetra_app.models.Employee.get_upload_path),
        ),
    ]
