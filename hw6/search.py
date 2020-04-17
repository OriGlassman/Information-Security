import addresses
import assemble
import string


GENERAL_REGISTERS = [
    'eax', 'ebx', 'ecx', 'edx', 'esi', 'edi'
]


ALL_REGISTERS = GENERAL_REGISTERS + [
    'esp', 'eip', 'ebp'
]


class GadgetSearch(object):
    def __init__(self, dump_path, start_addr=None):
        """
        Construct the GadgetSearch object.

        Input:
            dump_path: The path to the memory dump file created with GDB.
            start_addr: The starting memory address of this dump. Use
                        `addresses.LIBC_TEXT_START` by default.
        """
        self.start_addr = (start_addr if start_addr is not None
                           else addresses.LIBC_TEXT_START)
        with open(dump_path, 'rb') as f:
            self.dump = f.read()

    def get_format_count(self, gadget_format):
        """
        Get how many different register placeholders are in the pattern.
        
        Examples:
            self.get_format_count('POP ebx')
            => 0
            self.get_format_count('POP {0}')
            => 1
            self.get_format_count('XOR {0}, {0}; ADD {0}, {1}')
            => 2
        """
        # Hint: Use the string.Formatter().parse method:

        #print string.Formatter().parse(gadget_format)
        different_placeholders = set() # no duplicates so the length at the end will be the amount of different placeholders
        parsed_pattern = string.Formatter().parse(gadget_format)
        while True:
            try:
                placeholder = next(parsed_pattern)[1]
                if placeholder!=None:
                    different_placeholders.add(placeholder)
                else:
                    continue
            except StopIteration:
                break
        return len(different_placeholders)




    def get_register_combos(self, nregs, registers):
        """
        Return all the combinations of `registers` with `nregs` registers in
        each combination. Duplicates ARE allowed!

        Example:
            self.get_register_combos(2, ('eax', 'ebx'))
            => [['eax', 'eax'],
                ['eax', 'ebx'],
                ['ebx', 'eax'],
                ['ebx', 'ebx']]
        """
        import itertools
        lst_combos = []
        tup_combos = itertools.product(registers, repeat=nregs)
        for tup_combo in tup_combos:
            lst_combos.append(list(tup_combo))
        return lst_combos

    def format_all_gadgets(self, gadget_format, registers):
        """
        Format all the possible gadgets for this format with the given
        registers.

        Example:
            self.format_all_gadgets("POP {0}; ADD {0}, {1}", ('eax', 'ecx'))
            => ['POP eax; ADD eax, eax',
                'POP eax; ADD eax, ecx',
                'POP ecx; ADD ecx, eax',
                'POP ecx; ADD ecx, ecx']
        """
        # Hints:
        #
        # 0. Use the previous functions to count the number of placeholders,
        #    and get all combinations of registers.
        #
        # 1. Use the `format` function to build the string:
        #
        #    'Hi {0}! I am {1}, you are {0}'.format('Luke', 'Vader')
        #    => 'Hi Luke! I am Vader, you are Luke'
        #
        # 2. You can use pass a list of arguments instead of specifying each
        #    argument individually. Use the internet, the force is strong with
        #    StackOverflow.
        num_gadget = self.get_format_count(gadget_format)
        all_reg_combos = self.get_register_combos(num_gadget, registers)
        formatted_gadgets_lst = []
        for reg_option in all_reg_combos:
            formatted_gadgets_lst.append(gadget_format.format(*reg_option))
        return formatted_gadgets_lst



    def find_all(self, gadget):
        """
        Return all the addresses of the gadget inside the memory dump.

        Example:
            self.find_all('POP eax')
            => < all ABSOLUTE addresses in memory of 'POP eax; RET' >
        """
        # Notes:
        #
        # 1. Addresses are ABSOLUTE (for example, 0x08403214), NOT RELATIVE to
        #    the beginning of the file (for example, 12).
        #
        # 2. Don't forget to add the 'RET'.
        haystack = self.dump
        needle = assemble.assemble_data(gadget + '\nret')
        return find_indexes(needle,haystack, self.start_addr)








    def find(self, gadget, condition=None):
        """
        Return the first result of find_all. If condition is specified, only
        consider addresses that meet the condition.
        """
        condition = condition or (lambda x: True)
        try:
            return next(addr for addr in self.find_all(gadget)
                        if condition(addr))
        except StopIteration:
            raise ValueError("Couldn't find matching address for " + gadget)

    def find_all_formats(self, gadget_format, registers=GENERAL_REGISTERS):
        """
        Similar to find_all - but return all the addresses of all
        possible gadgets that can be created with this format and registers.
        Every elemnt in the result will be a tuple of the gadget string and
        the address in which it appears.

        Example:
            self.find_all_formats('POP {0}; POP {1}')
            => [('POP eax; POP ebx', address1),
                ('POP ecx; POP esi', address2),
                ...]
        """
        lst_all_formats =[]
        formatted_gadgets = self.format_all_gadgets(gadget_format, registers)
        for temp_gadget in formatted_gadgets:
            indexes = self.find_all(temp_gadget)
            if indexes!=[]:
                for index in indexes:
                    lst_all_formats.append( (temp_gadget,index) )
        return lst_all_formats

    def find_format(self, gadget_format, registers=GENERAL_REGISTERS,
                    condition=None):
        """
        Return the first result of find_all_formats. If condition is specified,
        only consider addresses that meet the condition.
        """
        condition = condition or (lambda x: True)
        try:
            return next(
                addr for addr in self.find_all_formats(gadget_format, registers)
                if condition(addr)
            )
        except StopIteration:
            raise ValueError(
                "Couldn't find matching address for " + gadget_format)


def find_indexes(needle, haystack, start_addr):
    indexes = []
    index = 0
    while index < len(haystack):
        index = haystack.find(needle, index)
        if index == -1:
            break
        hexa_num = hex(start_addr+index)
        if "L" in hexa_num:
            hexa_num = hexa_num[:-1]
        indexes.append(hexa_num)
        index+=1
    return indexes  