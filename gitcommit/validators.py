from prompt_toolkit.validation import Validator, ValidationError
import re


class TypeValidator(Validator):
    def __init__(self, valid_types: list):
        self.valid_types = valid_types
        super().__init__()

    def validate(self, document):
        text = document.text
        if text not in self.valid_types:
            raise ValidationError(message="That is not a valid type.")


class YesNoValidator(Validator):
    def validate(self, document):
        text = document.text
        if text.lower().strip() not in ["", "y", "n", "yes", "no"]:
            raise ValidationError(message="Answer must be yes/no.")


class DescriptionValidator(Validator):
    def __init__(self, maximum_chars: int):
        if maximum_chars < 0:
            raise ValueError("Cannot have sub-zero maximum")
        self.max_chars_allowed = maximum_chars
        super().__init__()

    def validate(self, document):
        text = document.text

        if text.strip() == "":
            raise ValidationError(message="You must write a description.")

        if len(text) > self.max_chars_allowed:
            num_chars_overflowed = len(text) - self.max_chars_allowed
            raise ValidationError(
                message=f"You are {num_chars_overflowed} characters over the limit."
            )


class FooterValidator(Validator):
    def __init__(self, session):
        self.session = session

    def validate(self, document):
        text = document.text
        if text.strip() != "":
            self.session.multiline = True
        else:
            self.session.multiline = False

        if text.strip() != "":
            input_lines = text.split("\n")
            for line in input_lines:
                matches_incomplete = [
                    m[0]
                    for m in re.findall(
                        r"(\[\s*(ch|branch(\s*ch)?)\s*[0-9]+\s*\]?)", line
                    )
                ]  # rough matches
                matches_complete = [
                    m[0] for m in re.findall(r"(\[(ch|branch ch)[0-9]+\])", line)
                ]  # strict matches

                if len(matches_incomplete) != len(matches_complete):
                    for match in matches_incomplete:
                        if match not in matches_complete:
                            raise ValidationError(
                                message="An invalid Clubhouse reference was found: "
                                + str(match)
                            )