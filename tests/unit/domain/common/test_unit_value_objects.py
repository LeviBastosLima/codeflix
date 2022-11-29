import unittest
import uuid
from abc import ABC
from dataclasses import is_dataclass, FrozenInstanceError, dataclass
from unittest.mock import patch

from src.domain.common.exceptions import InvalidUuiException
from src.domain.common.value_objects import UniqueEntityId, ValueObject


@dataclass(frozen=True)
class StubOneProp(ValueObject):
    prop: str


@dataclass(frozen=True)
class StubTwoProp(ValueObject):
    prop1: str
    prop2: str


class TestValueObjectUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(ValueObject))

    def test_if_is_a_abstract_class(self):
        self.assertIsInstance(ValueObject(), ABC)

    def test_init_prop(self):
        prop1 = 'Value1'
        prop2 = 'Value2'

        vo1 = StubOneProp(prop=prop1)
        self.assertEqual(vo1.prop, prop1)

        vo2 = StubTwoProp(prop1=prop1, prop2=prop2)
        self.assertEqual(vo2.prop1, prop1)
        self.assertEqual(vo2.prop2, prop2)

    def test_convert_to_string(self):
        prop1 = 'Value1'
        prop2 = 'Value2'

        vo1 = StubOneProp(prop=prop1)
        self.assertEqual(vo1.prop, str(vo1))

        expect_vo2 = '{"prop1": "Value1", "prop2": "Value2"}'
        vo2 = StubTwoProp(prop1=prop1, prop2=prop2)
        self.assertEqual(expect_vo2, str(vo2))

    def test_if_id_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            prop = 'Value'
            value_object = StubOneProp(prop=prop)
            value_object.prop = 'Nha'


class TestUniqueEntityIdUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_uuid_is_invalid(self):
        with self.assertRaises(InvalidUuiException) as assert_error:
            UniqueEntityId(id='fake_id')

        self.assertEqual(assert_error.exception.args[0], 'ID must be a valid UUID')

    def test_if_validator_is_called_once(self):
        with patch.object(
                UniqueEntityId,
                '_UniqueEntityId__validate',
                autospec=True,
                side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            UniqueEntityId()
            mock_validate.assert_called_once()

    def test_accept_uuid_passed_in_constructor(self):
        uuid4 = '3aaa851a-d31a-4de6-9971-9065ae71aded'

        value_object = UniqueEntityId(id=uuid4)

        self.assertEqual(value_object.id, uuid4)

    def test_generate_id_when_no_passed_id_in_constructor(self):
        value_object = UniqueEntityId()
        uuid.UUID(value_object.id)

    def test_if_id_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            uuid4 = '3aaa851a-d31a-4de6-9971-9065ae71aded'
            value_object = UniqueEntityId()
            value_object.id = uuid4
