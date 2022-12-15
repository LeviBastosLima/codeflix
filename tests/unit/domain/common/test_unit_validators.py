import unittest

from domain.common.exceptions import ValidationException
from domain.common.validators import ValidatorRules


class TestValidatorRules(unittest.TestCase):

    def test_values_method(self):
        validator = ValidatorRules('some value', 'prop')

        self.assertIsInstance(validator, ValidatorRules)
        self.assertEqual(validator.value, 'some value')
        self.assertEqual(validator.prop, 'prop')

    def test_required_method_with_None_value(self):
        with self.assertRaises(ValidationException) as actual_error:
            ValidatorRules(None, 'prop').required()

        expect_error = 'O prop é obrigatório'
        self.assertEqual(expect_error, actual_error.exception.args[0])

    def test_required_method_with_empty_value(self):
        with self.assertRaises(ValidationException) as actual_error:
            ValidatorRules('', 'prop').required()

        expect_error = 'O prop é obrigatório'
        self.assertEqual(expect_error, actual_error.exception.args[0])

    def test_required_method_with_string_value(self):
        validator = ValidatorRules('Valido', 'prop').required()
        self.assertIsInstance(validator, ValidatorRules)

    def test_required_method_with_int_value(self):
        validator = ValidatorRules(515, 'prop').required()
        self.assertIsInstance(validator, ValidatorRules)

    def test_string_method_with_None_value(self):
        validator = ValidatorRules(None, 'prop').string()
        self.assertIsInstance(validator, ValidatorRules)

    def test_string_method_with_empty_value(self):
        validator = ValidatorRules('', 'prop').string()
        self.assertIsInstance(validator, ValidatorRules)

    def test_string_method_with_string_value(self):
        validator = ValidatorRules('Valido', 'prop').string()
        self.assertIsInstance(validator, ValidatorRules)

    def test_string_method_with_int_value(self):
        with self.assertRaises(ValidationException) as actual_error:
            ValidatorRules(515, 'prop').string()

        expect_error = 'O prop deve ser string'
        self.assertEqual(expect_error, actual_error.exception.args[0])

    def test_max_length_successful(self):
        validator = ValidatorRules('Valido', 'prop').max_length(max_length=80)
        self.assertIsInstance(validator, ValidatorRules)

    def test_max_length_fail(self):
        with self.assertRaises(ValidationException) as actual_error:
            ValidatorRules('Invalido', 'prop').max_length(max_length=5)

        expect_error = 'O prop deve possuir a quantidade caracteres menor que 5'
        self.assertEqual(expect_error, actual_error.exception.args[0])

    def test_max_length_with_None_value(self):
        validator = ValidatorRules(None, 'prop').max_length(max_length=5)
        self.assertIsInstance(validator, ValidatorRules)

    def test_boolean_method_successful(self):
        validator = ValidatorRules(False, 'prop').boolean()
        self.assertIsInstance(validator, ValidatorRules)

    def test_boolean_method_failed(self):
        with self.assertRaises(ValidationException) as actual_error:
            ValidatorRules('invalido', 'prop').boolean()

        expect_error = 'O prop deve ser boolean'
        self.assertEqual(expect_error, actual_error.exception.args[0])

    def test_boolean_method_with_None_value(self):
        validator = ValidatorRules(None, 'prop').boolean()
        self.assertIsInstance(validator, ValidatorRules)

    # TODO: criar testes com os métodos aninhados