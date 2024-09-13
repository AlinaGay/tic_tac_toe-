class FieldIndexError(IndexError):

    def __str__(self):
        return 'Value entered outside the playing field'
