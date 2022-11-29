import unittest
from dataclasses import is_dataclass, FrozenInstanceError
from datetime import datetime

from src.domain.category.entities import Category


class TestCategory(unittest.TestCase):
    def test_is_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor_with_all_datas(self):
        category = Category(
            name='Movie',
            description='Some Description',
            is_active=False,
            created_at=datetime.now()
        )

        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'Some Description')
        self.assertEqual(category.is_active, False)
        self.assertIsInstance(category.created_at, datetime)

    def test_constructor_without_optional_datas(self):
        category = Category(
            name='Movie',
        )

        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, None)
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)

    def test_if_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = Category(
                name='test'
            )
            value_object.name = 'change'
