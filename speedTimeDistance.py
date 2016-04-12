def calculatespeedtimedistance(speed=None, time=None, distance=None):
        if distance and time:
            speed = distance / float(time)
        elif distance and speed:
            time = distance / float(speed)
        elif speed and time:
            distance = speed * time
        else:
            raise AttributeError("Please pass at least two values among speed, time and distance.")

        return {"speed": speed, "time": time, "distance": distance}

if __name__ == "__main__":
    print(str(calculatespeedtimedistance(time=10, distance=11)))
    print(str(calculatespeedtimedistance(speed=10, distance=11)))
    print(str(calculatespeedtimedistance(time=10, speed=11)))
