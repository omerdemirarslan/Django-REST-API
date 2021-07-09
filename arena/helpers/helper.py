""" This File Contains Generel Helper Functions For You :) """
import csv


def download_csv(modeladmin, request, queryset):
    """
    This Function Saves User Information as CSV File.
    :param modeladmin:
    :param request:
    :param queryset:
    """
    with open('gamer_user.csv', 'w') as file:
        writer = csv.writer(file)

        for item in queryset:
            writer.writerow([
                item.full_name,
                item.username,
                item.email,
                item.is_active,
                item.birthdate,
                item.about
            ])


download_csv.short_description = "Export as CSV"
