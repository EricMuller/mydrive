from django.test import TestCase
# import datetime
from ged.models import Basket
from ged.models import File
from ged.models import Folder
from ged.modules.tree import Tree
#from mysite import settings
from django.conf import settings


class BasketMethodTests(TestCase):

    def test_create_basket(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        basket = Basket.create('DOWNLOAD', 'download', 'Basket download')
        # me = timezone.now() + datetime.timedelta(days=30)
        # future_question = Question(pub_date=time)
        self.assertIsNotNone(basket)
        basket.save()

    def test_create_document(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        basket = Basket.create('DOWNLOAD', 'download', 'Basket download')
        basket.save()

        basket = Basket.objects.get(libelle="download")

        document = File.create('test', 'path', 'contentType', 1, basket)

        self.assertIsNotNone(document)

        document.save()


class FolderMethodTests(TestCase):

    def test_create_folder(self):

        folder = Folder.create(1, 3, 'Plan')

        self.assertIsNotNone(folder)
        folder.save()


class FolderServiceTests(TestCase):

    @staticmethod
    def setUpClass():
        # The test runner sets DEBUG to False. Set to True to enable SQL
        # logging.
        settings.DEBUG = True
        super(FolderServiceTests, FolderServiceTests).setUpClass()

    def test_create_folder(self):

        tree = Tree()

        folder = tree.create(1, 3, 'Plan')

        self.assertIsNotNone(folder)

        folder = tree.find(folder.id)

        self.assertIsNotNone(folder)

    def test_create_child_folder(self):

        tree = Tree()

        root = tree.createRoot('Plan2')

        self.assertIsNotNone(root)

        folder = tree.createChild(root.id, 'child1')

        self.assertIsNotNone(folder)
