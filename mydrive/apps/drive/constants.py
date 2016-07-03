
from drive.models import TypeRepository


class MetaConst(type):
    def __getattr__(cls, key):
        return cls[key]

    def __setattr__(cls, key, value):
        raise TypeError


class Const(object, metaclass=MetaConst):
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        raise TypeError


class Constants(Const):
    DEFAULT_TYPE_CODE = 'DRVF'

    def get_default_type(self):
        type = TypeRepository.objects.get(
            code=self.DEFAULT_TYPE_CODE)
        return type


DriveConstants = Constants()
