from typing import Union

from . import bindings
from .error import VdrError, VdrErrorCode


class Request:
    def __init__(self, handle: bindings.RequestHandle):
        self.handle = handle

    @property
    def body(self):
        if not self.handle:
            raise VdrError(VdrErrorCode.WRAPPER, "no request handle")
        return bindings.request_get_body(self.handle)

    @property
    def signature_input(self):
        if not self.handle:
            raise VdrError(VdrErrorCode.WRAPPER, "no request handle")
        return bindings.request_get_signature_input(self.handle)

    def set_endorser(self, endorser: str):
        if not self.handle:
            raise VdrError(VdrErrorCode.WRAPPER, "no request handle")
        bindings.request_set_endorser(self.handle, endorser)

    def set_signature(self, signature: bytes):
        if not self.handle:
            raise VdrError(VdrErrorCode.WRAPPER, "no request handle")
        bindings.request_set_signature(self.handle, signature)

    def set_taa_acceptance(self, acceptance: Union[str, dict]):
        if not self.handle:
            raise VdrError(VdrErrorCode.WRAPPER, "no request handle")
        bindings.request_set_taa_acceptance(self.handle, acceptance)

    def __del__(self):
        if self.handle:
            bindings.request_free(self.handle)
            self.handle = None

    def __repr__(self):
        if not self.handle:
            return f"{self.__class__.__name__}(freed)"
        return super().__repr__(self)
