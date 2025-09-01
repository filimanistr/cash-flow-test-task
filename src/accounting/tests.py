from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from accounting.models import Transaction

from . import selectors

# TODO: закончить


class TransactionTestCase(TestCase):
    """Тесты опираются на требования в тз"""
    fixtures = ['references', 'transactions']

    @classmethod
    def setUpTestData(cls):
        cls.transactions = Transaction.objects.all()

    def test_transactions_listed(self):
        """Вывод таблицы со всеми данными"""
        response = self.client.get("/")
        transactions = response.context['transaction_list'].values()
        self.assertTrue(len(transactions) == len(self.transactions))

    def test_all_columns_listed(self):
        """Вывод таблицы с данными: дата, статус, тип, категория, подкатегория, сумма, комментарий"""
        response = self.client.get("/")
        transactions = response.context['transaction_list'].values()[0]
        columns = ['created_at', 'status_id', 'type_id', 'category_id', 'subcategory_id', 'amount', 'comment']
        [self.assertTrue(column in transactions) for column in columns]
        self.assertTrue(len(transactions)-1 == len(columns))  # -1 for id that's not shown

    def test_crud_operations(self):
        create_response = self.client.post("/transactions/create/", {
            "created_at": "2025-09-02",
            "status": "1",
            "type": "1",
            "category": "6",
            "subcategory": "11",
            "amount": "110.10",
        })
        #update_response
        #get_response
        #print(response)
        # models.Transactions.get()

    def test_subcategories_filtered(self):
        pass

    def test_subcategories_chained_with_categories(self):
        """Пользователь не может выбрать подкатегорию, если она не связана с выбранной категорией"""
        pass

    def test_categories_chained_with_types(self):
        """Пользователь не может выбрать категорию, если она не относится к выбранному типу"""
        pass

    def test_fields_are_required(self):
        # ПОСТ кинуть сюда с полями незаполненными
        #я "сумма", "тип", "категория" и "подкатегория" о
        pass


class TransactionFilteringTestCase(TestCase):
    fixtures = ['references', 'transactions']

    @classmethod
    def setUpTestData(cls):
        cls.transactions = Transaction.objects.all()

    def test_date_filtering(self):
        greater = self.client.get("/?created_at__gte=2025-09-02")
        less = self.client.get("/?created_at__lte=2025-09-02")
        between = self.client.get("/?created_at__gte=2025-09-01&created_at__lte=2025-09-02")
        between_unorder = self.client.get("/?created_at__lte=2025-09-02&created_at__gte=2025-09-01")

        db_greater = self.transactions.filter(created_at__gte='2025-09-02')
        db_less = self.transactions.filter(created_at__lte='2025-09-02')
        db_between = self.transactions.filter(created_at__gte='2025-09-01', created_at__lte='2025-09-02')
        db_between_unorder = self.transactions.filter(created_at__lte='2025-09-02', created_at__gte='2025-09-01')

        self.assertEqual(len(greater.context['transaction_list'].values()), len(db_greater))
        self.assertEqual(len(less.context['transaction_list'].values()), len(db_less))
        self.assertEqual(len(between.context['transaction_list'].values()), len(db_between))
        self.assertEqual(len(between_unorder.context['transaction_list'].values()), len(db_between_unorder))

    def test_status_filtering(self):
        response = self.client.get("/?status__pk=1")
        context_transactions = response.context['transaction_list'].values()
        db_transactions = self.transactions.filter(status=1)
        self.assertEqual(len(context_transactions), len(db_transactions))

    def test_type_filtering(self):
        response = self.client.get("/?type__pk=1")
        context_transactions = response.context['transaction_list'].values()
        db_transactions = self.transactions.filter(type=1)
        self.assertEqual(len(context_transactions), len(db_transactions))

    def test_category_filtering(self):
        response = self.client.get("/?category__pk=6")
        context_transactions = response.context['transaction_list'].values()
        db_transactions = self.transactions.filter(category=6)
        self.assertEqual(len(context_transactions), len(db_transactions))

    def test_subcategory_filtering(self):
        response = self.client.get("/?subcategory__pk=11")
        context_transactions = response.context['transaction_list'].values()
        db_transactions = self.transactions.filter(subcategory=11)
        self.assertEqual(len(context_transactions), len(db_transactions))


class ReferencesTestCase(TestCase):
    fixtures = ['references']

    def test_crud_operations(self):
        pass
