class Solution:
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()

        for x in asteroids:
            if x > mass:
                return False
            mass += x

        return True