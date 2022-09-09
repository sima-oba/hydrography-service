from http import HTTPStatus
from flask import Flask, jsonify
from marshmallow.exceptions import ValidationError
from mongoengine.errors import OperationError
from pymongo.errors import OperationFailure

from domain.exception import EntityNotFound


def handle_validation_error(error: ValidationError):
    return jsonify(error.messages), HTTPStatus.BAD_REQUEST


def handle_database_error(error: OperationFailure):
    return jsonify({'error': str(error)}), HTTPStatus.INTERNAL_SERVER_ERROR


def handle_entity_not_found(error: EntityNotFound):
    return jsonify({'error': str(error)}), HTTPStatus.BAD_REQUEST


def register(flask: Flask):
    flask.register_error_handler(ValidationError, handle_validation_error)
    flask.register_error_handler(OperationError, handle_database_error)
    flask.register_error_handler(EntityNotFound, handle_entity_not_found)
