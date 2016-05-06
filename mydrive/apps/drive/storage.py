

class Store:

    def ___init__(self):
        pass


class FileStore(Store):

    def ___init__(self, rootPath):
        Store.___init__(self)
        self.rootPath = rootPath

    def _getPath(document):

        pass

    def store(self, document):
        path = self._getPath(document)

        pass


class DataBaseStore(Store):

    def ___init__(self, databaseName='default'):
        Store.___init__(self)


class FileUtil:
    pass
