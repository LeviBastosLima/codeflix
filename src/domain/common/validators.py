from dataclasses import dataclass
from typing import Any
from .exceptions import ValidationException


@dataclass(frozen=True, slots=True)
class ValidatorRules:
    value: Any
    prop: str

    def required(self) -> 'ValidatorRules':
        if self.value is None or self.value == '':
            raise ValidationException(f'O {self.prop} é obrigatório')
        return self

    def string(self) -> 'ValidatorRules':
        if self.value is not None and not isinstance(self.value, str):
            raise ValidationException(f'O {self.prop} deve ser string')
        return self

    def max_length(self, max_length: int) -> 'ValidatorRules':
        if self.value is not None and len(self.value) > max_length:
            raise ValidationException(f'O {self.prop} deve possuir a quantidade caracteres menor que {max_length}')
        return self

    def boolean(self) -> 'ValidatorRules':
        if self.value is not None and self.value is not True and self.value is not False:
            raise ValidationException(f'O {self.prop} deve ser boolean')
        return self
