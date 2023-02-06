"""Shapes that are composed of lines."""

from .shape import Shape


class Lines(Shape):
    """Class representing a shape consisting of multiple lines."""

    def __init__(self, *lines) -> None:
        self.lines = lines

    def distance(self, x, y) -> float:
        return min(
            self.distance_point_to_line(point=(x, y), line=line) for line in self.lines
        )

    def distance_point_to_line(self, point, line) -> float:
        """
        Calculate the minimum distance between a point and a line.

        Notes
        -----
        Implementation based on `this VBA code`_

        .. this VBA code: http://local.wasp.uwa.edu.au/~pbourke/geometry/pointline/source.vba

        Parameters
        ----------
        point : Iterable[int|float]
            Coordinates of a point in 2D space.
        line : Iterable[Iterable[int|float]]
            Coordinates of the endpoints of a line in 2D space.

        Returns
        -------
        float
            The minimum distance between the point and the line.
        """
        start, end = line
        line_mag = self._euclidean_distance(start, end)

        if line_mag < 0.00000001:
            # Arbitrarily large value
            return 9999

        px, py = point
        x1, y1 = start
        x2, y2 = end

        u1 = ((px - x1) * (x2 - x1)) + ((py - y1) * (y2 - y1))
        u = u1 / (line_mag * line_mag)

        if (u < 0.00001) or (u > 1):
            # closest point does not fall within the line segment, take the shorter
            # distance to an endpoint
            distance = max(
                self._euclidean_distance(point, start),
                self._euclidean_distance(point, end),
            )
        else:
            # Intersecting point is on the line, use the formula
            ix = x1 + u * (x2 - x1)
            iy = y1 + u * (y2 - y1)
            distance = self._euclidean_distance(point, (ix, iy))

        return distance
