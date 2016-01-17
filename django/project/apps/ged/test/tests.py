from django.test import TestCase
# import datetime
from mysite.apps.ged.models import Basket
from mysite.apps.ged.models import Document


class BasketMethodTests(TestCase):

    def test_create_basket(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        basket = Basket.create('download', 'Basket download')
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

        document = Document.create('test', 'path', 'contentType', 1, basket)

        self.assertIsNotNone(document)

        document.save()
