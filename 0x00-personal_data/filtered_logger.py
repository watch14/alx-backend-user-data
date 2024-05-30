#!/usr/bin/env python3
"""
filtered_logger module
"""
import re
import logging
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """
    Replaces field values in a log message with a redaction string.
    """
    pattern = f"({'|'.join(fields)})=.+?{separator}"
    return re.sub(
            pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message
            )


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with specific fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record, redacting specified fields.
        """
        original_message = super(RedactingFormatter, self).format(record)
        return filter_datum(
                self.fields, self.REDACTION, original_message, self.SEPARATOR)
