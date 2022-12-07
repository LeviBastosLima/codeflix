import unittest
from dataclasses import is_dataclass, FrozenInstanceError
from datetime import datetime

from src.domain.category.entities import Category


class TestCategory(unittest.TestCase):
    def setUp(self) -> None:
        self.category = Category(
            name='Movie',
        )

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
        self.assertEqual(self.category.name, 'Movie')
        self.assertEqual(self.category.description, None)
        self.assertEqual(self.category.is_active, True)
        self.assertIsInstance(self.category.created_at, datetime)

    def test_if_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = Category(
                name='test'
            )
            value_object.name = 'change'

    def test_update(self):
        mock_name = 'Series'
        mock_description = 'short description'

        category = Category(name='Movie')

        category.update(name=mock_name, description=mock_description)

        self.assertEqual(category.name, mock_name)
        self.assertEqual(category.description, mock_description)

    def test_activate(self):
        category = Category(name='Movie')
        category.activate()
        self.assertTrue(category.is_active)

    def test_deactivate(self):
        category = Category(name='Movie')
        category.deactivate()
        print(category)
        self.assertFalse(category.is_active)
