class FieldIndexError(IndexError):

    def __str__(self):
        return 'Value entered outside the playing field'


class CellOcupiederror(Exception):

    def __str__(self):
        return 'There is an attempt to change the value of cell'
