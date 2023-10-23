def calculate_surface_area(area_to_calculate: list[int], max_height: int) -> int:
    """
    Calculates empty surface area
    :param area_to_calculate: integer list of height values
    :param max_height the height of the area:
    :return empy surface area:
    """
    return sum(max_height - area for area in area_to_calculate)


def material(spaceship: list[int]) -> int:
    """
        Take description of a spaceship as a list and calculate empty space between materials
    :param spaceship: integer list of height values
    :return surface area:
    """
    whole_surface_area = 0
    max_idx = 0
    max_height = spaceship[0]
    for idx, height in enumerate(spaceship):
        if height >= max_height and idx != 0:
            whole_surface_area += calculate_surface_area(spaceship[max_idx:idx], max_height)
            max_height, max_idx = height, idx
        elif idx == len(spaceship) - 1 and max_idx != idx:
            remaining_area = spaceship[max_idx + 1:]
            max_value = max(remaining_area)
            idx_value = remaining_area.index(max_value)

            whole_surface_area += calculate_surface_area(remaining_area[:idx_value], max_value)
            whole_surface_area += material(remaining_area[idx_value:])

    return whole_surface_area
