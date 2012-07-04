from . import CDB
from .. import SCSIWriteCommand
from .operation_code import OperationCode
from .control import Control, DEFAULT_CONTROL
from infi.instruct import *
from ..errors import AsiException
# spc4r30: 6.4.1 (page 259)

CDB_OPCODE_WRITE_6 = 0x0A
CDB_OPCODE_WRITE_10 = 0x2A

# TODO move this
DEFAULT_BLOCK_SIZE = 512

class Write6Command(CDB):
    _fields_ = [
        ConstField("opcode", OperationCode(opcode=CDB_OPCODE_WRITE_6)),
        BitFields(
            BitField("logical_block_address__msb", 5),
            BitPadding(3),
            ),
        UBInt16("logical_block_address__lsb"),
        UBInt8("transfer_length"),
        Field("control", Control, DEFAULT_CONTROL)
    ]

    def __init__(self, logical_block_address, buffer, block_size=DEFAULT_BLOCK_SIZE):
        super(Write6Command, self).__init__()
        self.logical_block_address = logical_block_address
        self.buffer = buffer
        self.block_size = block_size
        self.transfer_length = len(buffer) / block_size
        assert len(buffer) % block_size == 0, "buffer length {0} is not a multiple of {1}".format(len(buffer), block_size)

    def execute(self, executer):
        assert self.logical_block_address < 2 ** 21
        assert self.transfer_length < 2 ** 8

        self.logical_block_address__msb = self.logical_block_address >> 16
        self.logical_block_address__lsb = self.logical_block_address & 0xffff

        datagram = self.create_datagram()

        result_datagram = yield executer.call(SCSIWriteCommand(datagram, self.buffer))

        yield result_datagram

class Write10Command(CDB):
    _fields_ = [
                ConstField("opcode", OperationCode(opcode=CDB_OPCODE_WRITE_10)),
                BitFields(
                          BitPadding(1),
                          BitFlag("fua_nv", 0),
                          BitPadding(1),
                          BitFlag("fua", 0),
                          BitFlag("dpo", 0),
                          BitField("rdprotect", 3, 0),
                          ),
                UBInt32("logical_block_address"),
                BitFields(
                          BitField("group_number", 5, 0),
                          BitPadding(3)),
                UBInt16("transfer_length"),
                Field("control", Control, DEFAULT_CONTROL)
                ]

    def __init__(self, logical_block_address, buffer, block_size=DEFAULT_BLOCK_SIZE):
        super(Write10Command, self).__init__()
        self.logical_block_address = logical_block_address
        self.buffer = buffer
        self.block_size = block_size
        self.transfer_length = len(buffer) / block_size
        assert len(buffer) % block_size == 0, "buffer length {0} is not a multiple of {1}".format(len(buffer), block_size)

    def execute(self, executer):
        assert self.logical_block_address < 2 ** 32
        assert self.transfer_length < 2 ** 16
        datagram = self.create_datagram()
        result_datagram = yield executer.call(SCSIWriteCommand(datagram, self.buffer))

        yield result_datagram