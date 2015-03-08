from infi.unittest import TestCase


SES_CONFIGURATION_PAGE_SAMPLE = \
    (b"\x01\x00\x00\xCC" +
     b"\x00\x00\x00\x01\x22\x00\x08\x24\x50\x00\x93\xd0\x00\x5f\xc0\x00" +
     b"\x4e\x45\x57\x49\x53\x59\x53\x20\x4e\x44\x53\x2d\x34\x36\x30\x30" +
     b"\x2d\x4a\x44\x20\x20\x20\x20\x20\x42\x35\x30\x37\x17\x3c\x00\x10" +
     b"\x9e\x01\x00\x10\x02\x02\x00\x10\x03\x04\x00\x10\x04\x06\x00\x10" +
     b"\x06\x01\x00\x10\x07\x02\x00\x10\x18\x06\x00\x10\x41\x72\x72\x61" +
     b"\x79\x20\x44\x65\x76\x20\x53\x6c\x6f\x74\x20\x20\x34\x36\x30\x30" +
     b"\x20\x45\x6e\x63\x6c\x6f\x73\x75\x72\x65\x20\x20\x50\x6f\x77\x65" +
     b"\x72\x20\x53\x75\x70\x70\x6c\x79\x20\x20\x20\x20\x43\x6f\x6f\x6c" +
     b"\x69\x6e\x67\x20\x46\x61\x6e\x20\x20\x20\x20\x20\x54\x65\x6d\x70" +
     b"\x20\x53\x65\x6e\x73\x6f\x72\x20\x20\x20\x20\x20\x42\x75\x7a\x7a" +
     b"\x65\x72\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x45\x53\x20\x50" +
     b"\x72\x6f\x63\x65\x73\x73\x6f\x72\x20\x20\x20\x20\x53\x41\x53\x20" +
     b"\x45\x78\x70\x61\x6e\x64\x65\x72\x20\x20\x20\x20")


SES_ENCL_STATUS_PAGE_SAMPLE = \
    (b"\x01\x00\x00\xCC" +
     b"\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00" +
     b"\x00\x00\x00\x20\x01\x00\x00\x20\x01\x00\x00\x20\x00\x00\x00\x00" +
     b"\x01\x03\x89\x25\x01\x03\x8e\x25\x01\x03\x8b\x25\x01\x03\x90\x25" +
     b"\x00\x00\x00\x00\x01\x00\x37\x00\x01\x00\x36\x00\x01\x00\x38\x00" +
     b"\x01\x00\x3a\x00\x01\x00\x30\x00\x01\x00\x30\x00\x00\x00\x00\x00" +
     b"\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x01\x00" +
     b"\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00" +
     b"\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00")


SES_ELEMENT_DESCR_PAGE_SAMPLE = \
    (b"\x01\x00\x00\xCC" +
     b"\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x20\x31\x20\x30\x30\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x20\x32\x20\x30\x31\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x20\x33\x20\x30\x32\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x20\x34\x20\x30\x33\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x20\x35\x20\x30\x34\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x20\x36\x20\x30\x35\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x20\x37\x20\x30\x36\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x20\x38\x20\x30\x37\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x20\x39\x20\x30\x38\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x31\x30\x20\x30\x39\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x31\x31\x20\x30\x41\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x31\x32\x20\x30\x42\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x31\x33\x20\x31\x30\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x31\x34\x20\x31\x31\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x31\x35\x20\x31\x32\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x31\x36\x20\x31\x33\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x31\x37\x20\x31\x34\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x31\x38\x20\x31\x35\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x31\x39\x20\x31\x36\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x32\x30\x20\x31\x37\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x32\x31\x20\x31\x38\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x32\x32\x20\x31\x39\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x32\x33\x20\x31\x41\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x32\x34\x20\x31\x42\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x32\x35\x20\x32\x30\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x32\x36\x20\x32\x31\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x32\x37\x20\x32\x32\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x32\x38\x20\x32\x33\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x32\x39\x20\x32\x34\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x33\x30\x20\x32\x35\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x33\x31\x20\x32\x36\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x33\x32\x20\x32\x37\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x33\x33\x20\x32\x38\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x33\x34\x20\x32\x39\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x33\x35\x20\x32\x41\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x33\x36\x20\x32\x42\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x33\x37\x20\x33\x30\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x33\x38\x20\x33\x31\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x33\x39\x20\x33\x32\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x34\x30\x20\x33\x33\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x34\x31\x20\x33\x34\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x34\x32\x20\x33\x35\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x34\x33\x20\x33\x36\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x34\x34\x20\x33\x37\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x34\x35\x20\x33\x38\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x34\x36\x20\x33\x39\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x34\x37\x20\x33\x41\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x34\x38\x20\x33\x42\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x34\x39\x20\x34\x30\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x35\x30\x20\x34\x31\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x35\x31\x20\x34\x32\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x35\x32\x20\x34\x33\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x35\x33\x20\x34\x34\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x35\x34\x20\x34\x35\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x35\x35\x20\x34\x36\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x35\x36\x20\x34\x37\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x35\x37\x20\x34\x38\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x35\x38\x20\x34\x39\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x35\x39\x20\x34\x41\x20\x20\x00\x00\x00\x0c\x53\x4c\x4f\x54" +
     b"\x20\x36\x30\x20\x34\x42\x20\x20\x00\x00\x00\x00\x00\x00\x00\xa8" +
     b"\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20" +
     b"\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20" +
     b"\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20" +
     b"\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x54\x43\x41\x2d" +
     b"\x30\x30\x33\x34\x31\x2d\x30\x31\x2d\x42\x2d\x41\x32\x20\x20\x20" +
     b"\x4d\x58\x45\x33\x34\x30\x30\x30\x32\x38\x38\x52\x42\x30\x33\x31" +
     b"\x54\x43\x41\x2d\x30\x30\x33\x34\x30\x2d\x30\x31\x2d\x42\x20\x20" +
     b"\x4d\x58\x45\x33\x34\x30\x30\x30\x32\x38\x50\x52\x41\x31\x36\x31" +
     b"\x54\x43\x41\x2d\x30\x30\x33\x34\x30\x2d\x30\x31\x2d\x42\x20\x20" +
     b"\x4d\x58\x45\x33\x34\x30\x30\x30\x32\x38\x56\x52\x41\x31\x30\x43" +
     b"\x30\x30\x30\x39\x30\x30\x30\x31\x00\x00\x00\x00\x00\x00\x00\x5c" +
     b"\x50\x43\x4d\x20\x41\x20\x20\x20\x50\x57\x52\x2d\x30\x30\x30\x35" +
     b"\x39\x2d\x30\x31\x2d\x42\x30\x30\x54\x48\x44\x45\x4c\x30\x30\x30" +
     b"\x31\x35\x4e\x52\x45\x31\x32\x46\x41\x31\x30\x30\x30\x30\x30\x30" +
     b"\x54\x44\x50\x53\x2d\x31\x32\x30\x30\x41\x42\x20\x41\x30\x30\x30" +
     b"\x41\x42\x4d\x54\x31\x31\x32\x31\x30\x30\x31\x38\x31\x32\x30\x30" +
     b"\x30\x30\x46\x30\x30\x30\x30\x30\x30\x31\x30\x39\x00\x00\x00\x5c" +
     b"\x50\x43\x4d\x20\x42\x20\x20\x20\x50\x57\x52\x2d\x30\x30\x30\x35" +
     b"\x39\x2d\x30\x31\x2d\x42\x30\x30\x54\x48\x44\x45\x4c\x30\x30\x30" +
     b"\x31\x35\x4e\x52\x45\x31\x35\x33\x41\x31\x30\x30\x30\x30\x30\x30" +
     b"\x54\x44\x50\x53\x2d\x31\x32\x30\x30\x41\x42\x20\x41\x30\x30\x30" +
     b"\x41\x42\x4d\x54\x31\x31\x32\x31\x30\x30\x31\x38\x34\x38\x30\x30" +
     b"\x30\x30\x46\x30\x30\x30\x30\x30\x30\x31\x30\x39\x00\x00\x00\x00" +
     b"\x00\x00\x00\x28\x50\x43\x4d\x41\x46\x41\x4e\x31\x50\x57\x52\x2d" +
     b"\x30\x30\x30\x35\x39\x2d\x30\x31\x2d\x42\x30\x30\x54\x48\x44\x45" +
     b"\x4c\x30\x30\x30\x31\x35\x4e\x52\x45\x31\x32\x46\x00\x00\x00\x28" +
     b"\x50\x43\x4d\x41\x46\x41\x4e\x32\x50\x57\x52\x2d\x30\x30\x30\x35" +
     b"\x39\x2d\x30\x31\x2d\x42\x30\x30\x54\x48\x44\x45\x4c\x30\x30\x30" +
     b"\x31\x35\x4e\x52\x45\x31\x32\x46\x00\x00\x00\x28\x50\x43\x4d\x42" +
     b"\x46\x41\x4e\x31\x50\x57\x52\x2d\x30\x30\x30\x35\x39\x2d\x30\x31" +
     b"\x2d\x42\x30\x30\x54\x48\x44\x45\x4c\x30\x30\x30\x31\x35\x4e\x52" +
     b"\x45\x31\x35\x33\x00\x00\x00\x28\x50\x43\x4d\x42\x46\x41\x4e\x32" +
     b"\x50\x57\x52\x2d\x30\x30\x30\x35\x39\x2d\x30\x31\x2d\x42\x30\x30" +
     b"\x54\x48\x44\x45\x4c\x30\x30\x30\x31\x35\x4e\x52\x45\x31\x35\x33" +
     b"\x00\x00\x00\x00\x00\x00\x00\x2c\x50\x43\x4d\x20\x41\x20\x20\x20" +
     b"\x50\x57\x52\x2d\x30\x30\x30\x35\x39\x2d\x30\x31\x2d\x42\x30\x30" +
     b"\x20\x20\x20\x20\x54\x48\x44\x45\x4c\x30\x30\x30\x31\x35\x4e\x52" +
     b"\x45\x31\x32\x46\x00\x00\x00\x2c\x50\x43\x4d\x20\x42\x20\x20\x20" +
     b"\x50\x57\x52\x2d\x30\x30\x30\x35\x39\x2d\x30\x31\x2d\x42\x30\x30" +
     b"\x20\x20\x20\x20\x54\x48\x44\x45\x4c\x30\x30\x30\x31\x35\x4e\x52" +
     b"\x45\x31\x35\x33\x00\x00\x00\x2c\x49\x4f\x4d\x20\x41\x20\x20\x20" +
     b"\x54\x43\x41\x2d\x30\x30\x33\x34\x30\x2d\x30\x31\x2d\x42\x20\x20" +
     b"\x20\x20\x20\x20\x4d\x58\x45\x33\x34\x30\x30\x30\x32\x38\x50\x52" +
     b"\x41\x31\x36\x31\x00\x00\x00\x2c\x49\x4f\x4d\x20\x42\x20\x20\x20" +
     b"\x54\x43\x41\x2d\x30\x30\x33\x34\x30\x2d\x30\x31\x2d\x42\x20\x20" +
     b"\x20\x20\x20\x20\x4d\x58\x45\x33\x34\x30\x30\x30\x32\x38\x56\x52" +
     b"\x41\x31\x30\x43\x00\x00\x00\x2c\x42\x73\x42\x6f\x61\x72\x64\x31" +
     b"\x54\x43\x41\x2d\x30\x30\x33\x34\x31\x2d\x30\x31\x2d\x42\x2d\x41" +
     b"\x32\x20\x20\x20\x4d\x58\x45\x33\x34\x30\x30\x30\x32\x38\x38\x52" +
     b"\x42\x30\x33\x31\x00\x00\x00\x2c\x42\x73\x42\x6f\x61\x72\x64\x32" +
     b"\x54\x43\x41\x2d\x30\x30\x33\x34\x31\x2d\x30\x31\x2d\x42\x2d\x41" +
     b"\x32\x20\x20\x20\x4d\x58\x45\x33\x34\x30\x30\x30\x32\x38\x38\x52" +
     b"\x42\x30\x33\x31\x00\x00\x00\x00\x00\x00\x00\x2c\x42\x73\x42\x6f" +
     b"\x61\x72\x64\x20\x54\x43\x41\x2d\x30\x30\x33\x34\x31\x2d\x30\x31" +
     b"\x2d\x42\x2d\x41\x32\x20\x20\x20\x4d\x58\x45\x33\x34\x30\x30\x30" +
     b"\x32\x38\x38\x52\x42\x30\x33\x31\x00\x00\x00\x00\x00\x00\x00\x30" +
     b"\x49\x4f\x4d\x20\x41\x20\x20\x20\x54\x43\x41\x2d\x30\x30\x33\x34" +
     b"\x30\x2d\x30\x31\x2d\x42\x20\x20\x4d\x58\x45\x33\x34\x30\x30\x30" +
     b"\x32\x38\x50\x52\x41\x31\x36\x31\x42\x35\x2e\x30\x37\x2e\x31\x36" +
     b"\x00\x00\x00\x30\x49\x4f\x4d\x20\x42\x20\x20\x20\x54\x43\x41\x2d" +
     b"\x30\x30\x33\x34\x30\x2d\x30\x31\x2d\x42\x20\x20\x4d\x58\x45\x33" +
     b"\x34\x30\x30\x30\x32\x38\x56\x52\x41\x31\x30\x43\x42\x35\x2e\x30" +
     b"\x37\x2e\x31\x36\x00\x00\x00\x00\x00\x00\x00\x38\x53\x58\x50\x5f" +
     b"\x41\x5f\x50\x20\x54\x43\x41\x2d\x30\x30\x33\x34\x30\x2d\x30\x31" +
     b"\x2d\x42\x20\x20\x4d\x58\x45\x33\x34\x30\x30\x30\x32\x38\x50\x52" +
     b"\x41\x31\x36\x31\x42\x35\x2e\x30\x37\x2e\x31\x36\x42\x35\x2e\x30" +
     b"\x37\x2e\x31\x36\x00\x00\x00\x38\x53\x58\x50\x5f\x41\x5f\x53\x31" +
     b"\x54\x43\x41\x2d\x30\x30\x33\x34\x30\x2d\x30\x31\x2d\x42\x20\x20" +
     b"\x4d\x58\x45\x33\x34\x30\x30\x30\x32\x38\x50\x52\x41\x31\x36\x31" +
     b"\x42\x35\x2e\x30\x37\x2e\x31\x36\x42\x35\x2e\x30\x37\x2e\x31\x36" +
     b"\x00\x00\x00\x38\x53\x58\x50\x5f\x41\x5f\x53\x32\x54\x43\x41\x2d" +
     b"\x30\x30\x33\x34\x30\x2d\x30\x31\x2d\x42\x20\x20\x4d\x58\x45\x33" +
     b"\x34\x30\x30\x30\x32\x38\x50\x52\x41\x31\x36\x31\x42\x35\x2e\x30" +
     b"\x37\x2e\x31\x36\x42\x35\x2e\x30\x37\x2e\x31\x36\x00\x00\x00\x38" +
     b"\x53\x58\x50\x5f\x42\x5f\x50\x20\x54\x43\x41\x2d\x30\x30\x33\x34" +
     b"\x30\x2d\x30\x31\x2d\x42\x20\x20\x4d\x58\x45\x33\x34\x30\x30\x30" +
     b"\x32\x38\x56\x52\x41\x31\x30\x43\x42\x35\x2e\x30\x37\x2e\x31\x36" +
     b"\x42\x35\x2e\x30\x37\x2e\x31\x36\x00\x00\x00\x38\x53\x58\x50\x5f" +
     b"\x42\x5f\x53\x31\x54\x43\x41\x2d\x30\x30\x33\x34\x30\x2d\x30\x31" +
     b"\x2d\x42\x20\x20\x4d\x58\x45\x33\x34\x30\x30\x30\x32\x38\x56\x52" +
     b"\x41\x31\x30\x43\x42\x35\x2e\x30\x37\x2e\x31\x36\x42\x35\x2e\x30" +
     b"\x37\x2e\x31\x36\x00\x00\x00\x38\x53\x58\x50\x5f\x42\x5f\x53\x32" +
     b"\x54\x43\x41\x2d\x30\x30\x33\x34\x30\x2d\x30\x31\x2d\x42\x20\x20" +
     b"\x4d\x58\x45\x33\x34\x30\x30\x30\x32\x38\x56\x52\x41\x31\x30\x43" +
     b"\x42\x35\x2e\x30\x37\x2e\x31\x36\x42\x35\x2e\x30\x37\x2e\x31\x36")


class SesDiagnostic(TestCase):
    def test__supported_pages(self):
        """
Supported diagnostic pages (0x0):
  Supported Diagnostic Pages [sdp] [0x0]
  Configuration (SES) [cf] [0x1]
  Enclosure Status/Control (SES) [ec,es] [0x2]
  String In/Out (SES) [str] [0x4]
  Threshold In/Out (SES) [th] [0x5]
  Element Descriptor (SES) [ed] [0x7]
  Additional Element Status (SES-2) [aes] [0xa]
  Download Microcode (SES-2) [dm] [0xe]
  <unknown> [0x80]
        """
        from infi.asi.cdb.diagnostic.ses_pages.supported_pages import SupportedDiagnosticPagesData
        buffer = b"\x00\x00\x00\x00\x00\x01\x02\x04\x05\x07\x0a\x0e\x80"
        obj = SupportedDiagnosticPagesData(None)
        obj.unpack(buffer)
        pages = [0x0, 0x1, 0x2, 0x4, 0x5, 0x7, 0xa, 0xe, 0x80]
        print(obj.supported_pages)
        self.assertEquals(obj.supported_pages, pages)

    def test__vendor0x80_page(self):
        """
      Vendor specific page (0x80):
Cannot decode response from diagnostic page: <unknown>
 00     80 00 00 80 ff ff ff ff  05 00 ff ff ff ff ff ff    ................
 10     ff ff ff ff ff ff ff ff  ff ff ff ff ff ff ff ff    ................
        """
        from infi.asi.cdb.diagnostic.ses_pages.vendor_0x80 import Vendor0x80DiagnosticPagesData
        buffer = b"\x80\x00\x00\x80\xff\xff\xff\xff\x05\x00\xff\xff\xff"
#        import pdb; pdb.set_trace()
        obj = Vendor0x80DiagnosticPagesData(None)
        obj.unpack(buffer)
        print(obj.vendor_specific)
        self.assertEquals(obj.vendor_specific[4], 0x05)

    def test_configuration_diagnostics_page(self):
        """
Configuration diagnostic page (0x01):
  number of secondary subenclosures: 0
  generation code: 0x1
  enclosure descriptor list
    Subenclosure identifier: 0 (primary)
      relative ES process id: 1, number of ES processes: 2
      number of type descriptor headers: 8
      enclosure logical identifier (hex): 500093d0006a7000
      enclosure vendor: NEWISYS   product: NDS-4600-JD       rev: B507
  type descriptor header/text list
    Element type: Array device slot, subenclosure id: 0
      number of possible elements: 60
      text: Array Dev Slot
    Element type: vendor specific [0x9e], subenclosure id: 0
      number of possible elements: 1
      text: 4600 Enclosure
    Element type: Power supply, subenclosure id: 0
      number of possible elements: 2
      text: Power Supply
    Element type: Cooling, subenclosure id: 0
      number of possible elements: 4
      text: Cooling Fan
    Element type: Temperature sensor, subenclosure id: 0
      number of possible elements: 6
      text: Temp Sensor
    Element type: Audible alarm, subenclosure id: 0
      number of possible elements: 1
      text: Buzzer
    Element type: Enclosure services controller electronics, subenclosure id: 0
      number of possible elements: 2
      text: ES Processor
    Element type: SAS expander, subenclosure id: 0
      number of possible elements: 6
      text: SAS Expander
      """
        from infi.asi.cdb.diagnostic.ses_pages.configuration import ConfigurationDiagnosticPagesData
        raw = SES_CONFIGURATION_PAGE_SAMPLE
        page = ConfigurationDiagnosticPagesData(None)
        page.unpack(raw)
        self.assertEquals(len(page.enclosure_descriptor_list), 1)
        self.assertEquals(len(page.type_descriptor_header_list), 8)
        self.assertEquals(len(page.type_descriptor_text_list), 8)
        #print(page)
        return page

    def test_enclosure_status_diagnostics_page(self):
        """
Enclosure Status diagnostic page:
  INVOP=0, INFO=1, NON-CRIT=0, CRIT=1, UNRECOV=0
  generation code: 0x1
  status descriptor list
    Element type: Array device slot, subenclosure id: 0 [ti=0]
      Overall descriptor:
        Predicted failure=0, Disabled=0, Swap=0, status: Unsupported
        OK=0, Reserved device=0, Hot spare=0, Cons check=0
        In crit array=0, In failed array=0, Rebuild/remap=0, R/R abort=0
        App client bypass A=0, Do not remove=0, Enc bypass A=0, Enc bypass B=0
        Ready to insert=0, RMV=0, Ident=0, Report=0
        App client bypass B=0, Fault sensed=0, Fault reqstd=0, Device off=0
        Bypassed A=0, Bypassed B=0, Dev bypassed A=0, Dev bypassed B=0
      Element 0 descriptor:
        Predicted failure=0, Disabled=0, Swap=0, status: OK
        OK=0, Reserved device=0, Hot spare=0, Cons check=0
        In crit array=0, In failed array=0, Rebuild/remap=0, R/R abort=0
        App client bypass A=0, Do not remove=0, Enc bypass A=0, Enc bypass B=0
        Ready to insert=0, RMV=0, Ident=0, Report=0
        App client bypass B=0, Fault sensed=0, Fault reqstd=0, Device off=0
        Bypassed A=0, Bypassed B=0, Dev bypassed A=0, Dev bypassed B=0
      Element 1 descriptor:
        Predicted failure=0, Disabled=0, Swap=0, status: OK
        OK=0, Reserved device=0, Hot spare=0, Cons check=0
        In crit array=0, In failed array=0, Rebuild/remap=0, R/R abort=0
        App client bypass A=0, Do not remove=0, Enc bypass A=0, Enc bypass B=0
        Ready to insert=0, RMV=0, Ident=0, Report=0
        App client bypass B=0, Fault sensed=0, Fault reqstd=0, Device off=0
        Bypassed A=0, Bypassed B=0, Dev bypassed A=0, Dev bypassed B=0
......
        """
        from infi.asi.cdb.diagnostic.ses_pages.enclosure_status import EnclosureStatusDiagnosticPagesData
        config_page = self.test_configuration_diagnostics_page()
        raw = SES_ENCL_STATUS_PAGE_SAMPLE
        status_page = EnclosureStatusDiagnosticPagesData(config_page)
        status_page.unpack(raw)
        self.assertEquals(len(status_page.status_descriptors), len(config_page.type_descriptor_header_list))
        for idx in range(len(config_page.type_descriptor_header_list)):
            self.assertEquals(len(status_page.status_descriptors[idx].individual_elements),
                              config_page.type_descriptor_header_list[idx].possible_elements_num)
            print("{!r} has {!r} elements".format(config_page.type_descriptor_header_list[idx].element_type,
                                                  len(status_page.status_descriptors[idx].individual_elements)))

    def test_element_descriptor_diagnostics_page(self):
        """
Element Descriptor In diagnostic page:
  generation code: 0x1
  element descriptor by type list
    Element type: Array device slot, subenclosure id: 0 [ti=0]
      Overall descriptor: <empty>
      Element 0 descriptor: SLOT  1 00
      Element 1 descriptor: SLOT  2 01
      Element 2 descriptor: SLOT  3 02
      Element 3 descriptor: SLOT  4 03
      Element 4 descriptor: SLOT  5 04
...
      Element 58 descriptor: SLOT 59 4A
      Element 59 descriptor: SLOT 60 4B
    Element type: vendor specific [0x9e], subenclosure id: 0 [ti=1]
      Overall descriptor: <empty>
      Element 0 descriptor:                                                             TCA-00341-01-B-A2   MXE34000288RB031TCA-00340-01-B  MXE3400028PRA161TCA-00340-01-B  MXE3400028VRA10C00090001
    Element type: Power supply, subenclosure id: 0 [ti=2]
      Overall descriptor: <empty>
      Element 0 descriptor: PCM A   PWR-00059-01-B00THDEL00015NRE12FA1000000TDPS-1200AB A000ABMT11210018120000F000000109
      Element 1 descriptor: PCM B   PWR-00059-01-B00THDEL00015NRE153A1000000TDPS-1200AB A000ABMT11210018480000F000000109
    Element type: Cooling, subenclosure id: 0 [ti=3]
      Overall descriptor: <empty>
      Element 0 descriptor: PCMAFAN1PWR-00059-01-B00THDEL00015NRE12F
      Element 1 descriptor: PCMAFAN2PWR-00059-01-B00THDEL00015NRE12F
      Element 2 descriptor: PCMBFAN1PWR-00059-01-B00THDEL00015NRE153
      Element 3 descriptor: PCMBFAN2PWR-00059-01-B00THDEL00015NRE153
    Element type: Temperature sensor, subenclosure id: 0 [ti=4]
      Overall descriptor: <empty>
      Element 0 descriptor: PCM A   PWR-00059-01-B00    THDEL00015NRE12F
      Element 1 descriptor: PCM B   PWR-00059-01-B00    THDEL00015NRE153
      Element 2 descriptor: IOM A   TCA-00340-01-B      MXE3400028PRA161
      Element 3 descriptor: IOM B   TCA-00340-01-B      MXE3400028VRA10C
      Element 4 descriptor: BsBoard1TCA-00341-01-B-A2   MXE34000288RB031
      Element 5 descriptor: BsBoard2TCA-00341-01-B-A2   MXE34000288RB031
    Element type: Audible alarm, subenclosure id: 0 [ti=5]
      Overall descriptor: <empty>
      Element 0 descriptor: BsBoard TCA-00341-01-B-A2   MXE34000288RB031
    Element type: Enclosure services controller electronics, subenclosure id: 0 [ti=6]
      Overall descriptor: <empty>
      Element 0 descriptor: IOM A   TCA-00340-01-B  MXE3400028PRA161B5.07.16
      Element 1 descriptor: IOM B   TCA-00340-01-B  MXE3400028VRA10CB5.07.16
    Element type: SAS expander, subenclosure id: 0 [ti=7]
      Overall descriptor: <empty>
      Element 0 descriptor: SXP_A_P TCA-00340-01-B  MXE3400028PRA161B5.07.16B5.07.16
      Element 1 descriptor: SXP_A_S1TCA-00340-01-B  MXE3400028PRA161B5.07.16B5.07.16
      Element 2 descriptor: SXP_A_S2TCA-00340-01-B  MXE3400028PRA161B5.07.16B5.07.16
      Element 3 descriptor: SXP_B_P TCA-00340-01-B  MXE3400028VRA10CB5.07.16B5.07.16
      Element 4 descriptor: SXP_B_S1TCA-00340-01-B  MXE3400028VRA10CB5.07.16B5.07.16
      Element 5 descriptor: SXP_B_S2TCA-00340-01-B  MXE3400028VRA10CB5.07.16B5.07.16
        """
        from infi.asi.cdb.diagnostic.ses_pages.element_descriptor import ElementDescriptorDiagnosticPagesData
        config_page = self.test_configuration_diagnostics_page()
        raw = SES_ELEMENT_DESCR_PAGE_SAMPLE
        descr_page = ElementDescriptorDiagnosticPagesData(config_page)
        descr_page.unpack(raw)
        self.assertEquals(len(descr_page.element_descriptors), len(config_page.type_descriptor_header_list))
        for idx in range(len(config_page.type_descriptor_header_list)):
            self.assertEquals(len(descr_page.element_descriptors[idx].individual_elements),
                              config_page.type_descriptor_header_list[idx].possible_elements_num)
            print("{!r} has {!r} elements".format(config_page.type_descriptor_header_list[idx].element_type,
                                                  len(descr_page.element_descriptors[idx].individual_elements)))
            for i in range(len(descr_page.element_descriptors[idx].individual_elements)):
                print("elem {!r}[{!r}] is {!r}".format(config_page.type_descriptor_header_list[idx].element_type, i,
                                                       descr_page.element_descriptors[idx].individual_elements[i].descriptor))
