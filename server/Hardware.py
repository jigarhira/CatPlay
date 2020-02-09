"""
CatPlay
Version 1.0
Jigar Hira
June 2019
"""


import RPi.GPIO as GPIO    # Raspberry Pi GPIO Library

GPIO.setmode(GPIO.BOARD)   # Sets the pin numbering system to the physical layout

# Pin definitions
SERVO_X_PIN = 11
SERVO_Y_PIN = 13
LASER_PIN = 15

class Servo:
    """
    Servo class for servo motor control.

    Attributes:
        angle (float): current angle of the servo from -90.0 to 90.0 degrees.
        _pin (int): Physical pin number
        _pwm (GPIO.PWM): pwm instance for controlling the servo.
    """

    def __init__(self, pin: int):
        """
        Constructor for servo class. Initializes servo object, starts PWM output, and sets servo to center.
        """

        PWM_FREQUENCY = 100    # Set the PWM frequency (Hz)

        # Sets pin attribute
        self._pin = pin

        # Configures pin as output and starts PWM
        GPIO.setup(pin, GPIO.OUT)
        self._pwm = GPIO.PWM(pin, PWM_FREQUENCY)

        # Sets angle attribute and adjusts PWM for center posistion
        self.angle = 0.0
        self._pwm.start(self._angle_to_dc(0.0))

    def _angle_to_dc(self, angle: float) -> float:
        """
        Converts the angle (-90.0 to 90.0 degrees) to duty cycle (0.0 to 100.0).

        Parameters:
            angle (float): Angle from -90.0 to 90.0 degrees.

        Returns:
            float: duty cycle from 0.0 to 100.0.
        """

        return (angle + 90.0)/(1.8)

    def set_servo(self, angle: float):
        """
        Sets the posistion angle of the servo.

        Parameters:
            angle (float): Angle from -90.0 to 90.0 degrees.
        """

        # Update the angle attribute
        self.angle = angle

        # Change servo position
        self._pwm.ChangeDutyCycle(self._angle_to_dc(angle))


class Laser:
    """
    Laser class for laser pointer control.

    Attributes:
        on (bool): Laser on or off
        _pin (int): Physical pin number
    """

    def __init__(self, pin: int):
        """
        Constructor for laser class. Initializes laser object for laser pointer control.
        """

        # Sets the pin and on attributes
        self._pin = pin
        self.on = False

        # Configures GPIO pin as output and initializes pin to low
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)

    def power(self, status: bool):
        """
        Updates the power status of the laser.

        Parameters:
            status (bool): True for on and False for off
        """

        # Update the GPIO pin
        GPIO.output(self._pin, status)












# Unit test
if __name__ == '__main__':
    pass

# EOF
