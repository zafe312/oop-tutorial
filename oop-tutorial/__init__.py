# __init__.py

# Importing classes and functions from base, advanced, and utils modules

# Base module (OOP fundamentals)
from .base import Animal, Dog, Cat

# Advanced module (OOP advanced concepts like abstraction and polymorphism)
from .advanced import Vehicle, Car, Airplane, vehicle_sound

# Utils module (helper functions)
from .utils import print_with_borders, read_json, log_to_file

# Defining the public API for the package
__all__ = [
    'Animal',  # Base class for all animals
    'Dog',     # Dog class, inherits from Animal
    'Cat',     # Cat class, inherits from Animal
    'Vehicle', # Abstract base class for vehicles
    'Car',     # Car class, inherits from Vehicle
    'Airplane',# Airplane class, inherits from Vehicle
    'vehicle_sound',  # Function demonstrating polymorphism
    'print_with_borders',  # Utility function for printing messages with borders
    'read_json',           # Utility function for reading JSON data
    'log_to_file'          # Utility function for logging messages to a file
]
