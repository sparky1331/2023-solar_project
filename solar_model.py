# coding: utf-8
# license: GPLv3
import math

G = 6.67408e-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
        # G = 6.6743 * (10 ** (-11))
        F = (G * body.mass * obj.mass) / (r**2)
        Ugol = math.atan2(obj.y - body.y, obj.x - body.x)
        body.Fx += F * math.cos(Ugol)
        body.Fy += F * math.sin(Ugol)


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.mass
    ay = body.Fy / body.mass
    body.x += body.Vx * dt + (ax * (dt**2)) / 2
    body.y += body.Vy * dt + (ay * (dt**2)) / 2
    body.Vx += ax * dt
    body.Vy += ay * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
