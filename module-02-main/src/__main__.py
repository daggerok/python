def app():
    print("Hello World!")
    print("""
    __name__ is stored in the global namespace of the module
    along with the __doc__, __package__, and other attributes
    __name__ value is: {0}
    __doc__ value is: {1}
    __package__ value is: {2}
    """.format(repr(__name__), repr(__doc__), repr(__package__)))

if __name__ == "__main__":
    app()
