import unittest
from abc import ABC
from dataclasses import is_dataclass, dataclass

from src.domain.common.entities import EntityBase
from src.domain.common.value_objects import UniqueEntityId


@dataclass(frozen=True, kw_only=True)
class StubEntity(EntityBase):
    prop1: str
    prop2: str


class TestEntityUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(EntityBase))

    def test_if_is_a_abstract_class(self):
        self.assertIsInstance(EntityBase(), ABC)

    def test_set_id_and_props(self):
        prop1 = 'value1'
        prop2 = 'value2'

        entity = StubEntity(prop1=prop1, prop2=prop2)
        self.assertEqual(entity.prop1, prop1)
        self.assertEqual(entity.prop2, prop2)
        self.assertIsInstance(entity.unique_entity_id, UniqueEntityId)
        self.assertEqual(entity.unique_entity_id.id, entity.id)
