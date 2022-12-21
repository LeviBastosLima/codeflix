import unittest
from dataclasses import is_dataclass, FrozenInstanceError
from datetime import datetime
from unittest.mock import patch

from src.domain.category.entities import Category


class TestCategory(unittest.TestCase):
    def test_is_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor_with_all_datas(self):
        with patch.object(Category, 'validate') as mock_validate_method:
            category = Category(
                name='Movie',
                description='Some Description',
                is_active=False,
                created_at=datetime.now()
            )

            mock_validate_method.assert_called_once()
            self.assertEqual(category.name, 'Movie')
            self.assertEqual(category.description, 'Some Description')
            self.assertEqual(category.is_active, False)
            self.assertIsInstance(category.created_at, datetime)

    @patch('src.domain.category.entities.Category.validate')
    def test_constructor_without_optional_datas(self, mock_validate_method):
        category = Category(
            name='Movie',
            description=None,
            is_active=True,
            created_at=datetime.now()
        )
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, None)
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)

    @patch('src.domain.category.entities.Category.validate')
    def test_if_is_immutable(self, mock_validate_method):
        with self.assertRaises(FrozenInstanceError):
            value_object = Category(
                name='test'
            )
            value_object.name = 'change'

    @patch('src.domain.category.entities.Category.validate')
    def test_update(self, mock_validate_method):
        mock_name = 'Series'
        mock_description = 'short description'

        category = Category(name='Movie')

        category.update(name=mock_name, description=mock_description)

        self.assertEqual(category.name, mock_name)
        self.assertEqual(category.description, mock_description)

    @patch('src.domain.category.entities.Category.validate')
    def test_activate(self, mock_validate_method):
        category = Category(name='Movie')
        category.activate()
        self.assertTrue(category.is_active)

    @patch('src.domain.category.entities.Category.validate')
    def test_deactivate(self, mock_validate_method):
        category = Category(name='Movie')
        category.deactivate()
        print(category)
        self.assertFalse(category.is_active)
