# Exceptions in Python

1. Raising Exceptions
    ``` python
    def raising_exception():
        raise <Exception>
    ```

2. Catching Exceptions
    ``` python
    def catching_exception():
        try:
            div = 12 / 0
        except ZeroDivisionError:
            print("Attempted to divide by Zero")

    ```
