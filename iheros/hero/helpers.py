import numpy as np
import math


def distanceInKmFromLatLon(center_coords, point_coords):
    """
    Return the distance in kilometers between two points using the Haversine formula
    Args: centerCoordinates<tuple>, pointCoordinates<tuple>
    Returns: distance<Float>
    """
    radius_earth = 6371  # approximate earth radius in km

    lat1, lon1 = center_coords
    lat2, lon2 = point_coords

    deg_lat = np.deg2rad(lat2 - lat1)
    deg_lon = np.deg2rad(lon2 - lon1)

    aux = math.sin(deg_lat / 2) * math.sin(deg_lat / 2) + \
        math.cos(np.deg2rad(lat1)) * \
        math.cos(np.deg2rad(lat2)) * \
        math.sin(deg_lon / 2) * \
        math.sin(deg_lon / 2)
    center = 2 * math.atan2(math.sqrt(aux), math.sqrt(1 - aux))
    distance = radius_earth * center

    return distance


def searchClosestHero(heros, location):
    """
    Return the closest_hero to the location
    Args: heros<array|Hero>, location<tuple>
    Return closest_hero<Hero>
    """
    latitude, longitude = location
    lower_distance = float('inf')
    for hero in heros:
        center_coords = latitude, longitude
        point_coords = hero.latitude, hero.longitude
        distance = distanceInKmFromLatLon(
            center_coords, point_coords)

        if distance < lower_distance:
            lower_distance = distance
            closest_hero = hero

    return closest_hero
