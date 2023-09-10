
from logging import LogRecord
from logging.handlers import QueueHandler


class ObjectQueueHandler(QueueHandler):
    """QueueHandler that preserves message as an object in the separate field - msg_object."""

    def prepare(self, record: LogRecord) -> LogRecord:
        """Create msg_object as raw message before it will be formatted as str."""

        setattr(record, 'msg_object', record.msg)
        setattr(record, 'exc_info_object', record.exc_info)

        record = super().prepare(record)

        return record
